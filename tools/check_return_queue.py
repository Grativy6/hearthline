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
TETHER_DOC = ROOT / "docs" / "HEARTHLINE_TETHER.md"
MORROW_LORE = ROOT / "lore" / "MORROW_AND_THE_MARKED_TETHERS.md"
BOUNDARY_DOC = ROOT / "BOUNDARY.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
CHANGE_RECORD = (
    ROOT / "docs" / "changelog" /
    "2026-09-05-hlp-000015-morrow-homecoming-priority.md"
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
    tether = TETHER_DOC.read_text(encoding="utf-8")
    morrow_lore = MORROW_LORE.read_text(encoding="utf-8")
    boundary = BOUNDARY_DOC.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    change_record = CHANGE_RECORD.read_text(encoding="utf-8")

    queue_words = words(queue)
    require("# Hearthline Return Queue" in queue,
            "Return Queue heading missing")
    require("| Version | `0.2` |" in queue,
            "Return Queue version is not 0.2")
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
            "The controller retains the full snapshot digest because it commits the hidden held, selected or in-service, and terminal partitions",
            "Morrow does not receive that digest",
            "only the closed ready-view digest and an invocation-scoped opaque snapshot/cut binding",
            "The controller alone carries those partitions forward unchanged",
            "Two distinct returns may both carry outcomes already established as valid wins",
            "Both remain separately attributable",
            "**Morrow** is the fictional presentation of the default deterministic Queue Steward profile",
            "grant-filtered **Queue Scheduling View**",
            "Its closed allowlist contains:",
            "A return payload or self-claim cannot set priority",
            "The view excludes raw or unselected payload, content identity, source Creature or objective identity and prestige",
            "Morrow is optional optimization",
            "A partial proposal may preserve useful named gaps as advisory evidence, but it is non-admissible as an order",
            "never as a service item in the exact data queue or snapshot it proposes over",
            "Only the canonical controller may validate an order proposal and append a final service snapshot",
            "the proposal carries only the ready-view digest and fresh invocation-scoped opaque snapshot/cut binding for the exact immutable queue identity, profile, and service epoch",
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

    require_all(
        queue_words,
        (
            "Hearthline assigns a bounded **Homecoming Priority Mark** when the task is commissioned, before dispatch",
            "**Homecoming Priority Assignment Receipt**",
            "An absent, invalid, conflicting, or outcome-unknown assignment blocks a new dispatch",
            "Typed idempotency lookup occurs before dispatch-lifecycle or current-head validation",
            "A byte-identical retry with the same key and binding resolves to the same assignment identity and its latest durable disposition",
            "Only an unseen key undergoes fresh lifecycle, ceiling, and policy validation",
            "`HEARTHLINE_TASK_TETHER_CORE_V1`",
            "Neither digest includes itself",
            "`P0_URGENT`, `P1_EXPEDITE`, `P2_ROUTINE`, and `P3_BACKGROUND`",
            "A return-injected mark or a valid mark transplanted from another TETHER or dispatch is ignored",
            "**Homecoming Priority Revision Receipt**",
            "exact predecessor revision, monotonic revision ordinal, compare-and-swap head",
            "Typed idempotency lookup also precedes revision lifecycle, predecessor, and compare-and-swap validation",
            "A byte-identical retry resolves to the same revision identity and latest durable disposition even after a later revision has advanced the head",
            "non-exact replay under a new key",
            "consumed revision budget and overtake count",
            "the first later snapshot whose frozen `priority_ledger_cut` includes that revision's durable ordinal",
            "a stale priority or snapshot head fails compare-and-swap without mutation",
            "An ambiguous append records an unknown disposition and does not become effective until durable reconciliation",
            "`PRIORITY_MIGRATION_REQUIRED` and enters the held partition",
            "It is never sent to Morrow or silently assigned the lowest or highest class",
            "Migration uses only a frozen mapping from pre-dispatch legacy records or an explicit `P3_BACKGROUND` fallback",
            "every item already due under the maximum-overtake rule is placed in stable arrival order ahead of ordinary priority bands",
            "fairness-due prefix, effective priority band, then stable FIFO arrival order",
            "`opaque_queue_item_binding`",
            "dense invocation-local `ready_arrival_rank`, numbered `1..N`",
            "controller-attested `effective_priority_rank`, but not the readable class or priority basis",
            "`controller_approved_processing_cost`",
            "The full snapshot digest, global arrival ordinals, queue identity, queue or service epoch, priority-ledger or snapshot cut, assignment/revision references, readable class, mark binding, and per-item attestation binding remain controller-only",
            "Dense ready ranks contain no gaps from held, selected, in-service, terminal, or post-cut items",
            "The initial profile gives Morrow no deadline, dependency, destination-readiness, safety, privacy, or other unused field",
            "Morrow's formal authority is `NONE`",
            "`QUEUE_ORDER_PROPOSAL_ONLY` names the one allowed output schema; it is not an authority, grant, permission, decision, or queue mutation",
            "The same profile, policy, and canonical input bytes must produce the same canonical proposal bytes",
            "the controller independently recomputes every count and fairness-due item from durable Service Admission Receipts",
            "There is no Morrow-to-Thulia or Thulia-to-Morrow request, receipt, ledger, storage path, message channel, mutual invocation, impersonation, or availability dependency",
            "each bounded function remains correct if the other is absent",
            "Service admission changes only queue service and overtake state",
            "It does not create or mutate result status, Homecoming custody, selected carry, grant, authority, publication, or external-effect state",
            "moves the selected item out of `READY` into an explicit held, terminal, or unknown state",
            "a new controller Readiness Receipt binds the resolved remedy",
            "cannot churn through proposals while lower items wait without earning overtakes",
            "Assignment, Revision, Intake Attempt, Intake Disposition, Enqueue, Proposal, Order, Service Admission, Service Disposition, Homecoming, and queue-close receipts occupy distinct typed identity domains",
            "If every eligible task is assigned `P0_URGENT`, the priority distinction collapses",
        ),
        "Morrow priority boundary",
    )
    morrow_allowlist = queue.split(
        "Its closed allowlist contains:", 1
    )[1].split("The ready-view digest", 1)[0]
    require("`arrival_ordinal`" not in morrow_allowlist,
            "Morrow allowlist leaks global arrival ordinals")
    require("`effective_priority_class`" not in morrow_allowlist,
            "Morrow allowlist leaks readable priority class")

    require("| Version | `0.6` |" in homecoming,
            "Homecoming Return Queue successor version missing")
    require_all(
        words(homecoming),
        (
            "Hearthline to assign one bounded Homecoming priority class while commissioning a task, before the controller records dispatch",
            "Homecoming Priority Assignment Receipt",
            "missing, invalid, conflicting, or ambiguous required assignment blocks a new dispatch",
            "Homecoming Priority Revision Receipt",
            "`priority_ledger_cut` includes it",
            "typed idempotency lookup precedes current lifecycle, predecessor, and head validation",
            "Only an unseen key undergoes fresh validation",
            "non-exact replay under a new key cannot alter the valid head",
            "Missing legacy priority is held for explicit migration rather than guessed",
            "Morrow and Thulia never overlap or communicate",
            "every durably recorded `HOMECOMING:RETURNED` bundle follows the same queue-intake path",
            "A lone return may be the immediate head",
            "Controller selection begins one revalidation; a pass permits service admission, which does not itself establish `HOMECOMING:RECONCILED`, task result, or carry",
            "Two distinct valid results remain two separately attributable results",
        ),
        "Homecoming queue integration",
    )

    require("| Version | `0.3` |" in creature,
            "Creature Queue Steward successor version missing")
    require_all(
        words(creature),
        (
            "the named Queue Steward, a deterministic stateless profile by default",
            "The controller owns the queue, priority receipt chain, snapshot, overtake counters, proposal receipt, final order, and admission",
            "Morrow's formal authority is `NONE`",
            "`QUEUE_ORDER_PROPOSAL_ONLY` is an allowed output schema, not a grant or decision",
            "Morrow and Thulia have no shared member, ledger, Home, context, storage, receipt, or direct channel",
            "Each remains correct when the other is absent",
            "optional [Queue Steward Creature]",
            "It is not the queue, scheduler, canonical controller, intake validator, Homecoming admitter, or owner of any return",
            "the controller retains every queue item and uses the frozen base service rule",
            "metadata-only scheduling view",
        ),
        "Creature Queue Steward integration",
    )

    require("| Version | `0.8` |" in ordered,
            "Ordered Lineage Return Queue successor version missing")
    require_all(
        words(ordered),
        (
            "Homecoming Priority Assignment Receipt",
            "Homecoming Priority Revision Receipt",
            "Queue Readiness Receipt",
            "snapshot cut share one controller-linearized compare-and-swap surface",
            "task TETHER",
            "`priority_ledger_cut` includes it",
            "typed idempotency lookup before current lifecycle, head, or compare-and-swap validation",
            "Revision idempotency lookup likewise precedes current-head and predecessor validation",
            "non-exact replay under a new key cannot mutate the valid head",
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

    require("version: 0.2-draft" in tether,
            "TETHER Homecoming-priority successor version missing")
    require_all(
        words(tether),
        (
            "Homecoming Priority Mark",
            "`task_tether_core_digest`",
            "`HEARTHLINE_TASK_TETHER_CORE_V1`",
            "neither digest includes itself",
            "Homecoming Priority Revision Receipt",
            "an ambiguous append has no effect until reconciled from durable state",
            "Typed idempotency lookup precedes current lifecycle, predecessor, and head validation for both assignment and revision",
            "non-exact replay under a new key cannot alter the valid head",
            "They have no direct channel or shared state",
        ),
        "TETHER priority integration",
    )

    require("# Morrow and the Marked Tethers" in morrow_lore,
            "Morrow lore heading missing")
    require_all(
        words(morrow_lore),
        (
            "Hearthline had prepared for this before any of them left",
            "No returning Creature could redraw its own mark",
            "grey coat with no pockets",
            "Every token on the rail had already been declared ready by the controller",
            "ready-arrival place on that rail",
            "places were numbered without gaps",
            "Morrow placed the twice-overtaken token first",
            "He kept no private notebook. He remembered no previous queue",
            "Morrow's rail still worked if Thulia was away",
            "Thulia's custody path still worked if Morrow's rail stood empty",
            "Hearthline marks the tether before the traveler leaves",
            "The controller alone opens the door",
            "He never decided what was true, worthy, or allowed",
        ),
        "Morrow lore boundary",
    )

    require_all(
        words(boundary),
        (
            "operational Return Queue profiles, queue items, arrival and service snapshots",
            "Homecoming Priority Marks, Assignment and Revision Receipts",
            "Morrow/Queue Steward views and proposals",
            "There is no direct channel, shared state, ledger, Perch, Bridge Gloss, custody, selected carry, mutual invocation, impersonation, or availability dependency between them",
        ),
        "private operational queue boundary",
    )
    require("docs/HEARTHLINE_RETURN_QUEUE.md" in readme,
            "README lacks the Return Queue route")
    require("only the controller owns counts, commits an order, and admits service" in words(readme),
            "README blurs Queue Steward and controller authority")
    require("HLP-000015" in changelog,
            "changelog lacks the Morrow priority successor")
    require("RESERVED_OFF_MAIN_NOT_ADOPTED" in changelog,
            "changelog lacks the reservation status")
    require("NAMESPACE_ONLY_NO_ADOPTION" in changelog,
            "changelog lacks the reservation effect ceiling")
    require("| Change ID | `HLP-000015` |" in change_record,
            "Morrow priority change record identity missing")
    require("| Predecessor | `HLP-000014` |" in change_record,
            "Morrow priority predecessor missing")
    require_all(
        words(change_record),
        (
            "dense invocation-local ready-arrival rank",
            "never global arrival ordinals, readable queue identities, epochs, or cuts",
            "Morrow's formal authority is `NONE`",
            "`QUEUE_ORDER_PROPOSAL_ONLY` is the stateless transform's allowed output schema, not a grant or decision",
        ),
        "Morrow change record least-view boundary",
    )

    for path in (
        QUEUE_DOC,
        HOMECOMING_DOC,
        CREATURE_DOC,
        ORDERED_DOC,
        TETHER_DOC,
        MORROW_LORE,
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
