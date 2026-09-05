# Name Morrow and bind priority at dispatch

| Field | Value |
|---|---|
| Change ID | `HLP-000015` |
| Record kind | `MORROW_PRIORITY_SUCCESSOR` |
| Recorded date | 2026-09-05 |
| Predecessor | `HLP-000014` |
| Branch base | `67cb39f56451a6aa3f3f5f872d82b3652b60cb17` |
| Return Queue | `0.1` -> `0.2` |
| Homecoming | `0.5` -> `0.6` |
| Creatures | `0.2` -> `0.3` |
| Ordered Lineage | `0.7` -> `0.8` |
| TETHER | `0.1-draft` -> `0.2-draft` |
| Scope | `PUBLIC_MORROW_HOMECOMING_PRIORITY_DESIGN_AND_LORE` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DESIGN_AND_LORE_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Named **Morrow** as the fictional face of the default deterministic,
  stateless Queue Steward profile and added *Morrow and the Marked Tethers* as
  a bounded lore story.
- Required Hearthline to assign one finite `homecoming_priority_class` while
  commissioning a task. The controller records a Homecoming Priority
  Assignment Receipt before dispatch and binds its compact mark to the exact
  task TETHER core without creating a self-hash.
- Defined `P0_URGENT`, `P1_EXPEDITE`, `P2_ROUTINE`, and `P3_BACKGROUND` as the
  initial sequencing-only class order under an operator-authorized,
  controller-frozen policy and per-task ceiling.
- Added append-only Homecoming Priority Revision Receipts with exact
  predecessor, idempotency, compare-and-swap, finite revision budget,
  controller-linearized snapshot cuts, and prospective effect only.
- Made typed idempotency lookup precede current lifecycle and head validation,
  so a byte-identical old retry returns its original identity and current
  disposition even after later state, while only unseen keys undergo fresh
  compare-and-swap checks.
- Made the controller's fallback priority-aware: fairness-due items first,
  then effective priority class, then stable arrival. Morrow may optimize only
  within a class and never owns queue state, overtake counts, order, or
  admission.
- Added strict non-interference between Morrow and Thulia. They share no
  channel, invocation, identity, state, ledger, Perch, Bridge Gloss, custody,
  selected carry, scheduling record, or availability dependency.
- Extended structural checks over the new versions, receipt fields, failure
  rules, story, public/private boundary, and Morrow/Thulia separation.

## Why

The original Return Queue gave a bounded sorter arrival, service-cost,
readiness, deadline, and overtake metadata but did not say where meaningful
task priority originated. Letting a returning bundle or sorter infer priority
from claimed content would invite self-promotion and would require access to
the very cargo the scheduling view is designed to hide.

The successor closes that loop at dispatch. Hearthline marks how urgently the
future return should be heard while the task is commissioned and before its
outcome is known. Morrow can then arrange sealed, opaque queue tokens without
judging their truth, value, prestige, or result. The controller still decides
eligibility, recomputes fairness, records order, and opens the service door.

A pure stateless profile fits that narrow job better than a persistent helper.
Every scheduling fact arrives in the frozen view, and every durable result
returns to controller custody. Naming the lore character does not manufacture
memory or an operational identity.

## Preserved boundaries

- The operator-authorized queue profile fixes the finite classes, class order,
  ceiling, revision budget, invalid-state behavior, and fairness rule.
  Hearthline assigns only within that frozen boundary.
- A Homecoming Priority Mark is scheduling metadata. It is not importance,
  truth, validity, safety certification, permission, authority, result status,
  deadline extension, or service admission.
- The controller freezes a priority-envelope-free TETHER core first and hashes
  it under `HEARTHLINE_TASK_TETHER_CORE_V1`. The Assignment Receipt binds that
  digest and the mark; the final envelope then carries the core, mark, and
  receipt reference. Neither digest includes itself.
- Missing or invalid required priority blocks new dispatch. A legacy or
  unresolved return preserves its intake and arrival identity but stays held
  for explicit controller migration; no class is guessed.
- A return, Spark, Creature, evaluator, Morrow, Thulia, payload claim, claimed
  win, source name, or prestige signal cannot assign or promote priority.
- Revisions never overwrite the initial assignment or task TETHER. Invalid or
  stale attempts leave the valid head unchanged, and ambiguous append outcomes
  cannot govern until reconciled.
- Revision append and snapshot cut share one controller-linearized surface.
  The first later snapshot whose `priority_ledger_cut` includes a revision may
  use it; no predicted next-snapshot label acts retroactively.
- Maximum-overtake fairness precedes ordinary priority bands. Morrow reads a
  frozen count only; the controller recomputes, owns, persists, and enforces it.
- Morrow receives only opaque bindings and controller-attested scheduling
  fields. It sees the ready-view digest and an invocation-scoped opaque cut
  binding, never the full snapshot digest that commits hidden partitions. It
  receives only a dense invocation-local ready-arrival rank, never global
  arrival ordinals, readable queue identities, epochs, or cuts. It sees neither
  readable class, mark or receipt binding, priority basis, cargo, identity,
  result, authority, Homecoming custody, carry, nor Thulia material.
- Morrow's formal authority is `NONE`. `QUEUE_ORDER_PROPOSAL_ONLY` is the
  stateless transform's allowed output schema, not a grant or decision; only
  the controller may use its candidate bytes.
- A failed or uncertain pre-admission head leaves `READY` with a Service
  Disposition Receipt before a successor snapshot. It needs a new controller
  Readiness Receipt after remedy, preventing high-priority retry livelock.
- Morrow and Thulia cannot call, impersonate, depend upon, or pass records to
  each other. Each bounded function remains correct when the other is absent.
- Two separately returned valid wins remain separately attributable. Priority
  and service order create no ownership, merger, or ranking of their truth.
- Repository publication creates no task, TETHER, queue, scheduler, Creature,
  runtime, model process, memory, credential, effect, result, or authority.

## Compatibility and migration

Return Queue `0.2`, Homecoming `0.6`, Creatures `0.3`, Ordered Lineage `0.8`,
and TETHER `0.2-draft` are additive successors. The `0.1` optional Queue
Steward Creature remains available only as a compatible experimental wrapper
around the same deterministic stateless profile and closed projection. It may
not introduce memory, broader access, different ordering semantics, or
authority.

Existing pre-priority task returns are not rewritten. If such a return enters a
successor queue, it receives `PRIORITY_MIGRATION_REQUIRED` and remains held
until an explicit controller migration receipt binds it prospectively under the
frozen profile. Its original identity, arrival ordinal, task, grant, consumed
limits, status, and receipts remain unchanged.

The current public Moltbook branch instruction, candidate manifest, source
profile, research-source registry, Static, Fireside, and Thulia profile remain
unchanged. The stricter Morrow/Thulia split is enforced by the queue's views and
controller routing boundary; it creates no new Thulia capability or profile.

## Verification observations

- The Return Queue checker binds all five successor document versions, the
  Homecoming Priority Mark construction, pre-dispatch assignment, finite class
  order, ceiling, idempotency, append-only revision chain, snapshot
  linearization, held legacy migration, controller fallback, and
  fairness-before-priority rule.
- The checker requires identical-input deterministic statelessness, controller
  ownership of overtake state and admission, the story route, and explicit
  Morrow/Thulia non-interference including absence independence.
- The checker requires idempotency-before-CAS retry semantics, ready-only digest
  exposure, controller-only full snapshot binding, and receipted removal and
  re-entry for a failed selected head.
- The TETHER checker binds the core-before-envelope construction and prevents a
  Priority Mark or revision from becoming a grant or renewal mechanism.
- Existing bounded-history, research-station, candidate-policy digest, source
  identity, local-link, and private-data checks remain in the verification
  suite.

## Open residuals

- This repository specifies public design and fictional lore. It does not
  implement a live queue, controller, scheduler, priority ledger, durable store,
  or task-dispatch service.
- The four readable priority labels and `maximum_overtakes: 2` are bounded
  initial policy choices, not measured universal optima.
- The class ceiling and revision budget prevent self-issued syntactic
  escalation but do not prove assignment calibration. If every eligible task
  receives `P0_URGENT`, priority collapses to within-band cost and arrival;
  semantic inflation would require a separately frozen class-capacity or quota
  policy and evidence.
- Real policy calibration, durable isolation, compare-and-swap behavior, crash
  recovery, fairness, starvation, legacy migration, privacy enforcement, and
  throughput benefit require a separately controlled implementation and
  prospective fabricated tests.
- The exact operator authority source, class ceiling, revision budget,
  service-cost bands, deadline classes, dependency fields, capacity, expiry,
  and exception policy remain task-specific frozen inputs.
- The optional Creature wrapper's equivalence to the stateless profile would
  require byte-domain and conformance tests before use.

## Evidence and exclusions

The public evidence consists of repository-authored design and lore text,
deterministic structural checks, and Git history. The story illustrates the
boundary; it is not an execution trace, operational report, witness statement,
or evidence that Morrow, Thulia, Hearthline, a queue, or a task process exists.

No private task or return payload, operational receipt, queue state, personal
context, credential, hidden reasoning, provider trace, benchmark data, or
external authorization is included. AI systems assisted inspection, drafting,
adversarial review, repository preparation, and validation as tools; they are
not authors, co-authors, witnesses, operators, or release authorities.

[Current changelog](../../CHANGELOG.md)
