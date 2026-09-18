"""Finite, source-honest context and re-entry contracts."""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Mapping

from .core import result, digest

MAX_BYTES = 100_000
MAX_DEPTH = 24
MAX_ITEMS = 10_000
PROFILES = {
    "mathematical": "definitions, derivations, proof obligations, and unresolved steps",
    "scientific": "observations, baselines, uncertainty, alternatives, and next tests",
    "philosophical": "concepts, distinctions, arguments, counterpositions, and limits",
    "game": "rules, state, choices, consequences, and player agency",
}
LEGACY_ALIASES = {"MPCP": "mathematical", "SPCP": "scientific", "PhPCP": "philosophical", "GPCP": "game"}


def _bounded(value: Any) -> tuple[bool, str | None]:
    try:
        raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError, UnicodeError, RecursionError):
        return False, "not_finite_json"
    try:
        encoded = raw.encode("utf-8")
    except (UnicodeError, RecursionError):
        return False, "not_finite_json"
    if len(encoded) > MAX_BYTES:
        return False, "input_too_large"
    def walk(node: Any, depth: int = 0) -> int:
        if depth > MAX_DEPTH:
            raise ValueError("depth")
        if isinstance(node, Mapping):
            if len(node) > MAX_ITEMS: raise ValueError("items")
            return 1 + sum(walk(k, depth + 1) + walk(v, depth + 1) for k, v in node.items())
        if isinstance(node, (list, tuple)):
            if len(node) > MAX_ITEMS: raise ValueError("items")
            return 1 + sum(walk(v, depth + 1) for v in node)
        return 1
    try:
        if walk(value) > MAX_ITEMS: return False, "too_many_nodes"
    except ValueError as exc:
        return False, "input_too_deep" if str(exc) == "depth" else "too_many_items"
    return True, None


def _invalid(kind: str, errors: list[str], **fields: Any) -> dict[str, Any]:
    return result(kind, status="INVALID_INPUT", errors=sorted(set(errors)), **fields)


def _strings(value: Any, field: str) -> tuple[list[str], list[str]]:
    if value is None: return [], []
    if not isinstance(value, list): return [], [f"{field}_must_be_list"]
    errors: list[str] = []
    items: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip(): errors.append(f"{field}_contains_nonempty_string_required")
        elif item in items: errors.append(f"{field}_contains_duplicate:{item}")
        else: items.append(item)
    return items, errors


def _content_digest(value: Any) -> str | None:
    try: return digest(value)
    except (TypeError, ValueError, UnicodeError): return None


def orient(request: Mapping[str, Any]) -> dict[str, Any]:
    """Return a provisional orientation with disjoint context sets."""
    ok, why = _bounded(request)
    if not ok or not isinstance(request, Mapping): return _invalid("context_orientation", [why or "request_must_be_object"])
    errors: list[str] = []
    raw_profiles = request.get("profiles", request.get("profile"))
    if raw_profiles is None: profiles: list[str] = []
    elif isinstance(raw_profiles, str): profiles = [raw_profiles]
    elif isinstance(raw_profiles, list): profiles = list(raw_profiles)
    else: profiles = []; errors.append("profiles_must_be_string_or_list")
    aliases: dict[str, str] = {}
    for index, profile in enumerate(profiles):
        if isinstance(profile, str) and profile in LEGACY_ALIASES:
            aliases[profile] = LEGACY_ALIASES[profile]
            profiles[index] = LEGACY_ALIASES[profile]
        elif not isinstance(profile, str) or profile not in PROFILES: errors.append(f"unknown_profile:{profile}")
    # A purpose without a purpose-specific profile is a valid, explicitly
    # unforced orientation.  An unknown requested profile remains invalid.
    purpose = request.get("purpose")
    if not isinstance(purpose, str) or not purpose.strip(): errors.append("purpose_required")
    fields = ("selected", "supplied", "available_unread", "inferred", "omitted_for_budget", "unavailable", "corrected")
    sets: dict[str, list[str]] = {}
    for field in fields:
        sets[field], field_errors = _strings(request.get(field, []), field); errors.extend(field_errors)
    locations: dict[str, list[str]] = {}
    for field, values in sets.items():
        for item in values: locations.setdefault(item, []).append(field)
    # `selected` is an orthogonal decision about what to load; it may name a
    # supplied item.  The other material-state buckets are exclusive.
    for item, where in locations.items():
        material_where = [field for field in where if field != "selected"]
        if len(material_where) > 1: errors.append(f"context_item_in_multiple_sets:{item}")
    bindings = request.get("source_bindings")
    normalized_bindings: list[dict[str, Any]] = []
    if bindings is not None:
        if isinstance(bindings, Mapping):
            bindings = [dict(value, source_id=key) if isinstance(value, Mapping) else {"source_id": key, "value": value} for key, value in bindings.items()]
        if not isinstance(bindings, list):
            errors.append("source_bindings_must_be_list_or_object")
        else:
            for binding in bindings:
                if not isinstance(binding, Mapping):
                    errors.append("source_binding_must_be_object"); continue
                item = dict(binding)
                if not isinstance(item.get("source_id"), str) or not item["source_id"].strip(): errors.append("source_binding_source_id_required")
                if not isinstance(item.get("version"), (str, int)) or isinstance(item.get("version"), bool): errors.append("source_binding_version_required")
                bound_hash = item.get("content_hash", item.get("expected_hash"))
                if not isinstance(bound_hash, str) or not bound_hash.startswith("sha256:"): errors.append("source_binding_hash_required")
                normalized_bindings.append(item)
            bound_ids = {item.get("source_id") for item in normalized_bindings}
            for item in sets["selected"]:
                if item not in bound_ids: errors.append(f"selected_source_unbound:{item}")
    if errors: return _invalid("context_orientation", errors, profiles=profiles, purpose=purpose, sets=sets)
    orientation_status = "VALID" if profiles else "UNFORCED"
    orientation = {"profiles": profiles, "purpose": purpose, "sets": sets, "mixed": len(profiles) > 1,
                   "profile_guidance": {profile: PROFILES[profile] for profile in profiles},
                   "selection_status": "PROVISIONAL", "source_bindings": normalized_bindings,
                   "notice": "Selection and availability do not establish that a source was read, understood, or true."}
    if aliases:
        orientation["legacy_profile_aliases"] = aliases
    # Compatibility field for callers of the preview adapter.  The canonical
    # representation remains the disjoint `sets` map above.
    orientation.update({field: values for field, values in sets.items() if field in {"available_unread", "supplied", "selected", "inferred", "omitted_for_budget"}})
    if request.get("actionable_guidance") is not None:
        guidance = request["actionable_guidance"]
        if not isinstance(guidance, list) or not all(isinstance(item, str) and item.strip() for item in guidance):
            return _invalid("context_orientation", ["actionable_guidance_must_be_nonempty_string_list"])
        orientation["actionable_guidance"] = list(guidance)
    orientation["orientation_hash"] = digest(orientation)
    return result("context_orientation", status=orientation_status, **orientation)


def source_status(request: Mapping[str, Any]) -> dict[str, Any]:
    """Classify content actually supplied; caller metadata is not trusted."""
    ok, why = _bounded(request)
    if not ok or not isinstance(request, Mapping): return _invalid("source_status", [why or "request_must_be_object"])
    supplied = request.get("supplied_content", request.get("supplied_source"))
    expected = request.get("expected_hash")
    version = request.get("version")
    expected_version = request.get("expected_version")
    expected_fingerprint = request.get("expected_fingerprint")
    fingerprint = request.get("fingerprint")
    errors: list[str] = []
    if not isinstance(request.get("source_id"), str) or not request["source_id"].strip(): errors.append("source_id_required")
    if expected is not None and (not isinstance(expected, str) or not expected.startswith("sha256:")): errors.append("expected_hash_must_be_sha256")
    observed = _content_digest(supplied) if supplied is not None else None
    if supplied is None: state = "MISSING"
    elif observed is None: state = "INVALID_INPUT"; errors.append("supplied_content_not_finite_json")
    elif expected and observed != expected: state = "CHANGED"
    elif expected_version is not None and version != expected_version: state = "STALE"
    elif expected_fingerprint is not None and fingerprint != expected_fingerprint: state = "STALE"
    elif request.get("stale") is True: state = "STALE"
    else: state = "AVAILABLE"
    if version is not None and not isinstance(version, (str, int)): errors.append("version_must_be_string_or_integer")
    if errors and state == "AVAILABLE": state = "INVALID_INPUT"
    return result("source_status", source_id=request.get("source_id"), version=version, expected_version=expected_version,
                  expected_hash=expected, observed_hash=observed, expected_fingerprint=expected_fingerprint, fingerprint=fingerprint,
                  state=state, claim_status="SOURCE_METADATA", errors=sorted(set(errors)), content_supplied=supplied is not None,
                  notice="Availability is conditional on supplied content and declared comparison inputs; metadata does not establish source truth.")


def _receipt_chain(chain: Any) -> tuple[bool, list[str], list[dict[str, Any]]]:
    if not isinstance(chain, list): return False, ["receipt_chain_must_be_list"], []
    errors: list[str] = []; normalized: list[dict[str, Any]] = []; previous: str | None = None
    for index, record in enumerate(chain):
        if not isinstance(record, Mapping): errors.append(f"receipt_chain_item_{index}_must_be_object"); continue
        item = dict(record); rid = item.get("receipt_id")
        if not isinstance(rid, str) or not rid.strip(): errors.append(f"receipt_chain_item_{index}_missing_receipt_id")
        link = item.get("previous_hash")
        if index == 0 and link not in (None, ""): errors.append("receipt_chain_first_previous_hash_must_be_empty")
        elif index and link != previous: errors.append(f"receipt_chain_link_mismatch:{index}")
        body = {key: value for key, value in item.items() if key not in {"receipt_hash", "previous_hash"}}
        calculated = _content_digest(body); supplied_hash = item.get("receipt_hash")
        if supplied_hash is not None and supplied_hash != calculated: errors.append(f"receipt_chain_hash_mismatch:{index}")
        previous = supplied_hash or calculated; normalized.append(item)
    return not errors, errors, normalized


def transport_capsule(request: Mapping[str, Any]) -> dict[str, Any]:
    """Validate finite re-entry fields and detect changed comparison inputs."""
    ok, why = _bounded(request)
    if not ok or not isinstance(request, Mapping): return _invalid("transport_capsule", [why or "request_must_be_object"])
    required = ("program", "cursor", "schedule", "dependencies", "comparator", "budget", "receipt_chain")
    missing = [field for field in required if field not in request]
    if missing: return result("transport_capsule", capsule=dict(request), missing=missing, status="INCOMPLETE", resume_effect="NONE", reassessment="REQUIRED_FIELDS_MISSING")
    errors: list[str] = []
    if not isinstance(request["program"], (str, Mapping)) or (isinstance(request["program"], str) and not request["program"].strip()): errors.append("program_must_be_nonempty_string_or_object")
    if not isinstance(request["cursor"], (str, Mapping, int)) or isinstance(request["cursor"], bool): errors.append("cursor_must_be_scalar_or_object")
    if not isinstance(request["dependencies"], (Mapping, list)): errors.append("dependencies_must_be_object_or_list")
    if not isinstance(request["comparator"], (str, Mapping)) or (isinstance(request["comparator"], str) and not request["comparator"].strip()): errors.append("comparator_identity_required")
    if not isinstance(request["budget"], Mapping): errors.append("budget_must_be_object")
    else:
        for key, value in request["budget"].items():
            if not isinstance(value, int) or isinstance(value, bool) or value < 0: errors.append(f"budget_value_invalid:{key}")
    chain_ok, chain_errors, chain = _receipt_chain(request["receipt_chain"]); errors.extend(chain_errors)
    capsule = {field: request[field] for field in required}; capsule_hash = digest(capsule)
    prior = request.get("prior_capsule"); reassessment = "NONE"; prior_hash = None
    if prior is not None:
        if not isinstance(prior, Mapping): errors.append("prior_capsule_must_be_object")
        else:
            prior_hash = prior.get("capsule_hash") or _content_digest({field: prior.get(field) for field in required})
            changed = [field for field in ("program", "cursor", "schedule", "dependencies", "comparator", "budget") if field in prior and prior.get(field) != request.get(field)]
            if changed: reassessment = "REASSESSMENT_REQUIRED"; errors.append("prior_comparison_changed:" + ",".join(changed))
            if prior.get("receipt_chain") is not None and prior.get("receipt_chain") != request.get("receipt_chain"):
                reassessment = "REASSESSMENT_REQUIRED"; errors.append("prior_receipt_chain_changed")
    structural = any(error.startswith(("receipt_chain", "budget", "program", "cursor", "comparator", "dependencies", "prior_capsule")) for error in errors)
    status = "INVALID_INPUT" if structural else ("REASSESSMENT_REQUIRED" if errors else "VALID")
    return result("transport_capsule", capsule=capsule, capsule_hash=capsule_hash, prior_capsule_hash=prior_hash, receipt_chain=chain,
                  missing=[], status=status, chain_status="VALID" if chain_ok else "INVALID", reassessment=reassessment, resume_effect="NONE",
                  notice="A valid capsule supports bounded restart checks; it does not prove semantic equivalence, permission, or execution.")
