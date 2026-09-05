#!/usr/bin/env python3
"""Validate the public Hearthline TETHER integration."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "hearthline_agent.md"
README = ROOT / "README.md"
DOC = ROOT / "docs" / "HEARTHLINE_TETHER.md"
MANIFEST = ROOT / "candidate_manifest.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    agent = AGENT.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    doc = DOC.read_text(encoding="utf-8")
    doc_words = " ".join(doc.split())
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    require("version: 0.4-draft" in agent, "agent draft version is not 0.4")
    require("### TETHER — Trace Externalization Through Handle-bound Exact Reopening" in agent,
            "agent lacks the TETHER technique")
    require("Never carry a material unresolved item without a concrete reopening route" in agent,
            "agent lacks the unresolved-route rule")
    require("docs/HEARTHLINE_TETHER.md" in agent,
            "agent lacks the full TETHER route")

    require("# Hearthline TETHER" in doc, "TETHER document heading missing")
    require("version: 0.2-draft" in doc,
            "TETHER document version is not 0.2-draft")
    require("Trace Externalization Through Handle-bound Exact Reopening" in doc,
            "TETHER expansion missing")
    for phrase in (
        "whatever reliable carrier is available",
        "The technique does not require one archive format",
        "Retrieval failure is not source loss",
        "A TETHER handle is not permission",
        "An unresolved state without a reopening route",
        "Resuming from a TETHER cannot create, renew, widen, transfer, or infer authority",
        "The larger trace remains external",
        "TraceKey names the key",
        "TETHER names the motion",
        "Homecoming Priority Mark",
        "Homecoming Priority Assignment Receipt",
        "task_tether_core_digest",
        "HEARTHLINE_TASK_TETHER_CORE_V1",
        "neither digest includes itself",
        "Homecoming Priority Revision Receipt",
        "priority-ledger head",
        "observed snapshot head",
        "an ambiguous append has no effect until reconciled from durable state",
        "A revision can never renew or expand the TETHER's source task",
        "Morrow sees only the controller-attested effective rank",
        "Thulia receives none of the mark, assignment, revision, view, proposal, order, or admission surfaces",
        "They have no direct channel or shared state",
    ):
        require(phrase in doc_words, f"TETHER boundary missing: {phrase}")

    for field in (
        "tether_id:",
        "source_identity:",
        "carrier_kind:",
        "locator:",
        "version_or_integrity:",
        "scope:",
        "claim_status:",
        "coverage:",
        "residuals:",
        "reopening_route:",
        "access_requirements:",
        "authority_ceiling:",
    ):
        require(field in doc, f"TETHER handle field missing: {field}")

    require("docs/HEARTHLINE_TETHER.md" in readme,
            "README lacks the TETHER document route")
    require("Version: `0.4-draft`" in readme,
            "README current version is not 0.4-draft")

    normalized = AGENT.read_bytes().replace(b"\r\n", b"\n")
    digest = hashlib.sha256(normalized).hexdigest()
    require(manifest.get("artifact_version") == "0.4-draft",
            "candidate manifest version is not 0.4-draft")
    require(manifest.get("policy_sha256") == digest,
            "candidate manifest does not bind the current agent bytes")
    require(manifest.get("authority") == "NONE", "TETHER widened authority")
    require(manifest.get("effect") == "NONE", "TETHER created an effect")

    lowered = doc.lower()
    for forbidden in ("c:\\users\\", "file://", "token=", "api_key"):
        require(forbidden not in lowered,
                f"TETHER document leaks forbidden text: {forbidden}")

    print("TETHER_OK")


if __name__ == "__main__":
    main()
