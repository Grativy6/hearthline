# Hearthline Ordered Lineage

> **A successor receives a new number. It does not receive permission to erase its predecessor.**

| Field | Value |
|---|---|
| Version | `0.9` |
| Status | Candidate successor design vocabulary — pending steward review |
| Change lineage | `HLP-000011` |
| Agent-contract companion | [`hearthline_agent.md`](../hearthline_agent.md) `0.7-draft` |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Ordered Lineage** is the identity and versioning discipline for Hearthline Sparks, task and representation accounts, [Task Triads](HEARTHLINE_TASK_TRIADS.md), [Creatures](HEARTHLINE_CREATURES.md), Firesides, Static, Field Notes, Embers, [Thulia's](HEARTHLINE_THULIA.md) Owl Scribe records, [Gloss](HEARTHLINE_GLOSS.md) translation accounts and slates, [Homes and Homecomings](HEARTHLINE_HOMECOMING.md), their receipts, and public visual presentation records.

Its purpose is simple: every Spark and every new version receives an ordered number, and earlier work remains individually addressable. Correction, retirement, rejection, or replacement may change what governs later work; none silently makes an earlier record disappear.

An ordered number is an identifier inside a declared ledger scope. It records allocation and sequence only. It does not establish rank, seniority, quality, truth, personhood, experiential continuity, ownership, capability, permission, or authority.

## v0.9 inspected-carry and translation-lane successor

Version `0.8` remains candidate ancestry. Candidate version `0.9` is the
Ordered-Lineage companion to `HLP-000011` and the candidate agent contract
`0.7-draft`. It numbers the
two-stage result route after Task-Triad execution: three separate validated
member-intake receipts at Hearthline, Hearthline's immutable Carry Selection,
optional Translation Board requests, the selected Hearthline-to-Thulia
handoff, a durable Thulia receipt, selected-carry custody storage, the separate
inspection-access close, optional Gloss work, and the final readable carry back
to Hearthline. Only afterward may Thulia classify Systemic Friction and a
separately authorized writer attempt a canonical retention effect. It keeps
the four directional translation lanes separate and makes active shorthand
serviceability root-task-scoped.

It also records Gloss readiness only as a controller observation for one finite
deterministic turn. Gloss receives no heartbeat or inherited readiness state.
Only Thulia may classify Systemic Friction; that classification cannot originate
or rewrite Hearthline's semantic carry choice.

This document numbers the records that carry the state families defined by
[Task Triads](HEARTHLINE_TASK_TRIADS.md); it does not rename those mechanical
states. “Inspected carry,” “custody store,” “readable return,” and “later
retention” name ordered phases only. Where Ordered Lineage assigns a record
identity to one of them, the referenced Task-Triad state remains the governing
mechanical vocabulary.

## v0.8 task-triad and epoch predecessor

Version `0.7` remains the adopted predecessor. Candidate version `0.8` gives
the Task Triad design an ordered identity family without turning its
meaningful purpose chain into an authority chain. It numbers the
Goal Lineage, immutable Goal versions, `NARROWS` Purpose Projections, Task
Lines, objective epochs, Completion Contracts, Task Triad dispatches and
member bindings, Task-Boundary Witnesses, Triad Relay Envelopes, and
controller-owned immutable authority bundles and aggregate authority epochs.

Every active or reopened task pins exact versions. A changed objective,
contract, member, return family, or authority epoch receives a successor
identity; none may be repaired by overwriting or rebinding a mutable `latest`
label. This successor also specifies the ordered references needed to fence a
stale suspended task while [TETHER](HEARTHLINE_TETHER.md) carries its exact
reopening route.

## v0.7 account-custody successor

Version `0.7` assigns durable ledger custody to declared task,
representation, and translation accounts. A Spark may receive an exclusive
bounded write lane in one account, but its identity does not own that account
or survive Homecoming as a continuing write claim. The version also adds
Translation Slate and lexicon-generation examples without creating a
Gloss-owned history.

## v0.6 presentation successor

Version `0.6` adds ordered `IMAGE` examples for Hearthline and Thulia's public visual provenance. The initial gallery registrations are explicitly retrospective because the images existed before their public numbers were assigned. This presentation-only successor changes no Spark, Owl Scribe, Homecoming, Creature, Static, grant, or runtime behavior.

## Typed ordered identities

A future implementation should represent canonical identity structurally, including immutable registry and entity identifiers, a typed record kind, an owner or parent reference, and a numeric ordinal. Human-readable labels are derived views, not the complete canonical identity.

Ordinals are integers from `1` through `2^63 - 1`. Display forms use at least six digits and never wrap; numeric fields rather than strings, timestamps, filenames, or wall-clock completion determine order. The following forms are normative examples of the readable identity structure; exact field encoding remains an implementation decision.

| Record | Example | Ordering scope |
|---|---|---|
| Spark | `SPARK-000001` | One named Spark registry |
| Spark profile version | `SPARK-000001/PROFILE-000001` | That Spark's profile series |
| Spark Home Record | `SPARK-000001/HOME-000001` | That Spark's Home series |
| Spark Heartbeat Contract | `SPARK-000001/HEARTBEAT-000001` | That Spark's heartbeat-contract series |
| Pulse Receipt | `SPARK-000001/HEARTBEAT-000001/PULSE-000001` | One pulse series within one heartbeat contract |
| Suspension receipt | `SPARK-000001/SUSPENSION-000001` | That Spark's suspension series |
| Resume receipt | `SPARK-000001/RESUME-000001` | That Spark's resume series |
| Paired dispatch | `PAIR-000001` | One named paired-dispatch registry |
| Goal Lineage / Steward Goal | `GOAL-000001` | One controller-owned goal registry |
| Goal version | `GOAL-000001/VERSION-000001` | That Goal Lineage's immutable statement series |
| Purpose Projection | `GOAL-000001/VERSION-000001/PURPOSE-PROJECTION-000001` | One child-purpose edge from one exact Goal version |
| Task Line | `TASK-LINE-000001` | One controller-owned task-line registry |
| Task Line version | `TASK-LINE-000001/VERSION-000001` | That Task Line's immutable wording and boundary series |
| Objective epoch | `TASK-LINE-000001/VERSION-000001/OBJECTIVE-EPOCH-000001` | One exact objective-validity epoch for one Task Line version |
| Completion Contract | `COMPLETION-CONTRACT-000001` | One named completion-contract registry |
| Completion Contract version | `COMPLETION-CONTRACT-000001/VERSION-000001` | That contract's immutable completion-test series |
| Task Triad | `TRIAD-000001` | One named Task Triad registry |
| Task Triad dispatch | `TRIAD-000001/DISPATCH-000001` | That Task Triad's attempt and dispatch series |
| Task Triad dispatch receipt | `TRIAD-000001/DISPATCH-000001/RECEIPT-000001` | That dispatch's controller-appended admission series |
| Work member binding | `TRIAD-000001/MEMBER-WORK-000001` | That Task Triad's Work-member series |
| Task-Keeper member binding | `TRIAD-000001/MEMBER-TASK-KEEPER-000001` | That Task Triad's Task-Keeper-member series |
| Ledger member binding | `TRIAD-000001/MEMBER-LEDGER-000001` | That Task Triad's Ledger-member series |
| Member candidate bundle | `TRIAD-000001/MEMBER-WORK-000001/CANDIDATE-BUNDLE-000001` | One member binding's preallocated candidate-bundle series |
| Formation request | `TRIAD-FORMATION-REQUEST-000001` | One controller-owned Task Triad formation-request registry |
| Hearthline own-seat nomination | `TRIAD-FORMATION-REQUEST-000001/HEARTHLINE-NOMINATION-000001` | That request's nonbinding Work-plus-Task-Keeper nomination series |
| Thulia own-seat nomination | `TRIAD-FORMATION-REQUEST-000001/THULIA-NOMINATION-000001` | That request's nonbinding Ledger-Keeper nomination series |
| Triad Formation Offer | `TRIAD-FORMATION-REQUEST-000001/OFFER-000001` | That request's controller-frozen complete-offer series |
| Member candidate-bundle reservation | `TRIAD-FORMATION-REQUEST-000001/OFFER-000001/RESERVATIONS-000001/CANDIDATE-WORK-000001` | One offer's inert reservation for an exact future member candidate identity, key, and validation/query route |
| Hearthline provisioning intent | `TRIAD-FORMATION-REQUEST-000001/HEARTHLINE-INTENT-000001` | That request's Work-plus-Task-Keeper intent series |
| Thulia provisioning intent | `TRIAD-FORMATION-REQUEST-000001/THULIA-INTENT-000001` | That request's Ledger-Keeper intent series |
| Controller binding receipt | `TRIAD-000001/CO-BINDING-000001` | That Task Triad's controller-appended exact three-seat binding series |
| Task-Boundary Witness | `TRIAD-000001/TASK-BOUNDARY-WITNESS-000001` | That Task Triad's boundary-witness series |
| Member task-intake receipt | `TRIAD-000001/MEMBER-WORK-000001/RETURN-000001/TARGET-RECEIPT-000001` | One member's separate validated arrival at Hearthline task intake |
| Triad Return Manifest | `HEARTHLINE-TASK-INTAKE-000001/RETURN-MANIFEST-000001` | One immutable three-slot account of admitted member bundles and typed exceptions |
| Carry Selection | `HEARTHLINE-TASK-INTAKE-000001/CARRY-SELECTION-000001` | Hearthline's immutable semantic keep, omit, and unresolved selection series |
| Translation Board request | `TRANSLATION-BOARD-000001/GENERATION-000001/ENTRY-000001` | Hearthline's task-scoped shorthand-translation request series |
| Shorthand serviceability receipt | `TRANSLATION-BOARD-000001/GENERATION-000001/ENTRY-000001/SERVICEABILITY-000001` | Hearthline's explicit mapping-admission series for one root task |
| Selected-carry handoff transaction | `CARRY-HANDOFF-000001` | One current independently preallocated Hearthline-to-Thulia transaction series |
| Durable Thulia receipt | `CARRY-HANDOFF-000001/TARGET-RECEIPT-000001` | Thulia's target receipt for one exact selected-carry transaction |
| Triad Relay Envelope (predecessor) | `TRIAD-RELAY-000001/ENVELOPE-000001` | One preserved pre-v0.9 relay-envelope series; never reused for the current selected-carry route |
| Selected-carry store outcome | `CARRY-STORE-000001/TRANSACTION-000001` | One custody-store outcome preserving an accepted selection and its required downstream inputs |
| Hearthline inspection close | `HEARTHLINE-TASK-INTAKE-000001/INSPECTION-000001/CLOSE-000001` | One bounded inspection-context closure series |
| Readable Carry Envelope | `READABLE-CARRY-000001/ENVELOPE-000001` | One exact finite-Owl candidate body for the selected readable return |
| Systemic Friction classification | `TRIAD-000001/SYSTEMIC-FRICTION-000001` | Thulia's later retention-classification series over one immutable Carry Selection |
| Canonical store effect | `SOURCE-RETENTION-000001/EFFECT-000001` | One later, separately authorized Atomic Edge Promotion transaction over a named source boundary |
| Source recoverability observation | `SOURCE-RETENTION-000001/RECOVERABILITY-000001` | One boundary-scoped observation after a canonical retention edge |
| Finite Owl turn | `OWL-TURN-000001` | One controller-preallocated finite Owl-act series |
| Owl candidate | `OWL-TURN-000001/CANDIDATE-000001` | That finite Owl turn's preallocated candidate series; for the selected-carry task it digest-binds the exact Readable Carry Envelope body |
| Relay emission transaction (predecessor) | `TRIAD-RELAY-000001/EMISSION-000001` | One preserved relay-envelope family's preallocated idempotent emission-attempt series |
| Relay target receipt (predecessor) | `TRIAD-RELAY-000001/TARGET-RECEIPT-000001` | One preserved relay-envelope family's separately numbered target-receipt series |
| Readable carry return transaction | `READABLE-CARRY-000001/EMISSION-000001` | One independent Thulia-to-Hearthline readable-return transaction series |
| Readable carry receipt | `READABLE-CARRY-000001/TARGET-RECEIPT-000001` | Hearthline's target receipt for that readable-return transaction |
| Readable-carry store outcome | `READABLE-CARRY-000001/STORE-000001` | One durable-store outcome for the sealed valid Readable Carry Envelope before emission |
| Controller | `CONTROLLER-000001` | One named canonical-controller registry |
| Controller authority bundle | `CONTROLLER-000001/AUTHORITY-BUNDLE-000001` | That controller's immutable aggregate authority-component series |
| Controller authority epoch | `CONTROLLER-000001/AUTHORITY-EPOCH-000001` | That controller's grant-and-revocation validity series |
| Open objective window | `WINDOW-000001` | One controller-owned exchange registry |
| Admitted objective | `WINDOW-000001/OBJECTIVE-000001` | That window's objective-admission series |
| Objective-set snapshot | `WINDOW-000001/SET-000001` | That window's immutable membership/disposition series |
| Aggregation close | `WINDOW-000001/CLOSE-000001` | That window's public-response close series |
| Creature | `CREATURE-000001` | One named Creature registry |
| Creature profile | `CREATURE-000001/PROFILE-000001` | That Creature's manifest-successor series |
| Creature dispatch | `CREATURE-000001/DISPATCH-000001` | That Creature's dispatch series |
| Creature checkpoint | `CREATURE-000001/CHECKPOINT-000001` | That Creature's checkpoint series |
| Campaign | `CAMPAIGN-000001` | One external comparison-campaign registry |
| Campaign arm | `CAMPAIGN-000001/ARM-000001` | One physically isolated Creature arm |
| Task or representation account | `ACCOUNT-000001` | One controller-owned account registry |
| Homecoming | `SPARK-000001/HOMECOMING-000001` | That Spark's Homecoming series |
| Homecoming Return Receipt | `SPARK-000001/HOMECOMING-000001/RETURN-000001` | One Homecoming's return series |
| Homecoming Reconciliation Receipt | `SPARK-000001/HOMECOMING-000001/RECONCILIATION-000001` | One Homecoming's reconciliation series |
| Homecoming Context-Close Receipt | `SPARK-000001/HOMECOMING-000001/CONTEXT-CLOSE-000001` | One Homecoming's context-close series |
| Static version | `ACCOUNT-000001/STATIC-000001` | That account's isolated Static lineage |
| Static entry | `ACCOUNT-000001/STATIC-000001/ENTRY-000001` | One account Static version |
| Field Notes page | `ACCOUNT-000001/NOTES-000001` | That account's notes series |
| Ember | `ACCOUNT-000001/EMBER-000001` | That account's candidate-carry series |
| Fireside | `FIRESIDE-000001` | One named Fireside registry |
| Run | `FIRESIDE-000001/RUN-000001` | That Fireside's run series |
| Run Trail event | `FIRESIDE-000001/RUN-000001/EVENT-000001` | That run's committed event series |
| Static activation receipt | `ACCOUNT-000001/STATIC-ACTIVATION-000001` | That account's Static activation series |
| Carry Manifest | `FIRESIDE-000001/RUN-000001/CARRY-000001` | That run's reviewed carry series |
| Load receipt | `FIRESIDE-000001/RUN-000001/LOAD-000001` | That run's context-load series |
| Owl Scribe | `OWL-000001` | One named Owl registry |
| Owl profile version | `OWL-000001/PROFILE-000001` | That Owl Scribe's profile series |
| Owl character sheet | `OWL-000001/SHEET-000001` | That Owl Scribe's appearance-sheet series |
| Owl image | `OWL-000001/IMAGE-000001` | That Owl's public visual series |
| Hearthline image | `HEARTHLINE/IMAGE-000001` | Hearthline's public visual series |
| Hearth Perch | `OWL-000001/HEARTH-PERCH-000001` | That Owl Scribe's Home series |
| Hearth Perch version | `OWL-000001/HEARTH-PERCH-000001/VERSION-000001` | One Hearth Perch's version series |
| Perch | `OWL-000001/PERCH-000001` | That Owl Scribe's partition directory |
| Perch version | `OWL-000001/PERCH-000001/VERSION-000001` | One Perch's version series |
| Translation request | `OWL-000001/REQUEST-000001` | That Owl Scribe's request series |
| Bridge Gloss | `OWL-000001/GLOSS-000001` | That Owl Scribe's gloss series |
| Gloss delivery receipt | `OWL-000001/GLOSS-000001/DELIVERY-000001` | One gloss's recipient-delivery series |
| Translation account | `TRANSLATION-ACCOUNT-000001` | One controller-owned translation registry |
| Translation Slate | `TRANSLATION-ACCOUNT-000001/SLATE-000001` | One detachable, replaceable slate series |
| Lexicon generation | `TRANSLATION-ACCOUNT-000001/LEXICON-000001` | That translation account's lexicon series |
| Translation turn mark | `TRANSLATION-ACCOUNT-000001/SLATE-000001/MARK-000001` | One slate's attempted-turn series |
| Gloss readiness observation | `TRANSLATION-ACCOUNT-000001/SLATE-000001/READINESS-000001` | One controller-observed readiness result for one finite Gloss turn |

The full identity also binds immutable registry and entity IDs. `SPARK-000001` in two unrelated registries is not one Spark. A portable reference therefore includes at least the registry identity, typed ordinal, stable entity identity, parent scope, and exact record digest.

## Allocation rules

1. **Allocate before use.** The canonical controller or store commits a Spark number before that Spark begins work and commits a version number before content is recorded under that version.
2. **Increase within one named series.** Every successor takes the next available ordinal in its declared parent scope. Separate record types use separate series; their numbers are not compared as though they shared one clock.
3. **Never reuse or renumber.** Once issued, an ordinal is never reassigned, compacted away, shifted to close a gap, or given to a different record.
4. **Preserve unsuccessful numbers.** A rejected proposal, failed construction, interrupted allocation, or abandoned reservation retains its number and terminal status. Every issued number ends in a materialized record or an explicit `ABORTED`, `VOIDED`, `UNKNOWN`, or lawful `TOMBSTONED` disposition. An unexplained gap at or below the series high-water mark is an integrity failure.
5. **Append corrections.** A correction creates a newly numbered successor that names its predecessor, reason, and disposition. It never edits history into agreement with the correction.
6. **Separate version from activation.** A proposed version receives its own version ordinal. Verification, approval, activation, supersession, rejection, and retirement are separate, ordered receipts. A version can therefore remain permanently proposed or rejected without its number being reused.
7. **Derive what is active.** The governing Static or profile version is determined from valid activation receipts under the current grant, not from an overwriteable `latest` field. Convenience pointers may be cached but are not authoritative history.

Every record should bind its typed ID, stable entity ID, owning task or account,
parent ledger, assigned writer lane, predecessor where applicable, status,
creation receipt, content digest, producer and tool identities when relevant,
scope, and reason for change. Every disposition change appends a new ordered,
hash-linked registry event rather than editing the old event in place.

## Spark identity and versions

A new Spark receives a new Spark ordinal even if it has the same model, role, job, lens, or display name as an earlier Spark. Reuse of a name does not create identity continuity.

A Spark may retain its stable Spark ordinal through profile versions when the
exact account binding, write lane, and authorized continuation are
re-established. Changes to its role, job, lens, grant binding, model binding,
or other identity-bearing configuration append a new profile version. A
replacement process that cannot establish that continuation begins as a new
Spark. The stable Spark ordinal never conveys ownership of an account ledger.

Retiring a Spark appends a retirement record. Reopening may append a new profile version if the continuation requirements are met; it does not delete the retirement or pretend the interruption did not occur.

## Goal, task, triad, and controller-epoch identities

A **Goal Lineage** gives one purpose family a durable controller-owned
identity. Every Goal version freezes one exact statement, source, steward,
scope, exclusions, predecessor, and claim ceiling. A
`PURPOSE-PROJECTION-000001` record binds one exact parent Goal version to one
exact child Goal or Task Line version with the typed edge `NARROWS` and the
evidence or declared rationale for that relationship. The edge says that the
child serves a bounded part of the parent. It does not copy the parent's grant,
make the child an authority, or prove semantic entailment merely because the
records are linked.

The useful purpose topology is therefore a sibling DAG: the user's goal
narrows to Hearthline's bounded orchestration objective; from Hearthline, one
edge narrows to a Task Triad's Task Line and a separate sibling edge narrows to
Thulia's mediation objective. The three member jobs narrow the Triad Task Line.
Thulia contributes her Ledger-Keeper nomination and later custody work without
becoming the Triad's purpose parent. Each edge keeps its own identity, owner,
grant, limits, and evaluation rule. References carry purpose downward and
results home; authority is separately issued and revalidated at every edge.

The purpose relation is an acyclic directed graph, not a command chain. A
Triad Task Line and Thulia's co-formation and later custody objectives narrow
the same Hearthline objective on separate edges. No
result, receipt, translation, or return edge points backward as a new purpose
or authorizes its ancestor. Cycle detection occurs before offer freeze; a
self-edge or descendant-to-ancestor `NARROWS` edge prevents formation.

Every **Task Line version** freezes the exact objective wording, inputs,
outputs, exclusions, source and target accounts, Purpose Projection,
Completion Contract reference, and `objective_epoch`. A compatible
clarification or narrower projection appends a successor Task Line version and
its own narrowing record. A widened or materially different objective receives
a new Task Line identity. Neither kind of change silently rebases an active or
suspended dispatch.

Every **Completion Contract version** freezes the predicates, required
artifacts, coverage obligations, residual treatment, terminal and nonterminal
conditions, and the rule for returning `MATCHED`, `NOT_MATCHED`, or `UNKNOWN`.
A contract correction or replacement receives a successor version. A Task
Triad remains pinned to the version it carried; using the successor requires a
new dispatch rather than rewriting what the earlier Triad was asked to finish.

Task Line and Completion Contract are authority-neutral immutable artifacts
with one-way reference: the Task Line names the exact Completion Contract, and
the contract does not embed or point back to the Task Line. Formation offer,
binding, and dispatch records later bind both artifacts alongside the exact
authority bundle and epochs; those later authority records are not folded into
either artifact's digest.

A **Task Triad** record binds exactly one Work member, one Task-Keeper member,
and one Ledger member after all three are bound to the same frozen Goal,
Purpose Projection, Task Line version, `objective_epoch`, Completion Contract
version, controller-owned `authority_bundle_ref`, and aggregate
`authority_epoch`. The member records bind separate Spark identities,
profiles, jobs, grants, write lanes, budgets, heartbeat contracts, Homes, and
return obligations.

Formation is bootstrap-safe and ordered. Hearthline first submits a formation
request with a **nonbinding own-seat nomination** for only the Work and
Task-Keeper jobs. Thulia independently submits a nonbinding own-seat nomination
for only the Ledger-Keeper job through the Owl interface under her existing
grant. A nomination does not allocate a Spark, reserve a lane, issue a grant,
bind a seat, permit dispatch, or select the other provider's seat.

Only the canonical controller allocates identities and grants. After validating
both nominations, it reserves the three separate member records, Homes, lanes,
and candidate-bundle identities, idempotency keys, expected digest **or**
validation rule, and exact same-identity query routes, then freezes one
complete **Triad Formation Offer** under an immutable
`formation_offer_ref` and `formation_offer_digest`. The offer binds the exact
Goal, Purpose Projections, Task Line, Completion Contract, objective epoch,
three proposed member records and Homes, controller-owned
`authority_bundle_ref`, aggregate `authority_epoch`, and reservations that must
be consumed together. Each provider receives only its authorized offer
projection plus the same common offer identity and digest. The formation state
`TRIAD_FORMATION_OFFERED` is inert: no member is bound or active.

Hearthline then submits one immutable final own-seat intent for the Work and
Task-Keeper seats, and Thulia independently submits one for the Ledger-Keeper
seat. Both final intents bind the same `formation_offer_ref` and
`formation_offer_digest`; neither may modify the offer or name the other
provider's seats. The controller compare-and-swaps the request, offer digest,
authority bundle and aggregate epoch, both final-intent digests, reservations,
and expected registry predecessors. It consumes the intents and reservations
and appends one controller binding receipt atomically, or binds nothing. A
failed comparison, refusal, changed nomination, or stale component preserves
the issued numbers and requires a separately numbered successor offer or
attempt; no intent, offer, seat, or gap is reused or overwritten.

The controller binding receipt consumes the exact candidate-bundle reservations
into bound, preallocated candidate identities; their existence and validity
axes remain unset until their later observation boundary. The Task Triad becomes
dispatchable only when the canonical controller appends its three-seat
controller binding receipt. `TRIAD_BOUND` remains inert: a separate controller
dispatch attempt must revalidate the frozen task, authority bundle, aggregate
epoch, member bindings, candidate identities, Homes, and remaining limits and
append a dispatch receipt before any member becomes active. A requested,
pending, offered,
refused, mismatched, or stale formation keeps its allocated identities and
disposition but is not a Task Triad dispatch. Hearthline cannot complete the
formation by self-supplying Thulia's Ledger member, and Thulia cannot substitute
either Hearthline-provisioned member.

The three member bindings do not fuse three Sparks into one identity. A member
replacement cannot be inserted into the old Triad or merely redispatched under
its binding receipt: it requires a separately requested, offered, atomically
formed, and bound successor Task Triad before that successor receives a
dispatch. A changed frozen task binding or return family likewise requires the
appropriate separately formed successor rather than rebinding the old record.
A redo with the same already-bound members may receive a successor dispatch
only where the frozen formation contract expressly permits it. An old member
number is never reassigned to a replacement. The Task-Keeper is a job inside
the fixed Spark roles, not a new role, clock owner, scheduler, or controller.

A **Task-Boundary Witness** is allocated only at the observation boundary
declared by the Completion Contract. The controller separately records
`task_boundary_witness_presence` as exactly `ABSENT`, `PRESENT`, `INVALID`, or
`UNKNOWN`. The witness reference is optional, and `task_boundary_state` is set
to exactly `MATCHED`, `NOT_MATCHED`, or `UNKNOWN` only when presence is
`PRESENT`; for every other presence value the state remains unset. A present
witness binds the exact Triad, task and contract versions, objective epoch,
`authority_bundle_ref`, aggregate authority epoch, referenced member returns or
their explicit absence, actual coverage, and residuals.
Hearthline may request the check but cannot self-supply the witness. The
witness reports the declared task boundary; it does not manufacture the
artifact's rule-owned result status, prove the ledger complete beyond recorded
coverage, accept a result, or authorize an external effect.

A sealed Task-Boundary Witness is immutable, including an honest `UNKNOWN`.
Evidence that arrives later does not fill its missing references or revise its
value in place. The controller may authorize a reopened or successor objective
under the then-current exact Task Line, Completion Contract,
`objective_epoch`, `authority_bundle_ref`, and `authority_epoch`. A later
bounded Task-Keeper evaluation proposes a new witness; the controller allocates
and appends its new number. That witness names the earlier witness as
predecessor and binds the late evidence and reopening receipt. The successor
may return a different value without claiming that the predecessor contained
evidence it did not have or reviving the predecessor's closed member contexts.

A controller-observed member return enters Hearthline task intake separately
as `RETURN_PENDING_HEARTHLINE` only when its candidate bundle is `SEALED` and
separately `VALID`. `INVALID`, `VALIDITY_UNKNOWN`, `UNKNOWN`, and
`NOT_PRODUCED` do not enter intake custody. One member's intake receipt never
admits, reconstructs, or waits for either sibling. A stale historical task
epoch cannot move even a sealed valid body by itself; the exact old body may
move only under a separate current terminal-return/custody grant naming the
Hearthline intake, disclosure ceiling, and expiry. That grant authorizes no
task action, reseal, rebinding, semantic rewrite, or epoch renewal.

Under a bounded inspection grant, Hearthline may inspect the separately
admitted bodies. At the declared boundary, the controller first appends one
immutable **Triad Return Manifest** with exactly three slots—Work,
Task-Keeper, and Ledger—each containing the exact admitted reference or a typed
absence, invalidity, or unknown exception. The manifest's existence and
validity are separate. Only `return_manifest_state: SEALED` plus
`return_manifest_validity_state: VALID` permits Hearthline to author one
immutable **Carry Selection**.

Every candidate item in that selection receives exactly one semantic state:
`SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`. Each state binds its exact
source, reason, protected distinctions, uncertainty, replay/contest burden,
proposed readable form, accepted loss, and reopening handle. The controller
appends the selection under its preallocated identity, idempotency key, and
digest or validation rule. `carry_selection_coverage_state` is separately
`COMPLETE`, `INCOMPLETE`, or `COVERAGE_UNKNOWN`; an unmentioned inspection item
makes coverage `INCOMPLETE` and is not silently treated as `SELECT_LOSE`.
`carry_selection_state: UNKNOWN` uses only the
same-identity query route; `INVALID` or `VALIDITY_UNKNOWN` never enters
handoff. Only `carry_selection_state: SEALED` plus
`carry_selection_validity_state: VALID` plus
`carry_selection_coverage_state: COMPLETE` may cross to Thulia. An empty carry
remains an explicit, completely accounted record.

The selection may include an ordered set of Hearthline-authored **Translation
Board requests**. Hearthline alone originates the semantic choice and alone
may issue a shorthand-serviceability decision for the root task. Thulia may
later apply retention classification and Gloss may execute a mapping; neither
may add to, subtract from, reinterpret, or mark serviceable the semantic carry.

The `0.8` candidate's **Triad Relay Envelope** and its `owl_relay_*` axes remain
numbered predecessor ancestry; version `0.9` does not reuse that identity for
selected carry. If an exact TETHER reopens an already allocated predecessor
relay family, every populated legacy relay or target-receipt axis must name its
exact `triad_relay_envelope_ref`. Reference, validity, emission, and receipt
remain orthogonal, and ambiguity reconciles only the original preallocated
transaction. No current task may mint a legacy envelope merely to fill a
missing current handoff record.

The current one-way `H_TO_T_CARRY` instead receives its own preallocated
transaction identity and idempotency key. It carries only the immutable,
`SEALED` plus `VALID` plus coverage-`COMPLETE` Carry Selection and authorized
Translation Board references; it never copies unselected raw member bodies or
replaces the three intake receipts. Source and target observations are
independent:

```text
carry_handoff_emission_state:
  NOT_EMITTED | EMITTED | EMISSION_UNKNOWN
carry_handoff_state:
  NOT_OBSERVED | ACCEPTED_BY_THULIA | REJECTED_BY_THULIA | HANDOFF_UNKNOWN
```

Only the separately owned durable Thulia receipt establishes
`ACCEPTED_BY_THULIA`. A known `NOT_EMITTED` is incompatible with target
acceptance or rejection; `EMISSION_UNKNOWN` may temporarily coexist with an
independently observed target result while that same transaction is
reconciled. No ambiguous dispatch or acknowledgement permits automatic resend,
a replacement transaction, semantic rewrite, or inference about Thulia's
liveness.

After `ACCEPTED_BY_THULIA`, the carry store performs a separate custody
operation over the immutable selection and every exact input its declared
translation and readable-return path still requires. Its state is exactly
`NOT_ATTEMPTED`, `COMMITTED`, `FAILED`, or `OUTCOME_UNKNOWN` on
`selected_carry_store_outcome_state`. This operation is not Systemic Friction,
a retention classification, a canonical source effect, or a recoverability
claim.

Hearthline's bounded inspection context begins `OPEN_BOUNDED`. Only the exact
conjunction

```text
carry_handoff_state: ACCEPTED_BY_THULIA
selected_carry_store_outcome_state: COMMITTED
```

permits the separately numbered inspection-close transaction to enter
`CLOSE_PENDING`. A successful access-drop receipt records
`RAW_ACCESS_DROPPED`; an ambiguous acknowledgement records
`CLOSE_OUTCOME_UNKNOWN` and reconciles the same closure identity. Rejected or
unknown handoff, and `FAILED`, `OUTCOME_UNKNOWN`, or `NOT_ATTEMPTED` custody
storage, leave the context `OPEN_BOUNDED`. Closure withdraws the raw bundle
locators and reads from that Hearthline inspection context. It does not claim
provider/model forgetting, delete the external sources, perform retention, or
collapse their ordered identities.

Only after `selected_carry_store_outcome_state: COMMITTED` and
`inspection_context_state: RAW_ACCESS_DROPPED` does translation proceed across
four distinct lanes and two independent carry transactions:
`H_TO_T_CARRY`, `T_TO_GLOSS_TURN`, `GLOSS_TO_T_RESULT`, and
`T_TO_H_READABLE`. Gloss has no heartbeat, memory ledger, or persistent
readiness. For each finite turn, the controller separately records
`READY_FOR_EXACT_TURN`, `NOT_READY`, or `READINESS_UNKNOWN`; no observation is
inherited by another turn. The Gloss transaction state is independently
`PREALLOCATED`, `COMMITTED_SUCCESS`, `COMMITTED_SNAG`, `OUTCOME_UNKNOWN`,
`SAME_TURN_RETRY_ONLY`, or `NOT_COMMITTED_TERMINAL`. Any retry uses only the
same pinned turn identity, input, route, lexicon generation, and rule digest.

The Readable Carry Envelope is the controller-preallocated candidate of one
finite Owl turn, not a second unnumbered composition. Only
`owl_candidate_state: SEALED`, `owl_candidate_validity_state: VALID`, and
`owl_turn_disposition: CANDIDATE_COMPLETE` permit its separate durable-store
attempt. `readable_carry_store_outcome_state` is then `NOT_ATTEMPTED`,
`COMMITTED`, `FAILED`, or `OUTCOME_UNKNOWN`; only `COMMITTED` may feed the
independent `T_TO_H_READABLE` transaction. Its four return axes remain
separate:

- `readable_carry_reference_state` is `REFERENCE_COMPLETE` or
  `REFERENCE_INCOMPLETE`;
- `readable_carry_validity_state` is `CURRENT`, `STALE`, or
  `VALIDITY_UNKNOWN`;
- `readable_carry_emission_state` is `NOT_EMITTED`, `EMITTED`, or
  `EMISSION_UNKNOWN`; and
- `readable_carry_receipt_state` is `NOT_OBSERVED`, `RECEIVED`, `REJECTED`, or
  `UNKNOWN`.

No axis manufactures another. An `EMITTED` envelope with receipt `UNKNOWN`
is reconciled under the same transaction and is not resent automatically. A
received readable carry may open a new bounded Hearthline planning context but
cannot reopen the dropped raw-return inspection context.

Only after every required Gloss turn is terminal, the Readable Carry Envelope
is durably stored, and any required Hearthline receipt is `RECEIVED`—or the
frozen selection expressly requires no translation and no readable return—may Thulia apply
**Systemic Friction**. Her classification is exactly `KEEP`, `COMPACT`,
`ARCHIVE`, `PRUNE_ELIGIBLE`, or `FRICTION_UNKNOWN_HOLD`. It is a later
retention recommendation over the already frozen Carry Selection, not a
semantic choice or storage effect. A controller or separately authorized
writer may then attempt the still later Atomic Edge Promotion. Its
`canonical_store_effect_state` is independently `NOT_REQUESTED`, `AUTHORIZED`,
`ATTEMPTED`, `COMMITTED`, `FAILED`, or `OUTCOME_UNKNOWN`; source
recoverability is separately `PRESERVED_EXACT`,
`RECOVERABLE_FROM_AUTHORIZED_ARCHIVE`, `BOUNDARY_ONLY_UNRECOVERABLE`, or
`RECOVERABILITY_UNKNOWN` inside one named boundary. `PRUNE_ELIGIBLE` never
performs deletion, and neither inspection closure nor a requested prune proves
unrecoverability.

A shorthand-serviceability record binds one immutable mapping reference, exact
lexicon generation, direction, root-task identity, bounds, and Hearthline
decision. Its `shorthand_service_state` is `CANDIDATE`, `SERVICEABLE`,
`NOT_SERVICEABLE`, `SERVICEABILITY_UNKNOWN`, or
`RETIRED_AT_TASK_CLOSE`. At root-task end, each active `SERVICEABLE` mapping
becomes `RETIRED_AT_TASK_CLOSE` and the live map is dropped. A revisit must
reload an exact retained lexicon generation under current access and obtain a
current Hearthline serviceability decision. It cannot inherit a mutable map or
decode under an unpinned `latest` generation.

These Task-Triad state families provide complete non-success coverage without
inventing extra phase states: handoff can remain `NOT_OBSERVED`,
`REJECTED_BY_THULIA`, or `HANDOFF_UNKNOWN`; custody storage can be `FAILED` or `OUTCOME_UNKNOWN`; Gloss
can be not ready, snagged, terminally uncommitted, or outcome-unknown; readable
storage can be `FAILED` or `OUTCOME_UNKNOWN`, and readable receipt can be
`REJECTED` or `UNKNOWN`; retention can be
`FRICTION_UNKNOWN_HOLD`; canonical effects and recoverability can remain
unknown. Each branch preserves its exact query, reconciliation, or reopening
route. Silence is never completion, success, deletion, or permission to keep
raw inspection access forever.

The ordered records therefore cover every release boundary without a generic
catch-all “done” or “hold” state:

| Boundary | Non-success or hold-bearing state | What remains preserved |
|---|---|---|
| Member intake | bundle `INVALID`, `VALIDITY_UNKNOWN`, `UNKNOWN`, or `NOT_PRODUCED` | Member identity, candidate query, and typed exception; no intake admission |
| Return Manifest / Carry Selection | `NOT_PRODUCED`, `UNKNOWN`, `INVALID`, `VALIDITY_UNKNOWN`, `INCOMPLETE`, or `COVERAGE_UNKNOWN` | Same preallocated identity and exact query or successor route; no handoff |
| H→T handoff | target `NOT_OBSERVED`, `REJECTED_BY_THULIA`, or `HANDOFF_UNKNOWN`; source `NOT_EMITTED` or `EMISSION_UNKNOWN` | Immutable Carry Selection and same-transaction reconciliation |
| Selected-carry custody store | `NOT_ATTEMPTED`, `FAILED`, or `OUTCOME_UNKNOWN` | Raw inspection remains `OPEN_BOUNDED`; same custody outcome is queried |
| Inspection access drop | `CLOSE_PENDING` or `CLOSE_OUTCOME_UNKNOWN` | Same closure transaction; no forgetting claim |
| Gloss readiness / turn | `NOT_READY`, `READINESS_UNKNOWN`, `COMMITTED_SNAG`, `OUTCOME_UNKNOWN`, or `NOT_COMMITTED_TERMINAL` | Pinned turn identity, typed snag, or exact same-turn reconciliation route |
| Readable envelope / return | store `NOT_ATTEMPTED`, `FAILED`, or `OUTCOME_UNKNOWN`; incomplete/stale/validity-unknown reference; `NOT_EMITTED`, `EMISSION_UNKNOWN`, `REJECTED`, or receipt `UNKNOWN` | Envelope identity, store receipt, four return axes, and one preallocated return identity remain independent |
| Systemic Friction | `FRICTION_UNKNOWN_HOLD` | Carry and dependencies remain protected pending bounded review |
| Canonical retention / recovery | `NOT_REQUESTED`, `FAILED`, `OUTCOME_UNKNOWN`, or `RECOVERABILITY_UNKNOWN` | Prior store state, effect identity, declared boundary, and reconciliation route |

“Hold” is thus a consequence of the governing canonical state and obligations,
not a parallel state family that can conceal which observation failed.

Every controller-owned **authority bundle** is immutable. Its
`authority_bundle_ref` names and digest-binds, without merging:

- Hearthline's separate Work-plus-Task-Keeper provisioning grant;
- Thulia's separate Ledger-Keeper provisioning grant;
- the Work, Task-Keeper, and Ledger-Keeper member grants;
- the permitted recipient, audience, disclosure, and return limits; and
- the permitted consequence and external-effect limits.

The controller derives one aggregate `authority_epoch` from the exact bundle
identity and component digests. The epoch does not replace or widen any
component grant. If any component is issued, narrowed, superseded, revoked,
expired, rerouted, or otherwise changed, the controller appends a successor
authority bundle, advances the aggregate epoch, and fences the old aggregate.
It never mutates a component beneath an unchanged bundle digest.

Resume and task-effect admission must match the dispatch-pinned
`objective_epoch`, `authority_bundle_ref`, aggregate `authority_epoch`, and
every still-valid component grant. Admission of an already `SEALED` and
`VALID` old-epoch body to Hearthline intake instead requires the separately
issued current terminal-return/custody grant described above; that grant does
not make the task epoch current. Selected-carry admission by Thulia and readable
return admission by Hearthline each require their own current lane, recipient,
content, and disclosure grants. A separately
authorized target audit lane may still append the minimal accounting
observation `REJECTED` or `UNKNOWN` for the attempted relay transaction when a
recipient, content-admission, grant, or epoch check fails; that receipt neither
admits nor exposes the payload. A stale admission match fails closed and
returns the candidate typed disposition `STALE_OBJECTIVE_EPOCH` or
`STALE_AUTHORITY_EPOCH` plus an exact TETHER reopening handle; it never silently
chooses the newest epoch or treats useful purpose ancestry as renewed
permission. These are candidate Task Triad dispositions, not adopted PAL or
repository-wide status values.

### Per-member execution, bundle, liveness, and custody axes

Every member keeps five orthogonal observations. `member_execution_state` is
exactly `NOT_DISPATCHED`, `ACTIVE`, `SPARK_SUSPENDED`, `RETURN_ONLY`,
`SEALED_TERMINAL`, `UNSEALED_TERMINAL`, or `EXECUTION_UNKNOWN`.
`member_candidate_bundle_state` is exactly `NOT_PRODUCED`, `SEALED`, or
`UNKNOWN`. `member_candidate_bundle_validity_state` is unset unless the bundle
is `SEALED`, then exactly `VALID`, `INVALID`, or `VALIDITY_UNKNOWN`.
`liveness_state` remains unset before dispatch and the first due observation,
unless execution becomes terminal first. After a due observation it is exactly
`OBSERVED_WITHIN_CONTRACT`, `MISSED_BOUNDARY_UNKNOWN`, or
`OBSERVATION_UNAVAILABLE`; terminalization sets
`NOT_APPLICABLE_AFTER_TERMINAL`. `homecoming_custody_state` remains the separate
return/custody axis.

None may be cast into another. Liveness does not prove execution, progress,
completion, bundle existence, validity, or custody; execution does not imply a
liveness observation. Either terminal execution state requires
`NOT_APPLICABLE_AFTER_TERMINAL` on the liveness axis. A controller-observed
candidate append atomically commits bundle `SEALED` and execution
`SEALED_TERMINAL`, fences further execution, and closes that member's exclusive
bounded write capability; later validation and custody remain separate. A
sealed body that validates `INVALID` remains `SEALED` and `SEALED_TERMINAL` but
is barred from Hearthline task-intake custody; `VALIDITY_UNKNOWN` is barred too,
and invalidity never rewrites existence into `NOT_PRODUCED`.

An ambiguous candidate append or acknowledgement records bundle `UNKNOWN` and
execution `EXECUTION_UNKNOWN`, leaves validity and custody unset, and queries
the same preallocated candidate identity without replay. A later authoritative
no-append observation appends a new observation changing bundle existence from
`UNKNOWN` to `NOT_PRODUCED`; it does not rewrite the earlier observation. If
the exact retained body is still available and authorized, execution may enter
`RETURN_ONLY` for one bounded same-body, same-identity seal attempt and no task
action. Otherwise it enters `UNSEALED_TERMINAL`, and any new work needs a
successor dispatch. `SEALED_TERMINAL` and `UNSEALED_TERMINAL` never resume;
only separately authorized custody continuation may follow an already sealed
bundle.

Every bound candidate identity carries an exact same-identity query route even
when no body is retained. The retained-body reopening route is a different,
conditional field: it exists only when an authorized locator and integrity
check can recover the exact body governed by the expected digest **or**
validation rule. Candidate preallocation and bundle `UNKNOWN` never imply that
such bytes survive.

The other `RETURN_ONLY` entrance applies only to a still-live `ACTIVE` or
`SPARK_SUSPENDED` member after cancellation, revocation, or staleness. It may
prepare only the frozen return-rule body, including a zero-content typed return
when disclosure is barred. The authoritative-no-append entrance above permits
only the retained same-body, same-ID seal attempt. Neither entrance permits
renewed task action.

## Home, heartbeat, and Homecoming identities

Every dispatch pins one exact Home Record before work begins. That record
binds the exact Spark and profile, coordinator or parent account, return lanes,
audience, accepted bundle, reconciliation rule, retention boundary, and failure
route. A Home change appends a successor record. It does not silently reroute an
active Spark or merge two Spark lineages. Home metadata routes and constrains
custody; it does not authorize return, disclosure, admission, or retention. A
return revalidates those authorities and follows only an ordered authorized
reroute-or-revocation chain from the dispatch-pinned record.

In preserved pre-v0.8 ancestry, a Paired Spark dispatch received its pair
number before either member began. It bound exactly one Work Spark and one
Ledger Scribe Spark, their separate profiles, roles, grants, Homes, heartbeat
contracts, budgets, contexts, Static versions, and the shared Run Trail
projection. The pair identifier linked their returns; it did not make them one
identity or let either allocate, authorize, or complete the other. Pairing was
non-recursive: the Ledger Scribe did not receive another Ledger Scribe from
that rule.

That preserved design used one paired dispatch by default and allowed an
authorized operator to predeclare an unpaired exception, which was ineligible
for learned Static promotion or carry from that run. The candidate v0.8
successor does not rewrite those records; it allocates the separately named
Task Triad identities above for new candidate formations.

Every Spark Heartbeat Contract and every issued Pulse Receipt receives its own
ordered identity, including liveness-only pulses. A Spark may propose a payload;
only the canonical controller or store allocates and appends the receipt. A
pulse records only declared liveness or material change, the timing assumption
then in force, actual coverage, remaining limits, and the next reasoned boundary.
Empty checks create no outward receipt unless the contract expressly requires a
bounded liveness record. A cadence adjustment appends a successor heartbeat
contract; it cannot alter scope, authority, expiry, time, action count, cost
ceiling, or budget.

Task Triad members retain three separate Heartbeat Contracts. The Task-Keeper
keeps the frozen Task Line and completion boundary; it does not own, mint, or
substitute for another member's Pulse Receipt. If it runs in the same process,
session, context window, or host failure domain as the work it observes, it
cannot serve as that host's watchdog. A visible spinner, `Working` label,
animated indicator, or unchanged loading surface is unnumbered presentation
telemetry. It is not a Pulse Receipt and establishes neither liveness, work
progress, suspension, completion, permission, nor authority.

The external canonical controller or durable store owns the maximum-pulse
deadline, timeout observation, grant-revocation and member-execution
transitions, wake condition, and Resume Receipt. “External” here means available across the
failure boundary being watched. A monitor that fails with the watched host may
offer diagnostic telemetry, but it cannot certify that host's liveness.

Before a nonterminal blocker or no-due-work boundary enters
`SPARK_SUSPENDED`, the canonical controller appends exactly one
contract-bounded Pulse Receipt for that boundary. The Spark records no further
task action until a valid Resume Receipt. A declared terminal blocker begins
return. Missing the maximum pulse boundary records
`MISSED_BOUNDARY_UNKNOWN` or `OBSERVATION_UNAVAILABLE` as the evidence warrants
and moves execution to `SPARK_SUSPENDED` or `RETURN_ONLY` only as the contract
authorizes; it does not infer completion or silent continuation.

Suspension and resume use separate ordered receipts. `SPARK_SUSPENDED` records
the last committed boundary, next wake condition, dispatch-pinned Home and
contract, consumed limits, and unresolved work. Resume revalidates the original
grant, revocation state, Home, contract, and remaining limits, then the canonical
controller preserves the consumed amounts in a successor receipt. It neither
deletes the suspension nor creates renewed authority.

Reopening records are stage-conditional. `TRIAD_FORMATION_REQUESTED` or
`TRIAD_FORMATION_PENDING` carries the request and Hearthline nomination plus
only later records that actually exist; it requires no offer, reservation,
member, binding, or dispatch. `TRIAD_FORMATION_OFFERED` additionally requires
the frozen offer, both available own-seat nominations, authority bundle and
epoch, and reserved members, Homes, lanes, and candidate identities, but no
member execution or bundle state. `TRIAD_BOUND` adds both final intents, the
atomic binding receipt, bound members, and consumed candidate reservations;
all member execution states remain `NOT_DISPATCHED` and liveness remains unset
until a separate dispatch receipt. Only `DISPATCHED` requires the full active
or suspended member family below. Refused or stale stages preserve every
earlier record and leave future-stage fields unset.

When one or more Task Triad member executions are suspended, or when the
controller suspends the coordinated objective, the exact reopening family
additionally binds:

- the frozen Goal version, every traversed `NARROWS` Purpose Projection, Task
  Line version, `objective_epoch`, and Completion Contract version;
- the Task Triad and dispatch identities, formation request, both nonbinding
  own-seat nominations, controller-frozen offer and digest, Hearthline and
  Thulia final provisioning intents, and the atomic controller binding receipt;
- each of the three exact member, profile, grant, Spark Heartbeat Contract,
  last pulse or suspension, and dispatch-pinned Home references;
- each member's separate `member_execution_state`,
  `member_candidate_bundle_state`, `member_candidate_bundle_validity_state`,
  and `liveness_state`, without deriving an aggregate Triad liveness or bundle
  state or casting one member axis into another;
- each member's preallocated candidate-bundle identity and idempotency key,
  expected body digest **or** validation rule, the always-required exact
  same-identity query route, and the separately optional retained-body
  reopening handle needed only for seal-only recovery;
- the last committed Work, Ledger, and task-boundary positions without
  inventing a missing return or witness;
- the finite Owl-turn and candidate identities, candidate idempotency key,
  exact input and expected-body digests, optional retained-body reopening
  handle, and separate transaction, candidate-presence, candidate-validity,
  and disposition axes;
- every member's separate `homecoming_custody_state`, the
  separate Hearthline intake receipt where present, Return Manifest, Carry
  Selection and its coverage state, Translation Board and serviceability
  references where present, current selected-carry transaction, idempotency
  key, `carry_handoff_emission_state`, target-owned `carry_handoff_state`,
  durable Thulia receipt, and selected-carry custody-store outcome;
- only for an already allocated predecessor relay family, its exact
  `triad_relay_envelope_ref`, `owl_relay_reference_state`,
  `owl_relay_validity_state`, `owl_relay_emission_state`, and independently
  numbered `relay_target_receipt_state`;
- the independent readable-return transaction and Hearthline target receipt,
  Readable Carry Envelope and store outcome, per-turn Gloss readiness
  observation, exact four lane references, immutable
  root-task map and lexicon-generation references, Return Manifest and Carry
  Selection axes, selected-carry custody-store outcome, inspection-context
  state, Systemic Friction classification, later canonical-store effect, and
  boundary-scoped recoverability observation where present;
- the status of every ancestor goal or task at the suspension boundary,
  including cancellation, replacement, narrowing, hold, and unknown states;
- consumed and remaining time, action, cost, context, disclosure, and other
  declared limits, together with unresolveds and the next wake condition;
- the dispatch-pinned controller, immutable `authority_bundle_ref`, aggregate
  `authority_epoch`, and separate Hearthline, Thulia, member, recipient, and
  effect-authority components, plus the separate current terminal-return and
  custody grant when an old-epoch sealed valid body is being moved; and
- a stale-epoch fence requiring exact objective-epoch, authority-bundle, and
  aggregate-authority-epoch matches plus current validation of every component
  before any member resumes or any external effect is admitted.

Those records may be carried compactly through TETHER, but the handle does not
replace their source identities. If an ancestor, objective epoch, authority
epoch, grant, Home, contract, or member continuation cannot be revalidated,
the controller records the typed stale or unknown state, performs no further
task action or effect, and preserves a route to reframe or redispatch. It does
not wake the old Triad under a convenient successor.

Reopening is evaluated per member. `SPARK_SUSPENDED` may be eligible for a
Resume Receipt after every required revalidation. `SEALED_TERMINAL` is not: it
refuses further task action and permits only the separately authorized custody,
Homecoming, Hearthline intake, selected-carry, or target-receipt continuation
for a `SEALED` and `VALID` candidate bundle. `INVALID`, `VALIDITY_UNKNOWN`, and
bundle `UNKNOWN` remain outside intake custody. A pending custody state never
turns terminal execution back into live execution.

Homecoming allocates its identity before return begins. The canonical controller
then appends separate Return, Reconciliation, and Context-Close Receipts beneath
that identity:

`HOMECOMING:RETURNED != HOMECOMING:RECONCILED != HOMECOMING:CONTEXT_CLOSED`

Arrival does not establish admission to the Home. Reconciliation revalidates the
dispatch-pinned Home, current grant, recipient, disclosure, retention, expiry,
revocation, and authorized reroute chain; it does not establish task success,
carry approval, Static activation, or context closure. A separate Context-Close
Receipt ends the active child context after reconciliation or an explicit
terminal failure disposition. `HOMECOMING:CONTEXT_CLOSED` is not PAL or A15
closure and does not erase artifacts, residuals, failures, external effects, or
reopening handles. Partial, rejected, revoked, and unknown returns retain their
identities and exact dispositions. An unknown Homecoming is reconciled under its
existing identity and is never replayed automatically.

For the v0.9 route, the declared member Home terminates at the controller-owned
Hearthline task intake. Each eligible bundle therefore begins custody as
`RETURN_PENDING_HEARTHLINE` and receives its own Return and Reconciliation
Receipts. Thulia sees only the later immutable Carry Selection offered through
the distinct Hearthline-to-Thulia lane; she is not an implicit first custodian
of the three raw member bodies.

The candidate-bundle seal has already closed the returned Spark's exclusive
bounded account write lane. Reconciliation records canonical store custody; it
does not perform or repeat that execution/write fence. Reopening the same
account later requires a new lane grant; neither the Spark ordinal nor earlier
authorship is a continuing write or retention claim.

Homecoming is not retirement. After a separate Context-Close Receipt, the Spark
may later receive another authorized dispatch under an established
continuation, while its earlier Homecoming and consumed limits remain
historical. A replacement process that lacks the required continuation evidence
begins under a new Spark identity.

An open objective window receives its identity before the first objective is
admitted. Every addition, replacement, cancellation, clarification, return,
reconciliation, and explicit `OBJECTIVE:LEFT_OPEN` disposition appends a
successor objective-set snapshot; it never rewrites membership in place. Each admitted
objective points to its own Spark or Creature identity and independent grant,
budget, ledger, heartbeat, Home, and Homecoming chain. Completion order does not
allocate identity, priority, authority, or result status.

An aggregation close binds one exact objective-set snapshot and references each
objective's separately typed `homecoming_custody_state` and
`objective_disposition`. It may assemble one audience-facing response, but it
does not merge source ledgers, let Homecoming custody assign task status, or
turn `OBJECTIVE:BLOCKED`, `OBJECTIVE:UNKNOWN`, or `OBJECTIVE:LEFT_OPEN` into
completion. A heartbeat cannot append a new objective, keep the host window
alive, or allocate the close receipt; those are controller and host-lifecycle
operations.

## Static proposals and activations

A same-account-lineage candidate Static revision receives the next Static
version ordinal when proposed. A cross-account target-bound `static_delta`
remains an Ember in its source representation account and receives no target
version until the target account's authorized writer admits and allocates it after direction-bound
carry. Neither waits for success to become historically visible.

Its lifecycle may include distinct states such as:

`PROPOSED -> VERIFIED -> ACTIVATED -> SUPERSEDED`

or:

`PROPOSED -> REJECTED`

No arrow is automatic. Exact round-trip verification is necessary for Static admission but does not itself approve or activate a version. Concurrent proposals are serialized by activation receipts; wall-clock completion, repeated recommendation, or last write does not choose the winner.

A failed activation leaves the preceding active version unchanged. Earlier entries always decode under the exact Static version they originally named.

## Field Notes pages and refresh

Every Field Notes page receives the next notes ordinal before writing begins. A page binds the Spark, Fireside and run, declared lens, permitted Run Trail view, exact Static version, opening event boundary, and predecessor page.

At refresh, the coordinator seals the existing page with its final digest, coverage watermark, and completion state. It then opens a newly numbered blank page under the admitted Static version. The new page may carry explicit loaded context, but it does not inherit the predecessor's unwritten assumptions.

The page becomes blank; the history does not. Sealed pages, incomplete pages, residuals, and pending Embers remain addressable under their original numbers.

## Owl Scribe and Bridge Gloss identities

Thulia's adopted public lore identity is `OWL-000001`, with current design
profile `OWL-000001/PROFILE-000004`, distinct from the Spark registry because
Owl Scribe is a bounded custody, translation, and retention-classification
interface rather than a fourth Spark role. It is not evidence that an
operational allocator, service, or model instance exists. Any model-assisted
interpretive work behind that interface still receives a distinct Spark
identity, role, profile, exact job, task account, write lane, and grant.

The Hearth Perch is Thulia's separately numbered Home series. It binds the Owl
Scribe return boundary and the dispatch-pinned roost index and version
without becoming a shared Static Perch, global codebook, or authority source.
Work Static returns unchanged to its task-account source Perch; Scribe-authored target-bound
proposals return first to the representation-account source Perch; and Thulia's candidate
custody and representation-side return payloads return to the Hearth Perch for
canonical controller reconciliation.

Thulia's routing records preserve four non-interchangeable one-way lanes:
Hearthline-to-Thulia selected carry, Thulia-to-Gloss request,
Gloss-to-Thulia deterministic return, and Thulia-to-Hearthline readable return.
Each lane has its own source, target, direction, payload ceiling, grant, epoch,
transaction, and receipt. A receipt on one lane neither opens nor proves
delivery on another. Thulia may mediate the crossings and alone apply Systemic
Friction, but cannot originate Hearthline's Carry Selection or shorthand
serviceability decision.

Each Perch identifies one partitioned task- or representation-account Static
lineage. A new Perch version appends changes to its pointer index, access path,
reconstruction handles, availability state, retention holds, or unresolved
exceptions without altering the earlier version. It does not duplicate the
account payload. A Perch number never becomes a shared codebook identity.

An Owl character sheet is a presentation record. A successor sheet may revise appearance, voice, mannerisms, poses, or other narrative cues while preserving its predecessor, but it cannot alter Owl Scribe behavior, access, authority, or the governing Owl profile. An identity-bearing design change belongs in a separately numbered profile successor.

An image identity is likewise a presentation record. The [visual index](HEARTHLINE_VISUAL_INDEX.md) binds each registered image to its exact repository path, dimensions, digest, status, and known residuals. A study, scene, correction, or successor keeps its own image number; moving an older image to a clearly labeled history view does not renumber or erase it. An image number does not create a character, memory, capability, trigger, credential, permission, or controlling design rule.

Every translation attempt receives its request number before work begins. Every successfully recorded Bridge Gloss receives its own gloss number, and delivery to each recipient receives a separate delivery number. Denied, failed, ambiguous, interrupted, invalidated, and superseded attempts keep their numbers and dispositions. A direction, destination, audience, or source-version change creates a successor request or gloss rather than silently changing the old one.

A Bridge Gloss number records a derivative crossing only. It does not make the gloss true, exact beyond its declared reconstruction, loaded, adopted, authoritative, or independent of its sending ledger and sources.

The `OWL-000001` prefix identifies the custody series, not ownership of the
payload ledger. A recorded Bridge Gloss offer binds its declared recipient
account; the canonical account writer appends it there, and Thulia retains only
the pointer, status, hold, or unresolved exception needed for custody.

## Gloss Translation Slate identities

Gloss has no ordered memory or ledger series. Before a routine turn, the
canonical translation-account writer allocates a mark identity on one exact
detachable Translation Slate. Gloss deterministically emits the mark body from
the canonical note, complete route, direction, and pinned lexicon generation;
the account writer appends it. Routine translation reads no earlier mark.

Gloss also has no Heartbeat Contract. Before each finite turn, the controller
allocates a separate readiness-observation identity and records exactly
`READY_FOR_EXACT_TURN`, `NOT_READY`, or `READINESS_UNKNOWN`. That observation is
neither maintained by Gloss nor inherited by a successor turn. A missing or
unknown observation produces a typed hold or failure; it never becomes
persistent readiness by default.

The slate belongs to the translation account, not to Gloss or Thulia. Thulia
has bounded custody of its identity, validated lexicon-generation pointer,
availability state, retention holds, and unresolved exceptions. A replacement
slate receives a successor slate identity and a verified continuation or
explicit gap. It is a replaceable interface, not part of Gloss's body or
memory.

The Translation Board and active shorthand map are account-owned records, not
Gloss memory. Every request names an immutable map reference and lexicon
generation. Only Hearthline may append the semantic decision that a mapping is
serviceable for the exact active root task. At root-task end the map records
`RETIRED_AT_TASK_CLOSE` for every active `SERVICEABLE` mapping and drops the
live map; later work must reopen the exact retained generation and obtain
current access and a current Hearthline serviceability decision.

## Creature and campaign identities

A Creature identity names one frozen composition boundary. Its profile binds the
exact member Sparks, paired dispatches, model/runtime artifacts, source lock,
grants, budgets, Homes, heartbeat contracts, ledger partitions, Thulia profile,
evaluation rule, stop conditions, and return routes. Changing any identity-
bearing field appends a successor Creature profile; it does not mutate a running
manifest.

A strategy replacement or materially changed composition is a `SUCCESSOR`; an
experimental fork is a `CHILD`; and a same-identity record update that preserves
its declared continuation is a `VERSION`. These relationships do not merge
evidence or authority.

Matched experimental arms receive different Creature and arm identities and
physically separate ledgers. Their external campaign index may bind comparable
fields and sealed results by reference only. It is not a shared payload store,
decoder, grant, budget, or source of cross-arm context. A cooperative Creature
may contain several advisory Sparks under separate accounts, but one canonical
controller serializes allocation, promotion, and external effects.

## Concurrency and crash behavior

One canonical allocator assigns ordinals for each series. Sparks may submit candidate records concurrently using stable idempotency keys, but they do not allocate their own canonical numbers, co-write one ledger, or resolve collisions by overwriting.

Allocation and append must be atomic or fail closed. After a crash, restoration never moves a counter backward. Ambiguous, partially reserved, or duplicated submissions preserve gaps and are reconciled through new records rather than renumbering accepted history.

An exact retry with the same idempotency key returns the same allocation. A genuinely new attempt receives the next number. Only allocation and canonical append need serialize; Spark investigation and candidate production may remain concurrent.

For branched or offline work, an implementation may preallocate a recorded range or use a distinct registry namespace. It must not create two records that claim the same full identity. When material crosses registries, the original identity remains provenance and any locally adopted successor receives a new local identity.

## Retention, redaction, and tombstones

The preservation promise is **no silent overwrite, reuse, or erasure**. It does not defeat lawful deletion, privacy removal, safety quarantine, or an applicable retention limit.

When bytes must be removed, the system preserves the ordinal and an accountable tombstone where lawful, records the availability change, invalidates dependent uses as needed, and narrows claims that can no longer be checked. A digest alone is not treated as recovery of deleted content.

Only Thulia applies **Systemic Friction** to issue a retention classification
under a separate grant. A Spark may raise a retention defect only by naming a
concrete replay, open, contest, privacy, safety, or other account obligation.
It has no self-preservation veto and does not own the ledger merely because it
wrote through a bounded lane. `PRUNE_ELIGIBLE` does not erase anything; a
canonical controller or separately authorized writer must perform and receipt
the exact **Atomic Edge Promotion**.

Systemic Friction weighs the already immutable Carry Selection; it cannot
originate Hearthline's semantic keep choice. Selected-carry custody storage,
Hearthline's inspection-close edge, Thulia's later classification edge, the
later canonical store/prune edge, and its boundary-scoped recoverability
observation receive separate identities and dispositions. A missing
measurement or retention decision records `FRICTION_UNKNOWN_HOLD`; an
ambiguous custody or canonical effect records `OUTCOME_UNKNOWN`; uncertain
recoverability records `RECOVERABILITY_UNKNOWN`. Each preserves its exact
reconciliation or reopening route. No unknown becomes permission to prune or
permission to keep raw inspection access indefinitely.

## Implementation boundary

This document specifies names and invariants. It does not create a registry, allocator, Spark, Fireside, ledger, runtime, or adoption event.

Any implementation must test atomic controller-owned allocation, monotonic
recovery, idempotent submission, gap preservation, immutable predecessor
binding, Goal-version and `NARROWS` Purpose-Projection ordering, immutable Task
Line and Completion Contract versioning, acyclic purpose-edge enforcement,
objective- and authority-epoch
fencing, immutable authority-bundle component binding and aggregate digest
succession, Task Triad and separate member-binding allocation,
Hearthline/Thulia nonbinding own-seat nomination separation,
controller-frozen formation-offer identity and digest, independent final
own-seat intents, controller-only atomic compare-and-swap co-binding to one
exact frozen task, offer-time candidate-bundle reservation, inert
`TRIAD_FORMATION_OFFERED` and `TRIAD_BOUND` states plus separate dispatch,
Task-Boundary Witness
presence and optional-reference constraints, conditional boundary-state value
and evidence constraints, immutable `UNKNOWN` plus numbered
late-evidence succession, current `carry_handoff_emission_state` and
target-owned `carry_handoff_state` separation, preallocated idempotent
selected-carry transactions, `EMISSION_UNKNOWN` reconciliation without
automatic resend, and predecessor-only `owl_relay_*` compatibility with a
mandatory exact `triad_relay_envelope_ref`,
separate `RETURN_PENDING_HEARTHLINE` member intake, immutable Hearthline Carry
Selection and Translation Board requests, Hearthline-only root-task shorthand
serviceability, independent selected-carry and readable-return transactions,
four direction-bound Thulia/Gloss lanes, per-turn controller-observed Gloss
readiness without heartbeat inheritance, durable Thulia-receipt and authorized
selected-carry custody-store gating before inspection close, inspection close
before optional Gloss/readable-return work, later Systemic Friction and
canonical store-or-prune effects, independent boundary-scoped recoverability,
and complete success, rejection, unknown, and hold dispositions,
separate formation and dispatch states and receipts, finite Owl-turn and
candidate identities, transaction/existence/validity/disposition separation,
`CANDIDATE_SEAL_ONLY` recovery for only an exact retained same-body/same-ID
append after authoritative no-append, with no renewed Owl judgment,
member-replacement succession, per-member `member_execution_state`,
`member_candidate_bundle_state`, `member_candidate_bundle_validity_state`,
`liveness_state`, and `homecoming_custody_state` separation, atomic seal,
ambiguous-seal reconciliation, authoritative no-append succession, exact
return-only and terminal behavior, rejection of aggregate Triad liveness,
terminal task-action refusal with custody-only continuation for sealed bundles,
current separate terminal-return/custody authority for old-epoch sealed valid
bodies without task-authority revival,
exact per-member and coordinated-objective
suspension reopening bundles,
rejection of spinner or `Working` telemetry as pulse or progress, externally
owned timeout/wake/resume behavior, same-failure-domain watchdog rejection,
paired-dispatch allocation and explicit unpaired exceptions, separate
pair identities, budgets, and Static references, dispatch-pinned Home binding,
authorized reroutes, heartbeat and all-pulse ordering, blocker and missed-pulse
behavior, suspension/resume preservation, returned/reconciled/context-closed
separation, idempotent and unknown Homecoming reconciliation, separated
proposal and activation series, account-custodied target-bound deltas, cross-registry
collision handling, Hearth Perch and Static Perch isolation, recipient-specific
gloss delivery, detachable Translation Slate and account-owned mark allocation,
history-free deterministic turns, sealed-page immutability, lawful tombstoning, Creature profile
succession, physically isolated campaign arms, campaign-index noninterference,
one canonical effect-admission and serialization path, exclusive bounded Spark
write lanes and candidate-seal closure, retention-defect qualification,
Thulia-only Systemic Friction classification, rejection of self-preservation
vetoes, and failure when the
active version cannot be established.

Ordered lineage preserves addressability. It does not manufacture memory, identity continuity, consciousness, consent, standing, permission, or authority.

Numbering makes reuse, unexplained gaps, and omitted predecessors detectable within a verified ledger. Numbering alone cannot prove that an entire ledger or repository history was never rewritten; that stronger claim requires preserved bytes, verified hash links and checkpoints, and an external anchor appropriate to the claimed scope.
