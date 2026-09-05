# Hearthline Return Queue

> **When several bounded returns reach one narrow door, give every intake
> attempt a receipt and every accepted enqueue a place.**

| Field | Value |
|---|---|
| Version | `0.2.1` |
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

## v0.2.1 maximum-overtake claim-narrowing successor

Version `0.2.1` clarifies that `maximum_overtakes` bounds successful
admissions of later-arriving eligible items ahead of a continuously `READY`
item while controller service continues. It is not a wall-clock latency bound,
a controller-liveness promise, or an eventual-disposition guarantee.

This successor narrows the public claim only. It changes no queue state,
ordering rule, receipt, controller boundary, runtime behavior, or authority.
Version `0.2` remains the frozen design predecessor below.

## v0.2 Morrow and the dispatch-priority successor

Version `0.2` names **Morrow** as the fictional face of the default Queue
Steward profile and adds one missing input to the return loop: Hearthline
assigns a bounded **Homecoming Priority Mark** when the task is commissioned,
before dispatch. The canonical controller records that assignment in a
**Homecoming Priority Assignment Receipt** bound to the exact task TETHER,
dispatch, destination queue profile and epoch, policy, priority class, ceiling,
basis reference, and revision budget. Dispatch cannot begin while that required
binding is missing, invalid, or ambiguous.

Morrow does not discover priority by opening a return or judging its result.
For each frozen snapshot, the controller resolves the effective assignment and
any valid append-only revisions, then gives Morrow only an opaque,
scheduling-only projection. Morrow applies one pinned deterministic order rule
without retaining state and returns one proposal. The controller retains all
state, validates fairness, commits any order, and alone performs service
admission.

The `0.1` optional Queue Steward Creature remains a compatible experimental
wrapper. It is no longer the default form. A wrapper must invoke the same
stateless profile over the same closed view and may add no memory, payload
access, queue authority, or different ordering semantics.

Morrow and [Thulia](HEARTHLINE_THULIA.md) occupy disjoint surfaces. They have no
direct channel and never exchange records. Morrow cannot access a Perch,
Thulia's ledger or custody work, a Bridge Gloss, selected carry, or any Thulia
input or output. Thulia cannot access or alter priority assignments or
revisions, Queue Scheduling Views, Queue Order Proposals, final service orders,
or service admission. Only Hearthline through the canonical controller may
route their separate outputs under their separate grants; neither output is an
input to the other.

Version `0.1` remains the predecessor for every queue behavior not expressly
revised here.

## Queue boundary

Under Homecoming `0.6`, a future canonical controller freezes the destination's
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

## Dispatch-time priority assignment

Priority originates at commissioning, not at return. Before the controller
appends `TASK:DISPATCHED`, Hearthline assigns one class from the finite order
declared by the operator-authorized, controller-frozen destination queue
profile. Hearthline neither chooses that finite policy nor its ceiling. The
controller validates that the assigned class does not outrank the task's
frozen `priority_ceiling_class`, then appends one Homecoming Priority Assignment
Receipt. Typed idempotency lookup occurs before dispatch-lifecycle or
current-head validation. A byte-identical retry with the same key and binding
resolves to the same assignment identity and its latest durable disposition,
including an unknown-to-reconciled disposition, even after dispatch or later
priority state has advanced. Reuse with changed bindings records
`PRIORITY_IDEMPOTENCY_CONFLICT` and performs no dispatch or priority mutation.
Only an unseen key undergoes fresh lifecycle, ceiling, and policy validation.
An absent, invalid, conflicting, or outcome-unknown assignment blocks a new
dispatch.

The construction avoids a self-hash. First the controller freezes the task
TETHER core without a priority envelope and computes
`task_tether_core_digest` under the named byte domain
`HEARTHLINE_TASK_TETHER_CORE_V1`. The Assignment Receipt binds that core digest
and the complete mark. The final TETHER envelope then carries the frozen core,
mark, and Assignment Receipt reference and may receive its own separate envelope
digest. Neither digest includes itself, and a priority revision never rewrites
either one.

The task TETHER envelope carries the compact Homecoming Priority Mark rather
than an editable label:

```yaml
homecoming_priority_mark:
  task_tether_ref: exact immutable TETHER identity
  task_tether_core_digest: digest under HEARTHLINE_TASK_TETHER_CORE_V1
  dispatch_ref: exact task or Creature dispatch
  homecoming_destination_ref: declared destination
  queue_profile_ref: predeclared queue profile
  priority_policy_ref: finite class order and comparison rule
  homecoming_priority_class: one profile-defined class
  priority_ceiling_class: strongest class any revision may select
  priority_basis_ref: controller-readable source record, not free text
  dispatch_epoch: authority-and-objective epoch observed, not established, by assignment
  effective_queue_epoch: exact queue epoch
  priority_revision_budget: finite dispatch-pinned maximum
  priority_assignment_receipt_ref: canonical assignment receipt
```

The initial bounded policy uses the ordered classes `P0_URGENT`,
`P1_EXPEDITE`, `P2_ROUTINE`, and `P3_BACKGROUND`, in that order, after
eligibility and forced-fairness checks. Their readable names are queue
sequencing labels only. They do not state a task's worth, truth, safety, legal
importance, quality, result, permission, or authority. A successor profile may
use another finite class set only by assigning a new policy and profile identity
before dispatch.

The Spark, Creature, returned bundle, evaluator, Morrow, and Thulia cannot
create, revise, copy, inherit, or promote the mark. A payload field, claimed
win, source name, prestige signal, urgency statement, or self-issued receipt is
excluded from priority resolution. A return-injected mark or a valid mark
transplanted from another TETHER or dispatch is ignored, recorded as a binding
conflict, and cannot alter effective priority. Two separately commissioned
tasks may hold the same class and later return two separately attributable
valid wins; neither return acquires the other's class or position.

### Append-only priority revision

Hearthline may propose a changed class while the task is away only through a
controller-authored **Homecoming Priority Revision Receipt**. Each receipt binds
the original assignment, exact predecessor revision, monotonic revision
ordinal, compare-and-swap head, idempotency key, old and new class,
controller-readable basis reference, consumed and remaining revision budget,
exact queue epoch, current priority-ledger head, and exact observed snapshot
head. Revision append and snapshot cut share one controller-linearized surface:
a stale priority or snapshot head fails compare-and-swap without mutation.

A revision:

- must stay inside the original finite policy and
  `priority_ceiling_class`;
- becomes effective only for the named queue epoch in the first later snapshot
  whose frozen `priority_ledger_cut` includes that revision's durable ordinal;
- cannot alter a frozen earlier snapshot or an item already selected,
  in-service, or terminal;
- preserves the original mark, assignment, every superseded revision, and
  consumed revision budget and overtake count; and
- cannot create, renew, widen, transfer, or extend the task, grant, authority,
  Home, audience, disclosure, retention, expiry, deadline, capability, action
  count, cost ceiling, or any other budget.

Typed idempotency lookup also precedes revision lifecycle, predecessor, and
compare-and-swap validation. A byte-identical retry resolves to the same
revision identity and latest durable disposition even after a later revision
has advanced the head. Same-key changed binding conflicts. Only an unseen key
undergoes fresh validation; for it, a stale predecessor, non-exact replay under
a new key, no-op class, exceeded ceiling, exhausted budget, or invalid author
records a conflict and performs no priority mutation. An ambiguous append
records an unknown disposition and does not become effective until durable
reconciliation establishes its one canonical outcome. No revision takes effect
merely because a message, branch, return, or Queue Order Proposal describes it.

Each snapshot records the highest durable priority-ledger ordinal included by
its cut. A revision and a concurrent snapshot therefore have one controller
order: either the snapshot cut includes the revision and names it as effective,
or the revision waits for a later snapshot. No predicted `N + 1` label can make
a revision retroactive.

### Resolution failure

At queue intake and every snapshot, the controller resolves the assignment and
the single valid revision head from durable state. A rejected, stale, forked,
no-op, or otherwise invalid revision leaves the last unambiguous valid head in
force and cannot poison or mutate it. If an append outcome or competing head is
ambiguous, priority service for that item stops until reconciliation.

A legacy return that predates the required mark, or an item whose assignment,
policy, epoch, receipt binding, ceiling, or revision head cannot be
established, keeps its intake and queue identity but receives
`PRIORITY_MIGRATION_REQUIRED` and enters the held partition. It is never sent
to Morrow or silently assigned the lowest or highest class. A separate
controller migration receipt may bind it prospectively to the frozen successor
profile without changing its arrival identity, source task, grant, consumed
limits, or earlier receipts. Migration uses only a frozen mapping from
pre-dispatch legacy records or an explicit `P3_BACKGROUND` fallback; it cannot
inspect the returned cargo, claimed result, source prestige, or later urgency
statement to manufacture priority. If neither route is established, the item
remains held. Until then it remains visible to the controller
and cannot be dropped, elevated, demoted by guess, or allowed to block service
for valid ready items. A malformed priority therefore fails safely without
corrupting the queue.

## Queue profile and item record

The queue profile is frozen before its first enqueue allocation. It binds at
least:

- the queue identity, controller, destination and accepted return classes;
- the immutable queue-profile identity and service epoch;
- the exact base service rule, optional sort-policy identity and version, and
  policy fields available to a sorter;
- the finite Homecoming priority class order, required-assignment rule,
  maximum class ceiling, priority-revision budget, and invalid-priority
  fallback;
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
task_tether_ref: exact dispatch-carried TETHER
task_tether_core_digest: assignment-bound pre-envelope core digest
priority_assignment_receipt_ref: immutable initial assignment
priority_resolution_state_at_enqueue: valid or PRIORITY_MIGRATION_REQUIRED
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

Assignment, Revision, Intake Attempt, Intake Disposition, Enqueue, Proposal,
Order, Service Admission, Service Disposition, Homecoming, and queue-close
receipts occupy distinct typed identity domains. A shared idempotency key,
digest, ordinal, readable label, or task cannot make one receipt stand in for
another.

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

The controller retains the full snapshot digest because it commits the hidden
held, selected or in-service, and terminal partitions. Morrow does not receive
that digest. He receives only the closed ready-view digest and an
invocation-scoped opaque snapshot/cut binding that the controller can map back
to the full snapshot without exposing a stable equality or dictionary oracle
over hidden partitions. Morrow does not receive the non-ready partition labels
or their custody, validity, or result state. The controller alone carries those
partitions forward unchanged and checks that no proposal binding can readmit
them.

The controller maintains three distinct surfaces:

| Surface | Meaning | Essential ceiling |
|---|---|---|
| Arrival snapshot | Every queue item in immutable arrival order | Does not choose service priority or result status |
| Order proposal | Optional ready-only permutation plus policy, reasons, and complete ready coverage | Cannot mutate the queue or authorize service |
| Final service snapshot | Controller-committed order for one exact queue epoch | Does not validate, admit, merge, or reclassify an item |

The `0.2` base service rule is deterministic and priority-aware among currently
eligible items. First, every item already due under the maximum-overtake rule is
placed in stable arrival order ahead of ordinary priority bands. Remaining
items are ordered by effective Homecoming priority rank and then immutable
arrival ordinal. This controller-computable order is the mandatory fallback
when Morrow is absent or a proposal is late, partial, invalid, revoked, or
uncertain. Hearthline's dispatch mark therefore remains effective without
making Morrow necessary for correctness.

A valid Morrow proposal may apply only the pinned within-class
controller-approved processing-cost and deterministic arrival tie-break rules;
it cannot move a lower-priority item ahead of a higher-priority item or any item
ahead of a fairness-due item. Only the controller may apply a separately
authorized cross-band, deadline, dependency, or safety exception under the frozen policy,
and it records that exception without presenting it as Morrow's choice. Every
different order requires complete proposal coverage and a controller-owned
order receipt. Every frozen snapshot pins, per ready item, the immutable
assignment receipt, effective valid revision head or null, resolved class, and
resolution evidence used at that cut; a later revision never rewrites those
bytes or the queue item. Every final snapshot preserves the arrival snapshot,
those effective priority-state references, proposed order if any, final order,
policy version, per-item reason, overtake counts, exceptions, and unresolveds.

Two distinct returns may both carry outcomes already established as valid wins
under their separate evaluation rules. Queue order does not make either win
the other's predecessor, owner, duplicate, or loser. Both remain separately
attributable and both may proceed through their own Homecoming reconciliation
path.

## Morrow: the stateless Queue Steward

**Morrow** is the fictional presentation of the default deterministic Queue
Steward profile. The profile is a stateless scheduling transform, not a Spark,
persistent process, memory, controller, arbiter, or owner of the returns. For
each invocation it receives one complete frozen input and emits one Queue Order
Proposal; then its working surface is discarded. The same profile, policy, and
canonical input bytes must produce the same canonical proposal bytes.

Its exact task is limited to producing one **Queue Order Proposal** from a
grant-filtered **Queue Scheduling View**. That view may contain only the policy
fields declared before dispatch and enqueue. Its closed allowlist contains:

- invocation-scoped `opaque_queue_item_binding`;
- dense invocation-local `ready_arrival_rank`, numbered `1..N` in the true
  arrival order of only the ready items in that invocation;
- controller-attested `effective_priority_rank`, but not the readable class or
  priority basis;
- bounded `controller_approved_processing_cost`;
- controller-owned persisted `overtake_count`.

The ready-view digest, invocation-scoped opaque snapshot/cut binding, policy
reference, and maximum-overtake bound accompany the complete view rather than
being repeated as item payload. The full snapshot digest, global arrival
ordinals, queue identity, queue or service epoch, priority-ledger or snapshot
cut, assignment/revision references, readable class, mark binding, and
per-item attestation binding remain controller-only because Morrow does not
need them to sort. The opaque invocation binding is fresh for that call and
reveals no stable cross-invocation equality. Dense ready ranks contain no gaps
from held, selected, in-service, terminal, or post-cut items. The initial
profile gives Morrow no deadline, dependency, destination-readiness,
safety, privacy, or other unused field.
The controller resolves eligibility and the held partition before projection.
Adding another field or comparator requires a successor profile and new tests.

Every sortable value is controller-derived or predeclared and attested under
the frozen profile. A return payload or self-claim cannot set priority. Morrow
receives neither the assignment nor revision ledger; the controller projects
only the effective rank after validating their receipt chain.

Morrow's formal authority is `NONE`. `QUEUE_ORDER_PROPOSAL_ONLY` names the one
allowed output schema; it is not an authority, grant, permission, decision, or
queue mutation. The stateless transform emits candidate bytes. Only the
controller's separately established authority can validate, ignore, reject, or
use those bytes.

The view excludes raw or unselected payload, content identity, source Creature
or objective identity and prestige, priority basis, evaluator or result status,
bundle validity, Homecoming custody, carry state, grant or authority facts,
external-effect state, credentials, hidden reasoning, and every Thulia surface.
An opaque binding lets the controller map a proposal back to an item without
telling Morrow which task or win it might be.

Morrow may:

- use the frozen controller-owned `overtake_count` to propose the pinned
  fairness-first, priority-band, within-class cost, and arrival tie-break order;
- surface only the policy's declared fairness, priority, cost, and stable-tie
  reason codes;
- return a complete proposal, a partial proposal with named gaps, or
  `ORDER_PROPOSAL_UNKNOWN`; and
- bind the proposal to the ready-view digest and invocation-scoped opaque
  snapshot/cut binding without restating non-ready items or their private state.

Morrow may not open or close a queue; retain cross-invocation state; allocate or
remove an item; change arrival order or a priority mark; request or write a
priority revision; validate a bundle; assign result status; grant priority from
source prestige or claimed importance; merge, drop, appropriate, or replay a
return; perform a handoff; issue authority; or commit the final order.

The proposal travels through a controller-owned control-receipt aperture,
never as a service item in the exact data queue or snapshot it proposes over.
The stateless profile has no Homecoming of its own. A compatible optional
[Queue Steward Creature](HEARTHLINE_CREATURES.md) wrapper may return through a
distinct control queue/profile, but its return cannot enqueue into, reorder, or
block the data queue under review. This separation is not a fast path for
ordinary result bundles.

Morrow and Thulia never overlap or directly interact. No Perch, roost index,
Static ledger, Bridge Gloss, selected-carry record, custody state, priority
record, scheduling view, proposal, order, or admission record may cross between
their surfaces. There is no Morrow-to-Thulia or Thulia-to-Morrow request,
receipt, ledger, storage path, message channel, mutual invocation,
impersonation, or availability dependency. Neither can act under the other's
name, profile, identity, or grant, and each bounded function remains correct if
the other is absent. The controller may separately
route an already authorized post-admission projection to Thulia, but it removes
all Morrow and queue-scheduling material and does not make either character's
output an input to the other.

Morrow is optional optimization. A partial proposal may preserve useful named
gaps as advisory evidence, but it is non-admissible as an order. If a proposal
is absent, partial, late, invalid, non-deterministic, revoked, or uncertain,
the controller retains the queue and computes the frozen priority-aware base
service rule itself: fairness-due prefix, effective priority band, then stable
FIFO arrival order. Queue correctness, dispatch priority, and fairness-rule
computation never depend on Morrow remaining available. This fallback does not
promise controller liveness, wall-clock service latency, or eventual
disposition.

Reading `overtake_count` is not owning it. Before accepting any proposal, the
controller independently recomputes every count and fairness-due item from
durable Service Admission Receipts. Only the controller persists a changed
count, and only an actual admission can change one.

## Controller admission and fairness

Only the canonical controller may validate an order proposal and append a
final service snapshot. It checks the proposal and its own resulting record to
establish that:

1. the proposal carries only the ready-view digest and fresh invocation-scoped
   opaque snapshot/cut binding for the exact immutable queue identity, profile,
   and service epoch—not a readable queue identity, global epoch, mutable
   live-content digest, or full hidden-partition digest; the controller maps
   those fields back to the exact frozen snapshot and binds its full queue,
   epoch, cut, and snapshot digests only in the controller-owned order receipt;
2. the proposal includes every ready opaque binding exactly once and no unknown
   binding;
3. uses only the pinned policy fields, controller-resolved priority-state
   references, and current epochs, and does not alter a class or cross a
   priority band;
4. the controller carries every held, selected, in-service, terminal, blocked,
   cancelled, and unknown item forward unchanged rather than asking the
   Steward to classify, omit, or readmit it;
5. places every maximum-overtake-due item ahead of ordinary priority bands and
   respects capacity, privacy, safety, grant, deadline, expiry, and revocation
   bounds; and
6. creates no duplicated provider, environment, publication, or other external
   effect.

The controller may accept, reject, or replace the proposal only under the
frozen policy, and records that disposition and reason. Proposal usefulness
does not confer authority on the Queue Steward.

Priority cannot defeat eligibility, revocation, expiry, or the fairness bound.
The controller first removes non-ready items from Morrow's projection, then
places every maximum-overtake-due item as a stable-arrival prefix, then applies
effective dispatch priority, then considers Morrow's within-class proposal. A
high class cannot make an expired or unauthorized return ready, extend a
deadline, spend beyond a budget, or overtake a fairness-due item.

A final service snapshot records intended order but consumes no overtake and
admits no item by itself. It lets the controller allocate one service
transaction for the selected head. The controller first checks that item's
ordinary revalidation inputs. A passing check permits a separate append-only
Service Admission Receipt bound to the queue item, profile and service epoch,
final snapshot and order receipt, controller, revalidation inputs and pass
result, and the exact pre/post overtake counts. That receipt atomically marks
`RETURN_QUEUE:IN_SERVICE` and is the durable event that consumes an actual
overtake.

Service admission changes only queue service and overtake state. It does not
create or mutate result status, Homecoming custody, selected carry, grant,
authority, publication, or external-effect state.

A failed or uncertain pre-admission revalidation instead receives a Service
Disposition Receipt and consumes no overtake. That same controller transaction
moves the selected item out of `READY` into an explicit held, terminal, or
unknown state with its blocker, remedy, and reopening handle before any
successor snapshot. The item cannot re-enter `READY` for another attempt until
a new controller Readiness Receipt binds the resolved remedy and current
revalidation inputs; an unknown outcome must first be durably reconciled. A
repeatedly failing high-priority head therefore cannot churn through proposals
while lower items wait without earning overtakes.

After admitted work reaches a terminal queue observation or bounded handoff,
the controller appends a Service Disposition Receipt bound to the service
transaction and, when present, its admission and Homecoming Reconciliation
Receipts. Admission and disposition remain distinct from Homecoming
reconciliation and from any external effect.

An item's overtake counter increments only when a later-arriving eligible item
is actually admitted to service ahead of it. Merely proposing an order, or
leaving an item in the unserved suffix of a snapshot, does not increment the
counter. The initial queue profile sets `maximum_overtakes: 2` and an aging
rule. For an item that remains continuously `READY`, the bound counts successful
admissions of later-arriving eligible items ahead of it while controller service
continues; it is not a wall-clock latency bound, a service-liveness promise, or
an eventual-disposition guarantee. Reaching the bound makes the older item
service-due under the base rule unless a separately authorized exception records
the exact blocker, duration, remedy, and reopening route. Absent that exception,
an urgent item may move forward under a predeclared rule only before the
displaced item becomes fairness-due.

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
Home. Stateless Morrow has neither a heartbeat nor a Home and retains nothing
between invocations. Every compatible optional Queue Steward Creature wrapper
keeps its own heartbeat, suspension, and Home records. A liveness pulse does
not reorder an item, keep a host alive, renew authority, or prove queue
progress.

After a crash or interruption, the controller reconstructs the last durable
Homecoming Priority Assignment and Revision Receipts, their idempotency and
compare-and-swap dispositions, Intake Attempt and Disposition Receipts,
accepted Enqueue Receipts and arrival snapshot, order receipt, Service
Admission Receipt, in-service transaction, Service Disposition Receipts, and
consumed limits. It reconciles every
`ENQUEUE_OUTCOME_UNKNOWN` before deriving the accepted arrival set. It never moves an ordinal
backward or assumes an unreceipted admission or handoff completed. An ambiguous service effect stops at
`SERVICE_OUTCOME_UNKNOWN`; recovery reconciles the existing transaction before
any successor attempt.

A queue-close snapshot freezes an intake cutoff and covers every Intake Attempt
Receipt through it. Close is forbidden while any append outcome remains
ambiguous or any `ENQUEUE_OUTCOME_UNKNOWN` or `QUEUE_CAPACITY_UNKNOWN`
disposition remains unresolved. An unresolved priority assignment or revision
append must be reconciled or preserved in an explicit held/terminal handoff;
close cannot silently select a class. Every accepted intake disposition must link one handled queue item;
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

The finite class set, ceiling, and revision budget prevent a worker or sorter
from syntactically escalating itself. They do not prove that Hearthline's
assignments are well calibrated. If every eligible task is assigned
`P0_URGENT`, the priority distinction collapses and ordering falls through to
fairness, within-class processing cost when Morrow is valid, and arrival.
Preventing semantic priority inflation would require a separately frozen
class-capacity or quota policy, assignment evidence, and prospective tests; it
is not claimed by this version.

## Prospective conformance boundary

A future implementation should test at least:

- deterministic concurrent enqueue without busy-lock rejection;
- exact-retry idempotency and distinct-return allocation;
- same-key/different-binding conflict without queue mutation;
- immutable arrival order under proposed and committed reordering;
- complete-permutation validation and rejection of omission or duplication;
- controller-only final-order append and service admission;
- metadata-only Queue Steward access and failure fallback to the base rule;
- pre-dispatch, receipt-bound priority assignment and dispatch blocking when it
  is missing or invalid;
- exact-retry assignment and revision idempotency, compare-and-swap revision
  ordering, prospective snapshot effectiveness, and conflict without mutation;
- immutable per-snapshot priority-state binding, ceiling and revision-budget
  enforcement, and explicit legacy migration or hold;
- deterministic stateless Morrow output and priority-aware controller fallback;
- maximum-overtake precedence over priority and no deadline, expiry, grant, or
  budget renewal through a mark or revision;
- failed or uncertain selected-head removal from `READY`, receipted remedy
  before re-entry, and absence of high-priority retry livelock;
- complete Morrow/Thulia surface and channel separation;
- maximum-overtake and aging enforcement as a bound on successful later
  admissions ahead of a continuously `READY` item, conditional on controller
  service continuing, without asserting wall-clock latency, liveness, or
  eventual disposition;
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
