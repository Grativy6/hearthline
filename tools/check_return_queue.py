#!/usr/bin/env python3
"""Validate Hearthline's public Homecoming Return Queue design boundaries."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
QUEUE_DOC = ROOT / "docs" / "HEARTHLINE_RETURN_QUEUE.md"
HOMECOMING_DOC = ROOT / "docs" / "HEARTHLINE_HOMECOMING.md"
CREATURE_DOC = ROOT / "docs" / "HEARTHLINE_CREATURES.md"
ORDERED_DOC = ROOT / "docs" / "HEARTHLINE_ORDERED_LINEAGE.md"
BOUNDARY_DOC = ROOT / "BOUNDARY.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
CHANGE_RECORD = (
    ROOT / "docs" / "changelog" /
    "2026-09-05-hlp-000014-homecoming-return-queue.md"
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def words(text: str) -> str:
    return " ".join(text.split())


def require_all(text: str, phrases: tuple[str, ...], boundary: str) -> None:
    for phrase in phrases:
        require(phrase in text, f"{boundary} missing: {phrase}")


def check_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        parsed = urlparse(raw)
        if parsed.scheme or parsed.netloc or raw.startswith("#"):
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        require(target == ROOT or ROOT in target.parents,
                f"{path.relative_to(ROOT)} link escapes repository: {raw}")
        require(target.exists(),
                f"{path.relative_to(ROOT)} broken link: {raw}")


def main() -> None:
    queue = QUEUE_DOC.read_text(encoding="utf-8")
    homecoming = HOMECOMING_DOC.read_text(encoding="utf-8")
    creature = CREATURE_DOC.read_text(encoding="utf-8")
    ordered = ORDERED_DOC.read_text(encoding="utf-8")
    boundary = BOUNDARY_DOC.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    change_record = CHANGE_RECORD.read_text(encoding="utf-8")

    queue_words = words(queue)
    require("# Hearthline Return Queue" in queue,
            "Return Queue heading missing")
    require("| Version | `0.1` |" in queue,
            "Return Queue version is not 0.1")
    require("| Status | Adopted lore and design vocabulary |" in queue,
            "Return Queue design is not marked adopted")
    require("| Implementation | Not asserted by this document |" in queue,
            "Return Queue text manufactured an implementation")

    require_all(
        queue_words,
        (
            "durably recorded `HOMECOMING:RETURNED` bundles",
            "every successfully enqueued return receives an immutable place",
            "A lone return uses the same path",
            "Every bundle first receives its ordinary durable `HOMECOMING:RETURNED` receipt, then enters the same queue-intake-attempt path",
            "There is no separate fast path whose result semantics differ",
            "The attempt receives its own durable intake receipt before capacity or enqueue disposition is decided",
            "an exact retry with the same idempotency key resolves to the same accepted queue item or the same blocked or unknown intake disposition",
            "reuse of that key with any changed intake binding records `IDEMPOTENCY_CONFLICT` and performs no queue mutation",
            "`RETURN_QUEUE:ENQUEUED` records durable placement",
            "It is not bundle validity, service admission, reconciliation, task success, result status, carry approval, publication, or authority",
            "Arrival order is immutable evidence about the controller's linearized append order",
            "Service order is a separately derived scheduling choice",
            "It does not claim physical, causal, or globally true precedence between concurrent attempts",
            "An enqueue committed after that cut is explicitly post-cut and first becomes visible in a successor snapshot",
            "Only the ready partition enters a proposal; already selected or in-service items remain visible but cannot be admitted twice",
            "The Queue Steward receives the full snapshot digest plus only the closed ready projection described below",
            "The controller alone carries those partitions forward unchanged",
            "Two distinct returns may both carry outcomes already established as valid wins",
            "Both remain separately attributable",
            "optional **Queue Steward Creature**",
            "grant-filtered **Queue Scheduling View**",
            "Its closed allowlist contains an opaque queue-item binding",
            "a return payload or self-claim cannot set priority",
            "The view excludes raw or unselected payload, content identity, source Creature or objective identity and prestige",
            "The Queue Steward is optional optimization",
            "A partial proposal may preserve useful named gaps as advisory evidence, but it is non-admissible as an order",
            "never as a service item in the exact data queue or snapshot it proposes over",
            "Only the canonical controller may validate an order proposal and append a final service snapshot",
            "the exact immutable queue identity, profile and service epoch digest, plus the frozen snapshot digest",
            "A final service snapshot records intended order but consumes no overtake and admits no item by itself",
            "The controller first checks that item's ordinary revalidation inputs",
            "A passing check permits a separate append-only Service Admission Receipt",
            "A failed or uncertain pre-admission revalidation instead receives a Service Disposition Receipt and consumes no overtake",
            "`maximum_overtakes` is `2`",
            "a genuinely new attempt after the named remedy requires a new idempotency key",
            "It reconciles every `ENQUEUE_OUTCOME_UNKNOWN` before deriving the accepted arrival set",
            "A queue-close snapshot freezes an intake cutoff and covers every Intake Attempt Receipt through it",
            "Close is forbidden while any append outcome remains ambiguous or any `ENQUEUE_OUTCOME_UNKNOWN` or `QUEUE_CAPACITY_UNKNOWN` disposition remains unresolved",
            "Every accepted intake disposition must link one handled queue item",
            "An item's overtake counter increments only when a later-arriving eligible item is actually admitted to service ahead of it",
            "Merely proposing an order, or leaving an item in the unserved suffix of a snapshot, does not increment the counter",
            "Only a passing pre-admission check permits the Service Admission Receipt and opens that one reconciliation transaction; it does not append the Reconciliation Receipt by itself",
            "A rule-owned result status may already have been established before return",
            "Thulia](HEARTHLINE_THULIA.md) is not the queue sorter",
            "TETHER carries the route back to the trace; it is not queue storage, hidden state, a scheduler, or permission to resume",
            "This document creates no queue, Creature, Spark, controller, allocator, ledger, runtime, model process, memory, credential, external effect, benchmark result, or authority",
        ),
        "Return Queue boundary",
    )
    require_all(
        queue,
        (
            "HOMECOMING:RETURNED != RETURN_QUEUE:ENQUEUED",
            "RETURN_QUEUE:ENQUEUED != BUNDLE_VALID != SERVICE_SELECTED",
            "SERVICE_SELECTED != HOMECOMING:RECONCILED",
            "HOMECOMING:RECONCILED != TASK_RESULT",
        ),
        "Return Queue state separation",
    )
    require("Every reorder increments" not in queue,
            "proposal-time reorder still consumes the fairness bound")

    require("| Version | `0.5` |" in homecoming,
            "Homecoming Return Queue successor version missing")
    require_all(
        words(homecoming),
        (
            "every durably recorded `HOMECOMING:RETURNED` bundle follows the same queue-intake path",
            "A lone return may be the immediate head",
            "Controller selection begins one revalidation; a pass permits service admission, which does not itself establish `HOMECOMING:RECONCILED`, task result, or carry",
            "Two distinct valid results remain two separately attributable results",
        ),
        "Homecoming queue integration",
    )

    require("| Version | `0.2` |" in creature,
            "Creature Queue Steward successor version missing")
    require_all(
        words(creature),
        (
            "optional [Queue Steward Creature]",
            "It is not the queue, scheduler, canonical controller, intake validator, Homecoming admitter, or owner of any return",
            "the controller retains every queue item and uses the frozen base service rule",
            "metadata-only scheduling view",
        ),
        "Creature Queue Steward integration",
    )

    require("| Version | `0.7` |" in ordered,
            "Ordered Lineage Return Queue successor version missing")
    require_all(
        words(ordered),
        (
            "Arrival order and service order are different series",
            "Return Queue item",
            "Queue order proposal",
            "Final service snapshot",
            "Return Queue profile",
            "Service Admission Receipt",
            "Intake Attempt Receipt",
            "Intake Disposition Receipt",
            "Enqueue Receipt",
            "Service transaction",
            "Service Disposition Receipt",
            "An overtake is counted only when a later-arriving eligible item actually enters service first",
            "off-main numbers as reservations rather than reusing them",
        ),
        "Ordered Lineage queue integration",
    )

    require_all(
        words(boundary),
        (
            "operational Return Queue profiles, queue items, arrival and service snapshots",
            "Queue Steward views and proposals",
        ),
        "private operational queue boundary",
    )
    require("docs/HEARTHLINE_RETURN_QUEUE.md" in readme,
            "README lacks the Return Queue route")
    require("the controller commits service order" in readme,
            "README blurs Queue Steward and controller authority")
    require("HLP-000014" in changelog,
            "changelog lacks the Return Queue successor")
    require("RESERVED_OFF_MAIN_NOT_ADOPTED" in changelog,
            "changelog lacks the reservation status")
    require("NAMESPACE_ONLY_NO_ADOPTION" in changelog,
            "changelog lacks the reservation effect ceiling")
    require("| Change ID | `HLP-000014` |" in change_record,
            "Return Queue change record identity missing")
    require("| Mainline content predecessor | `HLP-000007` |" in change_record,
            "Return Queue mainline predecessor missing")

    for path in (
        QUEUE_DOC,
        HOMECOMING_DOC,
        CREATURE_DOC,
        ORDERED_DOC,
        BOUNDARY_DOC,
        README,
        CHANGELOG,
        CHANGE_RECORD,
    ):
        check_links(path)
        lowered = path.read_text(encoding="utf-8").lower()
        for forbidden in ("c:\\users\\", "file://", "token=", "api_key"):
            require(forbidden not in lowered,
                    f"{path.relative_to(ROOT)} contains forbidden private text")

    print("RETURN_QUEUE_OK")


if __name__ == "__main__":
    main()
