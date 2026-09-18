from hearthline_mcp.core import compact, dependency_correction, dependency_record, finite_packet, tether
from hearthline_mcp.context import orient, source_status, transport_capsule
from hearthline_mcp.core import collision_check


def test_finite_packet_is_bounded_and_hashed():
    out = finite_packet([{"id": "a"}], purpose="test")
    assert out["kind"] == "finite_packet"
    assert out["packet_hash"].startswith("sha256:")
    assert out["authority_effect"] == "NONE"


def test_compaction_preserves_declared_loss_and_questions():
    out = compact({"items": [{"id": "a"}, {"id": "b"}], "protected_questions": ["q"], "max_items": 1})
    assert out["declared_losses"] == ["b"]
    assert out["protected_questions"] == ["q"]


def test_load_bearing_correction_reopens_only_named_dependents():
    out = dependency_correction({"source_id": "s", "known_nodes": ["s", "d1"], "edges": [{"source_id": "s", "dependent_id": "d1", "adopted": True, "provisional": False, "adoption_ref": "human-1", "load_bearing": True}]})
    assert out["reconsider"] == ["d1"]
    assert out["preserved_history"] is True


def test_tether_does_not_renew_authority():
    out = tether({"tether_id": "t", "task_id": "x", "scope": "s", "return_target": "r", "finish_condition": "f"})
    assert out["status"] == "BOUND"
    assert out["authority_renewal"] == "NONE"


def test_orientation_preserves_available_unread_state():
    out = orient({"profile": "MPCP", "purpose": "test", "available_unread": ["s1"]})
    assert out["available_unread"] == ["s1"]
    assert out["status"] == "VALID"


def test_transport_capsule_requires_all_reentry_fields():
    out = transport_capsule({"program": "p", "cursor": "c"})
    assert "schedule" in out["missing"]


def test_collision_detects_same_retained_packet_with_different_answers():
    packet = {"items": [{"id": "kept"}], "omitted_ids": ["hidden"]}
    out = collision_check({"left_retained_packet": packet, "right_retained_packet": packet,
                           "left_protected_answers": ["A"], "right_protected_answers": ["B"],
                           "protected_questions": ["q"]})
    assert out["same_packet"] is True
    assert out["status"] == "COLLISION_REVIEW_REQUIRED"


def test_source_status_detects_changed_supplied_bytes():
    out = source_status({"source_id": "s", "expected_hash": "sha256:wrong", "supplied_source": "current"})
    assert out["state"] == "CHANGED"


def test_dependency_correction_walks_transitive_adopted_edges_only():
    edges = [
        {"source_id": "s", "dependent_id": "d1", "adopted": True, "provisional": False, "adoption_ref": "human-1", "load_bearing": True},
        {"source_id": "d1", "dependent_id": "d2", "adopted": True, "provisional": False, "adoption_ref": "human-2", "load_bearing": True},
        {"source_id": "s", "dependent_id": "side", "adopted": True, "provisional": False, "adoption_ref": "human-3", "load_bearing": False},
    ]
    out = dependency_correction({"source_id": "s", "known_nodes": ["s", "d1", "d2", "side"], "edges": edges})
    assert out["reconsider"] == ["d1", "d2"]
    assert out["non_load_bearing_preserved"] is True


def test_dependency_rejects_self_reference_and_reports_cycles():
    invalid = dependency_record({"dependency_id": "x", "source_id": "a", "dependent_id": "a", "relation": "depends_on"})
    assert invalid["status"] == "INVALID"
    out = dependency_correction({"source_id": "a", "known_nodes": ["a", "b"], "edges": [
        {"source_id": "a", "dependent_id": "b", "relation": "depends_on", "adopted": True, "provisional": False, "adoption_ref": "human-1", "load_bearing": True},
        {"source_id": "b", "dependent_id": "a", "relation": "depends_on", "adopted": True, "provisional": False, "adoption_ref": "human-2", "load_bearing": True},
    ]})
    assert out["cycles"]
    assert out["residual"] == "CYCLE_REVIEW_REQUIRED"
