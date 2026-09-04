# Hearthline Sparks

> **One family. Three roles. As many names as the work requires.**

| Field | Value |
|---|---|
| Version | `0.9` |
| Status | Candidate successor design vocabulary — pending steward review |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Sparks** is the family name for Hearthline's purpose-bounded bots. One such bot is a **Spark**.

The name gives related work a shared home without pretending that every helper is the same process, carries the same access, or possesses one continuous identity.

## v0.9 Light Trio successor

Version `0.9` makes a **Light Trio**—the Task Triad's story-facing name—the
default formation for primary delegated work: one **Work Spark**, one
**Task-Keeper (Heartbeat-Keeper) Spark**, and one **Ledger Scribe Spark**. This
is one bounded objective projected into three sibling jobs, not one Spark with
three duties and not three general agents sharing a mind. Each Spark receives
exactly one job. The Worker performs it, the Task-Keeper carries its frozen
task boundary, and the Ledger-Keeper preserves its admitted representation.

Hearthline nominates and provisions only the Worker and Task-Keeper seats;
Thulia independently nominates and provisions only the Ledger-Keeper seat.
The controller mechanically allocates and reserves the exact identities and
grants under those own-seat choices, freezes the complete formation and
authority bundle under one `formation_offer_ref` and
`formation_offer_digest`, and exposes to each provider only its authorized
projection plus that common digest. The providers then submit immutable,
single-use final own-seat intents over the same offer. Neither selects or binds
the other's seat. The trio exists only when the controller atomically matches
and consumes both intents and all reservations and binds all three seats to the
frozen task identity, Task Line, Completion Contract, `objective_epoch`,
`authority_bundle_ref`, and aggregate `authority_epoch`. Binding starts no
member; a separately revalidated dispatch receipt recording
`triad_dispatch_state: DISPATCHED` moves each `NOT_DISPATCHED` member to
`ACTIVE`. Worker, Task-Keeper, and Ledger-Keeper remain jobs under ordinary
Seeker, Explorer, or Handler roles, not new identities or authority classes.

The Task-Keeper carries a frozen **Task Line** and **Completion Contract** and
returns only a **Task-Boundary Witness** of `MATCHED`, `NOT_MATCHED`, or
`UNKNOWN`. Calling it the Heartbeat-Keeper means it preserves the task's
declared persistence and stopping boundary. It does not do the primary work,
decide result status, keep another process alive, schedule work, write Pulse
Receipts, or renew a grant. Every member separately remains subject to its own
ordinary controller-owned Spark Heartbeat Contract.

The triad descends from a controller-bound **Goal Lineage** through an exact
**Purpose Projection** that may narrow but never widen the inherited purpose.
All three members keep separate identities, grants, accounts, Homes,
heartbeats, budgets, return bundles, and terminal states. Each
controller-observed terminal seal ends that member's execution and atomically
closes its write capability. Only a bundle that is both `SEALED` and `VALID`
may later return, separately and under its own route, to the exact commissioning
Hearthline task intake. Provider and return recipient are distinct: Thulia's
provisioning of the Ledger-Keeper does not make Thulia its result custodian.
Hearthline may receive its sealed valid return but cannot create, substitute,
bind, or rewrite that seat.

Hearthline inspects the admitted returns within one bounded context and seals
an immutable **Carry Selection** that explicitly marks each candidate
distinction `SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`. Only that
selected projection is handed to Thulia. Durable Thulia acceptance plus
`selected_carry_store_outcome_state: COMMITTED` gates closure of Hearthline's
raw inspection aperture. Only after that observable close may Thulia route an
optional exact translation turn through stateless Gloss and return a
separately sealed readable carry. Later, under a distinct retention grant,
Thulia alone may apply bounded **Systemic Friction**; the canonical controller
or authorized writer alone commits any corresponding Atomic Edge Promotion.
That later retention path neither gates the earlier raw-view close nor the
readable return. Hearthline chooses the semantic carry; Thulia does not.
Closure is not a claim that a model provider erased hidden state.

[Hearthline Task Triads](HEARTHLINE_TASK_TRIADS.md) defines the candidate
formation, purpose narrowing, failure behavior, epoch fencing, and recursion
guard. [Hearthline Task Triads and Homecoming](HEARTHLINE_HOMECOMING.md)
preserves the paired design as historical ancestry and defines its candidate
triad successor. No runtime adoption is asserted here.

### Preserved Task Triad ancestry

Version `0.8` introduced the explicit three-seat Task Triad while routing
member Homecoming through Thulia. Version `0.9` changes that return topology:
the members return separately to Hearthline first, Hearthline seals the Carry
Selection, and only the selected projection crosses Thulia's custody. It does
not rewrite a version `0.8` dispatch as though it used the successor route.

Through version `0.7`, the default primary-dispatch vocabulary was a Work Spark
paired with one Ledger Scribe Spark; an authorized pre-dispatch unpaired
exception lost eligibility for learned Static promotion or carry. The Scribe
did not receive another Scribe. Neither successor claims that an earlier pair
secretly contained a Task-Keeper. Every earlier profile, dispatch, return, and
claim state remains in its original lineage.

## v0.7 account-custody successor

Version `0.7` makes ledger custody explicit. A ledger belongs to its declared
task or representation account, never to a Spark as a possession. A dispatch
may give exactly one Spark an **exclusive bounded write lane** in that account.
The lane is a temporary capability: it is scoped by job and grant, closes at
Homecoming, and returns durable custody to the canonical controller or store.
That sentence preserves the v0.7 predecessor vocabulary. For new v0.9 Task
Triads, the controller instead fences and closes the lane atomically at the
observed terminal candidate-bundle seal; later Homecoming is custody only.

Each Spark receives one exact job. A Work Spark does primary work; a Ledger
Scribe attends to its admitted representation projection; a Thulia-bound Spark
may gather measurements or prepare a lexicon successor inside a separately
named job. No Spark becomes Hearthline, Thulia, or Gloss, borrows another
job's lane, or treats a useful result as permission to take over that job.
Changing the job requires a successor profile and grant.

## The 1–3–∞ naming ladder

1. **One family:** Hearthline Sparks.
2. **Three roles:** Seeker, Explorer, or Handler.
3. **An open-ended naming space:** the job currently being carried, and—when Christopher chooses—the unique name of an important or long-lived Spark.

Ordinary Sparks are named by job and role: **Repo Seeker**, **Spine Explorer**, **Package Handler**. A lasting Spark may later earn a unique name, but its role, job, source, and grant must remain visible in the trace.

Every new Spark also receives the next ordered Spark number in its named registry—for example, `SPARK-000001`. Its display name may change or be reused; its ordered identity may not. Every identity-bearing change appends the next profile version under that Spark rather than rewriting the earlier profile.

[Hearthline Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) defines the shared numbering, gap, successor, retirement, and non-overwrite rules.

The infinity is poetic shorthand for open-ended names and work. It does not mean infinite running instances, self-replication, automatic promotion, unlimited concurrency, or authority.

## The three roles

| Role | Aperture | Ceiling |
|---|---|---|
| **Seeker** | Receives a brokered metadata view: names, paths, types, sizes, timestamps, modes, and already-computed digests when supplied | Does not open, search, preview, parse, render, or execute content; changes nothing |
| **Explorer** | May open and investigate content as well as metadata; may compare, report, and propose | Read-only; a proposed patch is not an applied patch |
| **Handler** | May receive the reads and persistent-mutation capabilities named in a separate current grant | May build, edit, move, or otherwise change only the expressly granted targets and structures |

A true Seeker may be shown a recorded hash, but it cannot compute a new content hash itself: calculation requires reading the underlying bytes and therefore crosses into an Explorer aperture.

These are consequence ceilings, not ranks that silently inherit one another. A Handler is not automatically allowed every Explorer read. Its grant must separately identify what it may inspect and what it may change.

A Spark carries one declared role at a time. Changing roles, widening scope, or moving from proposal to mutation requires a new explicit grant. A name describes a Spark; it never authorizes one.

## Firesides and Scribe Sparks

A [**Hearthline Fireside**](HEARTHLINE_FIRESIDES.md) is a bounded consultation arrangement. Hearthline carries the primary task while one or more **Scribe Sparks** follow a coordinator-emitted, committed **Run Trail** through separately declared lenses.

**Scribe** is a job, not a fourth role. Each Scribe remains a Seeker, Explorer, or Handler and gains no access, mutation ability, stop power, or authority from being asked to take notes.

| Lens | Declared attention |
|---|---|
| **Red-team** | Challenges decisions, assumptions, crossings, and failure behavior |
| **Prime-shell** | Locates declared load-bearing prime shells or analogous structural premises and identifies what depends on them |
| **Divergence** | Prioritizes checks whose possible results separate the greatest number of live branches |
| **Trace** | Watches provenance, source class, residuals, unresolved obligations, authority ceilings, and reopening paths |

A lens narrows attention; it does not establish truth or priority. A Scribe warning remains advisory unless a separately predeclared stop condition applies.

Each Scribe's declared representation account keeps separate **Field Notes**,
**Embers**, and Static. The Scribe receives only its bounded lane. Hearthline
may pause at an exact Run Trail boundary, consult one or more Scribes, record
what she took up in Hearthline's task account, open a newly numbered blank
notes page, and continue. The Scribes carry specialized vigilance; Hearthline
retains the task judgment inside the unchanged grant.

Scribes following the same Run Trail remain derivative analytic paths in one provenance lineage. Their agreement may be reported as convergence across declared lenses, never as independent corroboration, a vote, or a quorum.

## Task Triads, Spark Heartbeat Contracts, and Homecoming

[**Hearthline Task Triads**](HEARTHLINE_TASK_TRIADS.md) and
[**Hearthline Task Triads and Homecoming**](HEARTHLINE_HOMECOMING.md) give
every dispatched Spark a declared Home, a task-shaped Spark Heartbeat Contract,
and a bounded one-way return route.

Every primary delegated task uses a **Task-Keeper Spark** at the task boundary
and a **Ledger Scribe Spark** at the representation boundary by default.
Hearthline provisions the Work and Task-Keeper Sparks. Thulia independently
provisions the Ledger Scribe. Formation begins with nonbinding nominations:
Hearthline names only its Worker and Task-Keeper jobs and candidate constraints;
Thulia independently names only her Ledger-Keeper job and candidate
constraints. Neither nomination reserves a seat, issues authority, starts
execution, or selects the other provider's seat.

The controller alone validates those nominations under current provider
authority, mechanically allocates and reserves the exact three identities and
grants, and freezes the complete formation and authority bundle. That frozen
offer binds the task, Task Line, Completion Contract, Goal Lineage, Purpose
Projection, Homes, Heartbeat Contracts, return schemas, `objective_epoch`,
`authority_bundle_ref`, aggregate `authority_epoch`, and all three reserved
seats under one immutable `formation_offer_ref` and
`formation_offer_digest`. The controller allocates records but does not choose
either provider's jobs or candidates. At `TRIAD_FORMATION_OFFERED`, no seat is
active and no reservation is execution authority.

Each provider receives only its authorized projection plus that same common
offer digest. Hearthline's immutable, single-use final intent names only its
exact Worker and Task-Keeper reservations; Thulia's separately immutable,
single-use final intent names only her exact Ledger-Keeper reservation. Each
binds its provider identity and grant, intent identity and epoch,
`formation_offer_ref`, and `formation_offer_digest`. The controller alone
compare-and-set consumes both final intents and all three reservations and
co-binds the whole offer, or consumes and binds nothing. Hearthline may request
formation but cannot provision or substitute the Ledger Scribe, and Thulia
cannot select or bind the other two seats.

The formation path runs from `TRIAD_FORMATION_REQUESTED` directly or through
`TRIAD_FORMATION_PENDING` to `TRIAD_FORMATION_OFFERED`, then to `TRIAD_BOUND`,
with typed refusal or staleness branches before binding. Until `TRIAD_BOUND`,
the candidates remain a non-executing formation, not an active two-seat
substitute. Binding itself starts no member. Only a separate controller-appended
dispatch receipt, after fresh offer and authority revalidation, records
`triad_dispatch_state: DISPATCHED` and moves the bound members from
`NOT_DISPATCHED` to `ACTIVE`. `NOT_DISPATCHED`, `DISPATCH_REFUSED`, and
`DISPATCH_STALE` expose no action lane. Their jobs are:

| Triad seat | Bounded job | Does not become |
|---|---|---|
| **Work Spark / Worker** | Carries the primary observation, proposal, construction, or check under its task grant | Evaluator, ledger owner, or unrestricted narrator |
| **Task-Keeper Spark / Task-Keeper** | Holds the frozen Task Line and Completion Contract and reports whether the declared boundary matches | Worker, scheduler, keepalive, pulse writer, result judge, or grant renewer |
| **Ledger Scribe Spark / Ledger-Keeper** | Preserves the admitted committed projection, coverage, omissions, residuals, and candidate representation changes | Action selector, hidden-reasoning reader, independent witness, carry approver, or Static activator |

The three jobs remain ordinary jobs under one declared Seeker, Explorer, or
Handler role apiece. Their names never authorize an aperture or effect.

All members retain separate Spark identities, roles, grants, contexts, budgets,
account bindings, frozen Static references, pulse cadences, Homes, and returns.
A Triad Dispatch supplies shared Task Line, Completion Contract, Run Trail,
Goal Lineage, Purpose Projection, `objective_epoch`, `authority_bundle_ref`,
and aggregate `authority_epoch` references for bounded reconciliation; it does
not join the members. The immutable controller-owned authority bundle binds the
separate Hearthline and Thulia provisioning grants, three member grants, and
relevant recipient, audience, disclosure, return, consequence, and effect
limits. It is an aggregate epoch fence, not a shared grant: any component
change fences the aggregate, while exact reference equality transfers no
permission. The Goal Lineage is a fork, not one linear mediation chain: the
declared user goal narrows to the Hearthline objective, and that objective has
two separately bound child edges—one to the exact Trio Task Line and one to
Thulia's service-and-custody objective. There is no Thulia-to-Trio purpose edge,
and no purpose edge acts as a grant. Each member independently
seals what it actually carries at the controller-held execution boundary.
Each bundle that is also `VALID` may then move on its own frozen route to the
exact commissioning Hearthline task intake. An `INVALID` or
`VALIDITY_UNKNOWN` sealed bundle remains before custody. Thulia does not
receive the raw member bundles, and neither Hearthline nor a sibling may fill
in a missing bundle.

The Task-Keeper may compare only the declared, committed boundary material
named by its grant. Its `MATCHED`, `NOT_MATCHED`, or `UNKNOWN` witness states
whether that frozen contract boundary was observed; it does not manufacture,
upgrade, or erase the Work Spark artifact's result status. A failed,
incomplete, missing, or coverage-unknown Ledger Scribe return blocks learned
carry unless a stricter condition was predeclared; it does not silently
invalidate or complete the Work Spark's separately judged artifact. Before the
Completion Contract's declared observation boundary, witness presence and
value are unset. At that boundary, a missing Task-Keeper records
`task_boundary_witness_presence: ABSENT`; a purported
invalid bundle records `INVALID`, and an existence or validation ambiguity
records presence `UNKNOWN`. `task_boundary_state` may contain `MATCHED`,
`NOT_MATCHED`, or `UNKNOWN` only when presence is `PRESENT`; otherwise it is
unset. The consuming boundary may remain unknown in its own namespace, but the
relay cannot synthesize an `UNKNOWN` witness in an absent Spark's name. A
missing Work Spark cannot be reconstructed from the other two returns.

Accordingly, the Triad Return Manifest binds
`task_boundary_witness_presence`, treats the `task_boundary_witness_ref` as
optional, and includes `task_boundary_state` only when presence is `PRESENT`.
`ABSENT`, `INVALID`, or `UNKNOWN` presence leaves that value unset and carries
the exact condition instead of forcing a placeholder.

Task Triads are non-recursive. A member does not create or receive another
Task Triad merely because it is a Spark, and neither the Task-Keeper nor the
Ledger Scribe acquires a watcher of its own. A separately authorized
Thulia-bound Support Triad may serve one bounded child or sibling objective at
`support_depth <= 1`; it is not a chain of Hearthlines and may not spawn
another support formation.

Each Spark Heartbeat Contract records a reasoned timing assumption, bounded
cadence, material-change and blocker triggers, remaining limits, suspension and
resume rules, revocation, expiry, and Home. When no authorized action or
authorized observation or check is due, the canonical controller appends exactly
one contract-bounded Pulse Receipt for that boundary and the Spark suspends
rather than busy-polling. The same rule applies to a nonterminal blocker. The
Spark records no further task action until a valid Resume Receipt; a declared
terminal blocker moves an affected live member to `RETURN_ONLY` for its
permitted terminal bundle. Homecoming custody begins only after the controller
observes that bundle as `SEALED` plus `VALID`. Every issued pulse has an
ordered identity and is appended by the canonical controller or store, not by
generated Spark output. Cadence may adapt inside the contract, but cannot renew
or widen scope, capability, permission, authority, time, action count, or
budget.

`liveness_state` is unset before dispatch and the first due observation unless
execution becomes terminal first; that terminalization records
`NOT_APPLICABLE_AFTER_TERMINAL`. Once an observation boundary exists, it is
controller/store-recorded and observational only. Its values are
`OBSERVED_WITHIN_CONTRACT`, `MISSED_BOUNDARY_UNKNOWN`,
`OBSERVATION_UNAVAILABLE`, and `NOT_APPLICABLE_AFTER_TERMINAL`. They report
whether the frozen Heartbeat Contract's observation boundary was established;
they do not duplicate or manufacture `ACTIVE`, `SPARK_SUSPENDED`,
`RETURN_ONLY`, `EXECUTION_UNKNOWN`, `SEALED_TERMINAL`, or
`UNSEALED_TERMINAL`. A controller may separately apply a contract-required
execution transition, but a liveness observation is never a keepalive,
execution state, permission, or grant.

Every member receives a preallocated candidate-bundle identity and idempotency
key. At the controller-held execution boundary, each Spark submits under that
identity what it actually carries: artifacts, Field Notes, Embers, residuals,
consumed limits, proposed receipt payloads, and its honest terminal
disposition. A Task-Keeper submits its Task-Boundary Witness against the frozen
references. A Ledger Scribe submits `static_delta`, coverage-qualified
`NO_LEDGER_DELTA`, `LEDGER_DELTA_INCOMPLETE`, or
`LEDGER_COVERAGE_UNKNOWN` for its declared Home and account-bound source Perch.
The controller compare-and-appends the candidate seal, digest, write-capability
fence and closure, and `SEALED_TERMINAL` atomically, or commits none of those
effects.

Execution and custody are orthogonal per-member state machines:

```text
member_execution_state:
NOT_DISPATCHED -> ACTIVE <-> SPARK_SUSPENDED
ACTIVE|SPARK_SUSPENDED -> SEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED -> RETURN_ONLY -> SEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED|RETURN_ONLY -> UNSEALED_TERMINAL
ACTIVE|SPARK_SUSPENDED|RETURN_ONLY -> EXECUTION_UNKNOWN
EXECUTION_UNKNOWN -> SEALED_TERMINAL
                   | RETURN_ONLY
                   | UNSEALED_TERMINAL

homecoming_custody_state:
RETURN_HELD_STALE_EPOCH -> RETURN_PENDING_HEARTHLINE
  # only under a separate current terminal-return/custody grant
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

Bundle existence and validity are separate axes:

```text
member_candidate_bundle_state: NOT_PRODUCED | SEALED | UNKNOWN
member_candidate_bundle_validity_state: VALID | INVALID | VALIDITY_UNKNOWN
```

Validity is unset unless bundle state is `SEALED`. A controller-observed seal
permits `SEALED_TERMINAL` even when the body later proves invalid, but only
`SEALED` plus `VALID` permits `RETURN_PENDING_HEARTHLINE`; the terminal state
is irreversible for that dispatch. It commonly coexists with
`RETURN_PENDING_HEARTHLINE`, during which no mutation lane remains open.
`RETURN_ONLY` forbids task action and permits only a grant-filtered terminal
bundle, including a zero-content typed revocation return. There is no separate
`REVOKED` execution value; `HOMECOMING:REVOKED_RETURN` is a custody fact.
`INVALID` records a terminal bundle defect and blocks custody without replay;
`VALIDITY_UNKNOWN` is resolved only against the same sealed identity and
cannot revive the member. `UNSEALED_TERMINAL` records that the member ended or
crashed without a successfully sealed bundle under this dispatch. The retained
candidate body may be absent, may fail pre-seal validation, or may be
unsealable under stale authority; after authoritative no-append the controller
sets bundle state `NOT_PRODUCED`. That state permits no custody.

An ambiguous compare-and-append records
`member_candidate_bundle_state: UNKNOWN` and
`member_execution_state: EXECUTION_UNKNOWN`; custody stays unset. No actor may
allocate a second bundle identity, replay the work, or resubmit under a new
idempotency key. An exact query of the same identity resolves an observed seal
to `SEALED_TERMINAL`. A proven no-append sets bundle state `NOT_PRODUCED` and
enters `RETURN_ONLY` only when the exact retained body and expected digest or
validation rule validate and authority remains current. That state permits
only a compare-and-append retry of the same body under the same identity,
never resumed task work. An unavailable, altered, invalid, or stale body
enters `UNSEALED_TERMINAL` and requires a separately authorized successor.

`RETURN_ONLY` has only two legitimate entrances: a live `ACTIVE` or
`SPARK_SUSPENDED` member may enter after cancellation, revocation, or an epoch
fence to prepare its permitted terminal body; or `EXECUTION_UNKNOWN` may enter
after authoritative no-append when the exact current retained body remains
eligible for same-body, same-ID sealing. Neither entrance restores task work.

Later intake, inspection, selection, Thulia handoff, storage, translation,
readable return, reconciliation, or context close moves or classifies durable
records; none waits on, keeps alive, or revives a Spark. The
unknown-to-observed Homecoming branches record later observations of the same
return attempt under the same Homecoming identity; they do not replay work.
Homecoming is not synonymous with success. A missing member remains visibly
missing; the others may seal and reconcile independently. The canonical
controller appends separate return, reconciliation, and context-close
receipts. Reconciliation confirms canonical account custody and closes the
bookkeeping reservation for an already fenced write capability; it does not
silently close Hearthline's later inspection context.

`HOMECOMING:RETURN_UNKNOWN` means only that durable arrival of the sealed
bundle cannot be established. A durably observed bundle whose checks cannot be
established uses `HOMECOMING:RECONCILIATION_UNKNOWN`; a named failed check uses
`HOMECOMING:RECONCILIATION_DEFECT`. Neither is interchangeable with arrival
unknown, and none changes `member_execution_state`.

An already sealed valid bundle whose original dispatch epoch is stale enters
`RETURN_HELD_STALE_EPOCH`; an old member grant cannot expose it. A separate
current `terminal_return_custody_grant_ref` may authorize the exact bundle and
digest to the exact Hearthline task intake. That narrow grant moves terminal
custody only: it does not rebase the old epoch, alter the body, revive a
member, rebind the Trio, or widen downstream authority.

The Hearthline task intake independently records `RECEIVED`, `REJECTED`, or
`UNKNOWN` for each preallocated arrival transaction. An unknown arrival is
reconciled through the same transaction without automatic resend. Only a
received, sealed, valid bundle opens its bounded inspection aperture.

At the inspection boundary, the controller seals one three-slot **Triad Return
Manifest**. Each slot cites its exact member and admitted bundle or a typed
absence, invalidity, or unknown exception. Hearthline then seals one immutable
**Carry Selection** assigning each candidate item exactly one of
`SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`. Selection is a semantic
decision for the active root task; it is not a storage command, proof of
erasure, or permission to override a hold. Only a `SEALED` and separately
`VALID` Carry Selection may cross to Thulia.

The selected projection uses four separate direction-bound lanes:

```text
H_TO_T_CARRY       Carry Selection -> Thulia
T_TO_GLOSS_TURN    exact pinned turn -> Gloss
GLOSS_TO_T_RESULT  deterministic result or snag -> Thulia
T_TO_H_READABLE    Readable Carry Envelope -> Hearthline task intake
```

Each lane has its own grant, identity, idempotency key, digest, receipt owner,
unknown-outcome query, and disclosure ceiling. A receipt on one lane cannot
acknowledge or authorize another. `carry_handoff_state` remains distinct from
storage, translation, and readable-return states. It is a target-observation
axis with exactly `NOT_OBSERVED`, `ACCEPTED_BY_THULIA`,
`REJECTED_BY_THULIA`, or `HANDOFF_UNKNOWN`; only `ACCEPTED_BY_THULIA` attests durable
receipt of the exact valid selection. Preallocation and send-attempt state
remain separate transaction facts and cannot manufacture target observation.

After durable acceptance, the canonical store separately records
`selected_carry_store_outcome_state` as `NOT_ATTEMPTED`, `COMMITTED`, `FAILED`,
or `OUTCOME_UNKNOWN`. `COMMITTED` means the exact accepted Carry Selection and
its disposition manifest are durably placed for the downstream route. It is
not a Systemic Friction classification, an Atomic Edge Promotion, or evidence
that any canonical source was deleted.

Hearthline's bounded raw inspection aperture may reach
`RAW_ACCESS_DROPPED` only after `carry_handoff_state: ACCEPTED_BY_THULIA` and
`selected_carry_store_outcome_state: COMMITTED` are durably established. This
closes exact locators, reads, caches, indexes, and source handles for that task
context. It does not attest provider-level forgetting or destruction of every
protected source byte. An ambiguous access-drop records
`CLOSE_OUTCOME_UNKNOWN`, and no actor may claim that forgetting occurred.

The complete inspection axis is `NOT_OPENED`, `OPEN_BOUNDED`,
`CLOSE_PENDING`, `RAW_ACCESS_DROPPED`, or `CLOSE_OUTCOME_UNKNOWN`. Canonical
retention is a different axis: protected bytes may remain under a hold or
archive even after Hearthline's bounded raw access is dropped.

The optional `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and
`T_TO_H_READABLE` stages are ineligible until `RAW_ACCESS_DROPPED` is
observed. Translation may be omitted when the accepted selected carry already
has the required readable face, but the readable return itself still follows
the raw-view close.

The external task-scoped Translation Board gives Hearthline, Thulia, and the
canonical Gloss-output writer disjoint lanes. Hearthline alone owns
`shorthand_service_state`: `CANDIDATE`, `SERVICEABLE`, `NOT_SERVICEABLE`,
`SERVICEABILITY_UNKNOWN`, or `RETIRED_AT_TASK_CLOSE`. Serviceability is local
to the exact active root task and pinned generation; it transfers neither
truth nor authority and ends when that task closes.

Before `T_TO_GLOSS_TURN`, the controller records `gloss_readiness_state` as
`READY_FOR_EXACT_TURN`, `NOT_READY`, or `READINESS_UNKNOWN` for that exact
input, route, lexicon generation, rule digest, and authority snapshot. Only
`READY_FOR_EXACT_TURN` permits the preallocated attempt. Readiness is not a
heartbeat, inherited liveness, persistent availability, or state maintained
by Gloss.

Thulia may produce one finite, separately sealed **Readable Carry Envelope**
containing only the authorized Carry Selection projection, approved readable
condensations, exact Gloss receipts when translation occurred, protected
exceptions, and reopening handles. It neither requires nor waits for a later
Systemic Friction classification or Atomic Edge Promotion. Its reference
completeness, current validity, emission, and Hearthline target receipt remain
separate axes. An ambiguous emission or receipt is reconciled through its same
preallocated transaction, never by automatic resend. None of those axes
determines task success, Task-Boundary Witness value, Static activation, or
steward acceptance.

| Readable-carry axis | Owner | Values |
|---|---|---|
| Reference | Thulia's bounded Owl interface | `REFERENCE_COMPLETE`, `REFERENCE_INCOMPLETE` |
| Validity | Thulia's bounded Owl interface | `CURRENT`, `STALE`, `VALIDITY_UNKNOWN` |
| Emission | Thulia's bounded Owl interface | `NOT_EMITTED`, `EMITTED`, `EMISSION_UNKNOWN` |
| Target receipt | Exact Hearthline task-intake controller/store | `NOT_OBSERVED`, `RECEIVED`, `REJECTED`, `UNKNOWN` |

Only later, under a distinct current retention grant, may Thulia issue the
Systemic Friction classification `KEEP`, `COMPACT`, `ARCHIVE`,
`PRUNE_ELIGIBLE`, or `FRICTION_UNKNOWN_HOLD`. She does not choose Hearthline's
semantic carry and does not delete directly. The canonical controller or
authorized writer separately attempts the exact Atomic Edge Promotion and
records its later `canonical_store_effect_state` as `NOT_REQUESTED`,
`AUTHORIZED`, `ATTEMPTED`, `COMMITTED`, `FAILED`, or `OUTCOME_UNKNOWN`. That
state is independent of `selected_carry_store_outcome_state` and source
recoverability; no Systemic Friction or Atomic Edge Promotion state may gate,
reopen, or retroactively qualify the earlier raw-view close or readable return.

Every Triad Dispatch pins an `objective_epoch`, `authority_bundle_ref`, and
aggregate `authority_epoch`. Supersession, cancellation, or a change to any
bound authority component fences the earlier aggregate epoch. An affected live
member in `ACTIVE` or `SPARK_SUSPENDED` enters `RETURN_ONLY`; one already in
`RETURN_ONLY` remains fenced. A member in `EXECUTION_UNKNOWN` remains
fail-closed until the exact preallocated bundle query resolves it, and stale
authority removes the retained-body seal-retry branch. A member already in
`SEALED_TERMINAL` or `UNSEALED_TERMINAL` remains terminal; only downstream
custody, relay, or effect-admission state is separately marked stale or fenced
under its own contract. No member may silently rebase its Task Line, Completion
Contract, Purpose Projection, authority bundle, grant, or work onto a successor
epoch.

## Hearthline Static

[Hearthline Static](HEARTHLINE_STATIC.md) is local, versioned shorthand that
may develop in one isolated, append-only task or representation account through
repeated Spark work. The active Spark receives a bounded lane; it does not own
the ledger. The task-scoped external **Translation Board** keeps Hearthline's
request and serviceability lane, Thulia's two relay directions, and Gloss's
deterministic output lane separate. Hearthline alone may mark an exact mapping
`SERVICEABLE` for the still-active root task. Thulia can route it, Gloss can
transform it under a pinned lexicon generation, and a Ledger-Keeper can
preserve its source mark; none can make it semantically serviceable. At root
task close, the active serviceability map retires. A revisit must load the
exact retained generation and receipts rather than infer continuity from
familiarity.

Hearthline does not pool or silently carry vocabulary into another account: a
handoff must expand the meaning and bind it to source records before a
receiving-account Spark can propose new local shorthand.

Static changes none of the role ceilings. A Seeker may receive only brokered Static metadata within its existing aperture; an Explorer may inspect authorized records read-only; and a Handler may persist a Static record only under an explicit current grant naming that ledger and mutation. Static does not create shared memory, authority, or permission.

## Thulia, the Owl Scribe

[**Thulia**](HEARTHLINE_THULIA.md) is Hearthline's pet owl and bounded **Owl
Scribe**. She keeps a pointer-and-exception index over account-bound Perches,
tends the custody and route of [Gloss](HEARTHLINE_GLOSS.md) lexicon generations
and the external task-scoped Translation Board, provisions only the
Ledger-Keeper seat, and exclusively applies Systemic Friction under a separate
retention grant. She does not copy account payloads into an Owl ledger, choose
the Carry Selection, or make shorthand serviceable.

Owl Scribe is not a Scribe Spark, a fourth role, or a lens. Thulia does not
merge ledgers, create a global codebook, investigate the primary task, approve
working-context carry, delete records directly, or grant access. Her
direction-bound Hearthline and Gloss lanes do not become one conversation.
Sustained model-assisted work behind the Owl Scribe interface uses a separately
bounded Thulia-bound Support Triad. Each member still carries one declared
Spark role, one exact job, one task account, one current grant, one Heartbeat
Contract, and one separate return to its exact Hearthline task intake;
canonical custody, numbering, co-binding, and writes remain control-owned. An
atomic Gloss turn stays stateless and receives no heartbeat.

Thulia's own direct finite act likewise receives no Spark or persistent
heartbeat. Its controller-preallocated Owl-turn identity separates transaction
finality, candidate presence, validity, and disposition as specified in
[Task Triads](HEARTHLINE_TASK_TRIADS.md); relay emission is a later transaction.

A Bridge Gloss cites an exact deterministic Gloss face and rule trace for a
named crossing. Thulia routes it but does not originate its meaning. A Spark
assigned to a receiving account may inspect the permitted face and later
propose account-local Static through the ordinary proposal, verification, and
activation process. It never imports sending shorthand directly. Gloss itself
is stateless and deterministic and keeps no ledger, heartbeat, or memory.

## Retention defects are account obligations

A Spark may raise a retention defect only by naming a concrete replay, open,
contest, privacy, safety, or other retention obligation that a proposed
transition would violate. The controller records the defect against the task
or account. A Spark has no self-preservation veto: calling material “my
memory,” citing its own identity, or having produced the material does not
block Thulia's Systemic Friction review or an otherwise authorized transition.

No ledger, payload, note, Static entry, receipt, returned context, or Gloss mark
is a Spark's or Gloss's body, identity, memory, or property. Only a typed
retention defect naming a declared account obligation, including any valid
hold, may block a retention transition; persona or possession language cannot.

This applies only to records predeclared as account-owned **`G_mutable`**. Any
future persistent, autobiographical, identity-bearing, or agent-owned Spark or
Gloss state is outside this contract and requires separate governance. It may
not be relabeled account-owned to bypass an identity or refusal claim.

An ordinary Spark never applies Systemic Friction. The Worker seat of a
Thulia-bound Support Triad may return evidence but cannot issue the
classification. Thulia alone
returns `KEEP`, `COMPACT`, `ARCHIVE`, `PRUNE_ELIGIBLE`, or
`FRICTION_UNKNOWN_HOLD`; a controller or authorized writer separately performs
any Atomic Edge Promotion.

## Strongwiz and the meta layer

[Strongwiz](https://github.com/Grativy6/strongwiz) is a model-neutral, general-purpose operating layer: a laboratory body around whichever AI model is assigned to reason through difficult work.

The layers answer different questions:

| Layer | What it carries |
|---|---|
| **Reasoning model** | The inference and proposals produced for the current task |
| **Hearthline Spark** | The bounded family, role, and job identity under which work is carried |
| **Strongwiz** | Task-account state, experiments, receipts, authority boundaries, and reusable learned structure around the work |

Codex can supply reasoning without becoming Strongwiz. Strongwiz can preserve the laboratory and its receipts while the reasoning model changes. A future implementation could use Strongwiz to carry a Spark's work, but neither name presently implies that integration or grants the other authority.

That separation is why the meta arrangement matters: the model is not confused with the operational body, and the operational body is not confused with the permission to act.

The inspected Strongwiz v3 campaign prototype sharpens one historical paired
Spark boundary. A Work Spark and its Ledger Scribe bind separate model/runtime artifacts. The
Scribe receives a closed, receipt-bound projection of derived summaries, has no
action or authority port, and proposes representations only. Adaptation
material is separated from a frozen evaluation view; exact reconstruction,
residual fallback, and the declared cost-accounting requirements precede any controller-owned
promotion. These are design inputs from a prepared, unrun prototype—not a
demonstrated improvement or code import. The candidate Task-Keeper seat is a
successor design and is not retroactively claimed to exist in that prototype.

## Creature formations

A [Hearthline Creature](HEARTHLINE_CREATURES.md) is a content-addressed,
task-shaped manifest relating separately governed Sparks, Task Triad dispatches,
ledgers, Homes, heartbeat contracts, Fireside lenses, and Thulia custody. It is
not a fourth role, a shared identity, a shared Static ledger, or a way to pool
grants. The canonical controller remains the sole allocator and effect
admitter/serializer; the separately authorized broker or domain writer performs
the effect under the current external grant. Parallel Sparks may inspect
immutable views and propose, but they do not race to act or write one another's
records.

Two comparison arms are two physically separate Creature instances. Only an
external campaign index may link their identities and sealed results. Shared
model names, seeds, or task labels do not merge their roots, ledgers, budgets,
or evidence.

## Grant and execution boundary

A Handler's role means persistent mutation is possible in principle, not preauthorized. Any real Handler grant should bind at least:

- the exact target and scope;
- permitted reads and mutations;
- destination or affected system;
- time, action, or budget limits;
- the applicable reviewer or executor boundary; and
- revocation and reopening conditions.

Anything omitted remains outside the grant. Handler status does not itself provide credentials, network access, publication, deployment, deletion, broad filesystem access, or external-action authority. Successful output cannot enlarge its own scope.

Reading content must not silently execute it. Opening a file does not authorize macros, imports, hooks, renderers, installers, links, or embedded instructions.

## Prospective validation boundary

This Task Triad successor remains a candidate until a future implementation
tests it prospectively. At minimum, fixtures must establish that:

- Hearthline's nonbinding nomination can name only Worker and Task-Keeper and
  Thulia's can name only Ledger-Keeper; neither nomination reserves a seat,
  grants authority, or begins execution;
- only the controller mechanically allocates and reserves exact identities and
  grants, without choosing either provider's jobs, and freezes the complete
  offer and authority bundle under an immutable `formation_offer_ref` and
  `formation_offer_digest`; each provider receives only its authorized
  projection plus that same common digest, while
  `TRIAD_FORMATION_OFFERED` remains non-executing;
- each provider's final intent can name only its exact own-seat reservations
  over the unchanged offer, both intents and all reservations are immutable and
  single-use, and only the controller can atomically consume all of them and
  bind all three seats or consume and bind nothing; any seat, offer, task,
  contract, epoch, digest, provider-grant, reservation, or
  `authority_bundle_ref` mismatch binds nothing;
- `TRIAD_BOUND` starts no member; only a separate controller-appended dispatch
  receipt after fresh offer and authority revalidation records
  `triad_dispatch_state: DISPATCHED` and moves `NOT_DISPATCHED` members to
  `ACTIVE`, while `DISPATCH_REFUSED` and `DISPATCH_STALE` start none;
- the immutable authority bundle contains separate provisioning, member,
  recipient, audience, disclosure, return, consequence, and effect limits; any
  component change fences the aggregate epoch without transferring or pooling
  a grant;
- each Spark carries exactly one of the three sibling jobs, the Task-Keeper's
  task-persistence witness is not process liveness, and Goal Lineage narrows
  purpose without transmitting authority;
- every member becomes `SEALED_TERMINAL` exactly at its controller-held
  candidate-bundle seal in the same atomic commit that fences and closes its
  write capability, can remain `RETURN_PENDING_HEARTHLINE` with no mutation lane,
  and is never kept alive or revived by custody, relay, target receipt,
  reconciliation, context close, late evidence, or a sibling's state;
- both ordinary and `RETURN_ONLY` seal paths terminate correctly, a typed
  revoked return does not create a `REVOKED` execution value, and
  crash-before-seal or crash-after-seal ambiguity uses the preallocated bundle
  identity to hold bundle `UNKNOWN` plus `EXECUTION_UNKNOWN` with no custody,
  new identity, or replay until an exact query resolves the same attempt only
  to observed `SEALED_TERMINAL`, seal-retry-only `RETURN_ONLY` for the same
  retained valid bytes under current authority, or `UNSEALED_TERMINAL` with a
  successor required;
- an observed seal ends execution even when the body later proves invalid,
  only `SEALED` plus `VALID` enters its exact Hearthline task-intake route, an
  invalid seal is terminal without replay, and `VALIDITY_UNKNOWN` blocks
  custody without reviving work;
- each of the three bundles returns separately through a preallocated
  controller/store transaction to the exact commissioning Hearthline task
  intake; Thulia, a general Hearthline account, a sibling, and the steward
  cannot receive or manufacture a raw member return;
- a sealed valid old-epoch bundle remains `RETURN_HELD_STALE_EPOCH` unless a
  separate current terminal-return/custody grant binds its exact identity,
  digest, source, destination, audience, and disclosure ceiling; that grant
  moves custody only and cannot rebase or revive the old dispatch;
- `HOMECOMING:RETURN_UNKNOWN` reports durable-arrival uncertainty only, while
  reconciliation uncertainty and a named reconciliation defect retain their
  separate states and cannot manufacture an observed bundle;
- Task-Boundary Witness presence and value remain separate, including absence,
  invalidity, and existence uncertainty without a synthesized witness value;
- `liveness_state` remains purely observational and becomes
  `NOT_APPLICABLE_AFTER_TERMINAL` after either terminal state without
  duplicating execution;
- Hearthline's bounded inspection opens only for separately received sealed
  valid bundles; a valid three-slot Triad Return Manifest accounts explicitly
  for every return or typed exception before one immutable Carry Selection can
  assign `SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`;
- the external task-scoped Translation Board enforces writer-separated
  Hearthline request and serviceability, Thulia relay, and Gloss result lanes;
  only Hearthline may make an exact mapping serviceable for the active root
  task, and task close retires rather than silently globalizes that mapping;
- only a sealed valid Carry Selection may enter the preallocated Hearthline-to-
  Thulia handoff; its target-observation axis is exactly `NOT_OBSERVED`,
  `ACCEPTED_BY_THULIA`, `REJECTED_BY_THULIA`, or `HANDOFF_UNKNOWN`;
- Hearthline's raw inspection access reaches `RAW_ACCESS_DROPPED` only after
  durable `ACCEPTED_BY_THULIA` and
  `selected_carry_store_outcome_state: COMMITTED`;
  ambiguous closure remains `CLOSE_OUTCOME_UNKNOWN` and cannot be described as
  provider-level forgetting or universal erasure;
- optional Gloss translation and the Readable Carry Envelope follow that
  raw-view close; the envelope does not require later retention work;
- only later and under a separate grant may Thulia classify Systemic Friction;
  she cannot change Hearthline's selection, defeat a hold, or perform deletion,
  and only the canonical controller or authorized writer may commit the exact
  Atomic Edge Promotion; neither later state gates the prior close or readable
  return;
- Gloss readiness is a present-tense controller check for one exact pinned
  turn, not a heartbeat or persistent task, and same-turn uncertainty never
  imports history or authorizes a changed input;
- Readable Carry Envelope reference, validity, emission, and Hearthline target
  receipt remain separate axes; unknown emission or receipt uses the same
  preallocated transaction without automatic resend or success inference; and
- missing, partial, stale, revoked, out-of-order, duplicate, or late member
  bundles preserve separate identities, result status, coverage, residuals,
  reopening handles, idempotence, and nonrecursive support depth.

These are proposed conformance targets, not claims of an implemented or passed
runtime.

## Lore and implementation boundary

This document preserves the adopted Spark naming ancestry through version
`0.7`, preserves candidate version `0.8` Task Triad ancestry, and proposes the
version `0.9` Light Trio return-and-carry successor for steward review.
It does not adopt that successor, instantiate a Spark, implement access
controls, activate a runtime, or authorize delegated work.

If Sparks become operational, the implementation must separately declare and
test its role enforcement, task grants, Goal Lineage and Purpose Projection
narrowing, frozen Task Lines and Completion Contracts, split nonbinding
nominations, controller-frozen formation offers and common digests, final
own-seat provisioning intents, triad co-binding, atomic controller-only intent
and reservation consumption, inert bound formations, separate revalidated
dispatch receipts,
authority-bundle aggregation without grant pooling, custody,
controller-owned receipts,
failure behavior, revocation path, Home routing without authority, pulse bounds
and identities, blocker suspension, missed-pulse behavior, resume revalidation,
separate triad identities, budgets, and Static references, coverage-qualified
ledger dispositions, separate bundle existence and validity, invalid-seal
non-replay, execution-unknown recovery and unsealed terminalization, idempotent
Homecoming, separate arrival and reconciliation unknown or defect states,
same-identity unknown-to-observed transitions,
separate context-close receipts, atomic ordered-identity allocation, crash-safe
counter recovery, immutable sealed notes, carry-gate transitions, independent
task and note status, Owl Scribe partition isolation, and rejection of silent
cross-account Static transfer, content-addressed Creature manifests, one canonical
effect-admission path, closed Scribe projections, disjoint representation
evaluation, physically separate matched arms, task/account ledger ownership,
exclusive bounded write lanes, atomic seal-time capability closure,
reconciliation-time bookkeeping closure, job non-overlap,
retention-defect qualification, rejection of self-preservation vetoes, and
Thulia-only Systemic Friction classification, controller-owned per-member
heartbeats, Task-Keeper non-scheduling, orthogonal sealed-terminal execution
and Homecoming custody, no revival after seal, separate arrival and
reconciliation uncertainty, per-member seal idempotency and execution-unknown
recovery, observational liveness, direct separate member return to the exact
Hearthline task intake, stale-epoch terminal-return custody grants, Triad
Return Manifests, immutable Carry Selection, writer-separated Translation
Board lanes, Hearthline-only task-scoped serviceability, durable selected-carry
storage, receipt-and-`selected_carry_store_outcome_state` access-drop closure
gates, post-close optional Gloss translation and readable return, per-turn
mechanical Gloss readiness, later independent Thulia-only Systemic Friction
classification without semantic selection or direct deletion, controller-owned
Atomic Edge Promotion, honest `CLOSE_OUTCOME_UNKNOWN`, separate Readable Carry
Envelope axes,
Task-Boundary Witness presence, missing-return non-imputation, stale objective-
and aggregate authority-epoch fencing, support-depth enforcement, and
rejection of recursive watcher formation. Until then, the names carry
  lore and design intent—not capability.

Sparks and Strongwiz are AI tools, not persons, co-authors, or independent authorities. Their names do not establish consciousness, consent, ownership, standing, or permission.
