import importlib.util
from pathlib import Path

path = Path(__file__).parents[1] / "hearthline_mcp" / "science_math.py"
spec = importlib.util.spec_from_file_location("science_math_contracts", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_observation_requires_calibration_and_typed_channels():
    base = {"question": "q", "raw": [1], "baseline": [0], "method": "m", "aperture": "a", "uncertainty": "u", "channels": [{"name": "observation", "kind": "observed"}, {"name": "interpretation", "kind": "interpretation"}]}
    assert module.observation_contract(base)["status"] == "INCOMPLETE"
    base["calibration"] = "c"
    assert module.observation_contract(base)["status"] == "DECLARED_CONTRACT_CHECKED"
    base["channels"] = [{"name": "o"}]
    assert module.observation_contract(base)["status"] == "INCOMPLETE"


def test_apci_is_collision_witness_only():
    assert module.apci_cost({"protected_question": "q", "retained_a": "p", "retained_b": "p", "answer_a": 1, "answer_b": 2})["status"] == "COLLISION"
    assert module.apci_cost({"terms": [1, 2]})["status"] == "INSUFFICIENT_EVIDENCE"


def test_endpoint_preserves_exact_rational_and_rejects_huge_exponent():
    assert module.finite_endpoint({"point": ["1/3"]})["endpoint"] == ["1/3"]
    assert module.finite_endpoint({"point": ["1e1000000000"]})["status"] == "INVALID"
