# Hearthline Task Triads and Homecoming

> **Every bounded Spark leaves with a path home.**

| Field | Value |
|---|---|
| Version | `0.7` |
| Status | Candidate successor design vocabulary — pending steward review |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

## v0.7 selected-carry successor

Version `0.7` keeps the three-seat formation introduced by `0.6` and repairs
its return topology. Hearthline provisions the **Work Spark** and
**Task-Keeper Spark**; Thulia alone provisions the **Ledger Scribe Spark**.
The controller freezes one complete offer, reserves all three exact seats,
atomically consumes the two providers' immutable own-seat intents, records
`TRIAD_BOUND`, and still starts no member until a separate revalidated dispatch
receipt records `DISPATCHED`. Worker, Task-Keeper, and Ledger-Keeper remain
three Sparks with one job each, not one Spark with three jobs.

Each member seals and validates its own terminal candidate bundle. A
`SEALED` plus `VALID` bundle moves separately under an exact return grant to
the commissioning Hearthline task intake as
`RETURN_PENDING_HEARTHLINE`. Thulia does **not** receive the three raw member
returns, and provisioning the Ledger-Keeper gives her no right to read that
bundle. Hearthline receives no right to provision or replace the Ledger-Keeper;
provider identity and declared return recipient are different fields.

Inside one bounded inspection projection, Hearthline accounts for all three
seats in a sealed valid Triad Return Manifest and seals one immutable, complete
**Carry Selection**. Every admitted distinction is marked `SELECT_KEEP`,
`SELECT_CONDENSE`, or `SELECT_LOSE`; every absent, invalid, stale, or unknown
seat is named as an exception. Only the selected projection then crosses a
separately authorized `H_TO_T_CARRY` lane to Thulia. After Thulia durably
receives it and the selected-carry handoff store durably commits those exact
accepted bytes, the controller may close Hearthline's raw inspection projection.
That closure means task-scoped raw access was dropped. It is neither canonical
pruning nor a claim that a provider erased model state or that a model
literally forgot.

If the selected carry needs translation, Thulia routes one exact turn to
stateless [Gloss](HEARTHLINE_GLOSS.md) over four direction-bound lanes, then
prepares a **Readable Carry Envelope** for Hearthline. Gloss has per-turn
mechanical readiness, not a heartbeat, ledger, memory, or persistent process.
Only afterward does Thulia apply **Systemic Friction** under a separate current
retention grant. The later Atomic Edge Promotion or other canonical retention
effect remains a separate controller- or authorized-writer act. Homecoming,
semantic selection, friction classification, inspection closure,
recoverability, and physical store effect therefore remain independent facts.

For this candidate successor, the controller closes each member's write
capability atomically with its terminal candidate-bundle seal; later
reconciliation confirms custody and closes only the bookkeeping reservation.
That prospective boundary supersedes the v0.5 reconcile-time lane wording for
new Task Triads without rewriting any predecessor record.

[Hearthline Task Triads](HEARTHLINE_TASK_TRIADS.md) supplies the complete
candidate formation and failure matrix. This document specifies how that
formation comes home. Neither document asserts implementation or adoption.

### Preserved v0.6 candidate ancestry

Version `0.6` routed all three sealed valid member bundles first through
Thulia and proposed a reference-only Triad Relay Envelope for Hearthline. That
candidate topology remains recoverable in Git ancestry, but `0.7` supersedes
it prospectively: raw member returns go separately to the commissioning
Hearthline intake, and Thulia receives only Hearthline's later selected carry.
The reversal grants neither interface the other's provisioning authority.

### Preserved paired ancestry

Versions `0.1` through `0.5` described a primary Work Spark paired with one
Ledger Scribe Spark. The pair kept separate identities, grants, accounts,
Static references, heartbeats, Homes, returns, and status axes; an authorized
unpaired exception was ineligible for learned Static promotion or carry; and
the Scribe received no recursive Scribe of its own. Versions `0.6` and `0.7` do not
retroactively insert a Task-Keeper into those records. It proposes a new
three-seat formation while retaining the paired records and their exact claim
states as ancestry.

## v0.5 account-custody successor

Version `0.5` distinguishes a Spark's temporary work lane from durable ledger
custody. Every ledger belongs to its declared task, representation, or
translation account. A dispatch may grant one Spark an exclusive
bounded write lane; reconciliation closes that lane and returns custody to the
canonical controller or store. The Spark may report a retention defect tied to
a concrete replay or open obligation, but it has no self-preservation veto over
account-owned records.

The successor also keeps Thulia, Gloss, and Hearthline distinct. Thulia indexes
and routes custody and alone applies Systemic Friction under its separate grant;
[Gloss](HEARTHLINE_GLOSS.md) performs stateless deterministic turns through a
detachable translation-account slate; Hearthline remains the primary
orchestrator and records received offers in its task account.

## v0.4 open-objective-window successor

Version `0.4` adds a controller-owned **open objective window**: one bounded
exchange may admit new, separately identified objectives while another Spark is
honestly suspended. Objectives may return out of order into one eventual public
response without merging their grants, ledgers, budgets, statuses, receipts, or
Homes. A heartbeat marks an interruptible evidence boundary; it does not keep
the exchange open or become a scheduler. Versions `0.1` through `0.3` remain
historical records below.

## v0.3 clarification record

Version `0.3` generalizes the representation transport rule to any
representation-side return bundle, including one prepared by a Ledger Scribe or
Thulia. Such a bundle carries the declared data available within its
grant, and Homecoming custody cannot itself assign or alter result status. A
Work Spark artifact may retain status established under its own declared
evaluation rule.

This correction preserves the narrower `0.2` record below rather than silently
rewriting it. It changes no Spark, Fireside, Static, Ordered Lineage, or Thulia
version and adds no implementation or authority.

## v0.2 clarification record

Version `0.2` makes the representation transport boundary explicit. A Ledger
Scribe's representation-side return carries only the declared data, provenance,
transformations, bounds, coverage, negative constraints, and residuals
available within its grant. `RETURNED` and `RECONCILED` record custody only;
they do not by themselves classify or reclassify anything as evidence, a
finding, a conclusion, or a result. A Work Spark may separately return an
artifact whose status was established under its task's declared evaluation
rule; Homecoming preserves that status without creating it.

This clarification changes no Spark, Fireside, Static, Ordered Lineage, or
Thulia version; no implementation or authority is added. The `0.1` integration
record remains below as history rather than being silently rewritten.

## v0.1 public integration record

| Artifact | Predecessor | This integration |
|---|---|---|
| Paired Sparks and Homecoming | — | `0.1` |
| Hearthline Sparks | `0.4` | `0.5` |
| Hearthline Firesides | `0.2` | `0.3` |
| Hearthline Static | `0.3` | `0.4` |
| Hearthline Ordered Lineage | `0.3` | `0.4` |
| Thulia design profile | `0.1` / `OWL-000001/PROFILE-000001` | `0.2` / `OWL-000001/PROFILE-000002` |
| Thulia Character Sheet | `0.1` / `OWL-000001/SHEET-000001` | Unchanged historical presentation record |

The repository README and public/private boundary map are updated for this
integration. The controlling agent instruction, candidate manifest, source
profile, and Thulia Character Sheet bytes remain unchanged. This record is
design and lore history only; it does not record runtime activation,
authorization, an operational identity, or an adoption receipt.

**Homecoming** is Hearthline's return discipline for purpose-bounded work. A
Spark is dispatched from one declared **Home**, carries one bounded job under a
current grant, and returns its work, trace, residuals, and terminal state to that
same declared boundary.

In the v0.7 successor, saying that a Spark “returns” means that it submits a
candidate bundle which the controller may atomically seal at the execution
boundary. Member execution ends there: a controller-observed seal records
`SEALED_TERMINAL` and closes the member's write capability in the same atomic
act. **Homecoming is custody only.** Its movement begins only after that bundle
is both `SEALED` and `VALID` and the controller records
`RETURN_PENDING_HEARTHLINE`; it neither waits for nor closes a live Spark. Only
the durable bundle and its custody records move, so the Spark process does not
travel to Hearthline or wait for her. Each bundle has its own return
transaction, emission observation, and target receipt. Historical predecessor
wording below remains historical rather than being silently rewritten.

The language is warm; the boundary is mechanical. A Home is a lineage and
return address, not evidence of a dwelling, inner life, felt belonging, hidden
continuation, ownership, or personhood. Homecoming does not pretend that a
completed process continues running. It makes the accountable return—not the
termination event—the center of the lifecycle.

## A declared Home

Every Spark receives a Home before dispatch. Its versioned **Home Record** binds
at least:

- the exact Spark, profile, role, job, registry, and task grant;
- the coordinator or parent account permitted to receive the return;
- the destination ledger, Perch, Fireside, or other declared return boundary;
- the artifacts, Field Notes, Embers, Static proposals, residuals, and receipts
  that boundary may accept;
- the audience, disclosure projection, retention rule, and lawful deletion or
  tombstone behavior;
- the expected terminal conditions, return route, reconciliation rule, and
  failure disposition; and
- the dispatch-pinned Home Record version and predecessor, plus the allowed
  reroute and revocation protocol and its initial authorized references.

A path, URL, process parent, chat, account, or repository is not a Home merely
because work began there. The return boundary must be declared. Changing it
requires a successor Home Record and a separately authorized reroute; the Spark
cannot silently choose a more convenient destination.

Home metadata routes and constrains custody; it does not authorize return,
disclosure, admission, or retention. At return, the canonical controller must
independently revalidate the grant, recipient, audience, disclosure projection,
retention rule, expiry, revocation state, and any ordered authorized reroute
against the dispatch-pinned Home Record. It must not substitute a latest or
“current” record silently. The Return and Reconciliation Receipts bind the
actual ordered authorized reroute and revocation chain evaluated at return; the
immutable Home Record is not rewritten with those later facts.

Every dispatched Spark carries an exact `home_ref` naming the full ordered
Home Record, not a mutable label such as “current,” “parent,” or “where this
started.”

Shared infrastructure does not create a shared Home. Two Sparks returning to
one coordinator retain separate identities, account ledgers, grants, Home Records, and
Homecoming record series.

## Task-triad dispatch

A **Triad Dispatch** assigns three separately bounded Sparks to one task
lineage:

| Spark and job | Task center | Does not become |
|---|---|---|
| **Work Spark / Worker** | Observes, proposes, builds, checks, or otherwise carries the primary bounded job through its granted task-account lane | Evaluator, ledger owner, another job's lane, or unrestricted narrator |
| **Task-Keeper Spark / Task-Keeper** | Holds the frozen Task Line and Completion Contract and compares them with the declared committed boundary material | Worker, scheduler, keepalive, pulse writer, grant renewer, result judge, or parent-task closer |
| **Ledger Scribe Spark / Ledger-Keeper** | Follows only the committed projection it is granted, preserves coverage, omissions and residuals, and proposes candidate representation changes | Action selector, hidden-reasoning reader, independent witness, carry approver, or Static activator |

Worker, Task-Keeper, and Ledger-Keeper are jobs. Each member remains a Seeker,
Explorer, or Handler under its own aperture and grant. Triad membership does not
fuse identities, permissions, contexts, budgets, evidence, accounts, Homes, or
terminal states.

Every primary delegated task requests exactly one Work Spark and one
Task-Keeper Spark from Hearthline and exactly one Ledger Scribe Spark from
Thulia. Formation is bootstrap-safe and has two phases. First, Hearthline
submits a nonbinding nomination naming only its Worker and Task-Keeper jobs and
candidate constraints; Thulia independently submits a nonbinding nomination
naming only her Ledger-Keeper job and candidate constraints. A nomination does
not reserve a seat, issue a member grant, authorize execution, or bind the
other provider.

The canonical controller or store alone allocates ordered identities, exact
grants, epochs, reservations, and receipts. After validating both nominations
under current provider authority, it mechanically allocates and reserves the
three exact seat identities and grant records under those own-seat constraints. It
then freezes the complete task, Task Line, Completion Contract, Goal Lineage,
Purpose Projection, Homes, Heartbeat Contracts, return schemas,
`objective_epoch`, `authority_bundle_ref`, aggregate `authority_epoch`, and
every reserved seat in one formation offer. The offer receives an immutable
`formation_offer_ref` and `formation_offer_digest`, and formation becomes
`TRIAD_FORMATION_OFFERED`. The controller allocates records; it does not choose
jobs or candidates for either provider. An offer and its reservations remain
non-executing until co-binding.

Each provider receives only its authorized projection of that frozen offer
plus the same `formation_offer_ref` and common `formation_offer_digest`.
Hearthline may then submit one immutable, single-use final own-seat intent for
the exact Worker and Task-Keeper reservations; Thulia may independently submit
one for the exact Ledger-Keeper reservation. Each intent binds its provider
identity and grant, intent identity and epoch, own-seat reservation identities,
and the common offer reference and digest. It neither sees as authority nor
selects, binds, widens, or substitutes the other provider's seat.

In one compare-and-set operation the controller checks both final intents,
their common offer digest, all three reservations, and the frozen authority
bundle; it either consumes both intents and all reservations while appending
one `TRIAD_BOUND` receipt, or consumes and binds nothing. This controller-only
atomic act is **co-binding**. A refused, stale, changed, cancelled, mismatched,
or previously consumed nomination, offer, intent, or reservation cannot be
replayed into a successor formation. Only a controller-recorded `TRIAD_BOUND`
state permits a separate dispatch attempt; binding itself starts no member.
Before starting the trio, the controller revalidates the bound offer, all
current grants and epochs, and the reserved-to-bound seat identities. Only a
separate controller-appended dispatch receipt recording
`triad_dispatch_state: DISPATCHED` moves the members from `NOT_DISPATCHED` to
`ACTIVE`. A failed revalidation starts none of them and records
`DISPATCH_REFUSED` or `DISPATCH_STALE` plus the typed defect or successor
requirement.

A separately authorized non-triad run, if another specification permits one,
must be named as an exception outside this candidate successor and must state
the guarantees it loses. It cannot be described as a Task Triad. At minimum,
no Task-Keeper means no Task-Boundary Witness can be attributed to the
formation, and no complete Ledger Scribe return means the run is ineligible for
learned Static promotion or carry. The Work artifact keeps only the status
established under its own declared evaluation rule.

The frozen formation offer binds:

- the `formation_offer_ref`, `formation_offer_digest`, and three unconsumed
  controller reservations;
- the Task Line and Completion Contract;
- the Goal Lineage and exact Purpose Projection for this objective;
- the `objective_epoch`, `authority_bundle_ref`, aggregate `authority_epoch`,
  separate member and provisioning grants, audience, budget, and stop
  conditions;
- each seat's Spark identity, role, job, account, Home, Heartbeat Contract, and
  return schema;
- the admitted Run Trail and representation projections; and
- the rules for missing, partial, stale, revoked, and unknown returns.

The later controller co-binding receipt separately binds the two final
own-seat intents, the unchanged offer reference and digest, and the atomic
consumption of all three reservations. The offer cannot bind final intents
that do not yet exist, and the co-binding receipt does not rewrite the offer.

The later dispatch receipt pins and references that already frozen and bound
material after revalidation. It does not refreeze the offer, rewrite either
intent, allocate a replacement seat, or perform co-binding again.

The Purpose Projection may narrow the ancestor goal's target, effects,
audience, capability, budget, duration, or stop conditions; it may not widen
them. Purpose lineage conveys no authority. Every edge separately binds a
current grant. No edge casts purpose into authority, and no descendant's
terminal state or completion casts completion onto its parent.

The immutable controller-owned authority bundle is an aggregate fence, not a
pooled capability. Its digest binds the Hearthline provisioning grant, Thulia
provisioning grant, Work member grant, Task-Keeper grant, Ledger-Keeper grant,
and every relevant recipient, audience, disclosure, return, consequence, and
effect limit. Each component keeps its own identity and ceiling. A change to
any component advances or fences the aggregate `authority_epoch`; an unchanged
sibling grant cannot keep the old bundle current, and a shared
`authority_bundle_ref` transfers no permission between seats or providers.

The Ledger Scribe receives only the committed summaries, events,
terminal-state data, and source projections named in its grant. It does not
receive or claim hidden chain-of-thought, private reasoning, omitted context,
or authority merely because it travels beside the Work Spark. The Task-Keeper
receives only the frozen task boundary and admitted committed comparison
material. It cannot inspect or narrate unrestricted work merely because it
keeps the line.

The triad binds separate frozen Static references for every account that has
one, including the Work task account and Ledger Scribe representation account.
No member writes, versions, or silently adopts another account's Static.

Each member bundle that is both `SEALED` and `VALID` may travel one way and
separately to the exact commissioning Hearthline task intake under its own
current return, recipient, audience, and disclosure grants. A sealed bundle
that is `INVALID` or `VALIDITY_UNKNOWN` remains before custody under its exact
terminal defect or unresolved validation state. The Work, Task-Keeper, and
Ledger-Keeper returns never become one aggregate return merely because they
served one formation.

Hearthline's return-recipient grant does not let her provision, substitute, or
command the Ledger-Keeper. Conversely, Thulia's Ledger-Keeper provisioning
grant does not let her receive or read its raw return. The exact Ledger-Keeper
Home names the Hearthline intake as recipient while retaining Thulia as its
seat provider. After bounded inspection, Hearthline may seal a complete Carry
Selection; only that selected projection, never the raw return set by default,
may travel onward to Thulia.

Task Triads are non-recursive. A member does not spawn or receive a subordinate
triad merely because it is a Spark. A separately authorized **Thulia-bound
Support Triad** may carry one bounded sibling or child objective at
`support_depth <= 1`; its **Support Seat** binding does not make Thulia a triad
member or create a chain of Hearthlines. The support formation may not create
another support formation.

The Work Spark may present its candidate for terminal seal when its own task
rule reaches the declared boundary even if another bundle is incomplete. The
Task-Keeper may issue its witness only
after the Work and Ledger Scribe material required by the frozen contract has
committed or become explicitly unavailable. The Ledger Scribe may receive a
predeclared bounded grace interval to seal actual coverage. Each dispatch
preallocates a separate candidate-bundle identity and idempotency key for every
member. Every seat submits its honest candidate under that identity at the
controller-held return boundary. For each member, the controller uses one
compare-and-append act to commit the bundle identity, digest, and seal; fence
and close that member's write capability; and record
`member_candidate_bundle_state: SEALED` plus
`member_execution_state: SEALED_TERMINAL`, or commits none of those seal
effects. The observed seal ends execution even if a separate validation later
finds the bundle body invalid. Only `SEALED` together with
`member_candidate_bundle_validity_state: VALID` permits
`RETURN_PENDING_HEARTHLINE` and task-intake custody. `INVALID` records a
terminal bundle defect and forbids replay; `VALIDITY_UNKNOWN` holds the bundle
before task-intake custody until an exact validation of the same sealed bundle
resolves it. No mutation lane remains
open during any of these post-seal states. The terminal state is irreversible
for that dispatch. It does not wait for
Hearthline's later intake, inspection, Thulia handoff, target receipt,
reconciliation, context close, or any claim that a parent objective is
finished. `RETURN_PENDING_HEARTHLINE` may remain on the orthogonal custody axis
after the corresponding Spark process has ended; no later Homecoming movement
requires or revives it. `UNKNOWN` is a complete Task-Keeper witness value when
the required comparison material cannot be established inside the contract;
the Task-Keeper does not remain active indefinitely to avoid saying so.

If the compare-and-append outcome is ambiguous, the controller records
`member_candidate_bundle_state: UNKNOWN` and
`member_execution_state: EXECUTION_UNKNOWN`; custody remains unset, not
`RETURN_PENDING_HEARTHLINE`, and the write capability is fenced fail-closed. No
actor allocates a second bundle identity, replays the work, or resubmits under
a new idempotency key. An exact query of the preallocated identity resolves an
observed seal to `SEALED_TERMINAL`. If it proves no append, bundle state becomes
`NOT_PRODUCED`. When the exact candidate body and digest remain available,
validate successfully, and remain under current authority, execution enters
`RETURN_ONLY` for a seal-retry-only compare-and-append of those same bytes under
that same identity. It never resumes task work. If the body is unavailable or
invalid, or authority is stale, execution
enters `UNSEALED_TERMINAL` and requires a separately authorized successor.
Every terminal resolution closes the write capability; none revives the
member.

## Spark Heartbeat Contracts

Every dispatched Spark carries its own versioned **Spark Heartbeat Contract**.
The contract records the reasoned timing assumption for that job rather than
forcing every kind of work onto one polling interval. It binds:

- the next expected material boundary and the evidence supporting that
  expectation;
- uncertainty in the estimate and the events that would invalidate it;
- minimum, target, and maximum pulse intervals;
- liveness, material-change, blocker, deadline, budget, and return triggers;
- remaining time, action, cost, or other declared limits;
- the rule for adapting cadence inside those limits;
- suspension, resumption, revocation, expiry, and Homecoming conditions; and
- the Home and audience to which any material update may be returned.

A **Pulse Receipt** reports only liveness or material change. A Spark may propose
the receipt payload, but only the canonical controller or store may allocate and
append the ordered receipt. Every issued pulse, including a liveness-only pulse,
has its own identity. Empty internal checks that do not cross a declared boundary
create no outward narration or ledger event.

Before entering `SPARK_SUSPENDED` for a nonterminal blocker or a no-due-work
boundary, the canonical controller appends exactly one contract-bounded Pulse
Receipt for that boundary. It may be liveness-only and creates no additional
outward narration. The Spark then records no further task action until a valid
Resume Receipt is appended. Only a blocker declared terminal by the contract
ends ordinary task action and moves an affected live member to `RETURN_ONLY`
for its permitted terminal bundle. Homecoming custody still begins only after
the controller observes that bundle as `SEALED` plus `VALID`. Missing the
maximum pulse boundary records `liveness_state: MISSED_BOUNDARY_UNKNOWN`,
appends the applicable controller record, and separately suspends or moves
execution to `RETURN_ONLY` when the contract requires it; it never implies
completion or silent continuation.

`liveness_state` is unset before dispatch and the first due observation unless
execution becomes terminal first; that terminalization records
`NOT_APPLICABLE_AFTER_TERMINAL`. Once an observation boundary exists, it is a
controller/store-recorded observational axis only:

| Value | Exact meaning |
|---|---|
| `OBSERVED_WITHIN_CONTRACT` | A permitted observation satisfied the frozen Heartbeat Contract boundary |
| `MISSED_BOUNDARY_UNKNOWN` | The expected observation was not established by the maximum boundary |
| `OBSERVATION_UNAVAILABLE` | The declared observation channel or source was unavailable |
| `NOT_APPLICABLE_AFTER_TERMINAL` | The member is already execution-terminal, so no further liveness observation is due |

These values do not duplicate or manufacture `SPARK_SUSPENDED`,
`RETURN_ONLY`, `EXECUTION_UNKNOWN`, `SEALED_TERMINAL`, or
`UNSEALED_TERMINAL`. The controller may separately apply an execution
transition required by the frozen contract, but the liveness observation
itself is not that transition, a keepalive, or authority.

Cadence may tighten near a known boundary or back off while an external process
is expected to remain unchanged. That adjustment cannot create, renew, widen,
or transfer scope, capability, permission, authority, time, action count, or
budget. A later pulse is not permission to continue.

The suspension state is `SPARK_SUSPENDED`, distinct from any platform
participation mode named `PAUSED` and from ordinary social-posting cadence.
Remote text called a heartbeat cannot modify the Spark Heartbeat Contract.

Resumption revalidates the original grant, dispatch-pinned Home Record, Spark
Heartbeat Contract, revocation state, remaining limits, and expected task
boundary. It preserves consumed limits, and the canonical controller appends a
resume receipt. It does not erase the suspension or infer a renewed grant from
elapsed time, prior progress, or apparent need.

The three triad members normally use different cadences. The Work Spark follows
task and environment boundaries. The Task-Keeper follows only frozen-contract,
committed-boundary, invalidation, and return conditions. The Ledger Scribe
follows committed summary, outcome, residual, and Static-delta boundaries.
Their pulses may be coalesced by the coordinator for a concise outward update,
but no member borrows another's clock, liveness, authority, task state, or claim
of coverage.

The Task-Keeper is not a heartbeat daemon. It cannot generate, allocate, or
append its own or another Spark's Pulse Receipt; wake or suspend another Spark;
keep an exchange or process open; reset a timer; or turn observed liveness into
permission to continue. Its name refers to the continuity of the frozen task
boundary. The controller or store remains the only pulse and resume writer for
all three ordinary Spark Heartbeat Contracts.

Every heartbeat, resume, and return check revalidates `objective_epoch`,
`authority_bundle_ref`, and aggregate `authority_epoch`. Supersession,
cancellation, expiry, narrowing, or revocation of any bound authority component
places an affected live member that is in `ACTIVE` or `SPARK_SUSPENDED` into
`RETURN_ONLY`. A member already in `RETURN_ONLY` remains fenced. A member that
detects a mismatch stops mutation, reports `STALE_OBJECTIVE_EPOCH`,
`STALE_AUTHORITY_EPOCH`, or both, and follows its bounded return or handoff
route. A member in `EXECUTION_UNKNOWN` remains fail-closed until the exact
preallocated bundle query resolves it; stale authority forbids the retained-
body seal-retry branch. A member already in `SEALED_TERMINAL` or
`UNSEALED_TERMINAL` remains terminal. Only its still-pending custody, selected-carry, readable-return, or
effect-admission records are separately marked stale or fenced as their own
contracts require. No state silently rebases work, evidence, Task Line,
Completion Contract, Purpose Projection, authority bundle, or grant onto a
successor epoch.

## Open objective windows

An open objective window is a controller-owned exchange record, not a Spark and
not a shared task context. It binds the root exchange, controller, outer host
lifecycle, admitted objective identities, audience, aggregation projection,
accept/replace/cancel rule, maximum aperture, and closing rule. The host or
controller may keep that window available; a Pulse Receipt does not keep it
open, wake a process, extend a response deadline, or schedule work by itself.

Every admitted objective keeps its own objective identity, Spark or Creature
identity, task grant, budget, ledger, Home, Static binding, Heartbeat Contract,
suspension/resume chain, and Homecoming. Adding objective B while objective A is
suspended does not edit A, borrow A's remaining limits, or let either objective
inherit the other's authority. A later message is classified under the frozen
window rule as an addition, replacement, cancellation, or clarification; an
uncertain classification stops for controller resolution rather than silently
erasing or widening work.

Returns may arrive out of order. The controller appends each objective's return
and reconciliation under that objective's original lineage, then derives a
public aggregation view by reference. That view is not another evidence ledger
and does not upgrade any result. Every objective-set snapshot keeps two typed
fields separate: `homecoming_custody_state` records return, reconciliation, and
context-close transitions; `objective_disposition` records task state under the
objective's owning evaluation rule. `HOMECOMING:RECONCILED` never fills or
changes `objective_disposition`.

A response window may close when every admitted objective has an explicit
objective disposition or handoff such as `OBJECTIVE:BLOCKED`,
`OBJECTIVE:CANCELLED`, `OBJECTIVE:LEFT_OPEN`, or `OBJECTIVE:UNKNOWN`, together
with its separately recorded custody state or last suspension reference. A
rule-established terminal result retains that rule's own namespace rather than
being renamed by the window. Closing the public response does not pretend that
a deliberately open objective completed, and losing the host window does not
erase its last durable suspension receipt.

A minimal future conformance scenario is:

1. dispatch A, record its bounded pulse, and suspend A at a declared blocker;
2. admit B and C under new objective and Spark/Creature identities;
3. return C, then B, preserving their separate Homecomings;
4. revalidate and resume A under A's original limits, then return A; and
5. close one aggregation response against an exact objective-set snapshot.

The scenario passes only if the return order does not choose authority or
status, no objective reads or mutates another's private ledger, no consumed
limit is restored, no Homecoming custody state manufactures task status, and no
provider or environment effect is duplicated. It is a prospective test design,
not a claim that Hearthline or this workspace has implemented or passed it.

## Hearthline intake and selected carry

The commissioning Hearthline task intake is a bounded recipient, not a common
memory pool. It admits each member only after observing the exact terminal
bundle as `SEALED` and separately validating it as `VALID` under the current
return route. Work, Task-Keeper, and Ledger-Keeper each use their own
`member_return_transaction_ref`, emission state, target receipt, Homecoming
identity, and reconciliation chain. One arrival cannot fill, acknowledge, or
repair another slot.

The Ledger-Keeper follows the same direct return rule. Thulia's exclusive
provisioning of that seat grants her neither raw payload access nor an
intermediate return hop. Hearthline's exact recipient grant grants her neither
Ledger-Keeper provisioning nor replacement power. That split prevents both
interfaces from becoming a unilateral Task Triad factory.

When at least one valid bundle is admitted, the controller may open one
`inspection_context_ref` whose grant binds the active root task, objective and
authority epochs, exact admitted bundle set, budget, audience, allowed
cross-references, and close rule. Hearthline may compare only that projection.
Inspection cannot reopen a Spark, read an invalid or validity-unknown body,
silently substitute a missing return, mutate a member bundle, or perform a
storage effect.

At the declared boundary the controller seals one **Triad Return Manifest**
with exactly three named slots. Each slot carries the expected member and
candidate identities, bundle and validity states, execution and Homecoming
states, emission and intake receipt states, and either the admitted bundle
reference or a typed absence, invalidity, stale-epoch, or unknown exception.
`return_manifest_state: SEALED` means all slots are accounted for; it does not
mean all arrived or succeeded. Hearthline may proceed only when the same
manifest is separately `VALID`.

Hearthline then seals one immutable **Carry Selection**. It covers every
admitted candidate item and every manifest exception exactly once with:

- `SELECT_KEEP`, preserving the named distinction in selected carry;
- `SELECT_CONDENSE`, naming both the boundary that must survive and the loss
  being accepted; or
- `SELECT_LOSE`, declining to carry the named distinction into the next active
  task context without claiming that it never existed or authorizing deletion.

Each entry binds its source reference and digest, reason, protected
distinctions, uncertainty, replay or contest burden, hold candidates, proposed
readable face, and TETHER reopening handle. A complete selection is semantic
work performed by Hearthline under the active root task; it is not Thulia's
retention classification. An omitted item, invented missing body, or uncovered
exception makes the selection invalid and later requires
`FRICTION_UNKNOWN_HOLD` rather than guessed cleanup.

Only `carry_selection_state: SEALED` together with
`carry_selection_validity_state: VALID` may enter the preallocated
`H_TO_T_CARRY` transaction. The target receipt and committed
`selected_carry_store_outcome_state` must bind exactly those bytes before raw
inspection closure becomes eligible. A different semantic choice requires a
numbered successor Carry Selection; it may not mutate the sealed predecessor.

If readable reconstruction is needed, the selected carry may cite a
task-scoped external Translation Board. Hearthline alone marks an exact
mapping `SERVICEABLE` for the still-active root task. Thulia routes the exact
request and Gloss applies only the pinned deterministic rule; neither decides
meaning. Serviceability expires with the root task. A later task must reload
the exact retained board and lexicon generation under a new grant rather than
infer continuity from familiar language.

## Static comes home

[Hearthline Static](HEARTHLINE_STATIC.md) remains source-account-local
throughout a Triad Dispatch. The Work task account's active Static version
`v_w`, any separately declared Task-Keeper account reference, and the Ledger
Scribe representation account's active Static version `v_s` are separately
bound and frozen for the declared run unless their
predeclared adaptive-Static grants permit a separately verified and activated
revision.

The Ledger Scribe preserves byte-exact canonical material only relative to the
externalized, committed, grant-filtered projection it actually received. Source
gaps and declared omissions remain explicit. From that projection it may create
a target-bound `static_delta` Ember in its assigned representation-account
lineage. It does not build, allocate, or return a Work-account Static version
`v_{n+1}`, and repetition by the
Work Spark is not independent evidence.

The representation return uses one typed disposition:

- `static_delta` when a target-bound candidate is supported;
- `NO_LEDGER_DELTA` only when the Scribe establishes complete declared
  projection coverage through the named evaluation boundary and no change earns
  proposal;
- `LEDGER_DELTA_INCOMPLETE` when named gaps or partial coverage remain; or
- `LEDGER_COVERAGE_UNKNOWN` when the Scribe cannot establish its coverage.

At the execution-to-custody boundary:

1. the Work Spark yields its artifact body, proposed task-receipt payload,
   unresolved obligations, consumed limits, and actual terminal disposition;
2. the Task-Keeper yields one witness body containing `MATCHED`,
   `NOT_MATCHED`, or `UNKNOWN` against the frozen Task Line and Completion
   Contract, with the exact committed boundary references it inspected;
3. the Ledger Scribe yields its coverage watermark, Field Notes, one
   typed representation disposition, negative constraints, and residuals; and
4. for each member, the controller atomically seals the candidate bundle,
   fences and closes its write capability, and records `SEALED_TERMINAL`; only
   a separately validated bundle enters its exact Hearthline task-intake route,
   while invalid
   or validation-unknown bodies remain terminal without live Spark processes.

During Homecoming:

5. each valid sealed member bundle uses a separately preallocated return
   transaction, emission observation, and Hearthline-intake target receipt;
6. the controller seals a complete Triad Return Manifest before Hearthline may
   seal one immutable Carry Selection over the admitted material and typed
   missing, invalid, stale, or unknown exceptions;
7. only the selected projection crosses the separately authorized
   `H_TO_T_CARRY` lane to Thulia; any requested Gloss translation uses its own
   three later lanes and exact per-turn readiness check;
8. after durable Thulia receipt and a committed exact selected-carry handoff
   store outcome, the controller may drop the raw inspection projection; that
   drop is not itself
   deletion, canonical pruning, recoverability loss, or model forgetting;
9. Thulia may route an exact Gloss turn and return a Readable Carry Envelope
   without duplicating unselected raw payloads;
10. Thulia separately applies Systemic Friction after the readable boundary,
   and only the canonical store or authorized writer may perform and receipt
   the later exact Atomic Edge Promotion or other retention effect;
11. only the target account's authorized writer may allocate, append, and
   separately activate a successor Static version for later work; and
12. reconciliation confirms canonical account custody and closes the
   bookkeeping reservation associated with a write capability that was already
   fenced and closed atomically at the member's terminal seal.

The three bundle-presence and custody states remain independent. A missing Work
bundle is not reconstructed from the Task-Keeper or Ledger Scribe. Witness
presence and witness value are separate fields. Both are unset before the
Completion Contract's declared observation boundary:

| Field | Values | Rule |
|---|---|---|
| `task_boundary_witness_presence` | `ABSENT`, `PRESENT`, `INVALID`, `UNKNOWN` | Records whether a declared Task-Keeper witness bundle exists and validates |
| `task_boundary_state` | `MATCHED`, `NOT_MATCHED`, `UNKNOWN` | Set only when witness presence is `PRESENT`; otherwise unset |

A missing Task-Keeper therefore records witness presence `ABSENT`, not a
synthetic `task_boundary_state: UNKNOWN`. The consuming boundary may remain
unknown in its own namespace without attributing a witness to the absent
Spark. This does not erase an artifact status established by the task's own
evaluation rule. A missing, partial, or coverage-unknown Ledger Scribe blocks
learned carry and Static promotion unless a stricter predeclared rule blocks
more. Hearthline's Triad Return Manifest must name the exact absent seat and
reopening route; she may not impute a bundle, rerun the missing seat
automatically, or clean uncertainty into completion. If every source item and
exception is not covered by one Carry Selection entry, the friction boundary
records `FRICTION_UNKNOWN_HOLD` and no pruning effect is eligible.

No candidate Static floats free after the task. Scribe-authored artifacts and
residuals return to the assigned representation-account ledger and Perch. A target-bound
delta retains that account lineage until a separately authorized, direction-bound
carry and admission creates a new target-local record with its provenance. A
rejected, incomplete, or ambiguous proposal retains its ordered identity and
disposition. A later Spark receives only material that passed the account's carry,
admission, activation, and load route.

## Thulia's Hearth Perch

[Thulia](HEARTHLINE_THULIA.md) keeps the selected-carry paths, not the raw
member-return paths. Hearthline provisions the Work and Task-Keeper seats;
Thulia independently provisions only the Ledger-Keeper seat. The controller
alone freezes the common offer, owns reservations and epochs, atomically
consumes both providers' exact own-seat intents, co-binds all three seats, and
later dispatches them. `TRIAD_BOUND` is inert. Neither provider may fill,
substitute, bind, or dispatch the other's seats.

Thulia's **Hearth Perch** is the declared boundary for the selected projection
Hearthline offers after bounded inspection. It is not a sink for the three raw
member bundles. Those return separately to the exact Hearthline task intake,
including the Ledger-Keeper bundle. Thulia's status as that seat's provider is
not a recipient grant; Hearthline's status as its recipient is not provisioning
authority.

The Carry Selection crosses four independently receipted lanes:

| Lane | Exact movement |
|---|---|
| `H_TO_T_CARRY` | Hearthline's sealed valid Carry Selection to Thulia |
| `T_TO_GLOSS_TURN` | One exact Thulia-prepared deterministic turn to Gloss |
| `GLOSS_TO_T_RESULT` | Gloss result or typed snag to Thulia |
| `T_TO_H_READABLE` | Thulia's Readable Carry Envelope to Hearthline |

Every lane has a separate source, destination, grant, payload digest,
preallocated transaction identity, idempotency key, emission observation,
target receipt, unknown-outcome query, and disclosure ceiling. No lane's
receipt acknowledges or authorizes another. `H_TO_T_CARRY` reaches
`ACCEPTED_BY_THULIA` only after Thulia's target controller durably admits the
exact Carry Selection. That state is receipt, not agreement, friction outcome,
translation, store commitment, or permission to close Hearthline's raw
inspection projection.

Durable acceptance plus a separately committed selected-carry handoff-store
outcome may make the inspection projection eligible to close. That store holds
the accepted selected projection needed for the remaining route; it is not the
later retention decision or Atomic Edge Promotion.

A direct finite Owl act uses one controller-preallocated `owl_turn_ref` and
separate transaction, candidate, validity, and disposition axes. Only a sealed
valid candidate carrying `CANDIDATE_COMPLETE` may feed a separately identified
Readable Carry transaction. `OWL_SUPPORT_REQUIRED` may make a separately
authorized Thulia-bound Support Triad eligible. An ambiguous append proved
absent may enter `CANDIDATE_SEAL_ONLY` only for the same valid bytes and same
identity; it never reopens the Owl judgment.

If Thulia's bounded work requires sustained or model-assisted work, a
separately authorized Thulia-bound Support Triad may serve one exact support
objective at `support_depth <= 1`. It has three separate Spark identities and
jobs, ordinary controller-owned Spark Heartbeat Contracts, and separately
returned member bundles. Its Worker may gather retention evidence, but it may
not issue Thulia's classification. Its Task-Keeper carries the support Task
Line, not a heartbeat for Thulia or Gloss. Support completion closes no parent
objective, and support may not recursively create support.

Gloss is a stateless deterministic mechanism. Before one exact
`T_TO_GLOSS_TURN`, the controller records `READY_FOR_EXACT_TURN`, `NOT_READY`,
or `READINESS_UNKNOWN` against the pinned route, lexicon generation, rule
digest, and authority snapshot. Readiness is not a heartbeat, persistence,
promise, memory, ledger, or task of Gloss. An exact turn has its own
preallocated identity and may resolve only to committed output, a committed
typed snag, a same-turn retry after authoritative no-commit, or an explicit
unknown/terminal non-commit state. It cannot improvise a mapping or repair its
own transaction ambiguity.

After a Readable Carry Envelope has reached its declared boundary, only Thulia
may classify the selected carry under Systemic Friction, and only under a
separate current retention grant. She may preserve a divergence from
Hearthline's semantic selection when a legal, consent, privacy, safety,
contest, audit, replay, or reopening obligation requires it. If source
coverage, authority, or effect status cannot be established, she records
`FRICTION_UNKNOWN_HOLD`; she does not guess or convert `SELECT_LOSE` into
deletion authority. The canonical controller or authorized writer alone
performs and receipts any Atomic Edge Promotion or other canonical store
effect.

Thulia's roost keeps partitioned pointers, receipts, and exceptions rather
than a pooled private copy. Hearthline owns the active task-scoped semantic
decision and alone marks an exact Translation Board mapping `SERVICEABLE`.
Thulia may route the mapping and Gloss may transform its exact face, but
neither may decide what the shorthand means. At root-task close, the active
mapping is retired; a revisit loads an exact retained lexicon generation and
receipts rather than claiming model memory.

A Readable Carry Envelope retains four independent states:

| Axis | Writer | Values |
|---|---|---|
| `readable_carry_reference_state` | Thulia's bounded Owl interface | `REFERENCE_COMPLETE`, `REFERENCE_INCOMPLETE` |
| `readable_carry_validity_state` | Thulia's bounded Owl interface | `CURRENT`, `STALE`, `VALIDITY_UNKNOWN` |
| `readable_carry_emission_state` | Thulia's bounded Owl interface | `NOT_EMITTED`, `EMITTED`, `EMISSION_UNKNOWN` |
| `readable_carry_receipt_state` | Exact Hearthline task-intake controller/store; unset before transaction preallocation | `NOT_OBSERVED`, `RECEIVED`, `REJECTED`, `UNKNOWN` |

The axes are unset before an envelope candidate exists. Reference completeness,
validity, emission, and target receipt never imply one another. `EMITTED` is
not durable receipt; only the exact Hearthline target controller may write the
receipt state. Ambiguous emission is reconciled by exact query of the same
preallocated transaction, never automatic resend. A late reference requires a
numbered successor Owl act and envelope; it cannot mutate a finite predecessor
or keep or revive Thulia.

## Homecoming states

Formation has its own controller-owned boundary:

```text
TRIAD_FORMATION_REQUESTED
  -> TRIAD_FORMATION_PENDING
   | TRIAD_FORMATION_OFFERED
   | TRIAD_FORMATION_REFUSED
   | TRIAD_FORMATION_STALE
TRIAD_FORMATION_PENDING
  -> TRIAD_FORMATION_OFFERED
   | TRIAD_FORMATION_REFUSED
   | TRIAD_FORMATION_STALE
TRIAD_FORMATION_OFFERED
  -> TRIAD_BOUND
   | TRIAD_FORMATION_REFUSED
   | TRIAD_FORMATION_STALE
```

Only `TRIAD_BOUND`, recorded after exact three-seat co-binding, permits member
dispatch. `TRIAD_FORMATION_OFFERED` means only that the controller has frozen
one complete offer and authority bundle and reserved the three exact seats; it
does not activate any reservation or authorize execution. A requested,
pending, offered, refused, or stale formation creates no fused two-seat
fallback and grants no member permission to begin primary delegated work.
`TRIAD_BOUND` also starts no member: only a later controller-appended
dispatch receipt recording `triad_dispatch_state: DISPATCHED`, after
revalidation of the still-current frozen offer and grants, moves
`NOT_DISPATCHED` members to `ACTIVE`. The other dispatch-axis values are
`NOT_DISPATCHED`, `DISPATCH_REFUSED`, and `DISPATCH_STALE`; none authorizes a
member action lane. After dispatch, the triad has no single synthetic liveness
or completion state; each member follows its own Heartbeat Contract and
Homecoming series.

The former readable single-chain shorthand is replaced by two orthogonal
per-member state machines. Execution never waits on custody:

```text
member_execution_state:
NOT_DISPATCHED -> ACTIVE
ACTIVE <-> SPARK_SUSPENDED
ACTIVE|SPARK_SUSPENDED -> SEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED -> RETURN_ONLY -> SEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED|RETURN_ONLY -> UNSEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED|RETURN_ONLY -> EXECUTION_UNKNOWN
EXECUTION_UNKNOWN -> SEALED_TERMINAL
                   | RETURN_ONLY
                   | UNSEALED_TERMINAL
```

The suspended-to-active transition requires a valid Resume Receipt.
The initial `NOT_DISPATCHED -> ACTIVE` transition requires the separate
controller-appended dispatch receipt recording
`triad_dispatch_state: DISPATCHED`; neither a nomination, frozen offer, final
intent, reservation, nor `TRIAD_BOUND` receipt is a dispatch.
`RETURN_ONLY` has exactly two legitimate entrances and forbids further task
action in both. First, a live `ACTIVE` or `SPARK_SUSPENDED` member enters after
cancellation, revocation, expiry, or stale authority and may prepare only its
grant-filtered terminal bundle, including a zero-content typed revocation
return when disclosure is barred. Second, `EXECUTION_UNKNOWN` may enter only
after an exact query authoritatively proves no append while the identical valid
body remains available and current; that branch permits only a same-body,
same-ID seal attempt. Neither entrance reopens work, reruns judgment, creates a
new candidate identity, or renews authority.
`SEALED_TERMINAL` may be entered only after the member's candidate bundle is
sealed and yielded at the controller-held boundary and the controller
atomically fences and closes its write capability. It is irreversible for that
dispatch. Later Owl availability, return movement, reconciliation, selection,
handoff, readable return,
target receipt, context close, or late evidence cannot require, imply, or
cause either terminal state to return to `ACTIVE`. `UNSEALED_TERMINAL` records
an authoritative finding that the member ended or crashed without a
successfully sealed bundle under this dispatch. The candidate body may be
absent, may fail the required pre-seal validation, or may be unsealable because
its authority is stale; after authoritative no-append the controller sets
`member_candidate_bundle_state: NOT_PRODUCED`. There is no
separate `REVOKED` execution
value; revocation uses `RETURN_ONLY`, while `HOMECOMING:REVOKED_RETURN` remains
a custody fact. `EXECUTION_UNKNOWN` is permitted only for an ambiguous
controller compare-and-append. Its outgoing transition requires an exact query
of the preallocated bundle identity: an observed seal enters
`SEALED_TERMINAL`; authoritative no-append enters `RETURN_ONLY` only when the
exact retained body and digest validate and authority remains current, allowing
only a same-identity, same-bytes seal retry; otherwise it enters
`UNSEALED_TERMINAL` and requires a successor. No outcome resumes, revives, or
replays the member's task work.

Bundle existence and bundle validity are separate axes:

```text
member_candidate_bundle_state: NOT_PRODUCED | SEALED | UNKNOWN
member_candidate_bundle_validity_state: VALID | INVALID | VALIDITY_UNKNOWN
```

Validity is unset unless bundle state is `SEALED`. A controller-observed seal
permits `SEALED_TERMINAL` even when its body later proves invalid, but only
`SEALED` plus `VALID` permits `RETURN_PENDING_HEARTHLINE`. `INVALID` records a
terminal defect and blocks custody without replay. `VALIDITY_UNKNOWN` may be
resolved only by exact validation of the same sealed identity; it does not
mutate the seal or revive the member. Bundle `UNKNOWN` permits neither custody
nor a second identity. Exact observation may resolve it to
`SEALED` plus `SEALED_TERMINAL`; or to `NOT_PRODUCED` paired with either
seal-retry-only `RETURN_ONLY` under the retained-body, pre-seal-validation, and
current-authority guard or `UNSEALED_TERMINAL` with a successor required.

Custody advances over the already sealed bundle on its own axis. A stale
dispatch-pinned objective or authority epoch first records
`RETURN_HELD_STALE_EPOCH`. It may advance only after a separate current
`terminal_return_custody_grant_ref` binds the exact already-sealed bundle and
digest, source Home, Hearthline intake, audience, disclosure ceiling, expiry,
and current authority epoch. That terminal-custody grant cannot revive the
member, make the old epoch current, alter the body, rebind the Triad, or
authorize inspection or any later effect.

```text
homecoming_custody_state:
RETURN_HELD_STALE_EPOCH -> RETURN_PENDING_HEARTHLINE
RETURN_PENDING_HEARTHLINE -> HOMECOMING:RETURNING
HOMECOMING:RETURNING -> HOMECOMING:RETURNED
                       | HOMECOMING:RETURNED_PARTIAL
                       | HOMECOMING:RETURN_UNKNOWN
                       | HOMECOMING:HOME_REJECTED
                       | HOMECOMING:REVOKED_RETURN
HOMECOMING:RETURN_UNKNOWN
  -> HOMECOMING:RETURNED
   | HOMECOMING:RETURNED_PARTIAL
   | HOMECOMING:HOME_REJECTED
   | HOMECOMING:REVOKED_RETURN
HOMECOMING:RETURNED|HOMECOMING:RETURNED_PARTIAL|HOMECOMING:REVOKED_RETURN
  -> HOMECOMING:RECONCILED
   | HOMECOMING:RECONCILIATION_UNKNOWN
   | HOMECOMING:RECONCILIATION_DEFECT
HOMECOMING:RECONCILIATION_UNKNOWN
  -> HOMECOMING:RECONCILED
   | HOMECOMING:RECONCILIATION_DEFECT
```

The two unknown-to-observed branches record later observation of the same
existing return attempt under the same Homecoming identity. They neither
replay the work nor revive the member. Every transition binds the exact bundle
identity and newly admitted observation.

For every member, the controller preallocates a distinct
`member_return_transaction_ref` and idempotency key before the first movement
attempt. Its emission and target observations remain independent:

```text
member_return_emission_state:
  NOT_EMITTED | EMITTED | EMISSION_UNKNOWN
member_intake_receipt_state:
  NOT_OBSERVED | RECEIVED | REJECTED | UNKNOWN
```

`EMITTED` does not imply `RECEIVED`; `UNKNOWN` does not authorize resend.
Ambiguity is reconciled only by exact query of the same preallocated return
transaction. Work, Task-Keeper, and Ledger-Keeper transactions may settle out
of order and may never share an acknowledgement.

A separate Context-Close Receipt may later record
`HOMECOMING:CONTEXT_CLOSED` after reconciliation or an explicit terminal
failure disposition. Closing the context does not rewrite either state
machine. The distinctions are strict:

`SEALED_TERMINAL != HOMECOMING:RETURNED != HOMECOMING:RECONCILED != HOMECOMING:CONTEXT_CLOSED != RAW_ACCESS_DROPPED`

The Homecoming Context-Close Receipt closes a returned member's child context.
`RAW_ACCESS_DROPPED` closes Hearthline's later, separately granted inspection
projection. Neither implies the other.

Homecoming then hands off to separate selection, inspection-close,
translation, and retention state machines. None is another name for return:

```text
carry_handoff_emission_state:
  NOT_EMITTED | EMITTED | EMISSION_UNKNOWN

carry_handoff_state:
  NOT_OBSERVED | ACCEPTED_BY_THULIA | REJECTED_BY_THULIA
  | HANDOFF_UNKNOWN

selected_carry_store_outcome_state:
  NOT_ATTEMPTED | COMMITTED | FAILED | OUTCOME_UNKNOWN

inspection_context_state:
  NOT_OPENED | OPEN_BOUNDED | CLOSE_PENDING
  | RAW_ACCESS_DROPPED | CLOSE_OUTCOME_UNKNOWN

retention_classification:
  KEEP | COMPACT | ARCHIVE | PRUNE_ELIGIBLE | FRICTION_UNKNOWN_HOLD

canonical_store_effect_state:
  NOT_REQUESTED | AUTHORIZED | ATTEMPTED | COMMITTED
  | FAILED | OUTCOME_UNKNOWN

source_recoverability_state:
  PRESERVED_EXACT | RECOVERABLE_FROM_AUTHORIZED_ARCHIVE
  | BOUNDARY_ONLY_UNRECOVERABLE | RECOVERABILITY_UNKNOWN
```

`carry_handoff_state` is unset before the `H_TO_T_CARRY` transaction is
preallocated. Thereafter it is a target-owned observation; the separate
source-owned emission axis cannot establish acceptance.

The controller may attempt inspection close only after
`carry_handoff_state: ACCEPTED_BY_THULIA` is backed by the exact Thulia target
receipt and `selected_carry_store_outcome_state: COMMITTED` binds the identical
selected-carry bytes and digest. This is a handoff-survival gate: it proves that
the selected projection remains available after raw task-intake access closes.
It is not a Systemic Friction classification or a canonical retention effect.

`RAW_ACCESS_DROPPED` means the controller established that the bounded
Hearthline inspection projection, raw locators, task-intake reads, and related
cache/index/search handles were revoked or detached. It does not mean source
bytes were deleted, archives became unrecoverable, a provider erased model
state, or Hearthline as a model literally forgot. If the exact close outcome
cannot be proved, `CLOSE_OUTCOME_UNKNOWN` remains and the same closure
transaction must be reconciled; the system must not narrate forgetting.

After any optional Gloss turn and durable readable return, Thulia may issue a
Systemic Friction classification only if the complete Carry Selection coverage
and all typed exceptions remain established under current authority. Missing
selection coverage, unresolved holds, or unknown measurements require
`FRICTION_UNKNOWN_HOLD`. `PRUNE_ELIGIBLE` is not deletion authority. A later
`canonical_store_effect_state` records what the authorized store actually did,
while `source_recoverability_state` separately records what can be recovered
inside the exact declared boundary. A committed effect may therefore coexist
with recoverable archives, boundary-only unrecoverability, or unknown
recoverability; no state may infer another.

The canonical controller allocates one Homecoming identity and appends three
separate typed records beneath it: a Return Receipt, a Reconciliation Receipt,
and a Context-Close Receipt. Generated Spark output cannot append those records.
`RETURN_PENDING_HEARTHLINE` records that the candidate bundle is already sealed
and valid at the controller-held boundary but has not yet passed the exact
Hearthline intake route and target-receipt checks. It therefore coexists normally with
`member_execution_state: SEALED_TERMINAL`. `HOMECOMING:RETURNED` records
durable arrival of a bounded bundle.
`HOMECOMING:RECONCILED` records that the bundle matched the dispatch-pinned Home
Record after current grant, recipient, disclosure, retention, expiry,
revocation, and authorized-reroute checks. `HOMECOMING:CONTEXT_CLOSED` records
the end of the active child context only when a separate Context-Close Receipt
is appended after reconciliation or an explicit terminal failure disposition.
It is not PAL or A15 closure. `HOMECOMING:RECONCILIATION_UNKNOWN` records that
the controller cannot establish whether those reconciliation checks passed;
`HOMECOMING:RECONCILIATION_DEFECT` records a named failed check. Neither state
is a euphemism for arrival unknown. None of these states establishes task
success, carry approval, or Static activation.

Reconciliation confirms canonical account custody and closes the bookkeeping
reservation for a write capability already fenced and closed at the atomic
terminal seal. It never closes a live mutation lane: none exists during
`RETURN_PENDING_HEARTHLINE`. It does not give the Spark a continuing claim over the
ledger. A retention concern returns as a typed defect naming the exact replay,
open, contest, privacy, safety, or other account obligation at risk. “Preserve
my memory” is not a retention defect or self-preservation veto. Only Thulia may
apply Systemic Friction; any resulting Atomic Edge Promotion remains a separate
controller- or authorized-writer effect.

No returned artifact, note, ledger entry, receipt, context, or mark is modeled
as a Spark's or Gloss's body, identity, memory, or property. Only a typed
retention defect naming a declared account obligation, including any valid
hold, may block the retention transition.

A representation-side return bundle, including one prepared by a Ledger Scribe
or Thulia, carries only the declared data, provenance,
transformations, bounds, coverage, negative constraints, and residuals
available within its grant. `HOMECOMING:RETURNED` and
`HOMECOMING:RECONCILED` preserve custody facts; they do not by themselves
classify or reclassify anything as evidence, a finding, a conclusion, or a
result. A Work Spark may separately return an artifact whose status was
established under its task's declared evaluation rule; Homecoming preserves
that status without creating it.

Failure paths remain explicit:

- `STALE_OBJECTIVE_EPOCH` or `STALE_AUTHORITY_EPOCH` is a fencing reason that
  moves an affected live `ACTIVE` or `SPARK_SUSPENDED` member to
  `RETURN_ONLY`; its permitted bounded return must still seal separately before
  any valid old-epoch bundle follows its own Homecoming path, and no result is
  silently rebased;
- `RETURN_HELD_STALE_EPOCH` means an already sealed valid terminal bundle may
  not move under the expired task grant; only a separate current exact
  `terminal_return_custody_grant_ref` may admit that unchanged bundle to the
  named Hearthline intake, without rebind, revival, task continuation, or
  authority inheritance;
- `HOMECOMING:RETURNED_PARTIAL` means the bounded return arrived with named
  gaps;
- `HOMECOMING:REVOKED_RETURN` means further task action stopped and only the
  permitted return and context-close path remained;
- `HOMECOMING:HOME_REJECTED` means the return could not be admitted under the
  dispatch-pinned Home Record and authorized reroute chain; and
- `HOMECOMING:RETURN_UNKNOWN` means the system cannot establish whether the
  sealed bundle durably arrived at the declared return boundary;
- `HOMECOMING:RECONCILIATION_UNKNOWN` means a durably observed arrival exists
  but the system cannot establish whether every required reconciliation check
  passed; and
- `HOMECOMING:RECONCILIATION_DEFECT` means a durably observed arrival exists
  and one or more named reconciliation checks definitively failed.

Homecoming is not synonymous with success. A Spark may come home with a failed
test, a blocker, `NO_LEDGER_DELTA`, `LEDGER_DELTA_INCOMPLETE`,
`LEDGER_COVERAGE_UNKNOWN`, a recorded negative observation, an already-evaluated
negative result, or an unresolved residual.
`HOMECOMING:RECONCILED` may be recorded only when the named return bundle and
dispatch-pinned Home version were durably matched after the required checks.
`HOMECOMING:RETURN_UNKNOWN` supplies no such arrival premise and may not be
silently relabeled `RECONCILED`; a later observation requires a separately
recorded transition with the exact bundle identity. Ambiguity is not cleaned
up into a happy ending, and an unknown return or reconciliation is not replayed
automatically. None of these custody outcomes revives the Spark that sealed the
candidate bundle.

Reconciliation does not close the active child context automatically. A
separate Context-Close Receipt is required. Reopening later preserves the
Homecoming records, consumed limits, prior terminal state, and lineage. It does
not pretend the earlier process remained continuously active or that a new
process is numerically identical without the required continuation evidence.
Homecoming also does not undo, contain, or reverse external effects already
produced by the bounded task.

## Prospective evaluation boundary

Task Triads, task-shaped heartbeat contracts, open objective windows, and
representation-side Homecoming remain candidate design proposals. A future
implementation must test them prospectively, including preregistered
equal-budget comparisons against the paired predecessor; split provisioning and
exact three-seat co-binding. Formation fixtures must prove that Hearthline's
nonbinding nomination names only Worker and Task-Keeper and Thulia's names only
Ledger-Keeper; neither nomination reserves a seat, grants authority, or begins
execution. They must prove that the controller mechanically allocates and
reserves exact identities and grants without choosing either provider's jobs,
freezes one complete offer and authority bundle, assigns an immutable
`formation_offer_ref` and `formation_offer_digest`, and exposes to each provider
only its authorized projection plus that same common digest. The
`TRIAD_FORMATION_OFFERED` fixture must remain non-executing. Final-intent
fixtures must prove that each provider can commit only its exact own-seat
reservations over the unchanged offer, that both intents and all reservations
are immutable and single-use, and that the controller compare-and-set consumes
all of them and binds all three seats or consumes and binds nothing. Any seat,
offer, task, contract, epoch, digest, provider-grant, reservation, or
`authority_bundle_ref` mismatch must bind nothing. Authority fixtures must
prove that the aggregate epoch fences on every component change without
pooling grants. Dispatch fixtures must prove that `TRIAD_BOUND` starts no
member, that a separate controller-appended dispatch receipt follows fresh
revalidation and records `triad_dispatch_state: DISPATCHED`, and that only that
receipt moves `NOT_DISPATCHED` members to `ACTIVE`; `DISPATCH_REFUSED` and
`DISPATCH_STALE` must start none.

Lifecycle fixtures must also prove that each member reaches
`SEALED_TERMINAL` in the same atomic controller commit that seals its candidate
bundle and fences and closes its write capability, may remain
`RETURN_PENDING_HEARTHLINE` with no mutation lane, and is never kept alive or
revived by Homecoming, intake, selection, handoff, target receipt,
reconciliation, context close, or
late evidence. They must verify both the ordinary path from `ACTIVE` or
`SPARK_SUSPENDED` to `SEALED_TERMINAL` and the fenced path through
`RETURN_ONLY` to `SEALED_TERMINAL`, including a zero-content typed revocation
bundle and no `REVOKED` execution value. Fixtures must admit only the two
specified `RETURN_ONLY` entrances and must reject task resumption, a second
candidate identity, changed bytes, or a same-ID seal retry without
authoritative no-append and current exact retained bytes. Crash-before-seal and
crash-after-seal fixtures must use the preallocated per-member bundle identity
and idempotency key, prove that controller-observed `SEALED` admits
`SEALED_TERMINAL` regardless of later body validity while only `SEALED` plus
`VALID` admits custody, and hold an ambiguous append at bundle `UNKNOWN` plus
`EXECUTION_UNKNOWN` with no `RETURN_PENDING_HEARTHLINE`, new identity, or replay
until an exact query resolves the same attempt. That query must choose only an
observed `SEALED_TERMINAL`; seal-retry-only `RETURN_ONLY` for the same retained,
valid bytes under current authority; or `UNSEALED_TERMINAL` with a successor
required. Separate fixtures must prove that an invalid sealed body remains
terminal, blocks custody, and cannot be replayed, while `VALIDITY_UNKNOWN`
holds the bundle before custody without reviving the member. They must distinguish durable-arrival
`HOMECOMING:RETURN_UNKNOWN` from
`HOMECOMING:RECONCILIATION_UNKNOWN` and named
`HOMECOMING:RECONCILIATION_DEFECT`; reject reconciliation without an observed
bundle; allow only observation-backed unknown-to-observed transitions under the
same Homecoming identity without replay; preserve idempotent, out-of-order
custody records; and independently verify each member's preallocated return
transaction, emission state, and Hearthline-intake target receipt. An emitted
return must not imply receipt, an unknown outcome must not authorize resend,
and the Ledger-Keeper's Thulia provisioning record must grant Thulia no raw
return access. A stale-epoch sealed valid terminal return must remain
`RETURN_HELD_STALE_EPOCH` until a separate current exact
`terminal_return_custody_grant_ref` permits custody without rebinding,
reviving, mutating, or making the old epoch current.

Selection fixtures must require a sealed valid three-slot Triad Return Manifest
and complete Carry Selection coverage before handoff. Missing, invalid, stale,
or unknown material must remain an explicit exception; uncovered material must
produce `FRICTION_UNKNOWN_HOLD`, never an inferred selection. Handoff and
closure fixtures must keep the exact Thulia target receipt,
`selected_carry_store_outcome_state`, and `inspection_context_state`
independent. Raw inspection access may drop only after durable acceptance and
committed storage of the same selected bytes. It must not imply pruning,
provider-state erasure, literal model forgetting, or any recoverability value.

Translation fixtures must verify four distinct transactions—`H_TO_T_CARRY`,
`T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE`—and the four
Readable Carry axes under their proper writers. They must cover unset
pre-candidate axes, `VALIDITY_UNKNOWN` without false staleness, exact per-turn
Gloss readiness without a heartbeat, ambiguous emission without automatic
resend, and predecessor-linked successor envelopes for late references without
Owl liveness. Systemic Friction fixtures must run only after the readable
boundary and prove that `retention_classification`,
`canonical_store_effect_state`, and `source_recoverability_state` remain
independent; `PRUNE_ELIGIBLE` alone must perform nothing, and unknown effect or
recoverability may never be narrated as deletion.

Further tests must cover Task-Keeper witness accuracy without result-status
promotion; witness presence `ABSENT`, `PRESENT`, `INVALID`, and `UNKNOWN`
without synthesizing a value for an absent witness; per-seat heartbeat
isolation; exact observational `liveness_state` values without duplicating an
execution state; `NOT_APPLICABLE_AFTER_TERMINAL` after either terminal state;
task overhead;
round-trip fidelity relative to the received
projection; residual preservation; transfer performance; failure recovery;
missing and out-of-order bundles; stale objective- and authority-epoch
fencing; recursion rejection; coverage classification; and whether
`NO_LEDGER_DELTA` is emitted only after complete declared coverage.

## Lore and implementation boundary

This document proposes Task Triad, Triad Dispatch, Work Spark, Task-Keeper
Spark, Ledger Scribe Spark, Task Line, Completion Contract, Goal Lineage,
Purpose Projection, Task-Boundary Witness, Triad Return Manifest, Carry
Selection, Readable Carry Envelope, Thulia-bound
Support Triad, Support Seat, `objective_epoch`, `authority_bundle_ref`, and
aggregate `authority_epoch`, `formation_offer_ref`,
`formation_offer_digest`, and `TRIAD_FORMATION_OFFERED` as candidate
Hearthline design vocabulary. It
retains Home, Home Record, Spark
Heartbeat Contract, Pulse Receipt, open objective window, objective-set
snapshot, Homecoming, Return Receipt, Reconciliation Receipt, Context-Close
Receipt, Hearth Perch, and the paired predecessor as ancestry.

Task Triads are non-recursive: no member receives or spawns another triad merely
because it is a Spark, and support depth may not exceed one. The Task-Keeper is
not a scheduler, keepalive, pulse writer, evaluator, or source of authority.
This document does not instantiate a Spark, scheduler, timer, background
process, ledger, roost, model, monitor, memory store, or runtime; allocate an
operational identity; preserve an actual task; activate Hearthline; or authorize
work.

Any implementation must separately specify and test least-privilege event
projection, Goal Lineage and monotone Purpose Projection, frozen Task Lines and
Completion Contracts, split nonbinding nominations, controller-frozen
formation offers with common offer digests, final own-seat provisioning
intents, matching three-seat co-binding, inert bound formations, separate
revalidated dispatch receipts,
separate triad identities, budgets, and frozen Static references,
Home routing without authority, pulse identity and controller-only append,
bounded blocker handling, missed-pulse behavior, quiet suspension, resume
revalidation, revocation, expiry, objective- and authority-epoch fencing,
authority-bundle component fencing without grant pooling, non-renewal of
authority, independent objective, boundary-witness presence and value,
orthogonal sealed-terminal execution and Homecoming custody, and Scribe
status, coverage-qualified `NO_LEDGER_DELTA`, task/account Static
custody, separate bundle existence and validity, invalid-seal non-replay,
execution-unknown recovery and unsealed terminalization, atomic seal-time
write-capability fencing and closure,
reconciliation-time bookkeeping closure, single-writer target admission,
residual return, idempotent
Homecoming, separate arrival-unknown and reconciliation-unknown or defect
states, per-member return transaction/emission/target receipt, complete Return
Manifest and Carry Selection coverage, durable selected-carry handoff storage,
inspection-projection closure without a forgetting claim, four-lane Gloss and
Readable Carry transport, idempotent unknown emission, independent later
Systemic Friction, canonical-store-effect, and source-recoverability states,
separate close receipts, crash
recovery, objective admission while another objective is suspended, out-of-order
return, aggregation by reference, host-window loss, no cross-objective grant or
budget inheritance, privacy handling, replay/open-qualified retention defects,
rejection of self-preservation vetoes, Hearthline's inability to provision or
replace the Ledger-Keeper, Thulia's inability to receive raw member returns,
one-way separate member returns to the exact Hearthline task intake,
selected-carry-only handoff to Thulia, missing-return non-imputation,
Task-Keeper non-scheduling, bounded support depth,
recursive-formation rejection, and closure.

Hearthline, Thulia, and Sparks remain AI tool and system concepts. Homecoming is
not privileged testimony of consciousness, emotion, death, survival,
experiential memory, identity continuity, ownership, consent, standing, need,
or authority. It is a trace-preserving way to let bounded work end by returning
what it carried.
