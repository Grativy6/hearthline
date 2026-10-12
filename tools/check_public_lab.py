#!/usr/bin/env python3
"""Check the public split, frozen records, proof bytes and current navigation."""

import hashlib

from public_history import (
    ROOT, check_relative_links, historical_bytes, manifest, require, source_tree,
)


def main() -> None:
    ledger = manifest()
    tree = source_tree()
    retired = 0
    for row in ledger["sources"]:
        historical_bytes(row["path"])
        current = ROOT / row["path"]
        if row["disposition"] == "RETIRED_FROM_CURRENT_TREE":
            require(not current.exists(), f"retired file still current: {row['path']}")
            retired += 1
        else:
            require(current.is_file(), f"technical successor missing: {row['path']}")
    require(retired == 74, "retired inventory changed")
    expected_frozen = {
        p for p in tree
        if p.startswith("research/context-parallax/lean/")
        or (p.startswith("docs/changelog/") and p.endswith(".md") and "/index/" not in p)
    }
    require({r["path"] for r in ledger["frozen_files"]} == expected_frozen,
            "frozen inventory differs from the pinned public tree")
    for row in ledger["frozen_files"]:
        require(tree.get(row["path"]) == row["git_blob"],
                f"frozen source tree mismatch: {row['path']}")
        data = (ROOT / row["path"]).read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
        require(blob == tree[row["path"]],
                f"frozen public Git object changed: {row['path']}")
        require(hashlib.sha256(data).hexdigest() == row["sha256"],
                f"frozen public bytes changed: {row['path']}")
    lean = ROOT / "research/context-parallax/lean"
    pinned_lean = {r["path"] for r in ledger["frozen_files"] if r["path"].startswith("research/")}
    actual_lean = {p.relative_to(ROOT).as_posix() for p in lean.rglob("*") if p.is_file()}
    require(actual_lean == pinned_lean, "CPX inventory changed")
    for folder in (ROOT / "assets", ROOT / "lore"):
        require(not folder.exists() or not any(p.is_file() for p in folder.rglob("*")),
                "character collection remains in the current public tree")
    paths = [*ROOT.glob("*.md"), *(ROOT / "docs").rglob("*.md")]
    for path in paths:
        check_relative_links(path, path.read_text(encoding="utf-8"))
    print(f"PUBLIC_LAB_OK: {retired} retired paths; 9 technical successors; "
          f"{len(ledger['frozen_files'])} frozen files; {len(paths)} Markdown files checked")


if __name__ == "__main__":
    main()
