from pathlib import Path

import pytest

from hearthline_mcp.software import (
    SoftwareEngine, a0bk_operation, carrier_contract, c2c_capability,
    fbt_operation, p3la_compose,
)
from hearthline_mcp.store import SharedScopedStore


def engine(tmp_path: Path, **kwargs):
    return SoftwareEngine(SharedScopedStore(tmp_path, adapter="test", user="u"), **kwargs)


def test_trace_only_persists_trace_but_cannot_govern(tmp_path):
    e = engine(tmp_path)
    assert e.update_computation("x", {"value": 1})["status"] == "UPDATED"
    assert e.govern_transition("set", "x", 2)["status"] == "REJECTED"
    trace = e.read_trace()
    assert len(trace["trace"]) == 1
    assert trace["trace"][0]["record_type"] == "software.trace"


def test_model_cannot_escalate_mode_or_write_authority(tmp_path):
    e = engine(tmp_path, mode="SHADOW", policy_ref="p", operator_id="human", allowed_internal_actions=("set",))
    assert fbt_operation({"operation": "govern", "action": "set", "state_key": "x", "value": 1, "mode": "GOVERNING"}, engine=e)["status"] == "REJECTED"
    assert e.authority.policy_ref == "p"
    with pytest.raises(ValueError): engine(tmp_path / "bad", mode="GOVERNING")
    assert fbt_operation({"operation": "trace", "mode": "GOVERNING", "name": "x"}, engine=e)["status"] == "REJECTED"


def test_governing_is_constructor_bound_and_internal_only(tmp_path):
    e = engine(tmp_path, mode="GOVERNING", policy_ref="human-policy", allowed_internal_actions=("set",))
    assert e.govern_transition("external_send", "x", 1)["status"] == "REJECTED"
    out = e.govern_transition("set", "x", {"finite": True})
    assert out["status"] == "APPLIED" and out["external_action"] is False
    assert e.read_trace()["trace"][-1]["outcome"] == "APPLIED"


def test_shadow_compare_is_nonexecuting_and_trace_is_immutable(tmp_path):
    e = engine(tmp_path, mode="SHADOW")
    out = e.shadow_compare({"a": 1}, {"a": 2})
    assert out["status"] == "DIVERGENCE" and out["executed"] is False
    first = e.read_trace()["trace"]
    e.shadow_compare({"a": 1}, {"a": 1})
    second = e.read_trace()["trace"]
    assert len(second) == 2 and first[0]["event_id"] == second[0]["event_id"]


def test_a0bk_is_explicit_pal23_adaptation():
    out = a0bk_operation({"operation": "SUCCESSOR", "account": {}, "receipts": []})
    assert out["status"] == "INVALID_ADAPTED_INPUT" and out["source_pal"] == "2.2" and out["target_pal"] == "2.3"
    assert out["foundation_check"]["status"] == "INVALID_INPUT"
    assert out["semantic_authority"] == "NONE"
    assert a0bk_operation({"operation": "unknown"})["status"] == "INVALID"


def test_p3la_preserves_disagreement_and_requires_fusion_policy():
    edges = [{"edge_id": "a", "input_hash": "i", "output_hash": "o1", "schema": "s", "domain": "d", "output_claims": ["a", "b"], "disagreement": True},
             {"edge_id": "b", "input_hash": "i", "output_hash": "o2", "schema": "s", "domain": "d", "output_claims": ["b", "c"], "disagreement": False}]
    out = p3la_compose({"edges": edges})
    assert out["status"] == "COMPOSED" and len(out["alternatives"]) == 1 and out["consensus"] is False
    assert out["fusion"] is None
    fused = p3la_compose({"edges": [dict(edges[0], disagreement=False), edges[1]], "fusion_policy": "EXPLICIT_INTERSECTION"})
    assert fused["fusion"] is not None and fused["fusion"]["intersection_outputs"] == ["b"]
    incompatible = p3la_compose({"edges": [dict(edges[0], disagreement=False), dict(edges[1], schema="other")], "fusion_policy": "EXPLICIT_INTERSECTION"})
    assert incompatible["fusion"] is None


def test_carrier_and_c2c_keep_shape_separate_from_semantics():
    assert carrier_contract({"carrier_id": "c", "operator": "o", "write": "w", "transport": "t", "readout": "r"})["semantic_equivalence"] is False
    out = c2c_capability({"model_host": "api-host", "kv_cache_access": False})
    assert out["status"] == "UNAVAILABLE_API_OR_KV_ACCESS" and out["experiment_status"] == "NOT_RUN"
    local = c2c_capability({"model_host": "local", "kv_cache_access": True, "local_model_internals": True})
    assert local["status"] == "PREREQUISITES_DECLARED_NOT_VERIFIED" and local["learned_bridge_verified"] is False
