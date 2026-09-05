#!/usr/bin/env python3
"""Validate Hearthline's public research-station and Creature design surfaces."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "research-station" / "source-identities.json"
CANDIDATE_PATH = ROOT / "candidate_manifest.json"
AGENT_PATH = ROOT / "hearthline_agent.md"
RESEARCH_DOC = ROOT / "docs" / "HEARTHLINE_RESEARCH_STATION.md"
CREATURE_DOC = ROOT / "docs" / "HEARTHLINE_CREATURES.md"
HOMECOMING_DOC = ROOT / "docs" / "HEARTHLINE_HOMECOMING.md"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

EXPECTED_SOURCES = {
    "pal-v2.3": "CURRENT",
    "brrrt-v2.0": "BRANCH",
    "single-cut-transport-v0.2": "BRANCH",
    "compactification-costs-v0.2": "BRANCH",
    "strongwiz-v3-prototype": "EXPLORATORY",
    "gppr-v0.1": "BRANCH",
    "context-rhythm-v0.1": "EXPLORATORY",
    "full-bandwidth-not-full-trace-v0.1": "BRANCH",
    "gold-v0.1": "BRANCH",
    "context-map-v1.0": "EXPLORATORY",
}
EXPECTED_STRONGWIZ_BLOBS = {
    "docs/calibrations/003-strongwiz-v3-pal23-scribe.md":
        "dffda989417f6245db32da3756426805e29f14b111cf60444e99cbfe1b87c712",
    "docs/pal-v2.3-profile.md":
        "7a43a807262437ddeb55831045e75f309e853d2a4d21f9563fdc187b73a7388c",
    "docs/scribe.md":
        "4d41c381da487c4a28076e5bf6943c9b821132f20b79c37b6ede66f704e1541e",
    "docs/architecture.md":
        "ebbdbd05821e14552086dca44314c9d05304b2c5b1ed6624a8d7851110b759b7",
    "docs/receipts/v0.4.0-dev-verification.json":
        "546370565a9cd6d460247b1ee3f53f0df22777ad4795398aa3848677ba93f6c1",
    "docs/receipts/v0.4.0-dev-reproducible-build.json":
        "db6878167fa1a75549cc595b78273a14bd489049fe24557cdc4e00967ecf8ccd",
}
EXPECTED_STRONGWIZ = {
    "persistent_id": (
        "https://github.com/Grativy6/strongwiz/tree/"
        "edc88b80f872f766c22b3a050a7f6837d6e652d8"
    ),
    "repository_commit": "edc88b80f872f766c22b3a050a7f6837d6e652d8",
    "repository_tree": "18dd76355decdf8b1e98fff7dffeac222c0b3aa2",
    "implementation_freeze_commit": "300fd0b9ae1183e582bb834e17ff02bf80189fd8",
    "implementation_freeze_tree": "bb61230e0eacdaff42b8f9d6f2a7abf7b0efaf55",
    "source_registry_ref": "055bfbef1e5b0191ef84e266f1c8f888c58def5428113d8b262f0baa8b95dd9a",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_object
    )
    require(isinstance(value, dict), f"{path.name} root must be an object")
    return value


def check_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        parsed = urlparse(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("#"):
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        require(
            target == ROOT or ROOT in target.parents,
            f"{path.relative_to(ROOT)} link escapes repository: {raw}",
        )
        require(target.exists(), f"{path.relative_to(ROOT)} broken link: {raw}")


def find_source(registry: dict[str, Any], source_id: str) -> dict[str, Any]:
    matches = [
        source
        for source in registry["sources"]
        if source.get("source_id") == source_id
    ]
    require(len(matches) == 1, f"expected exactly one source {source_id}")
    return matches[0]


def check_digest_fields(value: Any, path: str = "registry") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "sha256" or key.endswith("_sha256"):
                require(
                    isinstance(child, str) and SHA256_RE.fullmatch(child) is not None,
                    f"{path}.{key} is not a lowercase SHA-256",
                )
            check_digest_fields(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            check_digest_fields(child, f"{path}[{index}]")


def main() -> None:
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    lowered = registry_text.lower()
    for forbidden in ("c:\\users\\", "e:\\", "file://", "token=", "api_key"):
        require(forbidden not in lowered, f"registry contains private-path text: {forbidden}")

    registry = read_json(REGISTRY_PATH)
    require(
        registry.get("schema") == "hearthline.research-station.sources.v1",
        "unexpected research-station schema",
    )
    require(registry.get("status") == "RESEARCH_CONTEXT_ONLY", "bad station status")
    require(registry.get("source_text_is_authorization") is False,
            "source text must not become authorization")
    require(registry.get("shared_author_lineage_is_independent_corroboration") is False,
            "shared author lineage must not become independent corroboration")
    require(registry.get("code_imported_or_executed_by_hearthline") is False,
            "station must not claim code import or execution")
    require(isinstance(registry.get("sources"), list), "sources must be an array")

    ids = [source.get("source_id") for source in registry["sources"]]
    require(len(ids) == len(set(ids)), "source IDs must be unique")
    require(set(ids) == set(EXPECTED_SOURCES), "source registry set changed")
    for source in registry["sources"]:
        source_id = source["source_id"]
        require(source.get("hearthline_status") == EXPECTED_SOURCES[source_id],
                f"unexpected status for {source_id}")
        require(source.get("bounded_use"), f"{source_id} lacks bounded use")
        require(source.get("authority_ceiling"), f"{source_id} lacks authority ceiling")

    check_digest_fields(registry)

    pal = find_source(registry, "pal-v2.3")
    require(pal.get("version") == "2.3", "PAL registry version drift")
    require(pal.get("persistent_id") == "https://doi.org/10.5281/zenodo.22240134",
            "PAL registry DOI drift")

    brrrt = find_source(registry, "brrrt-v2.0")
    require(brrrt.get("artifact_identity_status") ==
            "RESOLVED_LIVE_RECORD_CANONICAL_MATCH",
            "BRRRT live resolution must remain explicit")
    brrrt_pdfs = [
        item for item in brrrt.get("inspected_artifacts", [])
        if item.get("filename", "").endswith("BRRRT.pdf")
    ]
    require(len(brrrt_pdfs) == 3,
            "BRRRT must record live loose, package, and historical wrapper PDFs")
    current_pdfs = [
        item for item in brrrt_pdfs
        if not item.get("variant", "").startswith("superseded_")
    ]
    require(len(current_pdfs) == 2, "BRRRT current PDF surfaces changed")
    require({item.get("bytes") for item in current_pdfs} == {1_251_146},
            "BRRRT current PDF sizes differ")
    require({item.get("sha256") for item in current_pdfs} ==
            {"f9e699ad4a8541506ecc6678c3296bdf4fbe4dd249a0dd6759c7fd0d22837e0a"},
            "BRRRT current loose/package SHA match lost")
    historical = [
        item for item in brrrt_pdfs
        if item.get("variant", "").startswith("superseded_")
    ]
    require(len(historical) == 1 and historical[0].get("current_live_record") is False,
            "BRRRT superseded wrapper observation missing")

    strongwiz = find_source(registry, "strongwiz-v3-prototype")
    require(strongwiz.get("prototype_status") == "PREPARED_NOT_RUN_NOT_PREREGISTERED",
            "Strongwiz prototype status was inflated")
    require(strongwiz.get("inspection_status") == "PINNED_DESIGN_SOURCE",
            "Strongwiz inspection status missing")
    require(strongwiz.get("inspected_artifact_hash_domain") ==
            "git_blob_bytes_at_repository_commit", "Strongwiz hash domain changed")
    for field, expected in EXPECTED_STRONGWIZ.items():
        require(strongwiz.get(field) == expected,
                f"Strongwiz {field} drifted from the inspected identity")
    for field in (
        "repository_commit",
        "repository_tree",
        "implementation_freeze_commit",
        "implementation_freeze_tree",
    ):
        require(COMMIT_RE.fullmatch(strongwiz[field]) is not None,
                f"Strongwiz {field} is not a pinned Git object")
    ci = strongwiz.get("verification_evidence", {})
    require(ci.get("head_ci_run") ==
            "https://github.com/Grativy6/strongwiz/actions/runs/33696382045",
            "Strongwiz CI receipt URL drifted")
    require(ci.get("head_ci_commit") == EXPECTED_STRONGWIZ["repository_commit"],
            "Strongwiz CI evidence is not bound to the inspected head")
    require(ci.get("head_ci_result") == "SUCCESS",
            "Strongwiz CI result changed")
    require(
        (
            ci.get("core_v3_tests_passed"),
            ci.get("ubuntu_full_tests_passed"),
            ci.get("windows_full_tests_passed"),
        ) == (51, 449, 449),
        "Strongwiz current-head CI test counts drifted",
    )
    blob_map = {
        item["filename"]: item["sha256"]
        for item in strongwiz.get("inspected_artifacts", [])
    }
    require(blob_map == EXPECTED_STRONGWIZ_BLOBS,
            "Strongwiz Git-blob identity set changed")

    candidate = read_json(CANDIDATE_PATH)
    policy_bytes = AGENT_PATH.read_bytes().replace(b"\r\n", b"\n")
    policy_hash = hashlib.sha256(policy_bytes).hexdigest()
    require(candidate.get("policy_hash_domain") ==
            "utf8_lf_normalized_repository_text_sha256",
            "policy hash domain missing")
    require(candidate.get("policy_sha256") == policy_hash,
            "candidate policy_sha256 does not match hearthline_agent.md")
    require(candidate.get("artifact_version") == "0.4-draft",
            "candidate artifact version drift")
    require(candidate.get("artifact_status") == "DRAFT_NOT_ACTIVATED",
            "candidate was activated by repository text")
    require(candidate.get("default_mode") == "DRAFT_ONLY", "default mode widened")
    require(candidate.get("source_profile_id") == "HEARTHLINE_PUBLIC_SOURCE_PROFILE_2",
            "source profile ID drift")
    candidate_pal = candidate["declared_sources"]["PAL"]
    require(candidate_pal.get("version") == "2.3", "candidate PAL version drift")
    require(candidate_pal.get("record_uri") == pal["persistent_id"],
            "candidate and registry PAL DOI differ")
    require(candidate.get("semantic_conformance") == "NOT_EVALUATED",
            "semantic conformance was manufactured")
    require(candidate.get("authority") == "NONE", "candidate authority widened")
    require(candidate.get("effect") == "NONE", "candidate effect widened")

    surfaces = {
        "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        "SOURCE_MAP.md": (ROOT / "SOURCE_MAP.md").read_text(encoding="utf-8"),
        "BOUNDARY.md": (ROOT / "BOUNDARY.md").read_text(encoding="utf-8"),
        "hearthline_agent.md": AGENT_PATH.read_text(encoding="utf-8"),
    }
    for name, text in surfaces.items():
        require("PAL v2.3" in text or "| PAL | 2.3 |" in text,
                f"{name} does not carry PAL v2.3")
    require("RESOLVED_LIVE_RECORD_CANONICAL_MATCH" in registry_text,
            "BRRRT live resolution status is absent")
    creature_text = CREATURE_DOC.read_text(encoding="utf-8")
    creature_words = " ".join(creature_text.split())
    for phrase in (
        "not a fourth Spark role",
        "physically isolated Creature instances",
        "canonical controller",
        "not a second ledger",
        "Pulse Receipt",
        "no action port",
    ):
        require(phrase in creature_words, f"Creature boundary missing: {phrase}")

    homecoming_text = HOMECOMING_DOC.read_text(encoding="utf-8")
    homecoming_words = " ".join(homecoming_text.split())
    require("| Version | `0.5` |" in homecoming_text,
            "Homecoming Return Queue successor version missing")
    for phrase in (
        "open objective window",
        "Returns may arrive out of order",
        "does not keep the exchange open",
        "one aggregation response",
        "homecoming_custody_state",
        "objective_disposition",
        "no Homecoming custody state manufactures task status",
        "no provider or environment effect is duplicated",
        "not a claim that Hearthline or this workspace has implemented or passed it",
    ):
        require(phrase in homecoming_words,
                f"objective-window boundary missing: {phrase}")

    for path in (
        RESEARCH_DOC,
        CREATURE_DOC,
        HOMECOMING_DOC,
        ROOT / "README.md",
        ROOT / "SOURCE_MAP.md",
    ):
        check_links(path)

    print("RESEARCH_STATION_OK")


if __name__ == "__main__":
    main()
