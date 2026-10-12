"""Resolve explicitly retired public sources at the pinned pre-split commit.

Only frozen history records may use retired relative targets. Current technical
documents must have working current links. No private repository is consulted.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "f5c69b912761f29e2c82f83d1fe412fc83ec873a"
MANIFEST = ROOT / "docs/history/public-lab-split.json"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def relative_path(path: Path) -> str:
    resolved = path.resolve()
    require(resolved == ROOT or ROOT in resolved.parents, "path escapes repository")
    return resolved.relative_to(ROOT).as_posix()


@lru_cache(maxsize=1)
def manifest() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(data["schema"] == "hearthline.public-lab-split.v1", "split schema changed")
    require(data["source_commit"] == SOURCE_COMMIT, "split source pin changed")
    paths = [row["path"] for row in data["sources"]]
    require(len(paths) == len(set(paths)) == 83, "split source inventory changed")
    for path in paths:
        parsed = PurePosixPath(path)
        require(not parsed.is_absolute() and ".." not in parsed.parts and "\\" not in path,
                f"unsafe split path: {path}")
    return data


def source_records() -> dict[str, dict]:
    return {row["path"]: row for row in manifest()["sources"]}


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, check=False,
    )
    require(result.returncode == 0,
            "Pinned public history is unavailable. From this public clone run: "
            f"git fetch --no-tags --depth=1 origin {SOURCE_COMMIT}")
    return result.stdout


@lru_cache(maxsize=1)
def source_tree() -> dict[str, str]:
    result = {}
    for item in git_bytes("ls-tree", "-rz", SOURCE_COMMIT).split(b"\0"):
        if item:
            metadata, path = item.split(b"\t", 1)
            result[path.decode("utf-8")] = metadata.decode().split()[2]
    return result


def historical_bytes(relative: str) -> bytes:
    record = source_records().get(relative)
    require(record is not None, f"unlisted historical source: {relative}")
    require(source_tree().get(relative) == record["git_blob"],
            f"pinned source tree mismatch: {relative}")
    data = git_bytes("cat-file", "blob", record["git_blob"])
    require(len(data) == record["bytes"], f"historical byte count changed: {relative}")
    require(hashlib.sha256(data).hexdigest() == record["sha256"],
            f"historical digest changed: {relative}")
    return data


def read_source_bytes(path: Path) -> bytes:
    relative = relative_path(path)
    record = source_records().get(relative)
    if record and record["disposition"] == "RETIRED_FROM_CURRENT_TREE":
        return historical_bytes(relative)
    return path.read_bytes()


def read_source_text(path: Path) -> str:
    return read_source_bytes(path).decode("utf-8")


def check_relative_links(path: Path, text: str) -> None:
    owner = relative_path(path)
    frozen = {r["path"]: r for r in manifest()["frozen_files"]}
    retired = {p for p, r in source_records().items()
               if r["disposition"] == "RETIRED_FROM_CURRENT_TREE"}
    is_frozen = owner in frozen and owner.startswith("docs/changelog/")
    if is_frozen:
        require(hashlib.sha256(path.read_bytes()).hexdigest() == frozen[owner]["sha256"],
                f"frozen history changed: {owner}")
    # A retired source is itself read only through its exact historical object.
    is_retired = owner in retired
    if is_retired:
        require(text == historical_bytes(owner).decode("utf-8"),
                f"historical source text changed: {owner}")
    for raw in LINK_RE.findall(text):
        parsed = urlparse(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("#") or not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        target_name = relative_path(target)
        if target.exists():
            continue
        allowed = target_name in retired or any(p.startswith(target_name + "/") for p in retired)
        require((is_frozen or is_retired) and allowed,
                f"{owner} has a broken current link: {raw}")
        tree = source_tree()
        require(target_name in tree or any(p.startswith(target_name + "/") for p in tree),
                f"{owner} historical target is absent from pinned tree: {raw}")
