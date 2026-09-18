import importlib.util
import sys
from pathlib import Path

_module_path = Path(__file__).parents[1] / "hearthline_mcp" / "science_math.py"
_spec = importlib.util.spec_from_file_location("science_math", _module_path)
_module = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_module)
TOOLS = _module.TOOLS


def test_observation_and_residuals_keep_channels_distinct():
    r = TOOLS["science.observation_contract"]({"question": "q", "raw": [1], "baseline": [0], "method": "m", "aperture": "a", "calibration": "c", "uncertainty": "u", "channels": [{"name": "observation", "kind": "observed"}, {"name": "interpretation", "kind": "interpretation"}], "simulation": False})
    assert r["status"] == "DECLARED_CONTRACT_CHECKED" and r["effects"] == []
    r = TOOLS["science.residual_alternatives"]({"alternatives": ["A", "B"], "missing_discriminators": ["sample"]})
    assert r["status"] == "RESIDUAL" and r["unique_cause"] is False


def test_science_limits_and_comparison():
    assert TOOLS["science.detection_limit"]({"value": "1.2", "limit": "1"})["status"] == "DETECTED"
    r = TOOLS["science.compare_prerequisites"]({"baseline": ["x", "y"], "comparison": ["x", "z"], "method_baseline": "m", "method_comparison": "m", "aperture_baseline": "a", "aperture_comparison": "a"})
    assert r["added"] == ["z"] and r["removed"] == ["y"]
    assert TOOLS["science.simulation_vs_observation"]({"kind": "simulation"})["supports_causal_claim"] is False


def test_endpoint_repair_does_not_claim_full_recovery():
    r = TOOLS["math.finite_endpoint"]({"point": ["1/2", 3], "readout": "r"})
    assert r["status"] == "PASS" and r["endpoint"][0] == "1/2"
    r = TOOLS["math.side_trace_repair"]({"trace": ["b"], "predecessor": "a"})
    assert r["status"] == "REPAIRED" and not r["answer_recovered"]
    assert TOOLS["math.side_trace_repair"]({"trace": []})["status"] == "INSUFFICIENT"


def test_apci_and_bridge_are_bounded():
    assert TOOLS["math.apci_cost"]({"protected_question": "q", "retained_a": "a", "retained_b": "b", "answer_a": 1, "answer_b": 1})["status"] == "NO_WITNESS_NOT_SUFFICIENT"
    assert TOOLS["math.bridge_repair"]({"source_map": {"a": {"protected_answer": 1}, "b": {"protected_answer": 2}}, "readout_map": {"a": "r1", "b": "r2"}, "side_trace_map": {"a": "s1", "b": "s2"}, "protected_query": ["a", "b"]})["status"] == "PASS"


def test_gold_exact_six_channels_and_collision_label():
    r = TOOLS["math.gold_channels"]({"values": [0, 1, 2, 3, 4, 5], "n": 3})
    assert r["status"] == "PASS" and r["collision"] == "COLLISION"
    assert r["differences"][0] == "-5/2" and len(r["projection_fibers"]) == 7
    assert TOOLS["math.gold_channels"]({"values": [1, 2]})["status"] == "INVALID"


def test_gppr_exact_events_and_conservative_interval_fallback():
    r = TOOLS["math.gppr_factor_events"]({"factors": {"2": 3, "3": -1}, "events": [{"op": "split"}]})
    assert r["status"] == "INVALID"
    assert TOOLS["math.gppr_factor_events"]({"factors": {"2": 3}, "events": [{"prime": 2, "multiplicity": 3}], "product": "8"})["status"] == "PASS"
    good = TOOLS["math.gppr_factor_events"]({"factors": {"2": 1, "3": 1}, "events": [{"prime": 2, "multiplicity": 1}, {"prime": 3, "multiplicity": 1}], "product": "6"})
    assert good["certificate_status"] == "FINITE_ARITHMETIC_CHECKED"
    assert [x["index"] for x in good["endpoint_terms"]] == [1, 2]
    extra = TOOLS["math.gppr_factor_events"]({"factors": {"2": 1}, "events": [{"prime": 2, "multiplicity": 1}, {"prime": 3, "multiplicity": 1}], "product": "2"})
    assert extra["status"] == "INCOMPLETE" and extra["extra_events"] == ["3"]
    r = TOOLS["math.gppr_partition"]({"partition_id": "p1", "precision": "exact", "source_endpoint": "e", "enclosures": [[0, 1.5], [1, 2]], "cells": [{"id": "a", "lo": 0, "hi": 1}, {"id": "b", "lo": 1, "hi": 2}]})
    assert r["status"] == "FALLBACK" and r["conservative"]
    assert len(TOOLS) == len(set(TOOLS))


def test_numeric_bounds_and_gold_sector_residual():
    assert TOOLS["math.gold_channels"]({"values": ["1e1000000000", 1, 2, 3, 4, 5]})["status"] == "INVALID"
    r = TOOLS["math.gold_channels"]({"values": [0, 1, 2, 3, 4, 5], "sector": {"base": "1"}, "residual": {"delta": "1/2"}})
    assert r["sector_reconstruction"] == "3/2"
    turn = TOOLS["math.gold_channels"]({"values": [0, 1, 2, 3, 4, 5], "n": 1})["beta_turn"]
    assert turn["K"] == 2 and turn["floor_certificate"] == "integer_inequality"


def test_audit_counterexamples_remain_unresolved():
    bridge = TOOLS["math.bridge_repair"]({"source_map": {"a": {"protected_answer": 1}, "b": {"protected_answer": 2}}, "readout_map": {"a": "r", "b": "r"}, "side_trace_map": {"a": "s", "b": "s"}, "protected_query": ["a", "b"]})
    assert bridge["status"] == "INSUFFICIENT" and not bridge["answer_recovered"]
    assert TOOLS["math.bridge_repair"]({"source_map": {"a": 1}, "readout_map": {"a": "r"}, "side_trace_map": {"a": "s"}, "protected_query": ["a"]})["status"] == "INCOMPLETE"
    assert TOOLS["math.gppr_factor_events"]({"factors": {"2": 3}, "events": [], "product": "8"})["history_status"] == "HISTORY_NOT_SUPPLIED"
    routed = TOOLS["math.gppr_partition"]({"partition_id": "p", "precision": "exact", "source_endpoint": "e", "enclosures": [[0, 1]], "cells": [{"id": "c", "lo": 0, "hi": 1}], "enclosure_certificate": True, "certificate_hash": "x"})
    assert routed["status"] == "FALLBACK" and not routed["certificate_verified"]


def test_gppr_partition_is_two_dimensional_and_never_calls_metadata_a_proof():
    base = {"partition_id": "p", "precision": "80-bit", "source_endpoint": "e",
            "enclosure_certificate": True, "certificate_hash": "a" * 64}
    inside = dict(base, enclosures=[{"endpoint": "e", "re": ["0", "0.5"], "im": ["0", "0.5"]}],
                  cells=[{"id": "c", "re": ["0", "1"], "im": ["0", "1"]}])
    r = TOOLS["math.gppr_partition"](inside)
    assert r["status"] == "ROUTED_UNDER_SUPPLIED_ENCLOSURE"
    assert r["certificate_verified"] is False and r["certificate_metadata_present"] is True
    crossing = dict(base, enclosures=[{"re": ["0", "2"], "im": ["0", "1"]}],
                    cells=[{"id": "c", "re": ["0", "1"], "im": ["0", "1"]}])
    assert TOOLS["math.gppr_partition"](crossing)["status"] == "FALLBACK"
    mismatch = dict(base, enclosures=[{"endpoint": "other", "re": ["0", "0.5"], "im": ["0", "0.5"]}],
                    cells=[{"id": "c", "re": ["0", "1"], "im": ["0", "1"]}])
    assert TOOLS["math.gppr_partition"](mismatch)["status"] == "FALLBACK"
    malformed = dict(base, enclosures=[{"re": ["0", "1"], "im": ["0"]}],
                     cells=[{"id": "c", "re": ["0", "1"], "im": ["0", "1"]}])
    assert TOOLS["math.gppr_partition"](malformed)["status"] == "FALLBACK"
