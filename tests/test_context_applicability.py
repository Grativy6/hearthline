"""Synthetic boundary checks for the reduced MIND/CHARTER profile."""
import asyncio
from copy import deepcopy
import json

import pytest

from hearthline_mcp.applicability import context_sources, review_applicability
from hearthline_mcp.core import digest
from hearthline_mcp.server import create_server


def example():
    content = {
        "claim": "Keep routine answers short.",
        "applicability_conditions": [{"condition_id": "routine-only", "field": "question_kind",
                                      "equals": "routine", "evidence_refs": ["synthetic-user:1"]}],
        "unresolved": [],
    }
    return {"source": {"source_id": "preference:1", "version": "1", "expected_hash": digest(content),
                       "supplied_content": content},
            "target": {"context_id": "task:1", "facts": {
                "question_kind": {"value": "routine", "evidence_refs": ["synthetic-task:1"]}}},
            "reopen_handle": "tether:preference:1"}


def test_identical_content_can_be_mismatched_or_unresolved_in_new_target():
    request = example()
    untouched = deepcopy(request)
    matched = review_applicability(request)
    assert request == untouched
    assert matched["source_preservation"]["status"] == "MATCH"
    assert matched["target_applicability"]["status"] == "MATCHES_DECLARED_CONDITIONS"
    assert matched["source_preservation"]["semantic_fidelity"] == "NOT_ASSESSED"
    request["target"]["facts"]["question_kind"]["value"] = "detailed derivation"
    mismatch = review_applicability(request)
    assert mismatch["source_preservation"]["status"] == "MATCH"
    assert mismatch["target_applicability"]["status"] == "MISMATCHED"
    assert mismatch["target_applicability"]["target_hash"] != matched["target_applicability"]["target_hash"]
    request["target"]["facts"] = {}
    unknown = review_applicability(request)
    assert unknown["source_preservation"]["status"] == "MATCH"
    assert unknown["target_applicability"]["status"] == "UNRESOLVED"
    assert "routine-only:target_value_missing" in unknown["residuals"]
    assert unknown["reopen_handle"] == request["reopen_handle"]
    for report in (matched, mismatch, unknown):
        for field in ("authority_effect", "execution_effect", "admission_effect", "training_effect"):
            assert report[field] == "NONE"


@pytest.mark.parametrize("change, preservation", [
    ("content", "CHANGED"), ("strip_qualifier", "CHANGED"),
    ("missing", "MISSING"), ("unbound", "UNVERIFIED"), ("version", "STALE"),
])
def test_unverified_or_changed_source_cannot_pass_applicability(change, preservation):
    request = example()
    source = request["source"]
    if change == "content":
        source["supplied_content"]["claim"] = "Always give a short answer."
    elif change == "strip_qualifier":
        source["supplied_content"]["applicability_conditions"] = []
    elif change == "missing":
        del source["supplied_content"]
    elif change == "unbound":
        del source["expected_hash"]
    else:
        source["expected_version"] = "2"
    report = review_applicability(request)
    assert report["source_preservation"]["status"] == preservation
    assert report["target_applicability"]["status"] == "UNRESOLVED"


@pytest.mark.parametrize("gap", ["no_conditions", "source_refs", "target_refs", "target_value", "source_residual", "legacy_text"])
def test_identity_match_does_not_fill_evidence_gaps(gap):
    request = example()
    content = request["source"]["supplied_content"]
    if gap == "no_conditions":
        content["applicability_conditions"] = []
    elif gap == "source_refs":
        content["applicability_conditions"][0]["evidence_refs"] = []
    elif gap == "target_refs":
        request["target"]["facts"]["question_kind"]["evidence_refs"] = []
    elif gap == "target_value":
        del request["target"]["facts"]["question_kind"]["value"]
    elif gap == "source_residual":
        content["unresolved"] = ["exceptions not yet settled"]
    else:
        request["source"]["supplied_content"] = "Legacy context with no machine-readable conditions."
    request["source"]["expected_hash"] = digest(request["source"]["supplied_content"])
    report = review_applicability(request)
    assert report["source_preservation"]["status"] == "MATCH"
    assert report["target_applicability"]["status"] == "UNRESOLVED"
    assert report["residuals"]


@pytest.mark.parametrize("expected, observed, state", [
    (True, 1, "MISMATCHED"), (1, 1.0, "MISMATCHED"),
    (None, None, "MATCHES_DECLARED_CONDITIONS"),
    ({"a": 1, "b": 2}, {"b": 2, "a": 1}, "MATCHES_DECLARED_CONDITIONS"),
])
def test_exact_comparator_does_not_coerce_values(expected, observed, state):
    request = example()
    request["source"]["supplied_content"]["applicability_conditions"][0]["equals"] = expected
    request["source"]["expected_hash"] = digest(request["source"]["supplied_content"])
    request["target"]["facts"]["question_kind"]["value"] = observed
    assert review_applicability(request)["target_applicability"]["status"] == state


def test_mismatch_keeps_other_conditions_unresolved_and_repeated_refs_do_not_vote():
    request = example()
    content = request["source"]["supplied_content"]
    content["applicability_conditions"][0]["evidence_refs"] *= 5
    content["applicability_conditions"].append({"condition_id": "audience", "field": "audience",
                                              "equals": "beginner", "evidence_refs": ["synthetic-user:1"]})
    request["source"]["expected_hash"] = digest(content)
    request["target"]["facts"]["question_kind"]["value"] = "derivation"
    report = review_applicability(request)
    assert report["target_applicability"]["status"] == "MISMATCHED"
    assert report["target_applicability"]["checks"][1]["status"] == "UNRESOLVED"
    assert report["evidence_refs"] == ["synthetic-user:1", "synthetic-task:1"]
    assert report["evidence_independence"] == "NOT_ASSESSED"


@pytest.mark.parametrize("malformed", ["hash", "conditions", "duplicate", "operator", "fact", "refs", "unbound_conditions", "caller_verdict", "oversize", "nan", "deep"])
def test_malformed_or_unsupported_contract_is_explicit(malformed):
    request = example()
    content = request["source"]["supplied_content"]
    condition = content["applicability_conditions"][0]
    if malformed == "hash": request["source"]["expected_hash"] = "sha256:short"
    elif malformed == "conditions": content["applicability_conditions"] = "always"
    elif malformed == "duplicate": content["applicability_conditions"].append(deepcopy(condition))
    elif malformed == "operator": condition["operator"] = "not_equals"
    elif malformed == "fact": request["target"]["facts"]["question_kind"] = "routine"
    elif malformed == "refs": condition["evidence_refs"] = "a reference"
    elif malformed == "unbound_conditions": request["applicability_conditions"] = [condition]
    elif malformed == "caller_verdict": request["source"]["status"] = "MATCH"
    elif malformed == "oversize": content["claim"] = "x" * 100_001
    elif malformed == "nan": condition["equals"] = float("nan")
    else:
        value = []
        for _ in range(30): value = [value]
        condition["equals"] = value
    report = review_applicability(request)
    assert report["status"] == "INVALID_INPUT"
    assert report["errors"]


def test_source_registry_is_reference_only_and_context_tools_are_filterable(tmp_path):
    registry = context_sources()
    assert [(s["source_id"], s["version"]) for s in registry["sources"]] == [("MIND", "0.4"), ("TIES", "0.2")]
    assert registry["source_content_loaded"] is False
    assert registry["adoption_effect"] == "NONE"
    for source in registry["sources"]:
        assert len(source["artifact"]["sha256"]) == 64
        assert source["artifact"]["hash_domain"] == "raw_file_bytes"
    async def run():
        for groups, exposed in [(None, True), ({"foundation", "core", "continuity"}, False)]:
            server = create_server(store_root=tmp_path, allowed_tools=groups)
            names = {tool.name for tool in await server.list_tools()}
            resources = {str(resource.uri) for resource in await server.list_resources()}
            assert ("review_context_applicability" in names) is exposed
            assert ("read_context_sources" in names) is exposed
            assert ("hearthline://context-sources" in resources) is exposed
            if exposed:
                resources_content = await server.read_resource("hearthline://context-sources")
                assert json.loads(list(resources_content)[0].content) == registry
    asyncio.run(run())
