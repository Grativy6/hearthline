from hearthline_mcp.context import orient, source_status, transport_capsule
from hearthline_mcp.core import digest


def _capsule(**changes):
    body = {
        "program": "p1",
        "cursor": "c1",
        "schedule": {"mode": "manual"},
        "dependencies": {"foundation": "1.0"},
        "comparator": {"id": "cmp-1", "version": "1"},
        "budget": {"steps": 4, "bytes": 1000},
        "receipt_chain": [],
    }
    body.update(changes)
    return body


def test_orientation_uses_functional_profiles_and_disjoint_sets():
    out = orient({"profile": "scientific", "purpose": "compare observations", "supplied": ["s1"], "selected": ["s2"], "available_unread": ["s3"]})
    assert out["status"] == "VALID"
    assert out["sets"]["supplied"] == ["s1"]
    assert out["orientation_hash"].startswith("sha256:")


def test_orientation_rejects_unknown_profile_and_overlapping_context():
    out = orient({"profile": "unrecognized", "purpose": "test", "supplied": ["s1"], "inferred": ["s1"]})
    assert out["status"] == "INVALID_INPUT"
    assert any(error.startswith("unknown_profile") for error in out["errors"])
    assert "context_item_in_multiple_sets:s1" in out["errors"]


def test_orientation_allows_selected_supplied_overlap_and_unforced_purpose():
    selected = orient({"purpose": "ordinary work", "selected": ["s1"], "supplied": ["s1"]})
    assert selected["status"] == "UNFORCED"
    assert selected["sets"]["selected"] == ["s1"]


def test_source_status_recomputes_content_and_does_not_trust_observed_hash():
    content = {"answer": 1}
    out = source_status({"source_id": "s", "supplied_content": content, "expected_hash": digest(content), "observed_hash": "sha256:caller-lied"})
    assert out["state"] == "AVAILABLE"
    assert out["observed_hash"] == digest(content)


def test_source_status_missing_content_cannot_be_available():
    out = source_status({"source_id": "s", "state": "AVAILABLE", "observed_hash": "sha256:fake"})
    assert out["state"] == "MISSING"
    assert out["content_supplied"] is False


def test_source_status_stale_version_and_fingerprint_are_explicit():
    out = source_status({"source_id": "s", "supplied_content": "x", "version": "1", "expected_version": "2", "expected_fingerprint": "fp", "fingerprint": "old"})
    assert out["state"] == "STALE"


def test_transport_capsule_is_finite_and_hashes_all_reentry_fields():
    out = transport_capsule(_capsule())
    assert out["status"] == "VALID"
    assert out["capsule_hash"].startswith("sha256:")
    assert out["resume_effect"] == "NONE"


def test_transport_capsule_changed_comparator_requires_reassessment_and_preserves_prior():
    first = transport_capsule(_capsule())
    second = transport_capsule(_capsule(comparator={"id": "cmp-2", "version": "1"}, prior_capsule={**first["capsule"], "capsule_hash": first["capsule_hash"]}))
    assert second["status"] == "REASSESSMENT_REQUIRED"
    assert second["reassessment"] == "REASSESSMENT_REQUIRED"
    assert second["prior_capsule_hash"] == first["capsule_hash"]


def test_transport_capsule_rejects_broken_receipt_link():
    out = transport_capsule(_capsule(receipt_chain=[{"receipt_id": "r1", "previous_hash": "sha256:wrong"}]))
    assert out["status"] == "INVALID_INPUT"
    assert out["chain_status"] == "INVALID"
