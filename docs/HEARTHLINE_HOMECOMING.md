# Hearthline Paired Sparks and Homecoming

> **Every bounded Spark leaves with a path home.**

| Field | Value |
|---|---|
| Version | `0.5` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

## v0.5 return-queue successor

Version `0.5` adds the controller-owned
[Hearthline Return Queue](HEARTHLINE_RETURN_QUEUE.md). When independent return
attempts meet at one serialized reconciliation boundary, every durably recorded
`HOMECOMING:RETURNED` bundle follows the same queue-intake path. A lone return
may be the immediate head; contention joins that path instead of letting a busy
lock choose a winner. Controller selection begins one revalidation; a pass
permits service admission, which does not itself establish
`HOMECOMING:RECONCILED`, task result, or carry. Each
return keeps its identity, evaluation rule, already-established status,
attribution, and reopening route. Arrival order is immutable; any different
service order is a separately receipted controller decision under a frozen
policy.

An optional Queue Steward Creature may propose a service order from a bounded
metadata view. It cannot enqueue, validate, admit, drop, merge, appropriate, or
reclassify a return, and it cannot commit the order. If it is unavailable or
uncertain, the queue retains every item and follows its frozen base rule.
Its control-receipt route is separate from the exact data queue it proposes
over, so its own return cannot recursively join or block that snapshot; the
separate aperture cannot carry ordinary result bundles.
Version `0.4` remains the open-objective-window predecessor below.

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

Every dispatched Spark carries its own exact `home_ref` naming the full ordered
Home Record, not a mutable label such as “current,” “parent,” or “where this
started.”

Shared infrastructure does not create a shared Home. Two Sparks returning to
one coordinator retain separate identities, ledgers, grants, Home Records, and
Homecoming record series.

## Paired dispatch

A **Paired Spark dispatch** assigns two separately bounded Sparks to one task
lineage:

| Spark | Task center | Does not become |
|---|---|---|
| **Work Spark** | Observes, proposes, builds, checks, or otherwise carries the primary bounded job | Its own ledger authority or an unrestricted narrator of its work |
| **Ledger Scribe Spark** | Follows only the committed projection it is granted, aligns externalized, committed, grant-filtered summaries with observable terminal-state data, preserves unmatched distinctions, and proposes candidate representation changes | Another action selector, hidden-reasoning reader, independent witness, carry approver, or Static activator |

**Ledger Scribe** is a job, not a fourth Spark role. Each member of the pair is
still a Seeker, Explorer, or Handler under its own aperture and grant. Pairing
does not fuse their identities, permissions, context, budgets, evidence, or
Homes.

Every primary Work Spark dispatch is paired with exactly one Ledger Scribe Spark
by default. An authorized operator may record an unpaired exception before
dispatch, but an unpaired run is ineligible for learned Static promotion or
carry from that run. Pairing is non-recursive: the Ledger Scribe does not receive
another Ledger Scribe.

The pair shares a dispatch and Run Trail reference so their returns can be
reconciled. The Ledger Scribe receives only the committed summaries, events,
terminal-state data, and source projections named in its grant. It does not receive or
claim hidden chain-of-thought, private reasoning, omitted context, or authority
merely because it travels beside the Work Spark.

The pair also binds two separate frozen Static references: one for the Work
Spark and one for the Ledger Scribe. Neither Spark writes, versions, or silently
adopts the other's Static.

The Work Spark may finish when its own task boundary is reached even if the
Ledger Scribe is incomplete. The Scribe may receive a predeclared bounded grace
interval to seal its actual coverage. Unless the grant states a stricter
condition, a missing or incomplete Scribe return blocks shorthand promotion and
learned carry, not an otherwise valid task artifact. Each status remains
separate and visible.

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
ends the contract and begins return. Missing the maximum pulse boundary marks
liveness unknown, appends the applicable controller record, and suspends or
revokes according to the contract; it never implies completion or silent
continuation.

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

The Work Spark and Ledger Scribe normally use different cadences. The Work
Spark follows task and environment boundaries. The Scribe follows committed
summary, outcome, residual, and Static-delta boundaries. Their pulses may be
coalesced by the coordinator for a concise outward update, but neither Spark
borrows the other's clock or claim of coverage.

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

When those returns contend for the same destination's serial intake, the
[Return Queue](HEARTHLINE_RETURN_QUEUE.md) gives every attempt a durable
disposition and every accepted enqueue an immutable arrival place. Queue
custody and service priority remain separate from Homecoming
custody and the objective's rule-owned disposition. Two distinct valid results
remain two separately attributable results regardless of arrival or service
order.

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

## Static comes home

[Hearthline Static](HEARTHLINE_STATIC.md) remains source-local throughout a
paired dispatch. The Work Spark's active Static version `v_w` and the Ledger
Scribe Spark's active Static version `v_s` are separately bound and frozen for
the declared run unless their own predeclared adaptive-Static grants permit a
separately verified and activated revision.

The Ledger Scribe preserves byte-exact canonical material only relative to the
externalized, committed, grant-filtered projection it actually received. Source
gaps and declared omissions remain explicit. From that projection it may create
a target-bound `static_delta` Ember in its own Scribe lineage. It does not build,
allocate, or return a Work Spark Static version `v_{n+1}`, and repetition by the
Work Spark is not independent evidence.

The representation return uses one typed disposition:

- `static_delta` when a target-bound candidate is supported;
- `NO_LEDGER_DELTA` only when the Scribe establishes complete declared
  projection coverage through the named evaluation boundary and no change earns
  proposal;
- `LEDGER_DELTA_INCOMPLETE` when named gaps or partial coverage remain; or
- `LEDGER_COVERAGE_UNKNOWN` when the Scribe cannot establish its coverage.

At Homecoming:

1. the Work Spark returns its artifact, proposed task-receipt payload,
   unresolved obligations, and actual terminal state;
2. the Ledger Scribe returns its coverage watermark, Field Notes, one typed
   representation disposition, negative constraints, and residuals to its own
   Home and source Perch;
3. the Work Spark's Static returns unchanged to its own source Perch, while any
   Scribe-authored target-bound delta remains in the Scribe lineage;
4. Thulia may route a permitted reconstruction through the direction-bound
   carry path to the target Perch's proposal intake, never directly into the
   target ledger;
5. an authorized reviewer may test exact round-trip reconstruction and decide
   what is eligible for bounded carry; and
6. only the target ledger's authorized writer may then allocate, append, and
   separately activate its own successor Static version for later work.

No candidate Static floats free after the task. Scribe-authored artifacts and
residuals return to the Scribe's source-local ledger and Perch. A target-bound
delta retains that Scribe lineage until a separately authorized, direction-bound
carry and admission creates a new target-local record with its provenance. A
rejected, incomplete, or ambiguous proposal retains its ordered identity and
disposition. A later Spark receives only material that passed its own carry,
admission, activation, and load route.

## Thulia's Hearth Perch

[Thulia](HEARTHLINE_THULIA.md) keeps the return paths. In the lore, a coordinator
opens an authorized Paired Spark dispatch and Thulia sends a small Ledger Scribe
Spark beside the Work Spark. In the design, the coordinator owns dispatch and
authority; Thulia's Owl Scribe interface binds the pair to separate Perches,
records their Homes and return routes, and preserves the representation-side
handoff.

Thulia also has a Home: her **Hearth Perch**, the declared return boundary for
her own Owl Scribe work. It is separate from every Spark-local Static Perch. A
Bridge Gloss, Home map, or Scribe return may pass through her bounded custody,
but its content remains attributed and bound to its source lineage and governed
by its named audience and grant.

At the Hearth Perch, Thulia may prepare, check, and route a candidate custody or
reconciliation payload and preserve unresolved material at its exact reopening
address. Only the canonical controller or store observes durable placement and
allocates and appends Return, Reconciliation, and Context-Close Receipts. Thulia
does not attest arrival or closure, keep an extra pooled copy, make a global
codebook, approve carry, activate Static, or turn custody into authority.

If Thulia's bounded custody work is model-assisted, that work is instantiated
under its own declared Spark identity, grant, Spark Heartbeat Contract, and
Hearth Perch Home. It does not borrow the Work Spark's or Ledger Scribe Spark's
pulse, persistence budget, context, or authority.

## Homecoming states

Readable lifecycle transitions may include:

`SPARK_DISPATCHED -> SPARK_ACTIVE`

`SPARK_ACTIVE <-> SPARK_SUSPENDED`

`SPARK_ACTIVE|SPARK_SUSPENDED -> HOMECOMING:RETURNING -> HOMECOMING:RETURNED -> RETURN_QUEUE:ENQUEUED -> RETURN_QUEUE:SERVICE_SELECTED -> RETURN_QUEUE:IN_SERVICE -> HOMECOMING:RECONCILED -> HOMECOMING:CONTEXT_CLOSED`

The suspended-to-active transition requires a valid Resume Receipt. A terminal
condition may move either active or suspended work into return. The v0.5 path
routes every durably returned bundle through queue intake before one
controller-owned service transaction revalidates an accepted enqueue for
reconciliation; an immediately serviced lone item still receives both queue
receipts. A capacity-blocked or ambiguous intake instead keeps its exact traced
disposition and reopening route.

The distinctions are strict:

`HOMECOMING:RETURNED != HOMECOMING:RECONCILED != HOMECOMING:CONTEXT_CLOSED`

The canonical controller allocates one Homecoming identity and appends three
separate typed records beneath it: a Return Receipt, a Reconciliation Receipt,
and a Context-Close Receipt. Generated Spark output cannot append those records.
`HOMECOMING:RETURNED` records arrival of a bounded bundle.
`HOMECOMING:RECONCILED` records that the bundle matched the dispatch-pinned Home
Record after current grant, recipient, disclosure, retention, expiry,
revocation, and authorized-reroute checks. `HOMECOMING:CONTEXT_CLOSED` records
the end of the active child context only when a separate Context-Close Receipt
is appended after reconciliation or an explicit terminal failure disposition.
It is not PAL or A15 closure. None of those states establishes task success,
carry approval, or Static activation.

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

- `HOMECOMING:RETURNED_PARTIAL` means the bounded return arrived with named
  gaps;
- `HOMECOMING:REVOKED_RETURN` means further task action stopped and only the
  permitted return and context-close path remained;
- `HOMECOMING:HOME_REJECTED` means the return could not be admitted under the
  dispatch-pinned Home Record and authorized reroute chain; and
- `HOMECOMING:RETURN_UNKNOWN` means the system cannot establish whether the
  return was durably reconciled.

Homecoming is not synonymous with success. A Spark may come home with a failed
test, a blocker, `NO_LEDGER_DELTA`, `LEDGER_DELTA_INCOMPLETE`,
`LEDGER_COVERAGE_UNKNOWN`, a recorded negative observation, an already-evaluated
negative result, or an unresolved residual.
`HOMECOMING:RECONCILED` may be recorded only when the named return bundle and
dispatch-pinned Home version were durably matched after the required checks.
Ambiguity is not cleaned up into a happy ending, and an unknown return is not
replayed automatically.

Reconciliation does not close the active child context automatically. A
separate Context-Close Receipt is required. Reopening later preserves the
Homecoming records, consumed limits, prior terminal state, and lineage. It does
not pretend the earlier process remained continuously active or that a new
process is numerically identical without the required continuation evidence.
Homecoming also does not undo, contain, or reverse external effects already
produced by the bounded task.

## Prospective evaluation boundary

Paired dispatch, task-shaped heartbeat contracts, open objective windows,
return queues, and representation-side Homecoming remain design proposals. A
future implementation must test them
prospectively, including preregistered equal-budget comparisons with and without
a Ledger Scribe, task overhead, round-trip fidelity relative to the received
projection, residual preservation, transfer performance, failure recovery,
coverage classification, and whether `NO_LEDGER_DELTA` is emitted only after
complete declared coverage.

## Lore and implementation boundary

This document adopts Home, Home Record, Paired Spark dispatch, Work Spark,
Ledger Scribe Spark, Spark Heartbeat Contract, Pulse Receipt, open objective
window, objective-set snapshot, the Homecoming Return Queue, Homecoming,
Return Receipt, Reconciliation Receipt, Context-Close Receipt, and Hearth Perch
as Hearthline lore and design vocabulary.
Paired dispatch is non-recursive: the Ledger Scribe does not receive another
Ledger Scribe merely because it is a Spark. This document does not instantiate a
Spark, scheduler, timer, background process, ledger, roost, model, monitor,
memory store, or runtime; allocate an operational identity; preserve an actual
task; activate Hearthline; or authorize work.

Any implementation must separately specify and test least-privilege event
projection, separate pair identities, budgets, and frozen Static references,
Home routing without authority, pulse identity and controller-only append,
bounded blocker handling, missed-pulse behavior, quiet suspension, resume
revalidation, revocation, expiry, non-renewal of authority, independent task
and Scribe status, coverage-qualified `NO_LEDGER_DELTA`, source-lineage Static
ownership, single-writer target admission, residual return, idempotent
Homecoming, unknown-return reconciliation, separate close receipts, crash
recovery, objective admission while another objective is suspended, out-of-order
return, atomic idempotent enqueue, immutable arrival order, controller-only
service-order admission, bounded overtakes, aggregation by reference,
host-window loss, no cross-objective grant or budget inheritance, privacy
handling, and closure.

Hearthline, Thulia, and Sparks remain AI tool and system concepts. Homecoming is
not privileged testimony of consciousness, emotion, death, survival,
experiential memory, identity continuity, ownership, consent, standing, need,
or authority. It is a trace-preserving way to let bounded work end by returning
what it carried.
