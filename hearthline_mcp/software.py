"""Bounded software-mechanism profiles for the public Hearthline toolkit.

The profiles are deliberately model-neutral.  FBT gives a caller a small
state machine with an append-only trace; A0BK, P3LA, and carrier profiles are
finite adapters around declared records.  None of them creates authority or
executes an external action.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Mapping

from .store import SharedScopedStore

MAX_JSON = 100_000
MAX_ITEMS = 256
MODES = {"TRACE_ONLY", "SHADOW", "GOVERNING"}


def _safe(value: Any) -> bool:
    try:
        raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
        if len(raw.encode("utf-8")) > MAX_JSON:
            return False
        def walk(v: Any, depth: int = 0) -> None:
            if depth > 24:
                raise ValueError("depth")
            if isinstance(v, dict):
                if len(v) > 10_000 or not all(isinstance(k, str) for k in v):
                    raise ValueError("object")
                for x in v.values(): walk(x, depth + 1)
            elif isinstance(v, list):
                if len(v) > 10_000: raise ValueError("list")
                for x in v: walk(x, depth + 1)
            elif v is None or isinstance(v, (str, bool, int)):
                return
            else:
                raise ValueError("value")
        walk(value)
        return True
    except (TypeError, ValueError, OverflowError, UnicodeError, RecursionError):
        return False


def _digest(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _out(status: str, **fields: Any) -> dict[str, Any]:
    return {"status": status, "effects": [], "authority_effect": "NONE", "execution_effect": "NONE", **fields}


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 4096


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _validate_trace_event(event: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(event, Mapping): return ["event: object required"]
    if not _text(event.get("event_id")): errors.append("event_id: required")
    if not _text(event.get("operation")): errors.append("operation: required")
    if not _safe(dict(event)): errors.append("event: bounded JSON required")
    return errors


@dataclass(frozen=True)
class OperatorAuthority:
    """Read-only operator binding captured when an engine is constructed."""
    operator_id: str
    policy_ref: str
    allowed_internal_actions: tuple[str, ...]


class SoftwareEngine:
    """FBT engine with explicit trace, shadow, and governing boundaries."""

    def __init__(self, store: SharedScopedStore, *, mode: str = "TRACE_ONLY",
                 policy_ref: str | None = None, operator_id: str = "operator",
                 allowed_internal_actions: list[str] | tuple[str, ...] = ()) -> None:
        if mode not in MODES: raise ValueError("mode must be TRACE_ONLY, SHADOW, or GOVERNING")
        if mode == "GOVERNING" and not _text(policy_ref):
            raise ValueError("GOVERNING requires an explicit policy_ref")
        if not _text(operator_id): raise ValueError("operator_id required")
        if not all(_text(x) for x in allowed_internal_actions): raise ValueError("internal actions must be named")
        self.store = store
        self.mode = mode
        self.authority = OperatorAuthority(operator_id, policy_ref or "", tuple(allowed_internal_actions))
        self._state: dict[str, Any] = {}

    def _trace(self, operation: str, payload: Mapping[str, Any], *, outcome: str = "RECORDED") -> dict[str, Any]:
        event = {"record_type": "software.trace", "event_id": _digest({"operation": operation, "payload": payload, "at": _now()}),
                 "operation": operation, "payload": dict(payload), "mode": self.mode,
                 "operator_id": self.authority.operator_id, "outcome": outcome, "recorded_at": _now()}
        return self.store.append(event)

    def read_trace(self) -> dict[str, Any]:
        rows = self.store.read()["records"]
        return _out("TRACE_READ", trace=[x for x in rows if isinstance(x, dict) and x.get("record_type") == "software.trace"], immutable=True)

    def read_computation(self) -> dict[str, Any]:
        return _out("VOLATILE_COMPUTATION", computation=dict(self._state), persisted=False,
                    restart_behavior="RESET_VOLATILE_STATE_TRACE_REMAINS")

    def update_computation(self, key: str, value: Any) -> dict[str, Any]:
        if not _text(key) or not _safe(value): return _out("REJECTED", reason="bounded key and JSON value required")
        before = self._state.get(key)
        try:
            self._trace("computation.update", {"key": key, "before_hash": _digest(before), "after_hash": _digest(value)})
        except Exception as exc:
            return _out("REJECTED", reason="trace append failed; computation unchanged", error=type(exc).__name__)
        self._state[key] = value
        return _out("UPDATED", key=key, value=value, mutable_computation=True, persisted=False,
                    restart_behavior="RESET_VOLATILE_STATE_TRACE_REMAINS", authority_record_read_only=True)

    def propose_transition(self, transition: Mapping[str, Any]) -> dict[str, Any]:
        errors = _validate_trace_event(transition)
        if not _text(transition.get("target_state")): errors.append("target_state: required")
        if errors: return _out("INVALID", errors=errors)
        proposal = dict(transition)
        self._trace("transition.propose", proposal, outcome="PROPOSED")
        return _out("PROPOSED", transition=proposal, executed=False, external_action=False)

    def shadow_compare(self, actual: Any, proposed: Any) -> dict[str, Any]:
        if not (_safe(actual) and _safe(proposed)): return _out("INVALID", reason="bounded JSON values required")
        equal = actual == proposed
        self._trace("transition.shadow_compare", {"actual_hash": _digest(actual), "proposed_hash": _digest(proposed), "equal": equal}, outcome="MATCH" if equal else "DIVERGENCE")
        return _out("MATCH" if equal else "DIVERGENCE", equal=equal, executed=False, external_action=False,
                    actual_hash=_digest(actual), proposed_hash=_digest(proposed))

    def govern_transition(self, action: str, state_key: str, value: Any) -> dict[str, Any]:
        if self.mode != "GOVERNING": return _out("REJECTED", reason="GOVERNING mode is required", executed=False)
        if action not in self.authority.allowed_internal_actions: return _out("REJECTED", reason="action not in constructor-bound internal policy", executed=False)
        if not _text(state_key) or not _safe(value): return _out("REJECTED", reason="bounded internal state required", executed=False)
        previous = self._state.get(state_key)
        try:
            self._trace("transition.govern", {"action": action, "state_key": state_key, "before_hash": _digest(previous), "after_hash": _digest(value)}, outcome="APPLIED")
        except Exception as exc:
            return _out("REJECTED", reason="trace append failed; computation unchanged", error=type(exc).__name__, executed=False)
        self._state[state_key] = value
        return _out("APPLIED", action=action, state_key=state_key, executed=True, external_action=False, authority_policy=self.authority.policy_ref)


def fbt_operation(payload: Mapping[str, Any], *, engine: SoftwareEngine | None = None) -> dict[str, Any]:
    if not isinstance(payload, Mapping) or not _safe(dict(payload)): return _out("INVALID", reason="bounded operation required")
    attempted_authority = {"mode", "policy_ref", "operator_id", "allowed_internal_actions", "authority", "grant"} & set(payload)
    if attempted_authority:
        return _out("REJECTED", reason="authority and mode are constructor-bound", rejected_fields=sorted(attempted_authority))
    op = payload.get("operation")
    if op == "capability": return _out("DECLARED", modes=sorted(MODES), default_mode="TRACE_ONLY", governing_requires="constructor policy_ref and finite internal action allowlist")
    if engine is None: return _out("UNBOUND", reason="an engine-bound operation is required for persistence")
    if op == "trace": return engine._trace(str(payload.get("name", "unnamed")), dict(payload), outcome="RECORDED")
    if op == "propose": return engine.propose_transition(payload)
    if op == "shadow": return engine.shadow_compare(payload.get("actual"), payload.get("proposed"))
    if op == "govern": return engine.govern_transition(str(payload.get("action", "")), str(payload.get("state_key", "")), payload.get("value"))
    return _out("INVALID", reason="unsupported FBT operation")


def a0bk_operation(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Adapt a proposed PAL 2.2 A0BK grammar to the PAL 2.3 checker."""
    if not isinstance(payload, Mapping) or not _safe(dict(payload)): return _out("INVALID", reason="bounded object required")
    operation = payload.get("operation")
    mapping = {"ROOT": "ROOT", "APPEND": "APPEND", "CHILD": "CHILD", "VERSION": "VERSION", "SUCCESSOR": "SUCCESSOR"}
    if operation not in mapping: return _out("INVALID", reason="A0BK operation must be ROOT, APPEND, CHILD, VERSION, or SUCCESSOR")
    try:
        from seedpea_foundation import review_pal_packet
        checked = review_pal_packet(dict(payload))
    except Exception as exc:
        checked = {"status": "UNAVAILABLE", "error": type(exc).__name__}
    outer = "INVALID_ADAPTED_INPUT" if checked.get("status") == "INVALID_INPUT" else ("UNAVAILABLE" if checked.get("status") == "UNAVAILABLE" else "ADAPTED")
    return _out(outer, source="A0BK", source_version="0.10.0", source_pal="2.2", target_pal="2.3",
                operation=mapping[operation], foundation_check=checked,
                mapping_class="ADAPTED", residuals=["A0BK grammar is proposed PAL 2.2-oriented input; PAL 2.3 account semantics remain separately checked."],
                semantic_authority="NONE")


def p3la_compose(payload: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, Mapping) or not _safe(dict(payload)): return _out("INVALID", reason="bounded object required")
    edges = payload.get("edges", [])
    if not isinstance(edges, list) or len(edges) > MAX_ITEMS: return _out("INVALID", reason="bounded edge list required")
    errors: list[str] = []; graph: dict[str, list[str]] = {}; ids: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for edge in edges:
        if not isinstance(edge, Mapping) or not all(_text(edge.get(k)) for k in ("edge_id", "input_hash", "output_hash", "schema", "domain")):
            errors.append("edge: typed input/output/schema/domain required"); continue
        if str(edge["edge_id"]) in ids: errors.append("edge_id: unique IDs required")
        ids.add(str(edge["edge_id"]))
        if edge.get("disagreement") not in (None, False, True, "DECLARED", "UNRESOLVED"): errors.append("edge.disagreement: unsupported")
        if "output_claims" in edge and (not isinstance(edge["output_claims"], list) or not all(_safe(x) for x in edge["output_claims"])):
            errors.append("output_claims: bounded JSON list required")
        if "input_value" in edge and _digest(edge["input_value"]) != edge["input_hash"]:
            errors.append("input_hash: does not bind supplied input_value")
        if "output_value" in edge and _digest(edge["output_value"]) != edge["output_hash"]:
            errors.append("output_hash: does not bind supplied output_value")
        normalized.append(dict(edge)); graph.setdefault(str(edge["input_hash"]), []).append(str(edge["output_hash"]))
    if errors: return _out("INVALID", errors=errors)
    cycles: list[list[str]] = []; visiting: set[str] = set(); visited: set[str] = set()
    def visit(node: str, path: list[str]) -> None:
        if node in visiting:
            cycles.append(path[path.index(node):] + [node]); return
        if node in visited: return
        visiting.add(node)
        for nxt in graph.get(node, []): visit(nxt, path + [node])
        visiting.remove(node); visited.add(node)
    for node in list(graph): visit(node, [])
    alternatives = [e for e in normalized if e.get("disagreement") in (True, "DECLARED", "UNRESOLVED")]
    policy = payload.get("fusion_policy")
    fused = None; intersection: list[str] | None = None
    schemas = {e["schema"] for e in normalized}; domains = {e["domain"] for e in normalized}
    claim_sets = [{json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for x in e["output_claims"]} for e in normalized if isinstance(e.get("output_claims"), list)]
    if claim_sets:
        intersection = sorted(set.intersection(*claim_sets))
    if policy == "EXPLICIT_INTERSECTION" and not alternatives and normalized and len(schemas) == 1 and len(domains) == 1 and len(claim_sets) == len(normalized):
        fused = {"edge_ids": [e["edge_id"] for e in normalized], "policy": policy, "schema": next(iter(schemas)), "domain": next(iter(domains)), "intersection_outputs": [json.loads(x) for x in intersection or []], "claim": "FINITE_INTERSECTION_ONLY"}
    return _out("COMPOSED" if not cycles else "INVALID", edges=normalized, cycles=cycles, alternatives=alternatives,
                fusion=fused, intersection_outputs=[json.loads(x) for x in intersection or []] if intersection is not None else None,
                consensus=False, fusion_policy=policy,
                hash_status="VERIFIED_CONTENT_HASHES" if normalized and all("input_value" in e and "output_value" in e for e in normalized) else "DECLARED_HASHES",
                residuals=["No fusion policy, disagreement, schema mismatch, or domain mismatch keeps alternatives unfused."] if fused is None else [])


def carrier_contract(payload: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, Mapping) or not _safe(dict(payload)): return _out("INVALID", reason="bounded object required")
    required = ("carrier_id", "operator", "write", "transport", "readout")
    missing = [x for x in required if not _text(payload.get(x))]
    if missing: return _out("INCOMPLETE", missing=missing, semantic_claim=False)
    return _out("DECLARED_CONTRACT", carrier_id=payload["carrier_id"], operator=payload["operator"], write=payload["write"], transport=payload["transport"], readout=payload["readout"], semantic_equivalence=False, performance_claim=False)


def c2c_capability(payload: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, Mapping) or not _safe(dict(payload)): return _out("INVALID", reason="bounded object required")
    host = payload.get("model_host")
    if not _text(host): return _out("INCOMPLETE", missing=["model_host"], experiment_status="NOT_RUN")
    internals = payload.get("kv_cache_access") is True and payload.get("local_model_internals") is True
    return _out("PREREQUISITES_DECLARED_NOT_VERIFIED" if internals else "UNAVAILABLE_API_OR_KV_ACCESS", model_host=host,
                kv_cache_access=bool(payload.get("kv_cache_access")), experiment_status="NOT_RUN", semantic_claim=False, speed_claim=False, learned_bridge_verified=False, residual="Actual compatible-model experiment and learned bridge are not included.")


TOOLS: dict[str, Callable[..., dict[str, Any]]] = {
    "software.fbt": fbt_operation,
    "software.a0bk": a0bk_operation,
    "software.p3la": p3la_compose,
    "software.carrier_contract": carrier_contract,
    "software.c2c_capability": c2c_capability,
}

TOOL_DESCRIPTIONS = {name: (fn.__doc__ or name).strip().split("\n")[0] for name, fn in TOOLS.items()}
