from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MAPS = (
    ROOT / "START_HERE.md",
    ROOT / "docs" / "CURRENT_SYSTEM_MAP.md",
    ROOT / "docs" / "RUN_SURFACE_MAP.md",
    ROOT / "docs" / "ARC_AGI_3_HANDOFF.md",
    ROOT / "docs" / "history" / "SUPERSESSION_INDEX.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    raise SystemExit(f"foundation map check failed: {message}")


def check_links(path: Path, text: str) -> None:
    for raw in LINK.findall(text):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https", "mailto"}:
            continue
        relative = unquote(parsed.path)
        if not relative:
            continue
        resolved = (path.parent / relative).resolve()
        if not resolved.is_relative_to(ROOT):
            fail(f"{path.relative_to(ROOT)} links outside the repository")
        if not resolved.exists():
            fail(f"broken relative link in {path.relative_to(ROOT)}: {target}")


def main() -> None:
    for path in MAPS:
        if not path.is_file():
            fail(f"missing {path.relative_to(ROOT)}")

    combined_parts: list[str] = []
    for path in MAPS:
        text = path.read_text(encoding="utf-8")
        combined_parts.append(text)
        check_links(path, text)

    combined = "\n".join(combined_parts)
    for marker in (
        "REVIEW_ONLY_NOT_MERGE_READY",
        "ACTIVE_CANDIDATE",
        "OPEN_CONFLICT",
        "RUNTIME_CLOSURE_UNFROZEN",
        "PREPARED_NOT_RUN",
        "MAP_ONLY_NO_EXECUTION_AUTHORITY",
    ):
        if marker not in combined:
            fail(f"missing status marker {marker}")

    for forbidden in (
        "C:\\\\Users\\",
        "E:\\\\",
        "github.com/Grativy6/hearthline-workshop",
        "github.com/Grativy6/hearthline-cabin",
    ):
        if forbidden.lower() in combined.lower():
            fail(f"private or local locator leaked: {forbidden}")

    launch_sha = "97f580504e22bbd59b425274d6b5e0f9a18fe66e"
    plays_links = re.findall(r"https://github\.com/Grativy6/hearthline-plays/[^\s)>]+", combined)
    if not plays_links or any(launch_sha not in link and "37010b5c775d7e137b957e386fb5b79e7ce96be2" not in link and "eafa59a16877f544547081b6cb910fcde683907c" not in link for link in plays_links):
        fail("public Plays links must be commit-pinned")

    print("foundation map checks: PASS")


if __name__ == "__main__":
    main()
