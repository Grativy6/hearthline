#!/usr/bin/env python3
"""Validate the public Hearthline TETHER and Light-Trio integration."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "hearthline_agent.md"
README = ROOT / "README.md"
DOC = ROOT / "docs" / "HEARTHLINE_TETHER.md"
TASK_TRIADS = ROOT / "docs" / "HEARTHLINE_TASK_TRIADS.md"
MANIFEST = ROOT / "candidate_manifest.json"


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


def main() -> None:
    agent = AGENT.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    doc = DOC.read_text(encoding="utf-8")
    task_triads = TASK_TRIADS.read_text(encoding="utf-8")
    doc_words = words(doc)
    task_triads_words = words(task_triads)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # The public agent surface and its manifest must move together. Keeping
    # this digest check makes a prose-only version bump insufficient.
    require("version: 0.7-draft" in agent, "agent draft version is not 0.7-draft")
    require_all(
        agent,
        (
            "### TETHER — Trace Externalization Through Handle-bound Exact Reopening",
            "Never carry a material unresolved item without a concrete reopening route",
            "docs/HEARTHLINE_TETHER.md",
            "docs/HEARTHLINE_TASK_TRIADS.md",
        ),
        "agent TETHER route",
    )

    require("# Hearthline TETHER" in doc, "TETHER document heading missing")
    require("version: 0.3-draft" in doc, "TETHER version is not 0.3-draft")
    require(
        "status: CANDIDATE_PUBLIC_DESIGN_PROPOSAL_PENDING_STEWARD_REVIEW" in doc,
        "TETHER candidate status missing",
    )
    require_all(
        doc_words,
        (
            "Trace Externalization Through Handle-bound Exact Reopening",
            "whatever reliable carrier is available",
            "The technique does not require one archive format",
            "Retrieval failure is not source loss",
            "A TETHER handle is not permission",
            "An unresolved state without a reopening route",
            "Resuming from a TETHER cannot create, renew, widen, transfer, or infer authority",
            "The larger trace remains external",
            "TraceKey names the key",
            "TETHER names the motion",
            "A stale objective or authority epoch fails closed",
            "A spinner, `Working` label, animated loading surface",
            "presentation telemetry",
            "`HOST_HANDOFF_BLOCKED`",
        ),
        "TETHER continuity boundary",
    )

    # Preserve the carrier-neutral handle as well as the selected-carry layer.
    require_all(
        doc,
        (
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
        ),
        "TETHER handle schema",
    )

    # Formation remains co-bound and dispatch remains a later controller act.
    require_all(
        doc_words,
        (
            "task_triad_ref: required only when triad_formation_state is TRIAD_BOUND; otherwise unset",
            "triad_dispatch_state: unset before TRIAD_BOUND; thereafter exact one of [NOT_DISPATCHED, DISPATCHED, DISPATCH_REFUSED, DISPATCH_STALE]",
            "The request carries Hearthline's nonbinding nomination for only the Work and Task-Keeper seats; Thulia independently contributes a nonbinding nomination for only the Ledger-Keeper seat",
            "Neither nomination is authority or a seat binding, and `TRIAD_FORMATION_OFFERED` starts no member",
            "`triad_formation_state` and `triad_dispatch_state` remain separate",
            "`TRIAD_BOUND` is inert until the controller independently revalidates the frozen bundle and appends the exact dispatch receipt that establishes `DISPATCHED`",
            "The authority bundle is an aggregate reference, not an aggregate grant",
            "silent_rebase_permitted: false",
        ),
        "TETHER Light-Trio formation boundary",
    )

    # Each member seals and returns on its own transaction directly to the
    # commissioning Hearthline task intake.
    require_all(
        doc_words,
        (
            "hearthline_task_intake_ref: exact controller-owned intake account when the first member return becomes admissible; otherwise unset",
            "work: unset until the separate SEALED and VALID Work bundle is durably admitted; thereafter exact",
            "task_keeper: unset until the separate SEALED and VALID Task-Keeper bundle is durably admitted; thereafter exact",
            "ledger_keeper: unset until the separate SEALED and VALID Ledger-Keeper bundle is durably admitted; thereafter exact",
            "each bundle enters RETURN_PENDING_HEARTHLINE and is admitted separately only after controller-observed SEALED plus separately observed VALID",
            "each controller-observed `SEALED` plus separately `VALID` member bundle returns independently to the named Hearthline task intake as `RETURN_PENDING_HEARTHLINE`",
            "no aggregate envelope is needed to make the other two readable",
            "receives the Work, Task-Boundary Witness, and Ledger bundles separately through controller-observed Homecoming",
        ),
        "TETHER direct-return boundary",
    )
    require_all(
        doc,
        (
            "member_homecoming_refs:",
            "member_task_intake_receipt_refs:",
            "return_receipt_ref: unset until the Work Return Receipt is appended",
            "return_receipt_ref: unset until the Task-Keeper Return Receipt is appended",
            "return_receipt_ref: unset until the Ledger-Keeper Return Receipt is appended",
        ),
        "TETHER per-member Homecoming schema",
    )

    # Hearthline's finite inspection and immutable selection precede Thulia.
    require_all(
        doc_words,
        (
            "return_manifest_state: unset before manifest candidate allocation; thereafter exact one of [NOT_PRODUCED, SEALED, UNKNOWN]",
            "carry_selection_state: exact one of [NOT_PRODUCED, SEALED, UNKNOWN] after candidate preallocation; otherwise unset",
            "carry_selection_validity_state: unset unless carry_selection_state is SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]",
            "carry_selection_coverage_state: unset before the inspection universe is frozen; thereafter exact one of [COMPLETE, INCOMPLETE, COVERAGE_UNKNOWN]",
            "every candidate item has exactly one of [SELECT_KEEP, SELECT_CONDENSE, SELECT_LOSE]",
            "only SEALED plus VALID plus COMPLETE Carry Selection may enter H_TO_T_CARRY",
            "Hearthline alone originates the semantic carry choice",
            "An omitted item makes coverage `INCOMPLETE`; it is never silently recast as `SELECT_LOSE`",
        ),
        "TETHER Carry Selection boundary",
    )

    # Durable selected-carry storage—not acceptance alone—gates raw closure.
    require_all(
        doc_words,
        (
            "carry_handoff_emission_state: unset before transaction preallocation; thereafter exact one of [NOT_EMITTED, EMITTED, EMISSION_UNKNOWN]",
            "carry_handoff_state: unset before transaction preallocation; thereafter exact one of [NOT_OBSERVED, ACCEPTED_BY_THULIA, REJECTED_BY_THULIA, HANDOFF_UNKNOWN]",
            "selected_carry_store_outcome_state: unset before that custody operation is admitted; thereafter exact one of [NOT_ATTEMPTED, COMMITTED, FAILED, OUTCOME_UNKNOWN]",
            "inspection_context_state may enter CLOSE_PENDING only when carry_handoff_state is ACCEPTED_BY_THULIA and selected_carry_store_outcome_state is COMMITTED for the same carry_selection_ref",
            "RAW_ACCESS_DROPPED ends Hearthline's active access to the inspected Spark-return bodies; it does not assert hidden-state erasure, delete the external sources, or remove reopening handles",
            "It does not assert deletion of external sources, erase ordered identities, or claim provider/model forgetting",
        ),
        "TETHER selected-carry close gate",
    )

    # These are four independently granted lanes. Gloss has per-turn observed
    # readiness, never a heartbeat or inherited liveness.
    require_all(
        doc_words,
        (
            "hearthline_to_thulia_lane_ref: exact one-way lane and grant before an offer; otherwise unset",
            "thulia_to_gloss_lane_ref: exact one-way lane when translation is requested; otherwise unset",
            "gloss_to_thulia_lane_ref: exact distinct one-way lane when translation is requested; otherwise unset",
            "thulia_to_hearthline_lane_ref: exact distinct one-way lane for final readable carry; otherwise unset",
            "Gloss supplies no heartbeat or persistent readiness claim",
            "gloss_readiness_state: unset before the per-turn observation or when no gloss_turn_ref exists; thereafter exact one of [READY_FOR_EXACT_TURN, NOT_READY, READINESS_UNKNOWN]",
            "`READY_FOR_EXACT_TURN` for one turn says nothing about the next",
            "Gloss has no heartbeat, continuing context, ledger, or inherited readiness",
        ),
        "TETHER four-lane Gloss boundary",
    )

    # CANDIDATE_COMPLETE is the exact machine token. Validity, durable storage,
    # emission, and target receipt stay independent.
    require_all(
        doc_words,
        (
            "owl_turn_disposition: unset unless candidate SEALED and VALID; then exact one of [CANDIDATE_COMPLETE, OWL_SUPPORT_REQUIRED]",
            "readable_carry_reference_state: unset before the Readable Carry Envelope candidate exists; then exact one of [REFERENCE_COMPLETE, REFERENCE_INCOMPLETE]",
            "readable_carry_validity_state: unset before that candidate exists; then exact one of [CURRENT, STALE, VALIDITY_UNKNOWN]",
            "readable_carry_emission_state: unset before that candidate exists; then exact one of [NOT_EMITTED, EMITTED, EMISSION_UNKNOWN]",
            "readable_carry_receipt_state: unset before transaction allocation; thereafter exact one of [NOT_OBSERVED, RECEIVED, REJECTED, UNKNOWN]",
            "only readable_carry_store_outcome_state COMMITTED plus owl_candidate_state SEALED plus owl_candidate_validity_state VALID plus owl_turn_disposition CANDIDATE_COMPLETE may feed T_TO_H_READABLE emission",
        ),
        "TETHER readable-carry boundary",
    )

    # Closure, classification, external effect, and recoverability are distinct.
    require_all(
        doc_words,
        (
            "systemic_friction_classification_ref: later Thulia-only classification",
            "retention_classification: unset before classification; thereafter exact one of [KEEP, COMPACT, ARCHIVE, PRUNE_ELIGIBLE, FRICTION_UNKNOWN_HOLD]",
            "canonical_store_effect_ref: exact later Atomic Edge Promotion transaction and receipt over the named canonical source boundary; otherwise unset",
            "canonical_store_effect_state: unset before that later edge is requested; thereafter exact one of [NOT_REQUESTED, AUTHORIZED, ATTEMPTED, COMMITTED, FAILED, OUTCOME_UNKNOWN]",
            "source_recoverability_state: unset before observation; thereafter exact one of [PRESERVED_EXACT, RECOVERABLE_FROM_AUTHORIZED_ARCHIVE, BOUNDARY_ONLY_UNRECOVERABLE, RECOVERABILITY_UNKNOWN] within one named recovery boundary",
            "Only after every required Gloss turn is terminal, readable-carry storage is `COMMITTED`, and any required Hearthline receipt is `RECEIVED`",
            "may Thulia issue the later Systemic Friction classification",
            "Any canonical retention effect is later still and separately authorized",
            "occurs only after the readable-return prerequisites are satisfied",
        ),
        "TETHER retention/effect separation",
    )

    require_absent(
        doc_words,
        (
            "returns its Work, Task-Boundary Witness, and Ledger payloads separately through Thulia",
            "Task-Keeper keeps the Worker alive",
            "Task-Keeper is the host watchdog",
            "Gloss receives a heartbeat",
            "silent_rebase_permitted: true",
        ),
        "TETHER current route",
    )

    # The canonical dependency must expose the same current state model.
    require("| Version | `0.2-draft` |" in task_triads,
            "Task-Triad dependency is not 0.2-draft")
    require_all(
        task_triads_words,
        (
            "Member bundles never return to Thulia first: each valid sealed bundle returns separately to the exact Hearthline task intake that commissioned it",
            "`RETURN_HELD_STALE_EPOCH`",
            "`RETURN_PENDING_HEARTHLINE`",
            "`member_return_transaction_ref`",
            "`member_return_emission_state`",
            "`member_intake_receipt_state`",
            "carry_selection_coverage_state",
            "`SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`",
            "selected_carry_store_outcome_state: COMMITTED",
            "four separately granted and receipted `H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE` lanes",
            "`owl_turn_disposition: CANDIDATE_COMPLETE`",
            "Gloss has no Task Line of its own, no open objective, no context window, no prior-turn reads, no Homecoming, no ledger ownership, and no heartbeat",
            "Readiness is checked anew for each exact turn; it is never inherited",
            "Systemic Friction classification != Atomic Edge Promotion authority",
            "source_recoverability_state",
            "Inspection closure and pruning are independent edges",
            "MAX_SUPPORT_DEPTH = 1",
        ),
        "Task-Triad current dependency",
    )

    require("docs/HEARTHLINE_TETHER.md" in readme,
            "README lacks the TETHER document route")
    require("docs/HEARTHLINE_TASK_TRIADS.md" in readme,
            "README lacks the Task-Triad document route")
    require("Version: `0.7-draft`" in readme,
            "README current version is not 0.7-draft")

    normalized = AGENT.read_bytes().replace(b"\r\n", b"\n")
    digest = hashlib.sha256(normalized).hexdigest()
    require(manifest.get("artifact_version") == "0.7-draft",
            "candidate manifest version is not 0.7-draft")
    require(manifest.get("policy_hash_domain") ==
            "utf8_lf_normalized_repository_text_sha256",
            "candidate manifest policy hash domain changed")
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
