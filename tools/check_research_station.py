#!/usr/bin/env python3
"""Validate Hearthline's research station and current Light-Trio surfaces."""

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
FIRESIDES_DOC = ROOT / "docs" / "HEARTHLINE_FIRESIDES.md"
SPARKS_DOC = ROOT / "docs" / "HEARTHLINE_SPARKS.md"
STATIC_DOC = ROOT / "docs" / "HEARTHLINE_STATIC.md"
THULIA_DOC = ROOT / "docs" / "HEARTHLINE_THULIA.md"
GLOSS_DOC = ROOT / "docs" / "HEARTHLINE_GLOSS.md"
ORDERED_DOC = ROOT / "docs" / "HEARTHLINE_ORDERED_LINEAGE.md"
TASK_TRIADS_DOC = ROOT / "docs" / "HEARTHLINE_TASK_TRIADS.md"
VISUAL_DOC = ROOT / "docs" / "HEARTHLINE_VISUAL_INDEX.md"
THULIA_SHEET_DOC = ROOT / "docs" / "HEARTHLINE_THULIA_CHARACTER_SHEET_000002.md"
CHARACTERS_README = ROOT / "assets" / "characters" / "README.md"

THULIA_SHEET_000002_SHA256 = (
    "9080ca86547a8924e980e5339a8b45f6fce7bddb3a050115d4ddae19603b4650"
)
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


def words(text: str) -> str:
    return " ".join(text.split())


def require_all(text: str, phrases: tuple[str, ...], boundary: str) -> None:
    for phrase in phrases:
        require(phrase in text, f"{boundary} missing: {phrase}")


def require_absent(text: str, phrases: tuple[str, ...], boundary: str) -> None:
    for phrase in phrases:
        require(phrase not in text, f"{boundary} contains obsolete collapse: {phrase}")


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


def check_source_registry() -> tuple[dict[str, Any], str]:
    """Preserve the pinned public source and Strongwiz identity checks."""
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    lowered = registry_text.lower()
    for forbidden in ("c:\\users\\", "e:\\", "file://", "token=", "api_key"):
        require(forbidden not in lowered,
                f"registry contains private-path text: {forbidden}")

    registry = read_json(REGISTRY_PATH)
    require(registry.get("schema") == "hearthline.research-station.sources.v1",
            "unexpected research-station schema")
    require(registry.get("status") == "RESEARCH_CONTEXT_ONLY",
            "bad station status")
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
        require(source.get("authority_ceiling"),
                f"{source_id} lacks authority ceiling")
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
    require(
        {item.get("sha256") for item in current_pdfs}
        == {"f9e699ad4a8541506ecc6678c3296bdf4fbe4dd249a0dd6759c7fd0d22837e0a"},
        "BRRRT current loose/package SHA match lost",
    )
    historical = [
        item for item in brrrt_pdfs
        if item.get("variant", "").startswith("superseded_")
    ]
    require(len(historical) == 1 and historical[0].get("current_live_record") is False,
            "BRRRT superseded wrapper observation missing")

    strongwiz = find_source(registry, "strongwiz-v3-prototype")
    require(strongwiz.get("prototype_status") ==
            "PREPARED_NOT_RUN_NOT_PREREGISTERED",
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
    require(ci.get("head_ci_result") == "SUCCESS", "Strongwiz CI result changed")
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
    return pal, registry_text


def check_candidate(pal: dict[str, Any]) -> None:
    candidate = read_json(CANDIDATE_PATH)
    policy_bytes = AGENT_PATH.read_bytes().replace(b"\r\n", b"\n")
    policy_hash = hashlib.sha256(policy_bytes).hexdigest()
    require(candidate.get("policy_hash_domain") ==
            "utf8_lf_normalized_repository_text_sha256",
            "policy hash domain missing")
    require(candidate.get("policy_sha256") == policy_hash,
            "candidate policy_sha256 does not match hearthline_agent.md")
    require(candidate.get("artifact_version") == "0.7-draft",
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


def check_light_trio_surfaces(registry_text: str) -> dict[str, str]:
    surfaces = {
        "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        "SOURCE_MAP.md": (ROOT / "SOURCE_MAP.md").read_text(encoding="utf-8"),
        "BOUNDARY.md": (ROOT / "BOUNDARY.md").read_text(encoding="utf-8"),
        "hearthline_agent.md": AGENT_PATH.read_text(encoding="utf-8"),
        "HEARTHLINE_CREATURES.md": CREATURE_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_HOMECOMING.md": HOMECOMING_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_FIRESIDES.md": FIRESIDES_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_SPARKS.md": SPARKS_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_STATIC.md": STATIC_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_THULIA.md": THULIA_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_GLOSS.md": GLOSS_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_ORDERED_LINEAGE.md": ORDERED_DOC.read_text(encoding="utf-8"),
        "HEARTHLINE_TASK_TRIADS.md": TASK_TRIADS_DOC.read_text(encoding="utf-8"),
    }
    for name in ("README.md", "SOURCE_MAP.md", "BOUNDARY.md", "hearthline_agent.md"):
        text = surfaces[name]
        require("PAL v2.3" in text or "| PAL | 2.3 |" in text,
                f"{name} does not carry PAL v2.3")
    require("RESOLVED_LIVE_RECORD_CANONICAL_MATCH" in registry_text,
            "BRRRT live resolution status is absent")

    expected_versions = {
        "HEARTHLINE_CREATURES.md": "| Version | `0.4` |",
        "HEARTHLINE_HOMECOMING.md": "| Version | `0.7` |",
        "HEARTHLINE_FIRESIDES.md": "| Version | `0.6` |",
        "HEARTHLINE_SPARKS.md": "| Version | `0.9` |",
        "HEARTHLINE_STATIC.md": "| Version | `0.8` |",
        "HEARTHLINE_THULIA.md": "| Version | `0.6` |",
        "HEARTHLINE_GLOSS.md": "| Version | `0.3` |",
        "HEARTHLINE_ORDERED_LINEAGE.md": "| Version | `0.9` |",
        "HEARTHLINE_TASK_TRIADS.md": "| Version | `0.2-draft` |",
    }
    for name, marker in expected_versions.items():
        require(marker in surfaces[name], f"{name} current version marker missing")
    require("version: 0.7-draft" in surfaces["hearthline_agent.md"],
            "agent current version marker missing")

    task_triads = words(surfaces["HEARTHLINE_TASK_TRIADS.md"])
    require_all(
        task_triads,
        (
            "Hearthline exclusively provisions the Work Spark and Task-Keeper jobs",
            "Thulia exclusively provisions the Ledger Scribe/Ledger-Keeper job",
            "Neither interface provisions, selects, or binds the other interface's seat",
            "controller atomically matches their two independently committed final provisioning intents",
            "Only `TRIAD_BOUND` permits a later dispatch attempt; it does not itself start a member or expose an action lane",
            "Member bundles never return to Thulia first: each valid sealed bundle returns separately to the exact Hearthline task intake that commissioned it",
            "`RETURN_HELD_STALE_EPOCH`",
            "`RETURN_PENDING_HEARTHLINE`",
            "`member_return_transaction_ref`",
            "`member_return_emission_state`",
            "`member_intake_receipt_state`",
            "Triad Return Manifest",
            "immutable Carry Selection",
            "carry_selection_coverage_state",
            "`SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`",
            "selected_carry_store_outcome_state: COMMITTED",
            "`inspection_context_state: RAW_ACCESS_DROPPED`",
            "four separately granted and receipted `H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE` lanes",
            "`owl_turn_disposition: CANDIDATE_COMPLETE`",
            "Gloss has no Task Line of its own, no open objective, no context window, no prior-turn reads, no Homecoming, no ledger ownership, and no heartbeat",
            "Readiness is checked anew for each exact turn; it is never inherited",
            "Systemic Friction classification != Atomic Edge Promotion authority",
            "source_recoverability_state",
            "Inspection closure and pruning are independent edges",
            "MAX_SUPPORT_DEPTH = 1",
        ),
        "Task-Triad Light Trio architecture",
    )

    agent = words(surfaces["hearthline_agent.md"])
    require_all(
        agent,
        (
            "Hearthline nonbindingly nominates only Worker plus Task-Keeper; Thulia independently nominates only Ledger-Keeper",
            "Every Triad member returns through its own controller/store-mediated transaction to the exact predeclared Hearthline task intake, never to Thulia",
            "Only a controller-observed `SEALED`, separately `VALID` bundle from a `SEALED_TERMINAL` member may enter `RETURN_PENDING_HEARTHLINE`",
            "**Complete Return Manifest:**",
            "Immutable Carry Selection",
            "selected_carry_store_outcome_state: COMMITTED",
            "raw Hearthline aperture may enter `CLOSE_PENDING` only after durable `ACCEPTED_BY_THULIA`",
            "`H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE` each require their own grant",
            "exactly `CANDIDATE_COMPLETE`",
            "`gloss_readiness_state` is checked externally for each exact turn as `READY_FOR_EXACT_TURN`, `NOT_READY`, or `READINESS_UNKNOWN`",
            "only Thulia applies **Systemic Friction**",
            "A canonical controller or separately authorized writer must revalidate the exact candidate, epochs, and holds before recording any Atomic Edge Promotion",
            "`canonical_store_effect_state` and `source_recoverability_state` remain independent",
            "`RAW_ACCESS_DROPPED` attests only controller-observed closure",
        ),
        "agent Light Trio architecture",
    )

    homecoming = words(surfaces["HEARTHLINE_HOMECOMING.md"])
    require_all(
        homecoming,
        (
            "raw member returns go separately to the commissioning Hearthline intake",
            "`RETURN_PENDING_HEARTHLINE`",
            "immutable **Carry Selection**",
            "The Carry Selection crosses four independently receipted lanes",
            "`H_TO_T_CARRY`",
            "`T_TO_GLOSS_TURN`",
            "`GLOSS_TO_T_RESULT`",
            "`T_TO_H_READABLE`",
            "`CANDIDATE_COMPLETE`",
            "`selected_carry_store_outcome_state: COMMITTED`",
            "`RAW_ACCESS_DROPPED`",
            "Only afterward does Thulia apply **Systemic Friction**",
            "Atomic Edge Promotion",
            "source_recoverability_state",
        ),
        "Homecoming selected-carry route",
    )

    thulia = words(surfaces["HEARTHLINE_THULIA.md"])
    require_all(
        thulia,
        (
            "one bounded custody role with exactly three non-overlapping duties",
            "The three member bundles do **not** return to Thulia",
            "A controller-observed `SEALED` plus separately `VALID` bundle then returns directly to Hearthline's task intake under its own identity and target receipt",
            "Hearthline may inspect separately admitted member bundles and make the semantic Carry Selection",
            "`H_TO_T_CARRY`",
            "`T_TO_H_READABLE`",
            "`T_TO_GLOSS_TURN`",
            "`GLOSS_TO_T_RESULT`",
            "`CANDIDATE_COMPLETE`",
            "Only Thulia applies Systemic Friction",
            "The canonical store then performs **Atomic Edge Promotion**",
        ),
        "Thulia custody boundary",
    )

    gloss = words(surfaces["HEARTHLINE_GLOSS.md"])
    require_all(
        gloss,
        (
            "Mechanism class | `STATELESS_DETERMINISTIC`",
            "history_reads: 0",
            "`gloss_readiness_state`",
            "`READY_FOR_EXACT_TURN`",
            "`NOT_READY`",
            "`READINESS_UNKNOWN`",
            "Gloss does not receive a Spark identity, Task-Keeper, Ledger-Keeper, Heartbeat Contract, Pulse Receipt, Home, Homecoming, liveness state, or private ledger",
            "`T_TO_GLOSS_TURN`",
            "`GLOSS_TO_T_RESULT`",
            "`T_TO_H_READABLE`",
            "Gloss never applies **Systemic Friction**",
            "Atomic Edge Promotion",
        ),
        "Gloss deterministic-turn boundary",
    )

    supporting_requirements = {
        "HEARTHLINE_CREATURES.md": (
            "Task Triad",
            "Carry Selection",
            "`H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE`",
            "selected-carry",
            "Systemic Friction",
            "Atomic Edge Promotion",
            "source recoverability",
        ),
        "HEARTHLINE_FIRESIDES.md": (
            "`RETURN_PENDING_HEARTHLINE`",
            "Carry Selection",
            "`H_TO_T_CARRY`",
            "`T_TO_GLOSS_TURN`",
            "`GLOSS_TO_T_RESULT`",
            "`T_TO_H_READABLE`",
            "Systemic Friction",
            "Atomic Edge Promotion",
            "source recoverability",
        ),
        "HEARTHLINE_SPARKS.md": (
            "Light Trio",
            "`RETURN_PENDING_HEARTHLINE`",
            "Carry Selection",
            "H_TO_T_CARRY",
            "T_TO_GLOSS_TURN",
            "GLOSS_TO_T_RESULT",
            "T_TO_H_READABLE",
            "Systemic Friction",
            "Atomic Edge Promotion",
            "Gloss readiness",
        ),
        "HEARTHLINE_STATIC.md": (
            "`RETURN_PENDING_HEARTHLINE`",
            "Carry Selection",
            "`H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE`",
            "heartbeat-free deterministic turn",
            "Systemic Friction",
            "Atomic Edge Promotion",
            "recoverability state",
        ),
        "HEARTHLINE_ORDERED_LINEAGE.md": (
            "`RETURN_PENDING_HEARTHLINE`",
            "Carry Selection",
            "`selected_carry_store_outcome_state`",
            "`H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE`",
            "`owl_turn_disposition: CANDIDATE_COMPLETE`",
            "Gloss has no heartbeat",
            "Systemic Friction",
            "Atomic Edge Promotion",
            "source recoverability",
        ),
    }
    for name, phrases in supporting_requirements.items():
        require_all(words(surfaces[name]), phrases, f"{name} Light Trio alignment")

    # Reject the old active route and role absorption. Historical predecessor
    # descriptions remain allowed, but current normative sentences may not use
    # these exact obsolete forms.
    for name in (
        "hearthline_agent.md",
        "HEARTHLINE_CREATURES.md",
        "HEARTHLINE_HOMECOMING.md",
        "HEARTHLINE_FIRESIDES.md",
        "HEARTHLINE_SPARKS.md",
        "HEARTHLINE_STATIC.md",
        "HEARTHLINE_THULIA.md",
        "HEARTHLINE_GLOSS.md",
        "HEARTHLINE_ORDERED_LINEAGE.md",
        "HEARTHLINE_TASK_TRIADS.md",
    ):
        require_absent(
            words(surfaces[name]),
            (
                "returns its Work, Task-Boundary Witness, and Ledger payloads separately through Thulia",
                "Hearthline provisions the Ledger-Keeper",
                "Hearthline provisions the Ledger Scribe",
                "Thulia provisions the Worker and Task-Keeper",
                "Thulia provisions the Work Spark and Task-Keeper",
                "Task-Keeper keeps the Worker alive",
                "Task-Keeper keeps a runtime alive",
                "Gloss receives a heartbeat",
                "support_depth: 2",
                "MAX_SUPPORT_DEPTH = 2",
            ),
            name,
        )

    require("Systemic Friction" not in registry_text,
            "Systemic Friction must not become a Research Station source")
    return surfaces


def check_visual_lineage() -> None:
    visual_text = VISUAL_DOC.read_text(encoding="utf-8")
    characters_text = CHARACTERS_README.read_text(encoding="utf-8")
    require("| Version | `0.3` |" in visual_text,
            "visual index behavior-pointer successor version missing")
    require(
        hashlib.sha256(THULIA_SHEET_DOC.read_bytes()).hexdigest()
        == THULIA_SHEET_000002_SHA256,
        "issued Thulia SHEET-000002 changed in place",
    )
    for name, text in (
        ("HEARTHLINE_VISUAL_INDEX.md", visual_text),
        ("assets/characters/README.md", characters_text),
    ):
        require("OWL-000001/PROFILE-000004" in text,
                f"{name} lacks the adopted Thulia behavior pointer")
        for candidate_profile in (
            "OWL-000001/PROFILE-000005",
            "OWL-000001/PROFILE-000006",
        ):
            require(candidate_profile not in text,
                    f"{name} prematurely promotes {candidate_profile}")
        require("OWL-000001/PROFILE-000003" not in text,
                f"{name} still calls the predecessor Thulia profile current")


def main() -> None:
    pal, registry_text = check_source_registry()
    check_candidate(pal)
    check_light_trio_surfaces(registry_text)
    check_visual_lineage()

    for path in (
        RESEARCH_DOC,
        CREATURE_DOC,
        HOMECOMING_DOC,
        FIRESIDES_DOC,
        SPARKS_DOC,
        STATIC_DOC,
        THULIA_DOC,
        GLOSS_DOC,
        ORDERED_DOC,
        TASK_TRIADS_DOC,
        VISUAL_DOC,
        THULIA_SHEET_DOC,
        CHARACTERS_README,
        AGENT_PATH,
        ROOT / "README.md",
        ROOT / "SOURCE_MAP.md",
    ):
        check_links(path)

    print("RESEARCH_STATION_OK")


if __name__ == "__main__":
    main()
