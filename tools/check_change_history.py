#!/usr/bin/env python3
"""Validate Hearthline's bounded public change-history surfaces."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "CHANGELOG.md"
NOTES = ROOT / "docs" / "changelog"
ARCHIVES = NOTES / "index"
RESERVATIONS = NOTES / "branch-reservations.json"
START = "<!-- latest-change:start -->"
END = "<!-- latest-change:end -->"
ROW_RE = re.compile(
    r"^\|\s*`(?P<id>HLP-(?P<number>\d{6}))`\s*\|\s*"
    r"(?P<date>\d{4}-\d{2}-\d{2})\s*\|\s*`(?P<kind>[A-Z_]+)`\s*\|"
    r"(?P<summary>[^|]+)\|\s*\[Record\]\((?P<link>[^)]+)\)\s*\|\s*$",
    re.MULTILINE,
)
NOTE_NAME_RE = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<id>hlp-\d{6})-[a-z0-9-]+\.md"
)
ARCHIVE_NAME_RE = re.compile(r"hlp-(?P<low>\d{6})-to-hlp-(?P<high>\d{6})\.md")
WORD_RE = re.compile(r"\b[\w'-]+\b")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FULL_RECORD_RE = re.compile(r"\[Full change record\]\(([^)]+)\)")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_HEADINGS = (
    "## What changed",
    "## Why",
    "## Preserved boundaries",
    "## Compatibility and migration",
    "## Verification observations",
    "## Open residuals",
    "## Evidence and exclusions",
)
FORBIDDEN_TEXT = (
    "hearthline-workshop",
    "token=",
    "file://",
    "/workspace/",
    "c:\\users\\",
)
RESERVATION_SCHEMA = "hearthline.change-history.branch-reservations.v1"
RESERVATION_STATUS = "RESERVED_OFF_MAIN_NOT_ADOPTED"
RESERVATION_EFFECT = "NAMESPACE_ONLY_NO_ADOPTION"
FROZEN_RECORD_SHA256 = {
    "2026-09-05-hlp-000015-morrow-homecoming-priority.md":
        "3c9620320309573023e0f3659dba00d3cd52328999be2edab7fd4ab6d2dd2ae1",
}
RESERVATION_SOURCE = {
    "repository": "Grativy6/hearthline",
    "pull_request": 12,
    "pull_request_url": "https://github.com/Grativy6/hearthline/pull/12",
    "commit": "3da4aca46f4bc7b3bea2fcf31bdfb3ed8aa31274",
    "tree": "0f4ae1bcc16059c209b95959903f737c7507a555",
    "content_hash_domain": "git_object_content_bytes_sha256",
}
EXPECTED_RESERVATIONS = (
    (
        "HLP-000008",
        8,
        "docs/changelog/2026-09-04-hlp-000008-thulia-gloss-systemic-friction.md",
        "e838917cfe2a165212658c2ae8ae9ca24ab59372b76e912aec95f466b54cc40d",
    ),
    (
        "HLP-000009",
        9,
        "docs/changelog/2026-09-04-hlp-000009-the-night-the-garden-clicked.md",
        "92e225b3ca16a819be63cf2231f27b694fa85af5f06d3dede41bd322472ac58f",
    ),
    (
        "HLP-000010",
        10,
        "docs/changelog/2026-09-04-hlp-000010-task-triad-lifecycle.md",
        "40de422653944c1d90159b9a92866007cb146b1ff5e1a6f39e586dd5ce368473",
    ),
    (
        "HLP-000011",
        11,
        "docs/changelog/2026-09-04-hlp-000011-light-trio-selected-carry.md",
        "d73ad10c5623e068cf66d47ed0a4fe516c2250ec5f217fc6c2a5e3a0e9db3d1a",
    ),
    (
        "HLP-000012",
        12,
        "docs/changelog/2026-09-05-hlp-000012-creature-charter-companion.md",
        "e9219758066ef90ecf3e0c08878b21974f509c7629a36b67ff166e9d6de47645",
    ),
    (
        "HLP-000013",
        13,
        "docs/changelog/2026-09-05-hlp-000013-charter-publication-status.md",
        "ac7cbf940abfa6a8ef402b4af96626e607cda5fbbdef681b23e530a91608b36c",
    ),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def no_duplicate_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def relative_target(path: Path, raw_target: str) -> Path | None:
    parsed = urlparse(raw_target)
    if parsed.scheme or parsed.netloc or raw_target.startswith("#"):
        return None
    target_text = unquote(parsed.path)
    if not target_text:
        return None
    target = (path.parent / target_text).resolve()
    require(target == ROOT or ROOT in target.parents,
            f"{path.relative_to(ROOT)} link escapes repository: {raw_target}")
    return target


def check_relative_links(path: Path, text: str) -> None:
    for raw_target in LINK_RE.findall(text):
        target = relative_target(path, raw_target)
        if target is not None:
            require(target.exists(),
                    f"{path.relative_to(ROOT)} has a broken link: {raw_target}")


def check_public_text(path: Path, text: str) -> None:
    lowered = text.lower()
    for forbidden in FORBIDDEN_TEXT:
        require(forbidden not in lowered,
                f"{path.relative_to(ROOT)} contains forbidden public-history text: "
                f"{forbidden}")


def read_bounded(path: Path, byte_limit: int, line_limit: int) -> str:
    text = path.read_text(encoding="utf-8")
    require(len(text.encode("utf-8")) <= byte_limit,
            f"{path.relative_to(ROOT)} exceeds {byte_limit} bytes")
    require(len(text.splitlines()) <= line_limit,
            f"{path.relative_to(ROOT)} exceeds {line_limit} lines")
    check_public_text(path, text)
    check_relative_links(path, text)
    return text


def read_reservations() -> list[dict[str, Any]]:
    text = RESERVATIONS.read_text(encoding="utf-8")
    require(len(text.encode("utf-8")) <= 12 * 1024,
            "branch reservation registry exceeds 12288 bytes")
    require(len(text.splitlines()) <= 200,
            "branch reservation registry exceeds 200 lines")
    check_public_text(RESERVATIONS, text)
    registry = json.loads(text, object_pairs_hook=no_duplicate_object)
    require(isinstance(registry, dict),
            "branch reservation registry root must be an object")
    require(
        set(registry) == {
            "schema", "series", "status", "effect", "authority", "source",
            "reservations",
        },
        "branch reservation registry keys changed",
    )
    require(registry["schema"] == RESERVATION_SCHEMA,
            "branch reservation registry schema changed")
    require(registry["series"] == "HLP", "reservation series is not HLP")
    require(registry["status"] == RESERVATION_STATUS,
            "reservation status must remain off-main and not adopted")
    require(registry["effect"] == RESERVATION_EFFECT,
            "reservation effect widened beyond namespace preservation")
    require(registry["authority"] == "NONE",
            "branch reservation registry created authority")
    require(registry["source"] == RESERVATION_SOURCE,
            "branch reservation source identity changed")
    require(COMMIT_RE.fullmatch(registry["source"]["commit"]) is not None,
            "reservation source commit is not a full Git SHA")
    require(COMMIT_RE.fullmatch(registry["source"]["tree"]) is not None,
            "reservation source tree is not a full Git SHA")

    records = registry["reservations"]
    require(isinstance(records, list), "reservations must be an array")
    require(len(records) == len(EXPECTED_RESERVATIONS),
            "reservation count changed")
    expected_keys = {"id", "ordinal", "source_path", "source_sha256"}
    for record, expected in zip(records, EXPECTED_RESERVATIONS):
        require(isinstance(record, dict), "reservation record must be an object")
        require(set(record) == expected_keys,
                "reservation record keys changed")
        expected_id, expected_ordinal, expected_path, expected_sha256 = expected
        require(record["id"] == expected_id,
                f"reservation ID changed at {expected_ordinal}")
        require(record["ordinal"] == expected_ordinal,
                f"reservation ordinal changed for {expected_id}")
        require(record["source_path"] == expected_path,
                f"reservation source path changed for {expected_id}")
        require(record["source_sha256"] == expected_sha256,
                f"reservation digest changed for {expected_id}")
        require(SHA256_RE.fullmatch(record["source_sha256"]) is not None,
                f"reservation digest is not SHA-256 for {expected_id}")

        source_path = (ROOT / record["source_path"]).resolve()
        require(source_path.parent == NOTES,
                f"reservation path leaves docs/changelog: {expected_id}")
        require(not source_path.exists(),
                f"reserved off-main record appeared as adopted local content: "
                f"{expected_id}")
        filename = NOTE_NAME_RE.fullmatch(source_path.name)
        require(filename is not None,
                f"invalid reservation filename: {source_path.name}")
        require(filename.group("id") == expected_id.lower(),
                f"reservation filename ID mismatch: {expected_id}")

    ordinals = [int(record["ordinal"]) for record in records]
    require(ordinals == sorted(ordinals),
            "reservation ordinals must be strictly ascending")
    require(len(ordinals) == len(set(ordinals)),
            "reservation ordinals must be unique")
    require(len({record["source_path"] for record in records}) == len(records),
            "reservation source paths must be unique")
    return records


def parse_rows(path: Path, text: str) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for match in ROW_RE.finditer(text):
        row: dict[str, str | int] = match.groupdict()
        row["number"] = int(match.group("number"))
        target = relative_target(path, match.group("link"))
        require(target is not None, f"{path.relative_to(ROOT)} record link must be local")
        require(target.parent == NOTES,
                f"{path.relative_to(ROOT)} record link must target docs/changelog/")
        row["target"] = str(target)
        rows.append(row)
    return rows


def main() -> None:
    readme = read_bounded(README, 16 * 1024, 180)
    index = read_bounded(INDEX, 12 * 1024, 160)
    reservations = read_reservations()
    reserved_numbers = [int(record["ordinal"]) for record in reservations]
    reserved_ids = {str(record["id"]) for record in reservations}

    require("branch-reservations.json" in index,
            "changelog does not route to the branch reservation registry")
    require(RESERVATION_STATUS in index,
            "changelog does not state the off-main reservation status")
    require(RESERVATION_EFFECT in index,
            "changelog does not state the reservation effect ceiling")

    require(readme.count(START) == 1, "README must contain one latest start marker")
    require(readme.count(END) == 1, "README must contain one latest end marker")
    start = readme.index(START)
    end = readme.index(END, start) + len(END)
    block = readme[start:end]
    require(not readme[end:].strip(), "latest block must be the final README section")
    require(sum(line.startswith("- ") for line in block.splitlines()) <= 5,
            "latest block exceeds five bullets")
    require(len(WORD_RE.findall(block)) <= 120,
            "latest block exceeds 120 words")
    require(block.count("[All public changes](CHANGELOG.md)") == 1,
            "latest block must contain exactly one root-index link")

    current_rows = parse_rows(INDEX, index)
    require(current_rows,
            "current changelog cohort must contain at least one adopted record")
    current_numbers = [int(row["number"]) for row in current_rows]
    require(current_numbers == sorted(current_numbers, reverse=True),
            "current changelog cohort must be newest first")

    archive_rows: list[dict[str, str | int]] = []
    archive_paths = sorted(ARCHIVES.glob("*.md")) if ARCHIVES.exists() else []
    for archive_path in archive_paths:
        name_match = ARCHIVE_NAME_RE.fullmatch(archive_path.name)
        require(name_match is not None,
                f"invalid changelog archive name: {archive_path.name}")
        archive = read_bounded(archive_path, 12 * 1024, 100)
        require(archive.startswith("# Archived public change index"),
                f"{archive_path.relative_to(ROOT)} lacks archive heading")
        rows = parse_rows(archive_path, archive)
        low = int(name_match.group("low"))
        high = int(name_match.group("high"))
        expected = [
            number for number in range(high, low - 1, -1)
            if number not in reserved_numbers
        ]
        require(low % 25 == 1 and high == low + 24,
                f"{archive_path.name} is not a fixed 25-ID cohort")
        require([int(row["number"]) for row in rows] == expected,
                f"{archive_path.name} rows do not match its fixed range")
        archive_rows.extend(rows)

    all_rows = current_rows + archive_rows
    row_ids = [str(row["id"]) for row in all_rows]
    targets = [Path(str(row["target"])) for row in all_rows]
    require(len(row_ids) == len(set(row_ids)), "change IDs must be globally unique")
    require(len(targets) == len(set(targets)),
            "each full record must be indexed exactly once")
    require(set(row_ids).isdisjoint(reserved_ids),
            "an off-main namespace reservation appeared as an adopted row")

    all_numbers = sorted(int(row["number"]) for row in all_rows)
    issued_numbers = sorted(all_numbers + reserved_numbers)
    require(len(issued_numbers) == len(set(issued_numbers)),
            "adopted and reserved change IDs overlap")
    require(issued_numbers == list(range(1, max(issued_numbers) + 1)),
            "adopted plus reserved change IDs must be gap-free from HLP-000001")
    require(current_numbers[0] == max(issued_numbers),
            "newest issued change ID must be the latest adopted mainline row")
    current_range_low = 1
    if archive_rows:
        latest_archive = max(archive_paths)
        latest_name = ARCHIVE_NAME_RE.fullmatch(latest_archive.name)
        require(latest_name is not None, "latest archive filename is invalid")
        archive_high = int(latest_name.group("high"))
        current_range_low = archive_high + 1
        require(min(current_numbers) > archive_high,
                "current cohort overlaps an archived issued-ID range")
    current_issued_numbers = [
        number for number in issued_numbers if number >= current_range_low
    ]
    require(1 <= len(current_issued_numbers) <= 25,
            "current changelog cohort must cover 1 through 25 issued-ID slots")
    require(
        current_numbers == sorted(
            (
                number for number in current_issued_numbers
                if number not in reserved_numbers
            ),
            reverse=True,
        ),
        "current changelog rows do not match its issued-ID cohort",
    )

    disk_records = {path.resolve() for path in NOTES.glob("*.md")}
    require(set(targets) == disk_records,
            "current and archived indexes must cover every full record exactly once")

    for row, target in zip(all_rows, targets):
        filename = NOTE_NAME_RE.fullmatch(target.name)
        require(filename is not None, f"invalid full-record filename: {target.name}")
        require(filename.group("date") == row["date"],
                f"{target.name} date does not match its index row")
        require(filename.group("id") == str(row["id"]).lower(),
                f"{target.name} ID does not match its index row")
        if target.name in FROZEN_RECORD_SHA256:
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            require(
                digest == FROZEN_RECORD_SHA256[target.name],
                f"{target.name} changed after its frozen addition",
            )
        note = read_bounded(target, 32 * 1024, 500)
        require(f"| Change ID | `{row['id']}` |" in note,
                f"{target.name} does not declare index ID {row['id']}")
        require(f"| Record kind | `{row['kind']}` |" in note,
                f"{target.name} record kind does not match its index row")
        number = int(row["number"])
        earlier_adopted = [candidate for candidate in all_numbers if candidate < number]
        if earlier_adopted:
            mainline_predecessor = max(earlier_adopted)
            namespace_predecessor = number - 1
            if mainline_predecessor != namespace_predecessor:
                require(
                    f"| Namespace-allocation predecessor | "
                    f"`HLP-{namespace_predecessor:06d}`" in note,
                    f"{target.name} lacks its issued-namespace predecessor",
                )
                require(
                    f"| Mainline content predecessor | "
                    f"`HLP-{mainline_predecessor:06d}` |" in note,
                    f"{target.name} lacks its adopted mainline predecessor",
                )
                require("| Predecessor |" not in note,
                        f"{target.name} uses an ambiguous predecessor field")
        for heading in REQUIRED_HEADINGS:
            require(heading in note, f"{target.name} lacks {heading}")

    latest_matches = FULL_RECORD_RE.findall(block)
    require(len(latest_matches) == 1,
            "latest block must contain exactly one full-record link")
    require(str(current_rows[0]["id"]) in block,
            "latest block must name the newest change ID")
    latest_target = relative_target(README, latest_matches[0])
    require(latest_target == Path(str(current_rows[0]["target"])),
            "README latest record must match the first current changelog row")

    print("CHANGE_HISTORY_OK")


if __name__ == "__main__":
    main()
