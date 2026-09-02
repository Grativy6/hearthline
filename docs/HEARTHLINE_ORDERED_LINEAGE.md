# Hearthline Ordered Lineage

> **A successor receives a new number. It does not receive permission to erase its predecessor.**

| Field | Value |
|---|---|
| Version | `0.3` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Ordered Lineage** is the identity and versioning discipline for Hearthline Sparks, Firesides, Static, Field Notes, Embers, [Thulia's](HEARTHLINE_THULIA.md) Owl Scribe records, and their receipts.

Its purpose is simple: every Spark and every new version receives an ordered number, and earlier work remains individually addressable. Correction, retirement, rejection, or replacement may change what governs later work; none silently makes an earlier record disappear.

An ordered number is an identifier inside a declared ledger scope. It records allocation and sequence only. It does not establish rank, seniority, quality, truth, personhood, experiential continuity, ownership, capability, permission, or authority.

## Typed ordered identities

A future implementation should represent canonical identity structurally, including immutable registry and entity identifiers, a typed record kind, an owner or parent reference, and a numeric ordinal. Human-readable labels are derived views, not the complete canonical identity.

Ordinals are integers from `1` through `2^63 - 1`. Display forms use at least six digits and never wrap; numeric fields rather than strings, timestamps, filenames, or wall-clock completion determine order. The following forms are normative examples of the readable identity structure; exact field encoding remains an implementation decision.

| Record | Example | Ordering scope |
|---|---|---|
| Spark | `SPARK-000001` | One named Spark registry |
| Spark profile version | `SPARK-000001/PROFILE-000001` | That Spark's profile series |
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

## Static proposals and activations

A candidate Static revision receives the next Static version ordinal when proposed. It does not wait for success to become historically visible.

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

Thulia's adopted public lore identity is `OWL-000001`, distinct from the Spark registry because Owl Scribe is a bounded custody and translation interface rather than a fourth Spark role. It is not evidence that an operational allocator, service, or model instance exists. Any model-assisted interpretive work behind that interface still receives its own Spark identity, role, profile, and grant.

Each Perch identifies one partitioned Spark Static lineage. A new Perch version appends changes to its index, access path, reconstruction handles, or availability state without altering the earlier version. A Perch number never becomes a shared codebook identity.

An Owl character sheet is a presentation record. A successor sheet may revise appearance, voice, mannerisms, poses, or other narrative cues while preserving its predecessor, but it cannot alter Owl Scribe behavior, access, authority, or the governing Owl profile. An identity-bearing design change belongs in a separately numbered profile successor.

Every translation attempt receives its request number before work begins. Every successfully recorded Bridge Gloss receives its own gloss number, and delivery to each recipient receives a separate delivery number. Denied, failed, ambiguous, interrupted, invalidated, and superseded attempts keep their numbers and dispositions. A direction, destination, audience, or source-version change creates a successor request or gloss rather than silently changing the old one.

A Bridge Gloss number records a derivative crossing only. It does not make the gloss true, exact beyond its declared reconstruction, loaded, adopted, authoritative, or independent of its sending ledger and sources.

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

Any implementation must test atomic allocation, monotonic recovery, idempotent submission, gap preservation, immutable predecessor binding, separated proposal and activation series, cross-registry collision handling, Perch isolation, recipient-specific gloss delivery, sealed-page immutability, lawful tombstoning, and failure when the active version cannot be established.

Ordered lineage preserves addressability. It does not manufacture memory, identity continuity, consciousness, consent, standing, permission, or authority.

Numbering makes reuse, unexplained gaps, and omitted predecessors detectable within a verified ledger. Numbering alone cannot prove that an entire ledger or repository history was never rewritten; that stronger claim requires preserved bytes, verified hash links and checkpoints, and an external anchor appropriate to the claimed scope.
