# Hearthline Return Queue

> **When several bounded returns reach one narrow door, give every intake
> attempt a receipt and every accepted enqueue a place.**

| Field | Value |
|---|---|
| Version | `0.1` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

The **Hearthline Return Queue** is a controller-owned intake and service
discipline for independently identified, durably recorded
`HOMECOMING:RETURNED` bundles that traverse one serialized reconciliation
boundary. Every intake attempt receives a durable disposition, and every
successfully enqueued return receives an immutable place. A lone return uses
the same path and may become the immediately serviceable head; concurrent
returns join that path instead of letting a busy lock decide which return
matters.

The queue preserves each return as its own attributable object. It does not
merge workers, Creatures, Homes, ledgers, grants, evaluation rules, results, or
authority. A queue position is custody and scheduling state only.

## Queue boundary

Under Homecoming `0.5`, a future canonical controller freezes the destination's
queue profile before the first enqueue allocation. Every bundle first receives
its ordinary durable `HOMECOMING:RETURNED` receipt, then enters the same
queue-intake-attempt path whether it arrives alone or beside others. A lone
return may be enqueued and serviced without waiting for contention; later or
simultaneous returns join the same ordered surface. There is no separate fast
path whose result semantics differ.

Before enqueue, the controller journals one idempotent attempt bound to the
return identity, sealed bundle digest, Homecoming identity, destination, queue
profile, objective and authority epochs, and current grant and revocation
references. The attempt receives its own durable intake receipt before capacity
or enqueue disposition is decided. Its append-only disposition series records
accepted, blocked, unknown, reconciled, or conflict outcomes without rewriting
the original attempt.

The enqueue transaction is atomic:

- an exact retry with the same idempotency key resolves to the same accepted
  queue item or the same blocked or unknown intake disposition;
- reuse of that key with any changed intake binding records
  `IDEMPOTENCY_CONFLICT` and performs no queue mutation;
- a genuinely distinct accepted enqueue receives a distinct queue-item identity
  and immutable arrival ordinal;
- a busy service lane does not by itself reject, overwrite, or classify a
  return; and
- an ambiguous append remains `ENQUEUE_OUTCOME_UNKNOWN` until reconciled from
  durable state. It is not silently replayed.

`RETURN_QUEUE:ENQUEUED` records durable placement of a bounded, already returned
reference. It is not bundle validity, service admission, reconciliation, task
success, result status, carry approval, publication, or authority.

## Queue profile and item record

The queue profile is frozen before its first enqueue allocation. It binds at
least:

- the queue identity, controller, destination and accepted return classes;
- the immutable queue-profile identity and service epoch;
- the exact base service rule, optional sort-policy identity and version, and
  policy fields available to a sorter;
- maximum capacity, maximum overtakes, expiry behavior, close rule, and
  overflow disposition;
- the current objective and authority epochs, grant and revocation sources,
  privacy projection, and disclosure ceiling;
- the canonical allocator, append surface, service writer, and recovery rule;
  and
- the Homecoming, TETHER, residual, cancellation, and unknown-state routes.

Each queue item binds at least:

```yaml
queue_item_id: immutable queue-local identity
return_identity: exact source return identity
bundle_digest: digest under a named byte domain
homecoming_ref: exact source Homecoming
source_objective_ref: exact source objective
source_creature_or_spark_ref: exact source identity
arrival_ordinal: immutable append order
enqueue_receipt_ref: canonical durable placement receipt
bundle_validity_state: separate from queue custody
rule_owned_result_ref: unset unless established by the owning evaluation rule
service_state: pending, selected, in_service, terminal, or unknown
overtake_count: append-derived count, never silently reset
service_transaction_ref: unset until controller selection
service_admission_receipt_ref: unset until actual controller admission
service_disposition_receipt_ref: unset until a terminal or bounded handoff
reopen_handle: exact bounded route back to the unresolved return
```

For the initial bounded profile, `maximum_overtakes` is `2`. A successor
profile may choose another finite value, but it must freeze that value before
enqueue and cannot alter the count already carried by an item. A successor
receives a new profile identity and queue epoch. Pending items either finish
under their original profile or cross through an explicit controller migration
receipt that preserves their item identity, arrival evidence, and accumulated
overtake count; a successor never rewrites an earlier epoch.

The queue stores or references only what its declared intake aperture permits.
An item never gains a broader audience because it shares a queue. Raw return
payloads stay in their source-bound storage; scheduling views use only the
frozen metadata projection permitted by the queue profile.

## Arrival order and service order

Arrival order is immutable evidence about the controller's linearized append
order. It does not claim physical, causal, or globally true precedence between
concurrent attempts, and simultaneity supplies no native winner. Service order
is a separately derived scheduling choice. Neither is a ranking of truth,
quality, ownership, deservingness, or authority.

Before requesting a proposal, the controller freezes one finite snapshot bound
to the queue epoch, the largest durably committed arrival ordinal included by
the cut, the complete ready, held, selected or in-service, and terminal
partitions visible at that cut, the current bypass counts, and the policy
digest. Only the ready partition enters a proposal; already selected or
in-service items remain visible but cannot be admitted twice. An enqueue
committed after that cut is explicitly post-cut and first becomes visible in a
successor snapshot; it cannot invalidate or enter the frozen proposal. If the
committed cut itself is ambiguous, proposal and service stop until durable
state is reconciled.

The Queue Steward receives the full snapshot digest plus only the closed ready
projection described below. It does not receive the non-ready partition labels
or their custody, validity, or result state. The controller alone carries those
partitions forward unchanged and checks that no proposal binding can readmit
them.

The controller maintains three distinct surfaces:

| Surface | Meaning | Essential ceiling |
|---|---|---|
| Arrival snapshot | Every queue item in immutable arrival order | Does not choose service priority or result status |
| Order proposal | Optional ready-only permutation plus policy, reasons, and complete ready coverage | Cannot mutate the queue or authorize service |
| Final service snapshot | Controller-committed order for one exact queue epoch | Does not validate, admit, merge, or reclassify an item |

The default service rule is stable first-in, first-out among currently eligible
items. A different order requires a pinned policy, complete proposal coverage,
and a controller-owned order receipt. Every final snapshot preserves the
arrival snapshot, proposed order if any, final order, policy version, per-item
reason, overtake counts, exceptions, and unresolveds.

Two distinct returns may both carry outcomes already established as valid wins
under their separate evaluation rules. Queue order does not make either win
the other's predecessor, owner, duplicate, or loser. Both remain separately
attributable and both may proceed through their own Homecoming reconciliation
path.

## Queue Steward Creature

An optional **Queue Steward Creature** may propose a faster service order for
one frozen queue snapshot. It is a task-shaped, manifest-bound
[Creature](HEARTHLINE_CREATURES.md), not a new Spark role, scheduler, controller,
arbiter, or owner of the returns.

Its exact task is limited to producing one **Queue Order Proposal** from a
grant-filtered **Queue Scheduling View**. That view may contain only the policy
fields declared before enqueue. Its closed allowlist contains an opaque
queue-item binding, controller-linearized arrival ordinal, controller-approved
bounded service-cost or deadline class, attested dependency and destination
readiness, persisted overtake count, and named safety or privacy constraints.
Every sortable value is controller-derived or predeclared and attested under
the frozen profile; a return payload or self-claim cannot set priority.

The view excludes raw or unselected payload, content identity, source Creature
or objective identity and prestige, evaluator or result status, bundle validity,
Homecoming custody, carry state, grant or authority facts, external-effect
state, credentials, and hidden reasoning. An opaque binding lets the controller
map a proposal back to an item without telling the sorter which win it might be.

The Queue Steward Creature may:

- test a proposed permutation against the pinned policy;
- surface dependencies, bottlenecks, deadline risks, and starvation risks;
- return a complete proposal, a partial proposal with named gaps, or
  `ORDER_PROPOSAL_UNKNOWN`; and
- bind its return to the original snapshot digest without restating non-ready
  items or their private state.

It may not open or close a queue; allocate or remove an item; change arrival
order; validate a bundle; assign result status; grant priority from source
prestige or claimed importance; merge, drop, appropriate, or replay a return;
perform the handoff; issue authority; or commit the final order.

Its proposal travels through a manifest-bound controller control-receipt
aperture, never as a service item in the exact data queue or snapshot it
proposes over. If the Creature's own Homecoming uses a
`HOMECOMING:RETURNED` record, that record targets a distinct control
queue/profile and cannot enqueue into, reorder, or block the data queue under
review. This separation is not a fast path for ordinary result bundles.

The Queue Steward is optional optimization. A partial proposal may preserve
useful named gaps as advisory evidence, but it is non-admissible as an order.
If a proposal is absent, partial, late, invalid, revoked, or uncertain, the
controller retains the queue and uses the frozen base service rule. Queue
correctness and eventual disposition never depend on the Creature remaining
available.

## Controller admission and fairness

Only the canonical controller may validate an order proposal and append a
final service snapshot. It checks the proposal and its own resulting record to
establish that:

1. the proposal names the exact immutable queue identity, profile and service
   epoch digest, plus the frozen snapshot digest—not a mutable live-content
   digest;
2. the proposal includes every ready opaque binding exactly once and no unknown
   binding;
3. uses only the pinned policy fields and current epochs;
4. the controller carries every held, selected, in-service, terminal, blocked,
   cancelled, and unknown item forward unchanged rather than asking the
   Steward to classify, omit, or readmit it;
5. respects capacity, maximum-overtake, privacy, safety, grant, expiry, and
   revocation bounds; and
6. creates no duplicated provider, environment, publication, or other external
   effect.

The controller may accept, reject, or replace the proposal only under the
frozen policy, and records that disposition and reason. Proposal usefulness
does not confer authority on the Queue Steward.

A final service snapshot records intended order but consumes no overtake and
admits no item by itself. It lets the controller allocate one service
transaction for the selected head. The controller first checks that item's
ordinary revalidation inputs. A passing check permits a separate append-only
Service Admission Receipt bound to the queue item, profile and service epoch,
final snapshot and order receipt, controller, revalidation inputs and pass
result, and the exact pre/post overtake counts. That receipt atomically marks
`RETURN_QUEUE:IN_SERVICE` and is the durable event that consumes an actual
overtake.

A failed or uncertain pre-admission revalidation instead receives a Service
Disposition Receipt and consumes no overtake. After admitted work reaches a
terminal queue observation or bounded handoff, the controller appends a
Service Disposition Receipt bound to the service transaction and, when present,
its admission and Homecoming Reconciliation Receipts. Admission and disposition
remain distinct from Homecoming reconciliation and from any external effect.

An item's overtake counter increments only when a later-arriving eligible item
is actually admitted to service ahead of it. Merely proposing an order, or
leaving an item in the unserved suffix of a snapshot, does not increment the
counter. The initial queue profile sets `maximum_overtakes: 2` and an aging
rule. Reaching the bound makes the older item service-due under the base rule
unless a separately authorized exception records the exact blocker, duration, remedy,
and reopening route. An urgent item may move forward under a predeclared rule;
the displaced items remain visible and cannot be indefinitely starved.

Queue capacity is finite. When no slot can be durably allocated, the controller
records `QUEUE_CAPACITY_BLOCKED` or `QUEUE_CAPACITY_UNKNOWN`, preserves the
return's identity and sealed-source reference, and emits the permitted TETHER
reopening handle. An exact retry returns that recorded disposition; a genuinely
new attempt after the named remedy requires a new idempotency key. Overflow is
backpressure with trace, not silent loss or a
license to widen storage, retry an ambiguous effect, or discard another item.

## Service and Homecoming

For each service-due item, the controller begins one single-writer service
transaction, records selection, and applies the ordinary
[Homecoming](HEARTHLINE_HOMECOMING.md)
revalidation checks against that return's dispatch-pinned Home Record and
current grant, recipient, disclosure, retention, expiry, revocation, and
authorized-reroute state. Only a passing pre-admission check permits the Service
Admission Receipt and opens that one reconciliation transaction; it does not
append the Reconciliation Receipt by itself.

The queue never substitutes for those checks. Its item states remain distinct:

```text
HOMECOMING:RETURNED != RETURN_QUEUE:ENQUEUED
RETURN_QUEUE:ENQUEUED != BUNDLE_VALID != SERVICE_SELECTED
SERVICE_SELECTED != HOMECOMING:RECONCILED
HOMECOMING:RECONCILED != TASK_RESULT
```

A rule-owned result status may already have been established before return. It
remains attached to its source record throughout queueing and reconciliation;
the queue neither creates nor suspends that status.

After a terminal service observation, the controller appends the terminal
Service Disposition Receipt and advances to the next service-due item. A
rejected, partial, revoked,
cancelled, expired, blocked, or unknown return keeps its identity, arrival
ordinal, source references, disposition, residuals, and reopening handle. No
failure path is cleaned into success, and no successful item erases another.

[Thulia](HEARTHLINE_THULIA.md) is not the queue sorter. After an item completes
its ordinary admission path, her existing bounded custody or Bridge Gloss work
may receive only its separately permitted projection. Queue position does not
expand her grant or turn custody into scheduling authority.

## Suspension, recovery, and closure

The queue has controller-owned status and receipts, not its own heartbeat or
Home. Every optional Queue Steward Creature keeps its own heartbeat,
suspension, and Home records. A liveness pulse does not reorder an item, keep a
host alive, renew authority, or prove queue progress.

After a crash or interruption, the controller reconstructs the last durable
Intake Attempt and Disposition Receipts, accepted Enqueue Receipts and arrival
snapshot, order receipt, Service Admission Receipt, in-service transaction,
Service Disposition Receipts, and consumed limits. It reconciles every
`ENQUEUE_OUTCOME_UNKNOWN` before deriving the accepted arrival set. It never moves an ordinal
backward or assumes an unreceipted admission or handoff completed. An ambiguous service effect stops at
`SERVICE_OUTCOME_UNKNOWN`; recovery reconciles the existing transaction before
any successor attempt.

A queue-close snapshot freezes an intake cutoff and covers every Intake Attempt
Receipt through it. Close is forbidden while any append outcome remains
ambiguous or any `ENQUEUE_OUTCOME_UNKNOWN` or `QUEUE_CAPACITY_UNKNOWN`
disposition remains unresolved. Every accepted intake disposition must link one handled queue item;
every blocked, conflict, cancelled, or explicitly left-open intake must have a
terminal disposition and bounded TETHER route. Every enqueued item must then
have a terminal Service Disposition Receipt or an explicit bounded handoff such
as blocked, cancelled, left open, or unknown before the controller appends the
queue-close receipt against the exact final snapshot. Closing the queue does not
close a source objective, manufacture a result, erase residuals, or perform PAL
scoped closure.

Every unresolved queue state carries an exact [TETHER](HEARTHLINE_TETHER.md)
handle. TETHER carries the route back to the trace; it is not queue storage,
hidden state, a scheduler, or permission to resume.

## Prospective conformance boundary

A future implementation should test at least:

- deterministic concurrent enqueue without busy-lock rejection;
- exact-retry idempotency and distinct-return allocation;
- same-key/different-binding conflict without queue mutation;
- immutable arrival order under proposed and committed reordering;
- complete-permutation validation and rejection of omission or duplication;
- controller-only final-order append and service admission;
- metadata-only Queue Steward access and failure fallback to the base rule;
- maximum-overtake and aging enforcement without starvation;
- preservation of two separately valid wins and their attribution;
- bounded overflow with a reopening route;
- crash recovery before replay of an ambiguous service transaction; and
- separation of queue custody, bundle validity, Homecoming, result status,
  carry, external effects, and authority.

This document creates no queue, Creature, Spark, controller, allocator, ledger,
runtime, model process, memory, credential, external effect, benchmark result,
or authority. Implementation requires a separately specified private runtime,
fabricated conformance fixtures, prospective tests, review, and an exact current
authorization.
