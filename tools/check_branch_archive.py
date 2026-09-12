#!/usr/bin/env python3
"""Validate the pointer-only archive of retired Hearthline review lanes."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "changelog" / "branch-archive.json"
RESERVATIONS = ROOT / "docs" / "changelog" / "branch-reservations.json"
CHANGE_RECORD = (
    ROOT / "docs" / "changelog"
    / "2026-09-06-hlp-000019-retired-review-lanes.md"
)
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
CHANGELOG_ARCHIVES = ROOT / "docs" / "changelog" / "index"

SCHEMA = "hearthline.change-history.branch-archive.v1"
MAIN_COMMIT = "445d8e41df7129d67657130175644696d4d7e8e9"
MAIN_TREE = "96e31075aa2b117a8302c2d52df6b99156b85ea9"
STATUS = "RETIRED_REVIEW_LANES"
EFFECT = "TRACE_ONLY_NO_CONTENT_ADOPTION"
STORAGE = "SOURCE_BRANCH_GIT_OBJECTS_NOT_ARCHIVE_COPIES"
COMPARISON_SCOPE = "SOURCE_DELTA_FROM_MERGE_BASE_AGAINST_RECORDED_MAIN"
LANE_STATE = "OPEN_UNMERGED"
LANE_DISPOSITION = "RETIRED_FROM_ACTIVE_SELECTION_PRESERVED_FOR_REOPENING"
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

PR4_DUPLICATES = (
    (
        "assets/characters/hearthline/HEARTHLINE-IMAGE-000001-gremlin-hunter-reference-sheet.png",
        "ec83e6bbf711f58448f2d9022af2f37cb1a0a828",
        "assets/characters/hearthline-gremlin-hunter-reference-sheet.png",
        "c687dbc75f4209de4dad6c69e72b00221ad6b5cbbe5be2ba5037b075a7e8948b",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000001-fireside-portrait.png",
        "d1218e4ad2a0b28fb01ba335cc941187638d12a0",
        "assets/characters/history-and-artifacts/thulia-fireside-portrait-study.png",
        "f3aedaecdd63235f1e7485de6123aad5bf74780a5d778eef58ebbe84f6ff61ba",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000002-naturalistic-model-sheet-study.png",
        "f2fe17b6c1515b8bf1307ad33dd60258e6ce8509",
        "assets/characters/history-and-artifacts/thulia-naturalistic-model-sheet-study.png",
        "09977aff8345ed682da6ead729ef0497dc8b7fdb822e78ac99b2443ee22620ca",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000003-cartoon-expression-sheet-study.png",
        "a538ad613c9c580f21ebf4710824789ae71c938d",
        "assets/characters/history-and-artifacts/thulia-cartoon-expression-sheet-study.png",
        "9e26ce5be35f6f375cbf583da441b3cff613bcd05283a936332c9d483c565dcb",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000004-bilateral-sheet-initial.png",
        "c5c17fd2b3aaf3a62fed80c42f1a796ece5ea672",
        "assets/characters/history-and-artifacts/thulia-bilateral-sheet-initial.png",
        "d5c90e5052918ee5056852fd9d6113eff5bef951602e893de67b71e733da14fe",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000005-bilateral-sheet-front-correction.png",
        "bb0d2726c6c7ea2f33866990b9f483d746fdd15d",
        "assets/characters/history-and-artifacts/thulia-bilateral-sheet-front-correction.png",
        "774c68ad2901eac668288e21a785e8860d6e11e96205073af6df2951739f28ba",
    ),
    (
        "assets/characters/thulia/OWL-000001-IMAGE-000006-bilateral-animation-reference.png",
        "469e1fc04fa81d26ea8437dbc08b6e6aeacc9783",
        "assets/characters/thulia-bilateral-animation-reference-sheet.png",
        "89a1c020bdb523150d0271a702186bbeed967db4822063b3cc0b1e4d2e97bae5",
    ),
    (
        "assets/scenes/OWL-000001-IMAGE-000007-hearthline-thulia-fireside.png",
        "95fe547936bca9c1482857c97dcb05b1a25b76c4",
        "assets/scenes/hearthline-and-thulia-at-the-trace-workbench.png",
        "0919ec8bf0a0577f668a013b041be1b18a15e562bf9cc6d4c0c97a3c6775d602",
    ),
)

PR4_VARIANTS = (
    (
        "CHANGELOG.md",
        "71fe50d5a2e8c6b96067d0b9eaae57e8dd38fa8b",
        "9753408500d694e61078ef1572f92b17c939b87cef75db6f227ebb712711b5f1",
    ),
    (
        "README.md",
        "a3fe67fae58fb45fa1e597dad824c872fa56a74a",
        "dee10c3639a58c332d2efe21f1526f33028cc5c3fe5def95641d926c4e800db3",
    ),
    (
        "assets/README.md",
        "141bc5b021bdfcc333a64783ad7b458dc510b3d8",
        "bc5df43e89ebb1ccdf1fb373659948576bb708ad7a28cb6f884c5bc4a864c9b9",
    ),
    (
        "docs/HEARTHLINE_ORDERED_LINEAGE.md",
        "3a61a0d867832cb7bff25587872decc073f135a0",
        "979a9c1d0b26effde696b5c79b34610a0e77116dbe75beb07cd8459e3f245b19",
    ),
    (
        "docs/HEARTHLINE_THULIA_CHARACTER_SHEET_000002.md",
        "fc9fe9e8e8c444931baa44aa29242de480dbd3ab",
        "63707b0528a20abf3bb7588bf9292dfef835c2715c0902f078da22356844ca34",
    ),
    (
        "docs/HEARTHLINE_VISUAL_INDEX.md",
        "bcb0298496671954a70313f76caf388c8e71778d",
        "96db2fd055a5aa93b339d275f5eabdd15d42703df97e78158a7f5db6d3b03b17",
    ),
)

PR12_RESIDUALS = (
    (
        "START_HERE.md",
        "0ac0a084de28bc0dbbd6c16e4f39e48c4c120b8e",
        "66e9e79df5717366c2897a4a637dd3e9273a7f703a3dd6bed8da246f8531a7b4",
    ),
    (
        "docs/ARC_AGI_3_HANDOFF.md",
        "864aea3e58adba5cf1f7c91edaf95a5fc174b5e7",
        "88406e116f0a472550a38764931e96fc269fbaf77b47e6e84628325830371c06",
    ),
    (
        "docs/CURRENT_SYSTEM_MAP.md",
        "ad511759952027189d7a5850df707f1f0bd49555",
        "70098a6db717703f426515260c5ec9f8742eb386c1f927930ad572093cee7329",
    ),
    (
        "docs/HEARTHLINE_GLOSS.md",
        "0ace93d8d21e65153cd1cdc1e092a2a559ae0ac7",
        "1fd4f93232d641f3866fea879c5d8b8363a969e5bd3e924b366be3d36cbd0f61",
    ),
    (
        "docs/HEARTHLINE_TASK_TRIADS.md",
        "631719fd3bc19c62fe2b0c0954aaad523e389183",
        "b12260dc0f5d1fcb5babf2df4a4009d01b0fb00c96ae74c9080569cb1a252f37",
    ),
    (
        "docs/RUN_SURFACE_MAP.md",
        "9e3bd6c7f9be7c3f5e636d2ac6d60cf6e36ce80c",
        "564fc536f3fd3bbccbe1696a2273cc1052146421ace5a9e731910b63b2c58fe8",
    ),
    (
        "docs/history/SUPERSESSION_INDEX.md",
        "d2e8f7a337b24de245dc9cd385deea49a0fc6dcf",
        "b005d3d21bb01980e6aa777c178d6c593b378bff3eea449769b015ef53f32831",
    ),
    (
        "lore/THE_CREATURES_OF_THE_CIRCUIT_GARDEN.md",
        "16e7137eafc4510bf4f5bce5f51a97cbb30fbc69",
        "3077240eebfa5a4016cebef1175d88593734b5b01522a94b5b3db0567d182821",
    ),
    (
        "lore/THE_NIGHT_THE_GARDEN_CLICKED.md",
        "8b46d92cbb0bdf0468d39cc5a804c75d200df428",
        "f6ce21e0b506f2a53f058d6dcbcf6908300c90e83c1fc88d87103ba51dcff431",
    ),
    (
        "tools/check_foundation_maps.py",
        "7b361b73d01e29dc6e89d31d5be773bb4efe9bd3",
        "d18ba94a4abf844862648dab17dd15b805d2d9e2e187044af29cb3b0e95134bb",
    ),
)

EXPECTED_LANES = {
    4: {
        "source_branch": "codex/thulia-visual-lineage",
        "source_commit": "1780aafb13db926a49cd298b1765f260a5e3a145",
        "source_tree": "abe2cc6b381eda4705ccf5e00616fcbed33d4946",
        "merge_base": "b7297795845d5d6c3926e4f18fbef32790a1dab5",
    },
    12: {
        "source_branch": "codex/charter-publication-anchor-20260905",
        "source_commit": "3da4aca46f4bc7b3bea2fcf31bdfb3ed8aa31274",
        "source_tree": "0f4ae1bcc16059c209b95959903f737c7507a555",
        "merge_base": "dd00eaa30e46b74baf31f120622caef16a4e73dd",
    },
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


def load_json(path: Path, byte_limit: int) -> dict[str, Any]:
    raw = path.read_bytes()
    require(len(raw) <= byte_limit, f"{path.relative_to(ROOT)} is too large")
    require(b"/workspace/" not in raw, f"{path.relative_to(ROOT)} leaks a local path")
    value = json.loads(raw, object_pairs_hook=no_duplicate_object)
    require(isinstance(value, dict), f"{path.relative_to(ROOT)} root must be an object")
    return value


def git_blob_oid(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def expected_path_records(
    rows: tuple[tuple[str, str, str], ...],
) -> list[dict[str, str]]:
    return [
        {"path": path, "blob": blob, "sha256": digest}
        for path, blob, digest in rows
    ]


def check_lane_identity(lane: dict[str, Any], number: int) -> None:
    expected = EXPECTED_LANES[number]
    branch = expected["source_branch"]
    commit = expected["source_commit"]
    tree = expected["source_tree"]
    source_ref = f"refs/heads/{branch}"
    require(lane["pull_request"] == number, f"PR #{number} number changed")
    require(
        lane["pull_request_url"]
        == f"https://github.com/Grativy6/hearthline/pull/{number}",
        f"PR #{number} URL changed",
    )
    require(lane["source_branch"] == branch, f"PR #{number} branch changed")
    require(lane["source_ref"] == source_ref, f"PR #{number} ref changed")
    require(lane["state_at_recording"] == LANE_STATE, f"PR #{number} state changed")
    require(
        lane["disposition"] == LANE_DISPOSITION,
        f"PR #{number} retirement disposition changed",
    )
    require(lane["source_commit"] == commit, f"PR #{number} commit changed")
    require(lane["source_tree"] == tree, f"PR #{number} tree changed")
    require(
        lane["merge_base_with_recorded_main"] == expected["merge_base"],
        f"PR #{number} merge base changed",
    )
    require(
        lane["commit_url"]
        == f"https://github.com/Grativy6/hearthline/commit/{commit}",
        f"PR #{number} immutable locator changed",
    )
    require(
        lane["reopen_handle"]
        == {
            "preferred_ref": source_ref,
            "fallback_ref": f"refs/pull/{number}/head",
            "required_commit": commit,
            "required_tree": tree,
            "identity_rule": "COMMIT_AND_TREE_MUST_MATCH",
        },
        f"PR #{number} reopen handle changed",
    )
    require(lane["content_copied"] is False, f"PR #{number} claims copied content")
    for field in ("source_commit", "source_tree", "merge_base_with_recorded_main"):
        require(SHA1_RE.fullmatch(lane[field]) is not None,
                f"PR #{number} has invalid {field}")


def check_pr4(lane: dict[str, Any]) -> None:
    expected_duplicates = [
        {
            "source_path": source_path,
            "source_blob": blob,
            "canonical_main_path": main_path,
            "canonical_main_blob": blob,
            "sha256": digest,
        }
        for source_path, blob, main_path, digest in PR4_DUPLICATES
    ]
    require(
        lane["exact_duplicates_on_recorded_main"] == expected_duplicates,
        "PR #4 exact duplicate mappings changed",
    )
    for source_path, blob, main_path, digest in PR4_DUPLICATES:
        source = ROOT / source_path
        canonical = ROOT / main_path
        require(not source.exists(), f"PR #4 duplicate was copied locally: {source_path}")
        require(canonical.is_file(), f"PR #4 canonical duplicate is missing: {main_path}")
        data = canonical.read_bytes()
        require(git_blob_oid(data) == blob, f"PR #4 canonical blob changed: {main_path}")
        require(hashlib.sha256(data).hexdigest() == digest,
                f"PR #4 canonical digest changed: {main_path}")

    require(lane["selected_unique_residual_paths"] == [],
            "PR #4 gained selected content carry")
    require(
        lane["superseded_variant_paths"] == expected_path_records(PR4_VARIANTS),
        "PR #4 superseded variant pointers changed",
    )
    for path, source_blob, digest in PR4_VARIANTS:
        require(SHA1_RE.fullmatch(source_blob) is not None,
                f"PR #4 variant blob is invalid: {path}")
        require(SHA256_RE.fullmatch(digest) is not None,
                f"PR #4 variant digest is invalid: {path}")
        current = ROOT / path
        require(current.is_file(), f"current successor path is missing: {path}")
        require(git_blob_oid(current.read_bytes()) != source_blob,
                f"PR #4 variant became current without a successor record: {path}")
    require(lane["delegated_history_manifest"] is None,
            "PR #4 unexpectedly delegates history")
    require(lane["explicitly_unselected_paths"] == [],
            "PR #4 unselected-path contract changed")
    note = lane["selection_note"]
    require(isinstance(note, str) and "eight image blobs" in note
            and "superseded branch variants" in note,
            "PR #4 selection note lost its duplicate/variant boundary")


def check_pr12(lane: dict[str, Any]) -> None:
    require(lane["exact_duplicates_on_recorded_main"] == [],
            "PR #12 gained an unverified exact-duplicate claim")
    expected_residuals = expected_path_records(PR12_RESIDUALS)
    require(lane["selected_unique_residual_paths"] == expected_residuals,
            "PR #12 selected residual pointers changed")
    for path, blob, digest in PR12_RESIDUALS:
        require(SHA1_RE.fullmatch(blob) is not None,
                f"PR #12 residual blob is invalid: {path}")
        require(SHA256_RE.fullmatch(digest) is not None,
                f"PR #12 residual digest is invalid: {path}")
        require(not (ROOT / path).exists(),
                f"PR #12 residual was copied or adopted locally: {path}")
    require(lane["superseded_variant_paths"] == [],
            "PR #12 gained superseded variant carry")

    manifest = lane["delegated_history_manifest"]
    require(
        manifest
        == {
            "path": "docs/changelog/branch-reservations.json",
            "sha256": "8b98838dbbc66ea846d183a98241144e095baf9097cdd7237d112543daec7599",
            "covers_source_commit": EXPECTED_LANES[12]["source_commit"],
            "covered_ids": [f"HLP-{number:06d}" for number in range(8, 14)],
            "effect": "NAMESPACE_ONLY_NO_ADOPTION",
        },
        "PR #12 delegated history manifest changed",
    )
    require(hashlib.sha256(RESERVATIONS.read_bytes()).hexdigest() == manifest["sha256"],
            "branch reservation manifest digest changed")
    reservations = load_json(RESERVATIONS, 12 * 1024)
    require(reservations["source"]["commit"] == manifest["covers_source_commit"],
            "branch reservations no longer cover the archived PR #12 head")
    require(
        [record["id"] for record in reservations["reservations"]]
        == manifest["covered_ids"],
        "branch reservations no longer cover HLP-000008 through HLP-000013",
    )
    require(
        lane["explicitly_unselected_paths"]
        == [{
            "path": "docs/WIP_TASK_TRIAD_CHECKPOINT_2026-09-04.md",
            "classification": "WIP_UNSELECTED",
        }],
        "PR #12 WIP exclusion changed",
    )
    note = lane["selection_note"]
    require(isinstance(note, str) and "ten pointers" in note
            and "complete source commit and tree" in note,
            "PR #12 selection note lost its pointer-only coverage boundary")


def main() -> None:
    archive = load_json(LEDGER, 32 * 1024)
    require(
        set(archive)
        == {
            "schema", "series", "change_id", "recorded_date", "repository",
            "recorded_against_main", "comparison_scope", "status", "effect",
            "authority", "content_storage", "lanes",
        },
        "branch archive root keys changed",
    )
    require(archive["schema"] == SCHEMA, "branch archive schema changed")
    require(archive["series"] == "HLP", "branch archive series changed")
    require(archive["change_id"] == "HLP-000019",
            "branch archive change identity changed")
    require(archive["recorded_date"] == "2026-09-06",
            "branch archive recorded date changed")
    require(archive["repository"] == "Grativy6/hearthline",
            "branch archive repository changed")
    require(
        archive["recorded_against_main"]
        == {"commit": MAIN_COMMIT, "tree": MAIN_TREE},
        "branch archive mainline anchor changed",
    )
    require(archive["comparison_scope"] == COMPARISON_SCOPE,
            "branch archive comparison scope changed")
    require(archive["status"] == STATUS, "branch archive status changed")
    require(archive["effect"] == EFFECT, "branch archive effect widened")
    require(archive["authority"] == "NONE", "branch archive created authority")
    require(archive["content_storage"] == STORAGE,
            "branch archive content-storage boundary changed")

    lanes = archive["lanes"]
    require(isinstance(lanes, list) and len(lanes) == 2,
            "branch archive must contain exactly two lanes")
    require([lane.get("pull_request") for lane in lanes] == [4, 12],
            "branch archive lanes must remain PR #4 then PR #12")
    expected_keys = {
        "pull_request", "pull_request_url", "source_branch", "source_ref",
        "state_at_recording", "disposition", "source_commit", "source_tree",
        "merge_base_with_recorded_main", "commit_url", "reopen_handle",
        "content_copied", "exact_duplicates_on_recorded_main",
        "selected_unique_residual_paths", "superseded_variant_paths",
        "delegated_history_manifest", "explicitly_unselected_paths",
        "selection_note",
    }
    for lane in lanes:
        require(isinstance(lane, dict), "branch archive lane must be an object")
        require(set(lane) == expected_keys,
                f"PR #{lane.get('pull_request')} lane keys changed")
        check_lane_identity(lane, lane["pull_request"])

    check_pr4(lanes[0])
    check_pr12(lanes[1])

    all_source_paths: list[str] = []
    for lane in lanes:
        all_source_paths.extend(
            row["source_path"]
            for row in lane["exact_duplicates_on_recorded_main"]
        )
        all_source_paths.extend(
            row["path"] for row in lane["selected_unique_residual_paths"]
        )
        all_source_paths.extend(
            row["path"] for row in lane["superseded_variant_paths"]
        )
        all_source_paths.extend(
            row["path"] for row in lane["explicitly_unselected_paths"]
        )
    require(len(all_source_paths) == len(set(all_source_paths)),
            "branch archive source paths overlap across classifications")

    require(CHANGE_RECORD.is_file(), "HLP-000019 change record is missing")
    record = CHANGE_RECORD.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    changelog = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            CHANGELOG,
            *sorted(CHANGELOG_ARCHIVES.glob("*.md")),
        )
    )
    for anchor in (
        EXPECTED_LANES[4]["source_commit"], EXPECTED_LANES[4]["source_tree"],
        EXPECTED_LANES[12]["source_commit"], EXPECTED_LANES[12]["source_tree"],
    ):
        require(anchor in record, f"HLP-000019 does not name anchor {anchor}")
    require("branch-archive.json" in record,
            "HLP-000019 does not link the branch archive")
    require("branch-archive.json" in readme,
            "README does not route to the branch archive")
    require("HLP-000019" in readme and "HLP-000019" in changelog,
            "public history surfaces do not expose HLP-000019")

    print("BRANCH_ARCHIVE_OK")


if __name__ == "__main__":
    main()
