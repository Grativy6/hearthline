#!/usr/bin/env python3
"""Validate Hearthline's bounded public change-history surfaces."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "CHANGELOG.md"
NOTES = ROOT / "docs" / "changelog"
ARCHIVES = NOTES / "index"
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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


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
    require("[All public changes](CHANGELOG.md)" in block,
            "latest block lacks the root-index link")

    current_rows = parse_rows(INDEX, index)
    require(0 < len(current_rows) <= 25,
            "current changelog cohort must contain 1 through 25 records")
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
        expected = list(range(high, low - 1, -1))
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

    all_numbers = sorted(int(row["number"]) for row in all_rows)
    require(all_numbers == list(range(1, max(all_numbers) + 1)),
            "change IDs must form a complete sequence from HLP-000001")
    if archive_rows:
        archive_max = max(int(row["number"]) for row in archive_rows)
        require(min(current_numbers) == archive_max + 1,
                "current cohort must begin immediately after archived cohorts")

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
        note = read_bounded(target, 32 * 1024, 500)
        require(f"| Change ID | `{row['id']}` |" in note,
                f"{target.name} does not declare index ID {row['id']}")
        require(f"| Record kind | `{row['kind']}` |" in note,
                f"{target.name} record kind does not match its index row")
        for heading in REQUIRED_HEADINGS:
            require(heading in note, f"{target.name} lacks {heading}")

    latest_match = FULL_RECORD_RE.search(block)
    require(latest_match is not None, "latest block has no full-record link")
    latest_target = relative_target(README, latest_match.group(1))
    require(latest_target == Path(str(current_rows[0]["target"])),
            "README latest record must match the first current changelog row")

    print("CHANGE_HISTORY_OK")


if __name__ == "__main__":
    main()
