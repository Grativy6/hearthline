"""Regression cases for the narrow historical-link exception."""

import hashlib
import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "lab_history", Path(__file__).resolve().parents[1] / "tools/public_history.py"
)
history = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(history)


@pytest.fixture
def archive(tmp_path, monkeypatch):
    source = b"preserved original\n"
    row = {"path": "lore/example.md", "disposition": "RETIRED_FROM_CURRENT_TREE",
           "git_blob": "a" * 40, "sha256": hashlib.sha256(source).hexdigest(),
           "bytes": len(source)}
    old = tmp_path / "docs/changelog/old.md"
    old.parent.mkdir(parents=True)
    old.write_bytes(b"[old story](../../lore/example.md)\n")
    data = {"sources": [row], "frozen_files": [{"path": "docs/changelog/old.md",
            "sha256": hashlib.sha256(old.read_bytes()).hexdigest()}]}
    monkeypatch.setattr(history, "ROOT", tmp_path)
    monkeypatch.setattr(history, "manifest", lambda: data)
    monkeypatch.setattr(history, "source_tree", lambda: {row["path"]: row["git_blob"]})
    monkeypatch.setattr(history, "git_bytes", lambda *args: source)
    return tmp_path, old, row


def test_frozen_record_can_reopen_its_retired_target(archive):
    _, old, _ = archive
    history.check_relative_links(old, old.read_text())


def test_current_document_cannot_borrow_a_historical_exception(archive):
    root, _, _ = archive
    current = root / "README.md"
    current.write_text("[missing current route](lore/example.md)")
    with pytest.raises(SystemExit, match="broken current link"):
        history.check_relative_links(current, current.read_text())


def test_edited_record_cannot_claim_frozen_status(archive):
    _, old, _ = archive
    old.write_text(old.read_text() + "silently revised")
    with pytest.raises(SystemExit, match="frozen history changed"):
        history.check_relative_links(old, old.read_text())


def test_historical_bytes_require_the_recorded_digest(archive, monkeypatch):
    _, _, row = archive
    monkeypatch.setattr(history, "git_bytes", lambda *args: b"x" * row["bytes"])
    with pytest.raises(SystemExit, match="historical digest changed"):
        history.historical_bytes(row["path"])


def test_manifest_blob_must_belong_to_the_pinned_tree(archive, monkeypatch):
    _, _, row = archive
    monkeypatch.setattr(history, "source_tree", lambda: {row["path"]: "b" * 40})
    with pytest.raises(SystemExit, match="pinned source tree mismatch"):
        history.historical_bytes(row["path"])


def test_unlisted_source_is_not_a_historical_fallback(archive):
    with pytest.raises(SystemExit, match="unlisted historical source"):
        history.historical_bytes("lore/unlisted.md")


def test_current_link_cannot_escape_the_checkout(archive):
    root, _, _ = archive
    path = root / "README.md"
    with pytest.raises(SystemExit, match="path escapes repository"):
        history.check_relative_links(path, "[outside](../outside.md)")
