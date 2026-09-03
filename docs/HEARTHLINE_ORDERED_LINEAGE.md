# Hearthline Ordered Lineage

> **A successor receives a new number. It does not receive permission to erase its predecessor.**

| Field | Value |
|---|---|
| Version | `0.5` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Ordered Lineage** is the identity and versioning discipline for Hearthline Sparks, [Creatures](HEARTHLINE_CREATURES.md), Firesides, Static, Field Notes, Embers, [Thulia's](HEARTHLINE_THULIA.md) Owl Scribe records, [Homes and Homecomings](HEARTHLINE_HOMECOMING.md), and their receipts.

Its purpose is simple: every Spark and every new version receives an ordered number, and earlier work remains individually addressable. Correction, retirement, rejection, or replacement may change what governs later work; none silently makes an earlier record disappear.

An ordered number is an identifier inside a declared ledger scope. It records allocation and sequence only. It does not establish rank, seniority, quality, truth, personhood, experiential continuity, ownership, capability, permission, or authority.

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
| Homecoming | `SPARK-000001/HOMECOMING-000001` | That Spark's Homecoming series |
| Homecoming Return Receipt | `SPARK-000001/HOMECOMING-000001/RETURN-000001` | One Homecoming's return series |
| Homecoming Reconciliation Receipt | `SPARK-000001/HOMECOMING-000001/RECONCILIATION-000001` | One Homecoming's reconciliation series |
| Homecoming Context-Close Receipt | `SPARK-000001/HOMECOMING-000001/CONTEXT-CLOSE-000001` | One Homecoming's context-close series |
| Static version | `SPARK-000001/STATIC-000001` | That Spark's isolated Static lineage |
| Static entry | `SPARK-000001/STATIC-000001/ENTRY-000001` | One Static version |
| Field Notes page | `SPARK-000001/NOTES-000001` | That Spark's notes series |
| Ember | `SPARK-000001/EMBER-000001` | That Spark's candidate-carry series |
| Fireside | `FIRESIDE-000001` | One named Fireside registry |
| Run | `FIRESIDE-000001/RUN-000001` | That Fireside's run series |
| Run Trail event | `FIRESIDE-000001/RUN-000001/EVENT-000001` | That run's committed event series |
| Static activation receipt | `SPARK-000001/STATIC-ACTIVATION-000001` | That Spark's Static activation series |
| Carry Manifest | `FIRESIDE-000001/RUN-000001/CARRY-000001` | That run's reviewed carry series |
| Load receipt | `FIRESIDE-000001/RUN-000001/LOAD-000001` | That run's context-load series |
| Owl Scribe | `OWL-000001` | One named Owl registry |
| Owl profile version | `OWL-000001/PROFILE-000001` | That Owl Scribe's profile series |
| Owl character sheet | `OWL-000001/SHEET-000001` | That Owl Scribe's appearance-sheet series |
| Hearth Perch | `OWL-000001/HEARTH-PERCH-000001` | That Owl Scribe's Home series |
| Hearth Perch version | `OWL-000001/HEARTH-PERCH-000001/VERSION-000001` | One Hearth Perch's version series |
| Perch | `OWL-000001/PERCH-000001` | That Owl Scribe's partition directory |
| Perch version | `OWL-000001/PERCH-000001/VERSION-000001` | One Perch's version series |
| Translation request | `OWL-000001/REQUEST-000001` | That Owl Scribe's request series |
| Bridge Gloss | `OWL-000001/GLOSS-000001` | That Owl Scribe's gloss series |
| Gloss delivery receipt | `OWL-000001/GLOSS-000001/DELIVERY-000001` | One gloss's recipient-delivery series |

The full identity also binds immutable registry and entity IDs. `SPARK-000001` in two unrelated registries is not one Spark. A portable reference therefore includes at least the registry identity, typed ordinal, stable entity identity, parent scope, and exact record digest.

## Allocation rules

1. **Allocate before use.** The coordinator commits a Spark number before that Spark begins work and commits a version number before content is recorded under that version.
2. **Increase within one named series.** Every successor takes the next available ordinal in its declared parent scope. Separate record types use separate series; their numbers are not compared as though they shared one clock.
3. **Never reuse or renumber.** Once issued, an ordinal is never reassigned, compacted away, shifted to close a gap, or given to a different record.
4. **Preserve unsuccessful numbers.** A rejected proposal, failed construction, interrupted allocation, or abandoned reservation retains its number and terminal status. Every issued number ends in a materialized record or an explicit `ABORTED`, `VOIDED`, `UNKNOWN`, or lawful `TOMBSTONED` disposition. An unexplained gap at or below the series high-water mark is an integrity failure.
5. **Append corrections.** A correction creates a newly numbered successor that names its predecessor, reason, and disposition. It never edits history into agreement with the correction.
6. **Separate version from activation.** A proposed version receives its own version ordinal. Verification, approval, activation, supersession, rejection, and retirement are separate, ordered receipts. A version can therefore remain permanently proposed or rejected without its number being reused.
7. **Derive what is active.** The governing Static or profile version is determined from valid activation receipts under the current grant, not from an overwriteable `latest` field. Convenience pointers may be cached but are not authoritative history.

Every record should bind its typed ID, stable entity ID, parent ledger, predecessor where applicable, status, creation receipt, content digest, producer and tool identities when relevant, scope, and reason for change. Every disposition change appends a new ordered, hash-linked registry event rather than editing the old event in place.

## Spark identity and versions

A new Spark receives a new Spark ordinal even if it has the same model, role, job, lens, or display name as an earlier Spark. Reuse of a name does not create identity continuity.

A Spark may retain its stable Spark ordinal through profile versions when the exact ledger identity and authorized continuation are re-established. Changes to its role, job, lens, grant binding, model binding, or other identity-bearing configuration append a new profile version. A replacement process that cannot establish that continuation begins as a new Spark.

Retiring a Spark appends a retirement record. Reopening may append a new profile version if the continuation requirements are met; it does not delete the retirement or pretend the interruption did not occur.

## Home, heartbeat, and Homecoming identities

Every dispatch pins one exact Home Record before work begins. That record
binds the exact Spark and profile, coordinator or parent account, return lanes,
audience, accepted bundle, reconciliation rule, retention boundary, and failure
route. A Home change appends a successor record. It does not silently reroute an
active Spark or merge two Spark lineages. Home metadata routes and constrains
custody; it does not authorize return, disclosure, admission, or retention. A
return revalidates those authorities and follows only an ordered authorized
reroute-or-revocation chain from the dispatch-pinned record.

A Paired Spark dispatch receives its pair number before either member begins.
It binds exactly one Work Spark and one Ledger Scribe Spark, their separate
profiles, roles, grants, Homes, heartbeat contracts, budgets, contexts, Static
versions, and the shared Run Trail projection. The pair identifier links their
returns; it does not make them one identity or let either allocate, authorize,
or complete the other. Pairing is non-recursive: the Ledger Scribe does not
receive another Ledger Scribe from this rule.

Primary Work Spark dispatches use one paired dispatch by default. An authorized
operator may predeclare an unpaired exception, which receives its own record and
is ineligible for learned Static promotion or carry from that run.

Every Spark Heartbeat Contract and every issued Pulse Receipt receives its own
ordered identity, including liveness-only pulses. A Spark may propose a payload;
only the canonical controller or store allocates and appends the receipt. A
pulse records only declared liveness or material change, the timing assumption
then in force, actual coverage, remaining limits, and the next reasoned boundary.
Empty checks create no outward receipt unless the contract expressly requires a
bounded liveness record. A cadence adjustment appends a successor heartbeat
contract; it cannot alter scope, authority, expiry, time, action count, cost
ceiling, or budget.

Before a nonterminal blocker or no-due-work boundary enters
`SPARK_SUSPENDED`, the canonical controller appends exactly one
contract-bounded Pulse Receipt for that boundary. The Spark records no further
task action until a valid Resume Receipt. A declared terminal blocker begins
return. Missing the maximum pulse boundary records liveness as unknown and
suspends or revokes according to the contract; it does not infer completion or
silent continuation.

Suspension and resume use separate ordered receipts. `SPARK_SUSPENDED` records
the last committed boundary, next wake condition, dispatch-pinned Home and
contract, consumed limits, and unresolved work. Resume revalidates the original
grant, revocation state, Home, contract, and remaining limits, then the canonical
controller preserves the consumed amounts in a successor receipt. It neither
deletes the suspension nor creates renewed authority.

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

A same-lineage candidate Static revision receives the next Static version
ordinal when proposed. A cross-Spark target-bound `static_delta` remains an
Ember in its source Spark's lineage and receives no target version until the
target ledger's authorized writer admits and allocates it after direction-bound
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

Thulia's adopted public lore identity is `OWL-000001`, with current design profile `OWL-000001/PROFILE-000003`, distinct from the Spark registry because Owl Scribe is a bounded custody and translation interface rather than a fourth Spark role. It is not evidence that an operational allocator, service, or model instance exists. Any model-assisted interpretive work behind that interface still receives its own Spark identity, role, profile, and grant.

The Hearth Perch is Thulia's separately numbered Home series. It binds her own
Owl Scribe return boundary and the dispatch-pinned roost index and version
without becoming a shared Static Perch, global codebook, or authority source.
Work Static returns unchanged to its source Perch; Scribe-authored target-bound
proposals return first to the Scribe's source Perch; and Thulia's candidate
custody and representation-side return payloads return to the Hearth Perch for
canonical controller reconciliation.

Each Perch identifies one partitioned Spark Static lineage. A new Perch version appends changes to its index, access path, reconstruction handles, or availability state without altering the earlier version. A Perch number never becomes a shared codebook identity.

An Owl character sheet is a presentation record. A successor sheet may revise appearance, voice, mannerisms, poses, or other narrative cues while preserving its predecessor, but it cannot alter Owl Scribe behavior, access, authority, or the governing Owl profile. An identity-bearing design change belongs in a separately numbered profile successor.

Every translation attempt receives its request number before work begins. Every successfully recorded Bridge Gloss receives its own gloss number, and delivery to each recipient receives a separate delivery number. Denied, failed, ambiguous, interrupted, invalidated, and superseded attempts keep their numbers and dispositions. A direction, destination, audience, or source-version change creates a successor request or gloss rather than silently changing the old one.

A Bridge Gloss number records a derivative crossing only. It does not make the gloss true, exact beyond its declared reconstruction, loaded, adopted, authoritative, or independent of its sending ledger and sources.

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

## Implementation boundary

This document specifies names and invariants. It does not create a registry, allocator, Spark, Fireside, ledger, runtime, or adoption event.

Any implementation must test atomic controller-owned allocation, monotonic
recovery, idempotent submission, gap preservation, immutable predecessor
binding, paired-dispatch allocation and explicit unpaired exceptions, separate
pair identities, budgets, and Static references, dispatch-pinned Home binding,
authorized reroutes, heartbeat and all-pulse ordering, blocker and missed-pulse
behavior, suspension/resume preservation, returned/reconciled/context-closed
separation, idempotent and unknown Homecoming reconciliation, separated
proposal and activation series, source-owned target-bound deltas, cross-registry
collision handling, Hearth Perch and Static Perch isolation, recipient-specific
gloss delivery, sealed-page immutability, lawful tombstoning, Creature profile
succession, physically isolated campaign arms, campaign-index noninterference,
one canonical effect-admission and serialization path, and failure when the
active version cannot be established.

Ordered lineage preserves addressability. It does not manufacture memory, identity continuity, consciousness, consent, standing, permission, or authority.

Numbering makes reuse, unexplained gaps, and omitted predecessors detectable within a verified ledger. Numbering alone cannot prove that an entire ledger or repository history was never rewritten; that stronger claim requires preserved bytes, verified hash links and checkpoints, and an external anchor appropriate to the claimed scope.
