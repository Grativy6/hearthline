"""Explicit PAL 2.4 work checkpoints in the existing scoped append-only store.

Only supplied work coordinates are frozen. Recovery never restores a grant,
resource balance, audit history, hidden model state or permission to act.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from seedpea_foundation.pal24 import review_pal24_resources, review_pal24_resume
from .store import SharedScopedStore, canonical_json, sha256_text


def _text(value):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 4096


def _time(value):
    if not _text(value):
        return None
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return stamp if stamp.tzinfo is not None and stamp.utcoffset() is not None else None
    except ValueError:
        return None


def _hash(value):
    return sha256_text(canonical_json(value))


def _out(status, **data):
    return {"status": status, "authority_effect": "NONE", "authority_renewal": "NONE",
            "execution_effect": "NONE", "grant_check": "DECLARED_PARAMETERS_ONLY_NOT_AUTHENTICATED", **data}


class CheckpointEngine:
    def __init__(self, store: SharedScopedStore):
        self.store = store

    def _snapshot(self):
        return self.store.read()

    @staticmethod
    def _latest(rows, tether_id):
        return next((r for r in reversed(rows) if r.get("kind") == "work.checkpoint"
                     and r.get("tether_id") == tether_id), None)

    def freeze(self, request: dict[str, Any]):
        allowed = {"tether_id", "checkpoint", "resource_requirement", "predecessor_checkpoint_id", "adoption_ref"}
        if not isinstance(request, dict) or set(request) - allowed:
            return _out("INVALID_INPUT", errors=["unsupported checkpoint request fields"])
        checkpoint = request.get("checkpoint")
        requirement = request.get("resource_requirement")
        if not isinstance(checkpoint, dict) or not _text(checkpoint.get("checkpoint_id")):
            return _out("INVALID_INPUT", errors=["named checkpoint required"])
        if not isinstance(requirement, dict) or set(requirement) != {"unit", "epoch", "boundary", "budget", "next_cost"}:
            return _out("INVALID_INPUT", errors=["explicit resource boundary, unit, epoch, budget and next_cost required"])
        if any(not _text(requirement[k]) for k in ("unit", "epoch", "boundary")) or any(
                type(requirement[k]) is not int or not 0 <= requirement[k] <= 9007199254740991
                for k in ("budget", "next_cost")):
            return _out("INVALID_INPUT", errors=["invalid resource requirement"])
        schema = review_pal24_resume({"operation": "RESUME", "checkpoint": checkpoint,
                                      "observed": checkpoint, "current": {}})
        if schema["status"] == "INVALID_INPUT":
            return _out("INVALID_INPUT", errors=schema["errors"])
        try:
            canonical_json(request)
        except (ValueError, TypeError, RecursionError):
            return _out("INVALID_INPUT", errors=["checkpoint exceeds storage bounds"])
        snapshot = self._snapshot()
        rows = snapshot["records"]
        tether = next((r for r in reversed(rows) if r.get("kind") == "tether.bind"
                       and r.get("id") == request.get("tether_id")), None)
        if tether is None or checkpoint.get("task_id") != tether["task_id"]:
            return _out("TETHER_MISMATCH")
        if not all(isinstance(s, dict) and all(_text(s.get(k)) for k in ("source_id", "version", "hash"))
                   for s in tether["source_bindings"]):
            return _out("TETHER_SOURCE_MISMATCH", errors=["legacy source binding needs explicit repair"])
        inherited = {(s["source_id"], s["version"], s["hash"]) for s in tether["source_bindings"]}
        proposed = {(s["source_id"], s["version"], s["expected_hash"]) for s in checkpoint["source_bindings"]}
        if not inherited <= proposed:
            return _out("TETHER_SOURCE_MISMATCH", errors=["checkpoint cannot omit or change the TETHER's source bindings"])
        body = {"kind": "work.checkpoint", "id": checkpoint["checkpoint_id"],
                "tether_id": tether["id"], "checkpoint": checkpoint, "resource_requirement": requirement,
                "predecessor_checkpoint_id": request.get("predecessor_checkpoint_id"),
                "adoption_ref": request.get("adoption_ref"), "authority_effect": "NONE"}
        existing = next((r for r in rows if r.get("kind") == "work.checkpoint" and r.get("id") == body["id"]), None)
        if existing:
            equal = _hash(existing) == _hash(body)
            return _out("FROZEN" if equal else "CONFLICTING_REBIND",
                        checkpoint_id=body["id"], idempotent_retry=equal)
        previous = self._latest(rows, tether["id"])
        if previous:
            if request.get("predecessor_checkpoint_id") != previous["id"] or not _text(request.get("adoption_ref")):
                return _out("SUCCESSOR_REQUIRED", predecessor_checkpoint_id=previous["id"])
        elif request.get("predecessor_checkpoint_id") is not None:
            return _out("PREDECESSOR_MISSING")
        written = self.store.append_if_head(snapshot["head"], body)
        if written is None:
            return _out("CONCURRENT_STATE_CHANGED")
        return _out("FROZEN", checkpoint_id=body["id"], checkpoint_hash=_hash(checkpoint),
                    saved_head=snapshot["head"], preservation="DECLARED_WORK_ONLY")

    def read(self, checkpoint_id: str):
        rows = self._snapshot()["records"]
        record = next((r for r in rows if r.get("kind") == "work.checkpoint"
                       and r.get("id") == checkpoint_id), None)
        if record is None:
            return _out("MISSING")
        return _out("RECOVERED", record=record, checkpoint_hash=_hash(record["checkpoint"]),
                    active_checkpoint=self._latest(rows, record["tether_id"])["id"],
                    resume_check="NOT_PERFORMED", preservation="DECLARED_WORK_ONLY")

    @staticmethod
    def _grant(tether, supplied):
        if not isinstance(supplied, dict):
            return "UNKNOWN"
        if any(supplied.get(k) != tether.get(k) for k in ("grant_ref", "task_id", "scope")):
            return "UNKNOWN"
        if supplied.get("revoked") is True:
            return "REVOKED"
        expiry, observed = _time(supplied.get("expires_at")), _time(supplied.get("observed_at"))
        now = datetime.now(timezone.utc)
        if expiry and (expiry <= now or observed and expiry <= observed):
            return "EXPIRED"
        if expiry is None or observed is None or observed > now or supplied.get("revoked") is not False:
            return "UNKNOWN"
        if type(supplied.get("remaining_budget")) is not int or supplied["remaining_budget"] <= 0:
            return "UNKNOWN"
        if supplied.get("expired") or supplied.get("exhausted"):
            return "UNKNOWN"
        return "ACTIVE"

    @staticmethod
    def _resource_history(rows, tether_id, bound, packet):
        """Do not silently forget or lower costs already observed in this epoch.

        UNKNOWN may acquire a declared amount in a later observation; the prior
        unknown observation remains in the ledger. Known events are immutable.
        A deliberate accounting correction needs a separately bound successor.
        """
        def flatten(node):
            nodes = {node["node_id"]: node.get("parent_id")}
            events = {e["event_id"]: e for e in node["events"]}
            for child in node["children"]:
                child_nodes, child_events = flatten(child)
                # Containment is the parent declaration when parent_id is omitted.
                child_nodes[child["node_id"]] = node["node_id"]
                nodes.update(child_nodes)
                events.update(child_events)
            return nodes, events

        new_nodes, new_events = flatten(packet["root"])
        for record in rows:
            if record.get("kind") != "work.reopen" or record.get("tether_id") != tether_id:
                continue
            prior_review = record.get("resource_review", {})
            if prior_review.get("status") not in ("STRUCTURALLY_VALID_FOR_NAMED_PROFILE", "UNRESOLVED"):
                continue
            prior = record["request"]["resource_account"]
            if any(prior["root"].get(k) != bound[k] for k in ("unit", "epoch", "boundary")):
                continue
            old_nodes, old_events = flatten(prior["root"])
            if any(n not in new_nodes or new_nodes[n] != parent for n, parent in old_nodes.items()):
                return "previously observed account node removed or reparented"
            for identity, old in old_events.items():
                new = new_events.get(identity)
                if new is None:
                    return "previously observed cost omitted"
                if old.get("owner") != new.get("owner") or old.get("parent_exclusive", False) != new.get("parent_exclusive", False):
                    return "previously observed cost attribution changed"
                if old["amount"] != "UNKNOWN" and old["amount"] != new["amount"]:
                    return "known cost changed; use an explicit accounting successor"
        return None

    def reopen(self, request: dict[str, Any]):
        allowed = {"checkpoint_id", "observed", "current_grant", "facts", "resource_account"}
        if not isinstance(request, dict) or set(request) - allowed or not _text(request.get("checkpoint_id")):
            return _out("INVALID_INPUT", errors=["invalid reopening request"])
        snapshot = self._snapshot()
        rows = snapshot["records"]
        saved = next((r for r in rows if r.get("kind") == "work.checkpoint"
                      and r.get("id") == request["checkpoint_id"]), None)
        if saved is None:
            return _out("MISSING")
        if self._latest(rows, saved["tether_id"])["id"] != saved["id"]:
            return _out("SUPERSEDED_CHECKPOINT", active_checkpoint=self._latest(rows, saved["tether_id"])["id"])
        tether = next(r for r in rows if r.get("kind") == "tether.bind" and r.get("id") == saved["tether_id"])
        resource_packet = request.get("resource_account")
        resource_review = review_pal24_resources(resource_packet)
        resource_status = "UNKNOWN"
        remaining = None
        bound = saved["resource_requirement"]
        if isinstance(resource_packet, dict) and resource_review["status"] == "STRUCTURALLY_VALID_FOR_NAMED_PROFILE":
            root = resource_packet["root"]
            if all(root.get(k) == bound[k] for k in ("unit", "epoch", "boundary")):
                history_error = self._resource_history(rows, saved["tether_id"], bound, resource_packet)
                if history_error:
                    resource_review = {**resource_review, "status": "UNRESOLVED",
                                       "residuals": resource_review["residuals"] + [history_error]}
                else:
                    remaining = bound["budget"] - resource_review["accounting"]["known_total"]
                    resource_status = "AVAILABLE" if remaining >= bound["next_cost"] else "EXHAUSTED"
        review = review_pal24_resume({"operation": "RESUME", "checkpoint": saved["checkpoint"],
            "observed": request.get("observed"), "current": {
                "facts": request.get("facts", {}), "grant": {"status": self._grant(tether, request.get("current_grant"))},
                "resources": {"status": resource_status}}})
        event = {"kind": "work.reopen", "id": saved["id"], "tether_id": saved["tether_id"],
                 "request": request, "review": review, "resource_review": resource_review,
                 "observed_at": datetime.now(timezone.utc).isoformat(), "authority_renewal": "NONE",
                 "status": "REOPENED" if review["status"] == "STRUCTURALLY_VALID_FOR_NAMED_PROFILE" else "HELD_FOR_REVIEW"}
        try:
            # Check the entire evidence record before appending any part of it.
            canonical_json(event)
        except (ValueError, TypeError, RecursionError):
            return _out("INVALID_INPUT", errors=["reopening evidence exceeds storage bounds"])
        written = self.store.append_if_head(snapshot["head"], event)
        if written is None:
            return _out("CONCURRENT_STATE_CHANGED")
        return _out(event["status"], checkpoint_id=saved["id"], review=review, resource_review=resource_review,
                    declared_remaining=remaining, recovered_work=saved["checkpoint"]["work_state"],
                    consumed_resources=0, audit_effect="APPENDED_REVIEW_ONLY",
                    reopenable=event["status"] == "REOPENED")
