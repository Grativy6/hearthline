"""Synthetic unit coverage for the PAL 2.4 checkpoint bridge.

These tests exercise the finite adapter contract only.  A passing review is
an account of declared evidence; it does not authenticate a grant, execute a
task, or establish the truth of any supplied field.
"""
from copy import deepcopy

from hearthline_mcp.checkpoints import CheckpointEngine
from hearthline_mcp.continuity import ContinuityEngine
from hearthline_mcp.store import SharedScopedStore, canonical_json, sha256_text


def _source():
    content = {"measurement": 12, "baseline": 10, "labels": ["synthetic"]}
    return content, sha256_text(canonical_json(content))


def _tether(engine, tether_id="t1", task_id="task-1"):
    content, digest = _source()
    return engine.bind_tether({
        "tether_id": tether_id,
        "task_id": task_id,
        "scope": "bounded-comparison",
        "grant_ref": "grant-1",
        "finish_condition": "return comparison",
        "residual": "open",
        "return_target": "controller",
        "source_bindings": [{"source_id": "source-1", "version": "1", "hash": digest}],
        "retrieved_sources": [{"source_id": "source-1", "version": "1", "content": content}],
    })


def _checkpoint():
    _, digest = _source()
    return {
        "checkpoint_id": "checkpoint-1",
        "task_id": "task-1",
        "task_version": "v1",
        "projection_id": "projection-1",
        "transition_ref": "transition-1",
        "observation_ref": "observation-1",
        "horizon": "POINTWISE",
        "admitted_suffix": ["suffix-1"],
        "work_state": {"cursor": 2, "answer": 2},
        "source_bindings": [{"source_id": "source-1", "version": "1", "expected_hash": digest}],
        "requirements": [{"requirement_id": "r1", "field": "baseline", "equals": 10,
                           "evidence_refs": ["observation-1"]}],
    }


def _resource(*, amount=1, complete=True, unknown=False):
    event = {"event_id": "cost-1", "owner": "root", "amount": "UNKNOWN" if unknown else amount}
    return {"root": {"node_id": "root", "unit": "tokens", "epoch": "epoch-1", "boundary": "task-1",
                      "complete": complete, "expected_child_ids": [], "events": [event], "children": []},
            "declared_total": None if unknown else amount}


def _grant(**updates):
    grant = {"grant_ref": "grant-1", "task_id": "task-1", "scope": "bounded-comparison",
             "observed_at": "2026-09-01T00:00:00Z", "expires_at": "2099-01-01T00:00:00Z",
             "revoked": False, "remaining_budget": 3}
    return {**grant, **updates}


def _freeze(tmp_path, *, tether_id="t1", checkpoint=None):
    store = SharedScopedStore(tmp_path)
    continuity = ContinuityEngine(store)
    assert _tether(continuity, tether_id=tether_id)["status"] == "BOUND"
    checkpoint = deepcopy(checkpoint or _checkpoint())
    return store, CheckpointEngine(store), checkpoint


def _freeze_request(checkpoint, tether_id="t1", **extra):
    return {"tether_id": tether_id, "checkpoint": checkpoint,
            "resource_requirement": {"unit": "tokens", "epoch": "epoch-1", "boundary": "task-1",
                                      "budget": 10, "next_cost": 1}, **extra}


def test_freeze_read_is_idempotent_and_preserves_declared_work(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path)
    frozen = engine.freeze(_freeze_request(checkpoint))
    assert frozen["status"] == "FROZEN"
    assert frozen["authority_effect"] == frozen["execution_effect"] == "NONE"
    retry = engine.freeze(_freeze_request(checkpoint))
    assert retry["status"] == "FROZEN" and retry["idempotent_retry"] is True
    recovered = engine.read("checkpoint-1")
    assert recovered["status"] == "RECOVERED"
    assert recovered["record"]["checkpoint"] == checkpoint
    assert recovered["resume_check"] == "NOT_PERFORMED"
    assert len(store.read()["records"]) == 2


def test_checkpoint_rebind_and_successor_require_explicit_lineage(tmp_path):
    _, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    altered = deepcopy(checkpoint)
    altered["work_state"]["answer"] = 3
    assert engine.freeze(_freeze_request(altered))["status"] == "CONFLICTING_REBIND"
    successor = deepcopy(checkpoint)
    successor["checkpoint_id"] = "checkpoint-2"
    assert engine.freeze(_freeze_request(successor))["status"] == "SUCCESSOR_REQUIRED"
    assert engine.freeze(_freeze_request(successor, predecessor_checkpoint_id="checkpoint-1",
                                         adoption_ref="controller-adoption-1"))["status"] == "FROZEN"


def test_checkpoint_rebind_preserves_integer_and_boolean_distinction(tmp_path):
    _, engine, checkpoint = _freeze(tmp_path)
    checkpoint["work_state"]["answer"] = 0
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    boolean_variant = deepcopy(checkpoint)
    boolean_variant["work_state"]["answer"] = False
    assert engine.freeze(_freeze_request(boolean_variant))["status"] == "CONFLICTING_REBIND"


def test_superseded_checkpoint_cannot_be_reopened_in_place(tmp_path):
    _, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    successor = deepcopy(checkpoint)
    successor["checkpoint_id"] = "checkpoint-2"
    assert engine.freeze(_freeze_request(successor, predecessor_checkpoint_id="checkpoint-1",
                                         adoption_ref="controller-adoption-1"))["status"] == "FROZEN"
    assert engine.reopen({"checkpoint_id": "checkpoint-1"})["status"] == "SUPERSEDED_CHECKPOINT"


def test_reopen_keeps_expired_grant_missing_fact_and_unknown_cost_unresolved(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    observed = deepcopy(checkpoint)
    observed["source_bindings"][0]["content"] = _source()[0]
    base = {"checkpoint_id": "checkpoint-1", "observed": observed, "current_grant": _grant(),
            "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}},
            "resource_account": _resource()}
    expired = engine.reopen({**base, "current_grant": _grant(expires_at="2020-01-01T00:00:00Z")})
    assert expired["status"] == "HELD_FOR_REVIEW"
    assert expired["review"]["predicates"]["current_grant"] == "EXPIRED"
    missing = engine.reopen({**base, "facts": {}})
    assert missing["status"] == "HELD_FOR_REVIEW"
    assert missing["review"]["predicates"]["current_applicability"] == "UNKNOWN"
    unknown_cost = engine.reopen({**base, "resource_account": _resource(unknown=True)})
    assert unknown_cost["status"] == "HELD_FOR_REVIEW"
    assert unknown_cost["review"]["predicates"]["current_resources"] == "UNKNOWN"
    assert unknown_cost["declared_remaining"] is None
    assert unknown_cost["authority_renewal"] == "NONE"
    assert len(store.read()["records"]) == 5  # tether, checkpoint, and three review receipts


def test_matching_resume_is_reopened_without_consuming_resources_or_authority(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    observed = deepcopy(checkpoint)
    observed["source_bindings"][0]["content"] = _source()[0]
    result = engine.reopen({"checkpoint_id": "checkpoint-1", "observed": observed,
                            "current_grant": _grant(),
                            "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}},
                            "resource_account": _resource()})
    assert result["status"] == "REOPENED"
    assert result["review"]["predicates"]["exact_work_recovery"] == "PASS"
    assert result["review"]["predicates"]["current_grant"] == "ACTIVE"
    assert result["review"]["predicates"]["current_resources"] == "AVAILABLE"
    assert result["consumed_resources"] == 0
    assert result["authority_renewal"] == "NONE"
    records = store.read()["records"]
    assert records[0]["kind"] == "tether.bind" and records[1]["kind"] == "work.checkpoint"
    assert records[1]["checkpoint"] == checkpoint


def test_scope_isolation_and_read_do_not_reset_or_append_resource_state(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path, tether_id="t1")
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    before = store.read()
    assert CheckpointEngine(SharedScopedStore(tmp_path, namespace="other")).read("checkpoint-1")["status"] == "MISSING"
    assert engine.read("checkpoint-1")["status"] == "RECOVERED"
    after = store.read()
    assert before["head"] == after["head"] and len(before["records"]) == len(after["records"])


def test_resource_history_cannot_omit_or_lower_known_cost_but_can_append_within_budget(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    base = {"checkpoint_id": "checkpoint-1", "observed": {**checkpoint,
            "source_bindings": [{**checkpoint["source_bindings"][0], "content": _source()[0]}]},
            "current_grant": _grant(),
            "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}}}
    known = _resource(amount=3)
    first = engine.reopen({**base, "resource_account": known})
    assert first["status"] == "REOPENED" and first["declared_remaining"] == 7
    extended = _resource(amount=3)
    extended["root"]["events"].append({"event_id": "cost-2", "owner": "root", "amount": 2})
    extended["declared_total"] = 5
    appended = engine.reopen({**base, "resource_account": extended})
    assert appended["status"] == "REOPENED" and appended["declared_remaining"] == 5
    omitted = _resource(amount=3)
    omitted["root"]["events"] = []
    omitted["declared_total"] = 0
    assert engine.reopen({**base, "resource_account": omitted})["status"] == "HELD_FOR_REVIEW"
    lowered = _resource(amount=2)
    assert engine.reopen({**base, "resource_account": lowered})["status"] == "HELD_FOR_REVIEW"
    assert len(store.read()["records"]) == 6  # tether, checkpoint, and four review receipts


def test_unknown_cost_can_be_resolved_only_by_retaining_the_original_event(tmp_path):
    store, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    base = {"checkpoint_id": "checkpoint-1", "observed": {**checkpoint,
            "source_bindings": [{**checkpoint["source_bindings"][0], "content": _source()[0]}]},
            "current_grant": _grant(),
            "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}}}
    unknown = _resource(unknown=True)
    first = engine.reopen({**base, "resource_account": unknown})
    assert first["status"] == "HELD_FOR_REVIEW" and first["declared_remaining"] is None
    resolved = _resource(amount=3)
    resolved["root"]["events"][0]["event_id"] = "cost-1"
    second = engine.reopen({**base, "resource_account": resolved})
    assert second["status"] == "REOPENED" and second["declared_remaining"] == 7
    assert store.read()["records"][2]["resource_review"]["accounting"]["unknown_cost"] is True


def test_resource_epoch_change_is_a_successor_checkpoint_with_adoption(tmp_path):
    _, engine, checkpoint = _freeze(tmp_path)
    assert engine.freeze(_freeze_request(checkpoint))["status"] == "FROZEN"
    successor = deepcopy(checkpoint)
    successor["checkpoint_id"] = "checkpoint-2"
    next_epoch = _freeze_request(successor)
    next_epoch["resource_requirement"]["epoch"] = "epoch-2"
    assert engine.freeze(next_epoch)["status"] == "SUCCESSOR_REQUIRED"
    assert engine.freeze({**next_epoch, "predecessor_checkpoint_id": "checkpoint-1"})["status"] == "SUCCESSOR_REQUIRED"
    adopted = engine.freeze({**next_epoch, "predecessor_checkpoint_id": "checkpoint-1",
                             "adoption_ref": "controller-adoption-epoch-2"})
    assert adopted["status"] == "FROZEN"
