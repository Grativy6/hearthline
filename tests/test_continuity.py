import multiprocessing
import threading
from pathlib import Path

import pytest

from hearthline_mcp.continuity import ContinuityEngine
from hearthline_mcp.store import SharedScopedStore, StoreIntegrityError, canonical_json, sha256_text


def tether(e, **extra):
    content = {"source": "stable"}
    body = {"tether_id": "t1", "task_id": "task", "scope": "bounded", "grant_ref": "g1", "finish_condition": "done", "residual": "open", "return_target": "home", "source_bindings": [{"source_id": "s", "version": "1", "hash": sha256_text(canonical_json(content))}], "retrieved_sources": [{"source_id": "s", "version": "1", "content": content}]}
    body.update(extra)
    return e.bind_tether(body)


def test_store_reopens_and_preserves_hash_chain(tmp_path):
    first = SharedScopedStore(tmp_path, adapter="a", user="u")
    first.append({"kind": "x", "value": 1})
    second = SharedScopedStore(tmp_path, adapter="a", user="u")
    assert second.read()["records"] == [{"kind": "x", "value": 1}]
    assert second.verify()["trusted"]


def test_namespace_is_injective_for_separator_variants(tmp_path):
    assert SharedScopedStore(tmp_path, adapter="a", user="b_c").namespace != SharedScopedStore(tmp_path, adapter="a_b", user="c").namespace


def test_tether_requires_current_grant_on_reopen(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path))
    assert tether(e)["status"] == "BOUND"
    sources = [{"source_id": "s", "version": "1", "content": {"source": "stable"}}]
    grant = {"grant_ref": "g1", "task_id": "task", "scope": "bounded", "observed_at": "2026-01-01T00:00:00Z", "expires_at": "2099-01-01T00:00:00Z", "revoked": False, "remaining_budget": 1}
    assert e.reopen_tether({"tether_id": "t1", "current_grant": {**grant, "expired": True}, "retrieved_sources": sources})["status"] == "GRANT_REVIEW_REQUIRED"
    assert e.reopen_tether({"tether_id": "t1", "current_grant": grant, "retrieved_sources": sources})["status"] == "REOPENED"


def test_tether_reopen_rejects_changed_or_stale_source(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path)); tether(e)
    changed = [{"source_id": "s", "version": "1", "content": {"source": "changed"}}]
    stale = [{"source_id": "s", "version": "2", "content": {"source": "stable"}}]
    grant = {"grant_ref": "g1", "task_id": "task", "scope": "bounded", "observed_at": "2026-01-01T00:00:00Z", "expires_at": "2099-01-01T00:00:00Z", "revoked": False, "remaining_budget": 1}
    assert e.reopen_tether({"tether_id": "t1", "current_grant": grant, "retrieved_sources": changed})["status"] == "GRANT_REVIEW_REQUIRED"
    assert e.reopen_tether({"tether_id": "t1", "current_grant": grant, "retrieved_sources": stale})["status"] == "GRANT_REVIEW_REQUIRED"


def test_tether_and_heartbeat_conflicting_rebinds_are_preserved(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path)); tether(e)
    assert tether(e, scope="changed")["status"] == "CONFLICTING_REBIND"
    assert e.create_heartbeat({"heartbeat_id": "h", "tether_id": "t1", "finish_condition": "done", "budget": 2})["status"] == "ACTIVE"
    assert e.create_heartbeat({"heartbeat_id": "h", "tether_id": "t1", "finish_condition": "done", "budget": 3})["status"] == "CONFLICTING_REBIND"


def test_heartbeat_budget_monotonic_and_late_pulse_rejected(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path))
    tether(e)
    assert e.create_heartbeat({"heartbeat_id": "h", "tether_id": "t1", "finish_condition": "done", "budget": 2})["status"] == "ACTIVE"
    assert e.pulse_heartbeat({"heartbeat_id": "h", "cost": 1, "state": "working"})["remaining"] == 1
    assert e.pulse_heartbeat({"heartbeat_id": "h", "cost": 1})["status"] == "EXHAUSTED"
    assert e.pulse_heartbeat({"heartbeat_id": "h", "cost": 0})["status"] == "LATE_PULSE_REJECTED"


def test_heartbeat_retry_intent_is_bound(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path)); tether(e)
    e.create_heartbeat({"heartbeat_id": "h", "tether_id": "t1", "finish_condition": "done", "budget": 2})
    assert e.pulse_heartbeat({"heartbeat_id": "h", "event_id": "x", "cost": 1})["status"] == "ACTIVE"
    assert e.pulse_heartbeat({"heartbeat_id": "h", "event_id": "x", "cost": 0})["status"] == "IDEMPOTENCY_CONFLICT"


def test_concurrent_pulses_cannot_overspend(tmp_path):
    store = SharedScopedStore(tmp_path); e = ContinuityEngine(store); tether(e)
    e.create_heartbeat({"heartbeat_id": "h", "tether_id": "t1", "finish_condition": "done", "budget": 1})
    barrier = threading.Barrier(2); results = []
    def pulse():
        barrier.wait(); results.append(e.pulse_heartbeat({"heartbeat_id": "h", "cost": 1}))
    threads = [threading.Thread(target=pulse) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    assert "EXHAUSTED" in [x["status"] for x in results]
    assert all(x["status"] in {"EXHAUSTED", "CONCURRENT_STATE_CHANGED", "LATE_PULSE_REJECTED"} for x in results)
    assert e.read_heartbeat("h")["remaining"] == 0


def test_custody_requires_controller_selection_and_exact_hash(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path)); payload = {"x": 1}; h = sha256_text(canonical_json(payload))
    base = {"payload": payload, "payload_hash": h, "source": "s", "destination": "d", "return_route": "r"}
    assert e.record_custody(base)["status"] == "SELECTION_REQUIRED"
    assert e.record_custody({**base, "controller_selected": True})["status"] == "BOUND"


def test_formation_requires_distinct_complete_lanes(tmp_path):
    e = ContinuityEngine(SharedScopedStore(tmp_path))
    bad = {"formation_id": "f", "members": [{"identity": "x", "role": "worker", "lane": "a"}, {"identity": "x", "role": "keeper", "lane": "b"}]}
    assert e.validate_formation(bad)["status"] == "INCOMPLETE"


def test_tampered_storage_is_reported_untrusted(tmp_path):
    store = SharedScopedStore(tmp_path); store.append({"kind": "x"})
    with store._connect() as con:
        con.execute("UPDATE records SET payload=? WHERE namespace=?", ('{"kind":"tampered"}', store.namespace))
    assert store.verify()["trusted"] is False
    with pytest.raises(StoreIntegrityError):
        store.read()


def _append_many(root):
    store = SharedScopedStore(root, adapter="parallel", user="u")
    for i in range(8):
        store.append({"kind": "parallel", "i": i})


def test_two_processes_append_without_lost_writes(tmp_path):
    ctx = multiprocessing.get_context("spawn")
    jobs = [ctx.Process(target=_append_many, args=(str(tmp_path),)) for _ in range(2)]
    for job in jobs: job.start()
    for job in jobs: job.join(30)
    assert all(job.exitcode == 0 for job in jobs)
    assert len(SharedScopedStore(tmp_path, adapter="parallel", user="u").read()["records"]) == 16
