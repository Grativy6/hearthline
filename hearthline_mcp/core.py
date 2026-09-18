"""Stateless Hearthline toolkit operations.

Every operation returns a typed record with explicit effects.  These helpers
do not grant permission, renew authority, infer truth, or execute a task.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Mapping

VERSION = "0.1.0"
MAX_PACKET_CHARS = 100_000
MAX_ITEMS = 256
DEPENDENCY_RELATIONS = {"supports", "depends_on", "load_bearing", "compares", "derived_from"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def result(kind: str, **fields: Any) -> dict[str, Any]:
    return {
        "kind": kind,
        "toolkit_version": VERSION,
        "authority_effect": "NONE",
        "execution_effect": "NONE",
        "observed_at": now(),
        **fields,
    }


def finite_packet(items: list[Mapping[str, Any]], *, purpose: str = "") -> dict[str, Any]:
    bounded = list(items[:MAX_ITEMS])
    packet = {"purpose": purpose, "items": bounded, "item_count": len(bounded)}
    encoded = json.dumps(packet, ensure_ascii=False, sort_keys=True)
    if len(encoded) > MAX_PACKET_CHARS:
        raise ValueError("packet exceeds the bounded input limit")
    return result("finite_packet", packet=packet, packet_hash=digest(packet), truncated=len(items) > len(bounded))


def inspect_context(request: Mapping[str, Any]) -> dict[str, Any]:
    protected = list(request.get("protected_questions") or [])
    losses = list(request.get("declared_losses") or [])
    alternatives = list(request.get("alternatives") or [])
    return result(
        "context_inspection",
        protected_questions=protected,
        declared_losses=losses,
        alternatives=alternatives,
        unresolved=[q for q in protected if q in losses],
        coverage_status="PARTIAL" if losses else "DECLARED",
        notice="A compact packet is a route and coverage account, not a claim of full semantic preservation.",
    )


def compact(request: Mapping[str, Any]) -> dict[str, Any]:
    items = request.get("items", [])
    protected = request.get("protected_questions", [])
    if not isinstance(items, list) or not all(isinstance(item, dict) and isinstance(item.get("id"), str) and item["id"] for item in items):
        return result("compact_context", status="INVALID", errors=["items must be finite objects with IDs"])
    if len({item["id"] for item in items}) != len(items):
        return result("compact_context", status="INVALID", errors=["duplicate item IDs"])
    if not isinstance(protected, list) or not all(isinstance(q, str) and q for q in protected):
        return result("compact_context", status="INVALID", errors=["protected questions must be a finite string list"])
    budget = request.get("max_items", min(len(items), MAX_ITEMS))
    if type(budget) is not int or not 0 <= budget <= MAX_ITEMS:
        return result("compact_context", status="INVALID", errors=["max_items must be a bounded nonnegative integer"])
    from .store import canonical_json
    try:
        canonical_json(dict(request))
    except (ValueError, TypeError, RecursionError):
        return result("compact_context", status="INVALID", errors=["bounded finite JSON required"])
    if not isinstance(request.get("model_profile", "default"), str) or not isinstance(request.get("recovery_limits", {}), Mapping):
        return result("compact_context", status="INVALID", missing=["model_profile/recovery_limits"], authority_effect="NONE")
    kept = items[:budget]
    omitted = items[budget:]
    losses = [str(x.get("id", i)) for i, x in enumerate(omitted) if isinstance(x, Mapping)]
    packet = {
        "items": kept,
        "protected_questions": protected,
        "omitted_ids": losses,
        "source_bindings": list(request.get("source_bindings") or []),
        "alternatives": list(request.get("alternatives") or []),
        "purpose": request.get("purpose"),
        "model_profile": request.get("model_profile", "default"),
        "recovery_limits": dict(request.get("recovery_limits") or {}),
        "budget": {"max_items": budget},
        "recovery_route": request.get("recovery_route"),
    }
    return result(
        "compact_context",
        packet=packet,
        packet_hash=digest(packet),
        omitted_count=len(omitted),
        protected_questions=protected,
        declared_losses=losses,
        recovery_route=request.get("recovery_route"),
        status="COMPACTED",
    )


def collision_check(request: Mapping[str, Any]) -> dict[str, Any]:
    left = request.get("left") or {}
    right = request.get("right") or {}
    left_packet = request.get("left_retained_packet", left.get("retained_packet", left.get("packet", left)))
    right_packet = request.get("right_retained_packet", right.get("retained_packet", right.get("packet", right)))
    protected = list(request.get("protected_questions") or [])
    same_packet = digest(left_packet) == digest(right_packet)
    left_answers = left.get("protected_answers", request.get("left_protected_answers"))
    right_answers = right.get("protected_answers", request.get("right_protected_answers"))
    if left_answers is None or right_answers is None:
        return result("compaction_collision", same_packet=same_packet, status="INSUFFICIENT_EVIDENCE",
                      protected_questions=protected, notice="Both protected answer records are required to classify a collision.")
    collision = same_packet and left_answers != right_answers
    return result(
        "compaction_collision",
        same_packet=same_packet,
        same_protected_answers=left_answers == right_answers,
        protected_questions=protected,
        status="COLLISION_REVIEW_REQUIRED" if collision else "NO_DECLARED_COLLISION",
        notice="A collision is an observation for review; this operation does not select a winner.",
    )


def repair_context(request: Mapping[str, Any]) -> dict[str, Any]:
    if all(key in request for key in ("source_map", "readout_map", "side_trace_map", "protected_query")):
        from .science_math import bridge_repair
        checked = bridge_repair(dict(request))
        return result("context_repair", route="bridge_finite_repair", contract=checked,
                      restored=checked.get("protected_answers", {}), missing=[], status=checked.get("status", "UNKNOWN"))
    available = list(request.get("available_items") or [])
    needed = list(request.get("needed_ids") or [])
    by_id = {str(x.get("id")): x for x in available if isinstance(x, Mapping) and "id" in x}
    restored = [by_id[i] for i in needed if i in by_id]
    missing = [i for i in needed if i not in by_id]
    return result("context_repair", restored=restored, missing=missing, status="REPAIRED" if not missing else "PARTIAL")


def observation(request: Mapping[str, Any]) -> dict[str, Any]:
    from .science_math import observation_contract
    checked = observation_contract(dict(request))
    return result("observation", observation=dict(request), contract=checked,
                  claim_status=request.get("claim_status", "OBSERVED"), status=checked.get("status", "INCOMPLETE"))


def dependency_record(request: Mapping[str, Any]) -> dict[str, Any]:
    required = {"dependency_id", "source_id", "dependent_id", "relation"}
    missing = sorted(required - set(request))
    relation = request.get("relation")
    invalid: list[str] = []
    for field in ("adopted", "provisional", "load_bearing"):
        if field in request and type(request[field]) is not bool:
            invalid.append(f"{field}_must_be_boolean")
    origin = str(request.get("origin", "")).upper()
    model_proposed = origin in {"MODEL", "MODEL_GENERATED", "MODEL_PROPOSED"} or request.get("model_generated") is True
    adopted = request.get("adopted", False)
    provisional = request.get("provisional", True)
    adoption_ref = request.get("adoption_ref")
    if model_proposed and adopted and not isinstance(adoption_ref, str):
        invalid.append("model_edge_requires_distinct_adoption_ref")
    if adopted and provisional:
        invalid.append("adopted_edge_cannot_remain_provisional")
    if adopted and not isinstance(adoption_ref, str):
        invalid.append("adopted_edge_requires_adoption_ref")
    if request.get("source_id") == request.get("dependent_id"):
        return result("dependency_record", dependency=dict(request), status="INVALID", missing=missing,
                      invalid=["self_dependency"], provisional=bool(request.get("provisional", True)), adopted=False)
    if not isinstance(relation, str) or relation not in DEPENDENCY_RELATIONS:
        return result("dependency_record", dependency=dict(request), status="INVALID", missing=missing,
                      invalid=sorted(set(invalid + ["relation"]),), relation_allowed=sorted(DEPENDENCY_RELATIONS),
                      provisional=provisional, adopted=False)
    if not all(isinstance(request.get(k), str) and request.get(k).strip() for k in ("source_id", "dependent_id")):
        missing.append("source/dependent_reference")
    if invalid:
        return result("dependency_record", dependency=dict(request), status="INVALID", missing=sorted(set(missing)), invalid=sorted(set(invalid)), provisional=provisional, adopted=False)
    return result("dependency_record", dependency=dict(request), status="VALID" if not missing else "INCOMPLETE", missing=sorted(set(missing)), provisional=provisional, adopted=adopted)


def dependency_correction(request: Mapping[str, Any]) -> dict[str, Any]:
    source = str(request.get("source_id", ""))
    edges = list(request.get("edges") or [])
    nodes = {str(x) for x in (request.get("known_nodes") or [])}
    nodes.update(str(e.get("source_id")) for e in edges if isinstance(e, Mapping))
    nodes.update(str(e.get("dependent_id")) for e in edges if isinstance(e, Mapping))
    outgoing: dict[str, list[str]] = {}
    invalid = []
    for edge in edges:
        if not isinstance(edge, Mapping) or not {"source_id", "dependent_id"} <= set(edge):
            invalid.append(edge); continue
        a, b = str(edge["source_id"]), str(edge["dependent_id"])
        if a not in nodes or b not in nodes: invalid.append(edge); continue
        if edge.get("adopted") is True and edge.get("provisional") is False and edge.get("load_bearing") is True:
            outgoing.setdefault(a, []).append(b)
    affected, seen, cycles = [], {source}, []
    def walk(current: str, path: list[str]) -> None:
        for dependent in outgoing.get(current, []):
            if dependent in path:
                cycles.append(path[path.index(dependent):] + [dependent])
                continue
            if dependent not in seen:
                seen.add(dependent)
                affected.append(dependent)
                walk(dependent, path + [dependent])
    walk(source, [source])
    return result("dependency_correction", source_id=source, reconsider=affected, invalid_edges=invalid,
                  preserved_history=True, status="REOPEN_DEPENDENTS" if affected else "NO_DECLARED_DEPENDENTS",
                  non_load_bearing_preserved=True, provisional_edges_excluded=True,
                  cycles=cycles, residual="CYCLE_REVIEW_REQUIRED" if cycles else None)


def tether(request: Mapping[str, Any]) -> dict[str, Any]:
    required = {"tether_id", "task_id", "scope", "return_target", "finish_condition"}
    missing = sorted(required - set(request))
    body = dict(request)
    return result("tether", tether=body, tether_hash=digest(body), status="BOUND" if not missing else "INCOMPLETE", missing=missing, authority_renewal="NONE")


def heartbeat(request: Mapping[str, Any]) -> dict[str, Any]:
    state = request.get("state", "UNKNOWN")
    return result("heartbeat", state=state, material_change=request.get("material_change"), blocker=request.get("blocker"), finish_condition=request.get("finish_condition"), authority_renewal="NONE", scheduling_effect="NONE")


def custody(request: Mapping[str, Any]) -> dict[str, Any]:
    required = {"source_perch", "destination_perch", "payload_hash", "grant_ref"}
    missing = sorted(required - set(request))
    return result("custody", custody=dict(request), status="BOUND" if not missing else "INCOMPLETE", missing=missing, ledger_merge="NONE", authority_effect="NONE")


def formation(request: Mapping[str, Any]) -> dict[str, Any]:
    members = list(request.get("members") or [])
    return result("formation", formation_id=request.get("formation_id"), members=members, completion_keeper=request.get("completion_keeper"), dispatch_effect="NONE", authority_effect="NONE", status="VALID" if members else "INCOMPLETE")


def status_manifest() -> dict[str, Any]:
    return {"name": "hearthline-toolkit", "version": VERSION, "mode": "public_model_plus_mechanisms", "lore_default": False, "effects": {"authority": "NONE", "execution": "NONE", "scheduling": "NONE"}}
