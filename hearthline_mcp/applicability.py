"""A finite MIND/CHARTER-inspired review, not a semantic applicability oracle."""
from __future__ import annotations

import json
import re
from importlib.resources import files
from typing import Any, Mapping

from .context import _bounded
from .core import digest, result

HASH = re.compile(r"sha256:[0-9a-f]{64}\Z")
MAX_CONDITIONS = 256


def context_sources() -> dict[str, Any]:
    """Return packaged reference identities; never retrieve or adopt sources."""
    return json.loads(files("hearthline_mcp").joinpath("context_sources.json").read_text(encoding="utf-8"))


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _refs(value: Any, path: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or any(not _text(ref) for ref in value):
        errors.append(f"{path}_must_be_string_list")
        return []
    # Repetition is neither another source nor another vote.
    return list(dict.fromkeys(value))


def review_applicability(request: Mapping[str, Any]) -> dict[str, Any]:
    """Compare hash-bound equality conditions with supplied, attributed facts.

    Both axes concern declared finite inputs. Hash equality checks canonical
    JSON identity, not semantic fidelity; references are not authenticated.
    Conditions must live inside the bound content, so removing a qualifier
    changes the source digest. No result admits a source or renews a grant.
    """
    def invalid(errors: list[str]) -> dict[str, Any]:
        return result("context_applicability", status="INVALID_INPUT", errors=sorted(set(errors)),
                      admission_effect="NONE", training_effect="NONE")

    ok, why = _bounded(request)
    if not ok or not isinstance(request, Mapping):
        return invalid([why or "request_must_be_object"])
    errors: list[str] = []
    if set(request) - {"source", "target", "reopen_handle"}:
        errors.append("unsupported_request_fields")
    source, target = request.get("source"), request.get("target")
    if not isinstance(source, Mapping) or not isinstance(target, Mapping):
        return invalid(["source_and_target_must_be_objects"])
    if set(source) - {"source_id", "version", "expected_version", "expected_hash", "supplied_content"}:
        errors.append("unsupported_source_fields")
    if set(target) - {"context_id", "facts"}:
        errors.append("unsupported_target_fields")
    for field in ("source_id", "version"):
        if not _text(source.get(field)):
            errors.append(f"source_{field}_required")
    if "expected_version" in source and not _text(source["expected_version"]):
        errors.append("expected_version_must_be_nonempty_string")
    if not _text(target.get("context_id")):
        errors.append("target_context_id_required")
    if not _text(request.get("reopen_handle")):
        errors.append("reopen_handle_required")
    expected = source.get("expected_hash")
    if expected is not None and (not isinstance(expected, str) or not HASH.fullmatch(expected)):
        errors.append("expected_hash_must_be_full_sha256")

    facts = target.get("facts", {})
    fact_refs: dict[str, list[str]] = {}
    if not isinstance(facts, Mapping):
        errors.append("target_facts_must_be_object")
        facts = {}
    for field, fact in facts.items():
        if not _text(field) or not isinstance(fact, Mapping):
            errors.append("target_fact_must_be_named_object")
            continue
        if set(fact) - {"value", "evidence_refs"}:
            errors.append(f"unsupported_fact_fields:{field}")
        fact_refs[field] = _refs(fact.get("evidence_refs", []), f"fact:{field}:evidence_refs", errors)

    content = source.get("supplied_content")
    conditions = content.get("applicability_conditions", []) if isinstance(content, Mapping) else []
    unresolved = content.get("unresolved", []) if isinstance(content, Mapping) else []
    unresolved = _refs(unresolved, "source_unresolved", errors)
    if not isinstance(conditions, list) or len(conditions) > MAX_CONDITIONS:
        errors.append("conditions_must_be_list_of_at_most_256")
        conditions = []
    seen: set[str] = set()
    normalized: list[tuple[Mapping[str, Any], list[str]]] = []
    for condition in conditions:
        if not isinstance(condition, Mapping):
            errors.append("condition_must_be_object")
            continue
        if set(condition) - {"condition_id", "field", "equals", "evidence_refs"}:
            errors.append("unsupported_condition_fields")
        cid = condition.get("condition_id")
        if not _text(cid) or not _text(condition.get("field")) or "equals" not in condition:
            errors.append("condition_id_field_and_equals_required")
            continue
        if cid in seen:
            errors.append(f"duplicate_condition:{cid}")
        seen.add(cid)
        refs = _refs(condition.get("evidence_refs", []), f"condition:{cid}:evidence_refs", errors)
        normalized.append((condition, refs))
    if errors:
        return invalid(errors)

    observed = digest(content) if content is not None else None
    if content is None:
        preservation = "MISSING"
    elif expected is None:
        preservation = "UNVERIFIED"
    elif observed != expected:
        preservation = "CHANGED"
    elif "expected_version" in source and source["expected_version"] != source["version"]:
        preservation = "STALE"
    else:
        preservation = "MATCH"

    residuals = list(unresolved)
    if preservation != "MATCH":
        residuals.append(f"source_preservation:{preservation}")
    if not conditions:
        residuals.append("no_bound_applicability_conditions")
    checks = []
    all_refs: list[str] = []
    for condition, refs in normalized:
        field, cid = condition["field"], condition["condition_id"]
        fact = facts.get(field, {})
        receiving_refs = fact_refs.get(field, [])
        missing = []
        if not refs:
            missing.append("source_condition_evidence_missing")
        if "value" not in fact:
            missing.append("target_value_missing")
        if not receiving_refs:
            missing.append("target_evidence_missing")
        if preservation != "MATCH":
            missing.append("source_not_preserved")
        state = ("UNRESOLVED" if missing else
                 "MATCH" if digest(condition["equals"]) == digest(fact["value"]) else "MISMATCH")
        check = {"condition_id": cid, "field": field, "status": state,
                 "expected": condition["equals"], "target_value_supplied": "value" in fact,
                 "source_evidence_refs": refs, "target_evidence_refs": receiving_refs,
                 "residuals": missing}
        if "value" in fact:
            check["observed"] = fact["value"]
        checks.append(check)
        residuals.extend(f"{cid}:{reason}" for reason in missing)
        all_refs.extend(refs + receiving_refs)
    if any(check["status"] == "MISMATCH" for check in checks):
        applicability = "MISMATCHED"
    elif residuals:
        applicability = "UNRESOLVED"
    else:
        applicability = "MATCHES_DECLARED_CONDITIONS"
    return result(
        "context_applicability", status="REVIEWED", contract="hearthline.context-applicability.v1",
        source_preservation={"status": preservation, "source_id": source["source_id"],
                             "version": source["version"], "expected_version": source.get("expected_version"),
                             "expected_hash": expected, "observed_hash": observed,
                             "hash_domain": "hearthline_canonical_json_utf8",
                             "semantic_fidelity": "NOT_ASSESSED", "authenticity": "NOT_ASSESSED"},
        target_applicability={"status": applicability, "context_id": target["context_id"],
                              "target_hash": digest(target), "comparison": "ALL_DECLARED_EXACT_EQUALITIES",
                              "checks": checks},
        evidence_refs=list(dict.fromkeys(all_refs)), evidence_independence="NOT_ASSESSED",
        residuals=list(dict.fromkeys(residuals)), reopen_handle=request["reopen_handle"],
        review_input_hash=digest(request), admission_effect="NONE", training_effect="NONE",
        notice="Supplied declarations only. A match neither proves meaning or truth nor permits use. "
               "Retrieve missing evidence or revise the scoped account, then review the current target again.",
    )
