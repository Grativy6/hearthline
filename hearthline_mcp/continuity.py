"""Persistent TETHER, heartbeat, custody, and bounded-formation contracts."""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any, Mapping

from .store import SharedScopedStore, canonical_json, sha256_text

def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def _hash(value: Any) -> str:
    return sha256_text(canonical_json(value))

def _required(obj: Mapping[str, Any], fields: set[str]) -> list[str]:
    return sorted(k for k in fields if k not in obj)

def _text(value: Any) -> bool:
    return isinstance(value, str) and 0 < len(value.strip()) <= 4096

def _aware(value: Any):
    if not _text(value):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None
    except ValueError:
        return None

def _pulse_intent(request):
    return _hash({"cost": request.get("cost", 1), "state": request.get("state", "UNKNOWN"),
                  "material_change": request.get("material_change"), "blocker": request.get("blocker"),
                  "finish_condition": request.get("finish_condition"), "completion_evidence_ref": request.get("completion_evidence_ref")})

def _source_check(declared: list[Any], supplied: list[Any] | None = None) -> tuple[str, list[str]]:
    """Verify source identity only when actual content is supplied."""
    if not isinstance(declared, list) or supplied is not None and not isinstance(supplied, list):
        return "UNVERIFIED", ["sources_must_be_lists"]
    supplied_by_id = {}
    for item in supplied or []:
        if not isinstance(item, Mapping) or not _text(item.get("source_id")):
            return "UNVERIFIED", ["invalid_retrieved_source"]
        if item["source_id"] in supplied_by_id:
            return "UNVERIFIED", ["duplicate_retrieved_source:" + item["source_id"]]
        supplied_by_id[item["source_id"]] = item
    errors = []
    seen = set()
    for source in declared:
        if not isinstance(source, Mapping) or not _text(source.get("source_id")) or not source.get("version") or not source.get("hash"):
            errors.append("invalid_source_binding"); continue
        if source["source_id"] in seen:
            errors.append("duplicate_source_binding:" + source["source_id"])
        seen.add(source["source_id"])
        actual = supplied_by_id.get(str(source["source_id"]))
        if actual is None:
            errors.append("source_not_retrieved:" + str(source["source_id"])); continue
        if actual.get("version") != source.get("version"):
            errors.append("source_stale:" + str(source["source_id"])); continue
        content = actual.get("content", actual.get("value"))
        if "content" not in actual and "value" not in actual:
            errors.append("source_hash_unverified:" + str(source["source_id"])); continue
        if _hash(content) != source.get("hash"):
            errors.append("source_changed:" + str(source["source_id"]))
    return ("VERIFIED" if not errors else "UNVERIFIED", errors)

class ContinuityEngine:
    """Stateful continuity primitives; no method grants or renews authority."""
    def __init__(self, store: SharedScopedStore) -> None:
        self.store = store

    def _events(self, kind: str, ident: str) -> list[dict[str, Any]]:
        return [x for x in self.store.read()["records"] if x.get("kind") == kind and x.get("id") == ident]

    def bind_tether(self, request: Mapping[str, Any]) -> dict[str, Any]:
        expected_head = self.store.verify()["head"]
        missing = _required(request, {"tether_id", "task_id", "scope", "grant_ref", "finish_condition", "residual", "return_target"})
        missing += [k for k in ("tether_id", "task_id", "scope", "grant_ref", "finish_condition", "residual", "return_target") if k not in missing and not _text(request.get(k))]
        sources = request.get("source_bindings", [])
        source_status, source_errors = _source_check(sources, request.get("retrieved_sources"))
        body = {"kind": "tether.bind", "id": str(request.get("tether_id", "")), "task_id": request.get("task_id"), "scope": request.get("scope"), "grant_ref": request.get("grant_ref"), "finish_condition": request.get("finish_condition"), "residual": request.get("residual"), "return_target": request.get("return_target"), "reopen_handle": request.get("reopen_handle", request.get("tether_id")), "source_bindings": sources, "source_status": source_status, "authority_renewal": "NONE", "bound_at": _now()}
        if missing or source_errors:
            return {"kind": "tether", "status": "INCOMPLETE", "missing": missing, "source_errors": source_errors, "authority_renewal": "NONE"}
        prior = self._events("tether.bind", body["id"])
        if prior:
            frozen = {k: prior[-1].get(k) for k in ("task_id", "scope", "grant_ref", "finish_condition", "source_bindings")}
            proposed = {k: body.get(k) for k in frozen}
            if frozen != proposed:
                return {"kind": "tether", "status": "CONFLICTING_REBIND", "tether_id": body["id"], "preserved_history": True, "authority_renewal": "NONE"}
            return {**prior[-1], "status": "BOUND", "idempotent_retry": True, "authority_renewal": "NONE"}
        written = self.store.append_if_head(expected_head, body)
        if written is None:
            return {"kind": "tether", "status": "CONCURRENT_STATE_CHANGED", "authority_renewal": "NONE"}
        return written | {"status": "BOUND", "tether_hash": _hash(body), "authority_renewal": "NONE"}

    def read_tether(self, tether_id: str) -> dict[str, Any]:
        events = [r for r in self.store.read()["records"] if r.get("id") == tether_id and r.get("kind") in ("tether.bind", "tether.reopen")]
        binds = [r for r in events if r.get("kind") == "tether.bind"]
        if not binds:
            return {"kind": "tether", "status": "MISSING", "tether_id": tether_id, "reopenable": False}
        return {"kind": "tether", "status": "BOUND", "tether": binds[-1], "history": events, "reopenable": True, "authority_renewal": "NONE"}

    def reopen_tether(self, request: Mapping[str, Any]) -> dict[str, Any]:
        # A TETHER explicitly upgraded with a work checkpoint must use that
        # checkpoint's current predicates. The legacy route cannot skip them.
        checkpoints = [r for r in self.store.read()["records"] if r.get("kind") == "work.checkpoint"
                       and r.get("tether_id") == request.get("tether_id")]
        if checkpoints:
            return {"kind": "tether.reopen", "status": "CHECKPOINT_REVIEW_REQUIRED",
                    "checkpoint_id": checkpoints[-1]["id"], "route": "reopen_work_checkpoint",
                    "authority_renewal": "NONE", "reopened": False}
        current = self.read_tether(str(request.get("tether_id", "")))
        if current["status"] != "BOUND":
            return {"kind": "tether.reopen", "status": "MISSING", "authority_renewal": "NONE"}
        old = current["tether"]
        grant = request.get("current_grant") or {}
        if not isinstance(grant, Mapping):
            return {"kind": "tether.reopen", "status": "GRANT_REVIEW_REQUIRED", "grant_missing": ["current_grant_object"], "authority_renewal": "NONE", "reopened": False}
        grant_missing = sorted({"grant_ref", "task_id", "scope", "observed_at", "expires_at", "revoked", "remaining_budget"} - set(grant))
        ref_ok = not grant_missing and grant.get("grant_ref") == old.get("grant_ref") and grant.get("task_id") == old.get("task_id") and grant.get("scope") == old.get("scope")
        expired = bool(grant.get("expired") or grant.get("revoked") or grant.get("exhausted") or grant.get("revoked") is not False)
        expiry, observed = _aware(grant.get("expires_at")), _aware(grant.get("observed_at"))
        expired = expired or expiry is None or observed is None
        if expiry and observed:
            expired = expired or expiry <= datetime.now(timezone.utc) or expiry <= observed
        expired = expired or (type(grant.get("remaining_budget")) is not int) or grant.get("remaining_budget", 0) <= 0
        source_status, source_errors = _source_check(old.get("source_bindings", []), request.get("retrieved_sources"))
        valid = bool(ref_ok and not grant_missing and not expired and source_status == "VERIFIED")
        if not valid:
            return {"kind": "tether.reopen", "status": "GRANT_REVIEW_REQUIRED" if ref_ok else "GRANT_MISMATCH", "tether_id": old["id"], "grant_ref": old.get("grant_ref"), "grant_missing": grant_missing, "source_errors": source_errors, "authority_renewal": "NONE", "reopened": False}
        event = {"kind": "tether.reopen", "id": old["id"], "task_id": old["task_id"], "residual": request.get("residual", old["residual"]), "source_bindings": old["source_bindings"], "grant_ref": old["grant_ref"], "authority_renewal": "NONE", "reopened_at": _now()}
        return self.store.append(event) | {"status": "REOPENED", "authority_renewal": "NONE", "grant_check": "DECLARED_PARAMETERS_ONLY_NOT_AUTHENTICATED"}

    def create_heartbeat(self, request: Mapping[str, Any]) -> dict[str, Any]:
        expected_head = self.store.verify()["head"]
        missing = _required(request, {"heartbeat_id", "tether_id", "finish_condition", "budget"})
        missing += [k for k in ("heartbeat_id", "tether_id", "finish_condition") if not _text(request.get(k))]
        budget = request.get("budget")
        if missing or type(budget) is not int or budget < 0:
            return {"kind": "heartbeat", "status": "INCOMPLETE", "missing": missing, "authority_renewal": "NONE"}
        tether = self.read_tether(str(request["tether_id"]))
        if tether["status"] != "BOUND" or tether["tether"].get("finish_condition") != request["finish_condition"]:
            return {"kind": "heartbeat", "status": "TETHER_MISMATCH", "authority_renewal": "NONE"}
        existing = self._heartbeat(str(request["heartbeat_id"]))
        if existing:
            frozen = {k: existing.get(k) for k in ("tether_id", "finish_condition", "budget")}
            if any(frozen[k] != request.get(k) for k in frozen):
                return {"kind": "heartbeat", "status": "CONFLICTING_REBIND", "authority_renewal": "NONE"}
            return {**existing, "idempotent_retry": True, "authority_renewal": "NONE"}
        body = {"kind": "heartbeat.create", "id": str(request["heartbeat_id"]), "tether_id": request["tether_id"], "finish_condition": request["finish_condition"], "budget": budget, "remaining": budget, "status": "ACTIVE" if budget else "EXHAUSTED", "authority_renewal": "NONE", "created_at": _now()}
        written = self.store.append_if_head(expected_head, body)
        if written is None:
            return {"kind": "heartbeat", "status": "CONCURRENT_STATE_CHANGED", "authority_renewal": "NONE"}
        return written | {"status": body["status"], "authority_renewal": "NONE"}

    def _heartbeat(self, ident: str) -> dict[str, Any] | None:
        events = self._events("heartbeat.create", ident)
        if not events: return None
        current = dict(events[0])
        for event in self._events("heartbeat.event", ident):
            current.update({k: event[k] for k in ("remaining", "status", "last_state", "last_material_change", "last_blocker") if k in event})
        return current

    def pulse_heartbeat(self, request: Mapping[str, Any]) -> dict[str, Any]:
        ident = str(request.get("heartbeat_id", "")); expected_head = self.store.verify()["head"]; current = self._heartbeat(ident)
        if not current: return {"kind": "heartbeat", "status": "MISSING", "authority_renewal": "NONE"}
        event_id = request.get("event_id")
        if event_id:
            prior = [x for x in self._events("heartbeat.event", ident) if x.get("event_id") == event_id]
            if prior:
                intent = _pulse_intent(request)
                if prior[-1].get("intent_hash") != intent:
                    return {"kind": "heartbeat", "status": "IDEMPOTENCY_CONFLICT", "heartbeat_id": ident, "authority_renewal": "NONE"}
                return {**prior[-1], "status": prior[-1].get("status", "ACTIVE"), "idempotent_retry": True, "authority_renewal": "NONE"}
        if current["status"] in {"SUSPENDED", "COMPLETED", "EXHAUSTED"}:
            return {"kind": "heartbeat", "status": "LATE_PULSE_REJECTED", "heartbeat_id": ident, "authority_renewal": "NONE"}
        cost = request.get("cost", 1)
        if type(cost) is not int or cost < 0 or cost > current["remaining"]:
            return {"kind": "heartbeat", "status": "BUDGET_EXCEEDED", "remaining": current["remaining"], "authority_renewal": "NONE"}
        reported_complete = request.get("state") == "COMPLETED"
        if reported_complete and (request.get("finish_condition") != current["finish_condition"] or not _text(request.get("completion_evidence_ref"))):
            return {"kind": "heartbeat", "status": "COMPLETION_EVIDENCE_REQUIRED", "authority_renewal": "NONE"}
        body = {"kind": "heartbeat.event", "id": ident, "event_id": event_id, "intent_hash": _hash({"cost": cost, "state": request.get("state", "UNKNOWN"), "material_change": request.get("material_change"), "blocker": request.get("blocker")}), "remaining": current["remaining"] - cost, "status": "COMPLETED" if reported_complete else ("EXHAUSTED" if cost == current["remaining"] else "ACTIVE"), "last_state": request.get("state", "UNKNOWN"), "last_material_change": request.get("material_change"), "last_blocker": request.get("blocker"), "authority_renewal": "NONE", "scheduling_effect": "NONE",
                "completion_evidence_ref": request.get("completion_evidence_ref"), "completion_claim": "REPORTED_NOT_PROOF"}
        body["intent_hash"] = _pulse_intent(request)
        written = self.store.append_if_head(expected_head, body)
        if written is None:
            return {"kind": "heartbeat", "status": "CONCURRENT_STATE_CHANGED", "authority_renewal": "NONE"}
        return written | {"status": body["status"], "authority_renewal": "NONE", "scheduling_effect": "NONE"}

    def read_heartbeat(self, heartbeat_id: str) -> dict[str, Any]:
        current = self._heartbeat(str(heartbeat_id))
        return {"kind": "heartbeat", "status": "MISSING", "authority_renewal": "NONE"} if not current else {**current, "liveness_is_completion": False, "authority_renewal": "NONE"}

    def suspend_heartbeat(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return self._change_heartbeat(request, "SUSPENDED")

    def resume_heartbeat(self, request: Mapping[str, Any]) -> dict[str, Any]:
        return self._change_heartbeat(request, "ACTIVE")

    def _change_heartbeat(self, request: Mapping[str, Any], status: str) -> dict[str, Any]:
        expected_head = self.store.verify()["head"]
        current = self._heartbeat(str(request.get("heartbeat_id", "")))
        if not current: return {"kind": "heartbeat", "status": "MISSING", "authority_renewal": "NONE"}
        if current["status"] in ("EXHAUSTED", "COMPLETED"):
            return {"kind": "heartbeat", "status": current["status"], "authority_renewal": "NONE"}
        event = {"kind": "heartbeat.event", "id": request["heartbeat_id"], "remaining": current["remaining"], "status": status, "authority_renewal": "NONE"}
        written = self.store.append_if_head(expected_head, event)
        return ({"kind": "heartbeat", "status": "CONCURRENT_STATE_CHANGED", "authority_renewal": "NONE"} if written is None else written | {"status": status, "authority_renewal": "NONE"})

    def record_custody(self, request: Mapping[str, Any]) -> dict[str, Any]:
        required = {"payload", "payload_hash", "source", "destination", "return_route", "controller_selected"}
        missing = _required(request, required)
        computed = _hash(request.get("payload")) if "payload" in request else None
        if computed != request.get("payload_hash"): return {"kind": "custody", "status": "HASH_MISMATCH", "authority_effect": "NONE"}
        if missing or request.get("controller_selected") is not True: return {"kind": "custody", "status": "SELECTION_REQUIRED", "missing": missing, "authority_effect": "NONE"}
        body = {"kind": "custody", "id": request.get("custody_id", _hash(request.get("payload"))), "payload_hash": computed, "source": request["source"], "destination": request["destination"], "return_route": request["return_route"], "controller_selected": True, "ledger_merge": "NONE", "authority_effect": "NONE"}
        return self.store.append(body) | {"status": "BOUND", "authority_effect": "NONE"}

    def validate_formation(self, request: Mapping[str, Any]) -> dict[str, Any]:
        members = request.get("members", []); errors = []
        errors.extend(k + "_required" for k in ("formation_id", "source", "grant_ref", "return_route", "work", "completion_keeper", "finish_condition") if not _text(request.get(k)))
        if not isinstance(members, list) or not members or len(members) > 256:
            return {"kind":"formation", "status":"INCOMPLETE", "errors":["bounded_members_required"], "dispatch_effect":"NONE", "authority_effect":"NONE"}
        ids = [m.get("identity") for m in members if isinstance(m, Mapping) and _text(m.get("identity"))]
        if len(ids) != len(members) or len(ids) != len(set(ids)): errors.append("distinct_identities_required")
        lanes = {}
        for member in members:
            if not isinstance(member, Mapping) or not all(_text(member.get(k)) for k in ("identity", "role", "lane", "finish_condition", "grant_ref", "return_route")):
                errors.append("complete_lane_manifest_required")
                continue
            if member["role"] not in ("worker", "completion_keeper", "ledger_keeper"):
                errors.append("unsupported_role")
            lanes.setdefault(member["lane"], []).append(member["role"])
            if member["grant_ref"] != request.get("grant_ref"):
                errors.append("lane_grant_mismatch")
        if any(sorted(roles) != ["completion_keeper", "ledger_keeper", "worker"] for roles in lanes.values()):
            errors.append("each_lane_requires_complete_trio")
        if request.get("completion_keeper") not in [m["identity"] for m in members if isinstance(m, Mapping) and m.get("role") == "completion_keeper"]:
            errors.append("completion_keeper_binding_mismatch")
        status = "VALID" if not errors else "INCOMPLETE"
        return {"kind": "formation", "status": status, "formation_id": request.get("formation_id"), "members": list(members), "errors": sorted(set(errors)), "dispatch_effect": "NONE", "authority_effect": "NONE", "derived_completion": "NOT_ASSESSED", "trace_role": "MANIFEST_CHECK_ONLY"}

    def prepare_trace_key(self, request: Mapping[str, Any]) -> dict[str, Any]:
        """Create a portable locator for stored trace, never a grant or capability."""
        required = _required(request, {"record_id", "version", "source_hash", "locators"})
        if not _text(request.get("record_id")) or type(request.get("version")) is not int or request.get("version", 0) < 1:
            required.append("typed_record_identity_version")
        if not _text(request.get("source_hash")) or not isinstance(request.get("locators"), list) or not all(_text(x) for x in request["locators"]):
            required.append("typed_source_hash_locators")
        if required:
            return {"kind": "trace_key", "status": "INCOMPLETE", "missing": required}
        body = {"kind": "trace_key", "id": str(request["record_id"]), "version": request["version"], "source_hash": request["source_hash"], "locators": list(request["locators"]), "namespace": self.store.namespace, "trace_only": True, "authority_effect": "NONE"}
        return self.store.append(body) | {"status": "PREPARED", "authority_effect": "NONE"}

    def resolve_trace_key(self, key: Mapping[str, Any]) -> dict[str, Any]:
        if key.get("namespace") != self.store.namespace:
            return {"kind": "trace_key", "status": "CROSS_SCOPE_REJECTED", "authority_effect": "NONE"}
        records = self.store.read()["records"]
        matches = [x for x in records if x.get("kind") == "trace_key" and x.get("id") == key.get("id") and x.get("version") == key.get("version")]
        if not matches:
            return {"kind": "trace_key", "status": "MISSING", "authority_effect": "NONE"}
        found = matches[-1]
        if found.get("source_hash") != key.get("source_hash"):
            return {"kind": "trace_key", "status": "SOURCE_CHANGED", "authority_effect": "NONE"}
        return {"kind": "trace_key", "status": "RESOLVED", "record": found, "trace_only": True, "authority_effect": "NONE"}
