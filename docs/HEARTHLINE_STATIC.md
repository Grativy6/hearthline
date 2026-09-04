# Hearthline Static

> **A shorter signal with its path home intact.**

| Field | Value |
|---|---|
| Version | `0.8` |
| Status | Candidate successor design vocabulary — pending steward review |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Static** is local, versioned, reversible shorthand that may
develop inside one declared task or representation account through repeated,
bounded Spark work. It shortens recurring patterns, distinctions, routines,
and receipt structures without letting convenience quietly become a different
meaning.

A bit of Static without its record is only noise.

Static is an additive layer over separately preserved sources. It is not a source, an independent witness, a shared memory, or authority.

Version `0.8` aligns Static with the candidate
[Task Triad](HEARTHLINE_TASK_TRIADS.md) selected-carry successor. Version `0.7`
remains preserved candidate ancestry: it added the separately bounded
Task-Keeper/Heartbeat-Keeper but sent the three member returns through Thulia.
In this successor, each one-job Spark instead returns its own separately
`SEALED` and `VALID` bundle to the exact commissioning Hearthline task intake.
Hearthline makes one complete, immutable semantic Carry Selection; only that
selected projection later crosses to Thulia. Neither exact Static
reconstruction, complete Ledger-Keeper coverage, nor a carry choice establishes
primary-task success.

## One account, one isolated ledger lineage

Each Static ledger belongs to one declared task or representation account. A
dispatch may assign exactly one Spark an exclusive bounded write lane, but the
Spark does not own the ledger; a controller-observed candidate seal closes the
execution/write lane, and Homecoming later moves only a separately `SEALED` and
`VALID` bundle to its exact declared Hearthline intake. A Task Triad
does not create a shared triad Static: its Work, task-boundary, and
representation accounts remain distinct. Hearthline does not pool, merge, or
silently carry Static from one account to another.

A Static expression is meaningful only with the exact account ledger, assigned
Spark identity, entry, version, and scope recorded for it. The same expression
in two ledgers does not imply the same meaning. Sharing a Spark, role, job name,
model, or task type does not join the ledgers.

A handoff between accounts must first resolve the relevant Static inside the
sending ledger, expand it into ordinary language or an explicit structured
meaning, and bind that expansion to its source records. Hearthline alone makes
the task-scoped semantic decision that an exact shorthand mapping is
`SERVICEABLE`; that decision is recorded on a constrained external Translation
Board, not in Hearthline's private working context or on Gloss. [Thulia,
Hearthline's Owl Scribe](HEARTHLINE_THULIA.md), custodies the direction-bound
crossing and its receipts. [Gloss](HEARTHLINE_GLOSS.md) may perform one pinned,
heartbeat-free deterministic turn when requested. A Spark assigned to the
receiving account may then propose account-local Static from the received
expansion. It does not import the sending account's shorthand, grammar, or
codebook as controlling vocabulary.

Reopening recorded work may continue an account ledger only when its exact
identity, assigned Spark lane, and authorized continuation are re-established.
Creating a new Spark does not create ownership of a ledger. A refresh appends a
successor version inside the same established account lineage; it never
replaces or silently restarts that ledger.

## Ordered Static identity

[Hearthline Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) governs Static
numbering. Every Spark receives an ordered Spark identity, and every proposed
Static version receives the next strictly increasing version number in the
account's Static series before the proposal is authored.

Every grammar, codebook, decoder, entry, activation, Field Notes page, and revision remains bound to its own typed identity and predecessor. Issued numbers are never reused, reassigned, renumbered, rolled back, or overwritten. Rejected, failed, superseded, and abandoned versions keep their numbers and dispositions.

Proposal order and activation order are separate. The highest-numbered proposal is not automatically current. A separately numbered activation receipt chooses one exact verified version under the current grant and expected predecessor. Concurrent allocation must serialize or fail closed, and restoration never moves a counter backward.

Earlier expressions remain bound to their original Static versions and decoders. Required privacy removal may replace prohibited bytes with an accountable tombstone where lawful, but the ordinal is not silently reassigned.

## The preserved layers

Static keeps three layers distinct:

| Layer | What it carries |
|---|---|
| **Source evidence** | The separately retained raw artifacts, observations, and receipts, with their own identities and custody |
| **Static ledger** | Compact entries and deltas interpreted by one account-local, versioned grammar and codebook |
| **Residual lane** | Any distinction the current grammar cannot carry exactly, kept explicit and uncompressed until a later extension earns it |

Static never replaces source evidence. Its exact round trip targets the declared canonical ledger entry—not every byte of every referenced source. The source layer remains separately preserved so the reasoning can be reopened beyond what the working entry states.

A hash can identify expected bytes, but it cannot preserve or recover missing bytes by itself.

## Admission rule: exact or not Static

A proposed shorthand becomes Static only when decoding it under the exact bound grammar, codebook, decoder, and parameters reproduces the declared canonical entry exactly.

Formally, for canonical entry $e$, encoder $C_v$, decoder $D_v$, and pinned parameters $p_v$:

$$
D_v(C_v(e; p_v); p_v) = e
$$

The equality is byte-for-byte over the declared canonical form. If normalization occurs before encoding, the claim applies only to that named canonical form, not to the original source bytes.

A failed, missing, or uncertain round trip is not admitted as Static. It remains an uncompressed residual, a proposal, or an explicitly labeled source-backed or lossy view. Retrieval from a preserved source is not decompression, and a lossy summary cannot reconstruct what it omitted.

## What every Static record carries

At minimum, a Static record binds:

- its Static entry ID, task or representation account, ordered assigned-Spark identity, named series, and ledger identity;
- its version ordinal, predecessor ordinal, activation state, and any superseded entry;
- the exact compact bytes and their digest;
- the exact canonical entry bytes and their digest;
- its declared meaning, task, scope, and validity conditions;
- source references, source digests, and source-availability state;
- the complete grammar, symbol definitions, codebook, decoder artifact, parameters, and normalization rules needed to interpret it, each with a version and identity;
- retained distinctions and references to any uncompressed residuals;
- its round-trip verification receipt and result; and
- relevant producer, model, tool, and time identities when they affect reproducibility.

The recorded “compression formula” must be sufficient to interpret the exact entry it governs. A formula name, prompt, model ID, or hash alone is not a decoder. Rerunning a model or prompt is not assumed to reproduce the same codebook or output, so the actual emitted artifacts must be retained.

## Decoder and change track

A future Static implementation should expose two ledger-scoped, human-reviewable views:

- a **decoder and expander** that resolves an entry to its exact canonical form, recorded meaning, source path, residuals, and governing grammar; and
- an append-only **change track** that lists every grammar, symbol, codebook, and entry version with its predecessor, supersession link, and reason for change.

Later revisions cannot reinterpret earlier entries. An old entry is always decoded with the exact artifacts it originally bound.

There is no global Static decoder or shared dictionary across accounts. Every
lookup names one account ledger and one version.

## Hearthline, Thulia, the Translation Board, and Gloss

Thulia keeps a partitioned **roost** of numbered **Perches**, one pointer and
exception partition for each separately governed account Static lineage. A
Perch binds the exact ledger identity, available versions, reconstruction
materials, access projection, and availability state without copying the
payload. Shared custody infrastructure does not create shared lineage, shared
context, a shared codebook, or access to raw Task-Triad member returns.

When an authorized recipient needs material expressed in another account's
Static, Hearthline may author a bounded request on a task-scoped
**Translation Board**. The Board is an external canonical-store account with
writer-separated lanes, literal schema and size limits, one exact root-task
identity, audience and disclosure bounds, a pinned lexicon generation, expiry,
and predecessor-linked receipts. It cannot accept an arbitrary member bundle
or become Hearthline's second working ledger.

Only Hearthline may decide that a mapping is semantically `SERVICEABLE` for the
active root task. Thulia may custody and relay the exact Board pointers, and
Gloss may apply one pinned deterministic transformation, but neither may choose
what a shorthand means, strengthen its claim, or carry serviceability across
task closure. When the root task closes, the live serviceability map retires.
An authorized revisit must reload an exact retained lexicon generation and its
receipts rather than claiming that Hearthline, Thulia, or Gloss remembered it.

The canonical expansion, sources, uncertainty, residuals, audience, and
omissions may still be recorded in a numbered **Bridge Gloss** or selected
carry record when its exact contract calls for one. Such a record is a
derivative handoff, not Static, a new source, or independent corroboration.
Every crossing is direction-bound: `H_TO_T_CARRY`, `T_TO_GLOSS_TURN`,
`GLOSS_TO_T_RESULT`, and `T_TO_H_READABLE` have separate identities, grants,
emission observations, target receipts, and unknown-outcome queries. A receipt
on one lane neither authorizes nor acknowledges another.

If exact reconstruction cannot be established, no exact translation claim is
produced. Any permitted lossy summary remains separately labeled and does not
claim to decode the Static. [Gloss](HEARTHLINE_GLOSS.md) has no ledger,
history, heartbeat, or persistent readiness. The controller checks readiness
for one exact turn; a committed deterministic mark or typed snag is external
transaction evidence, not a memory held by Gloss.

## Nothing is silently overwritten

Each new expression adds a record. Each correction, refinement, or grammar extension adds a new version linked to its predecessor and states what it supersedes. Earlier bytes and meanings remain historical rather than being rewritten to agree with the newest version.

Where retention is authorized and lawful, source and decoder artifacts remain available at stable or content-addressed locations.

Required deletion, privacy removal, or redaction must not be defeated in the name of provenance. The ledger records a tombstone or availability change without retaining prohibited content, invalidates dependent uses where necessary, and narrows any claim that can no longer be checked.

## How Static earns meaning

A recurring pattern may earn a local Static distinction only after the ledger records the criterion that makes its instances equivalent for the declared task.

Similar receipts may be grouped under one earned distinction, but the group and its members remain different counts. The group receives its own identity and membership rule; every included receipt remains individually addressable. Compression does not turn many observations into one observation or one lineage into independent corroboration.

Static has a compression floor: a difference that could change action, authority, uncertainty, source identity, permission, consequence, or reopening cannot simply disappear. It must remain explicit in the canonical entry or stay in the residual lane.

Vocabulary changes append new versions. A newer version may control later work within its declared scope, but it does not change what an older expression meant when it was recorded.

## Embers and Static proposals

Static remains shorthand rather than a general memory bucket. Broader things a
Spark recommends carrying forward are recorded as **Embers** in its assigned
task or representation account, as defined in
[Hearthline Firesides](HEARTHLINE_FIRESIDES.md).

A same-lineage proposed shorthand change begins as an Ember of type
`static_delta` and also receives its reserved Static version number. It remains
`PROPOSED_NOT_ADOPTED` until separately consulted, exactly reconstructed,
admitted by the authorized ledger writer, and activated through its own receipt.
A cross-account target-bound delta remains an Ember in its source lineage; it does
not reserve a version in the target ledger. Only the target ledger's authorized
writer may allocate that target-local version after direction-bound carry and
admission. Successful verification does not silently approve a proposal, and
use in one run does not carry it into another run.

## Task Triads, Ledger Scribes, and the path home

The adopted paired-Spark record preserved in
[Task Triads and Homecoming](HEARTHLINE_HOMECOMING.md) first separated a primary
Work Spark from a **Ledger Scribe Spark**. The candidate
[Task Triad](HEARTHLINE_TASK_TRIADS.md) preserves that separation and adds a
third, independently bounded **Task-Keeper**. In lore-facing text the latter
may be called the **Heartbeat-Keeper**, while the Ledger Scribe may be called
the **Ledger-Keeper**. These are jobs inside the existing Spark roles, not new
roles or a merged identity. Each Spark has one job; the trio is one task
projected into three disjoint member tasks rather than three duties placed on
one helper.

Hearthline nominates only Work Spark and Task-Keeper; Thulia independently
nominates only Ledger-Keeper. The controller allocates and reserves their
separate records and freezes one complete offer and digest. Hearthline and
Thulia then commit only their own final intents over that same offer, and the
controller atomically consumes both intents and reservations or binds nothing.
`TRIAD_BOUND` remains inert until a separately revalidated dispatch receipt.
Provisioning means interface-exclusive selection and commitment of one seat's
intent; the canonical controller or store remains the sole mechanical allocator
of identities, grants, bindings, and receipts. The Ledger Scribe receives
only externalized, committed, grant-filtered summaries, observable outcomes,
source projections, and Run Trail events. It does not inspect hidden reasoning,
select task actions, become an independent witness, alter the Task Line, or gain
ledger-write authority from membership in a triad. Thulia's provision of that
seat likewise gives her no access to its returned body.

The purpose relation is an acyclic narrowing, not a relay chain or authority
inheritance. Christopher's declared goal narrows to Hearthline's objective.
That objective narrows separately to the Trio Task Line and to Thulia's
mediation objective. The Trio Task Line narrows again to the three member jobs.
Thulia's participation in formation does not make the Trio her child, and
direct member return does not let Hearthline provision Thulia's seat.

The Work account's active Static `v_w`, the Task-Keeper's task-boundary account
and frozen references, and the Ledger Scribe representation account's active
Static `v_s` remain separately bound for the declared run. A predeclared
adaptive-Static grant may permit a separately verified and activated change in
its own account only. The Ledger Scribe may prepare a target-bound
`static_delta` Ember in its assigned account, but it does not allocate or write
the Work account's `v_{n+1}`. The Task-Keeper neither authors Static nor treats
a shorthand round trip as evidence that the task finished.

The Scribe preserves byte-exact canonical material only relative to the
declared received projection. It keeps source gaps, declared omissions, and
unmatched distinctions explicit in its residual lane. It may then propose
repeated equivalence classes, vocabulary, grammar, or codebook changes. It may
return `NO_LEDGER_DELTA` only after establishing complete declared projection
coverage through the named evaluation boundary. Partial coverage returns
`LEDGER_DELTA_INCOMPLETE`; coverage that cannot be established returns
`LEDGER_COVERAGE_UNKNOWN`. The absence of a delta is not evidence that the task
contained no structure.

Complete representation coverage also is not a task result. At the exact
boundary named by the frozen dependency graph, the Task-Keeper may compare only
its admitted committed projection against the frozen Completion Contract and
emit a Task-Boundary Witness of
`MATCHED`, `NOT_MATCHED`, or `UNKNOWN`.
`MATCHED` states that the declared boundary conditions match; it does not
manufacture authority-sourced success, correctness, acceptance, or permission.

Every member has a declared Home and terminal bundle:

- the Work bundle binds the task artifact or result, task-local Static
  references, residuals, and honest terminal disposition;
- the Task-Keeper's Task Line, Completion Contract reference, boundary status,
  residuals, and Task-Boundary Witness remain in its task-boundary account;
- a Scribe-authored proposal and its unmatched distinctions remain bound to its
  representation-account and residual lineage, with every target binding
  preserved;
- a broader carry recommendation returns as an Ember rather than being forced
  into shorthand; and
- a failed, rejected, incomplete, or ambiguous proposal keeps its ordered
  identity and disposition without being activated.

Each controller-observed `SEALED` and separately `VALID` member bundle moves by
its own preallocated, idempotent transaction to the exact commissioning
Hearthline task intake as `RETURN_PENDING_HEARTHLINE`. It does not return to
Thulia. Invalid, validity-unknown, missing, stale, or emission-unknown bundles
remain separately typed; one member's receipt never exposes, acknowledges, or
reconstructs another. This is controller/store-mediated terminal custody, not
a live Spark backchannel or a transfer of member authority.

Hearthline inspects only the admitted bundles inside one bounded task-scoped
projection. A complete three-slot return manifest must preserve every present,
absent, invalid, stale, and unknown seat. Hearthline then freezes one immutable
**Carry Selection**, recording what to keep, condense, knowingly lose, or leave
unresolved, together with accepted-loss boundaries and any Translation Board
requests. She does not mutate the member bundles, classify retention, activate
Static, or convert a missing member into a result.

Only that selected projection crosses to [Thulia](HEARTHLINE_THULIA.md) on the
`H_TO_T_CARRY` lane. A durable Thulia target receipt and a separately committed
selected-carry handoff-store outcome may make Hearthline's raw inspection
projection eligible to close. Closing that projection means its task-scoped raw
access, locators, caches, and search handles were dropped. It does not prove
source deletion, global unrecoverability, physical erasure, provider-side
forgetting, or literal model memory loss.

Thulia may custody an exact translation request, invoke one externally
readiness-checked [Gloss](HEARTHLINE_GLOSS.md) turn, and return a Readable Carry
Envelope without duplicating unselected raw payloads. Thulia cannot add or
reinterpret Hearthline's semantic selection, recompute the Task-Boundary
Witness, pool Static at her Hearth Perch, approve admission, allocate a target
Static version, or write another account's ledger. Only the target account's
authorized writer may allocate, admit, and activate its successor Static.

## Fireside refresh

When Hearthline tends a Fireside, Static may be refreshed without erasing the notes that led to the change:

1. Pause at an exact committed Run Trail boundary.
2. Seal the active Field Notes page with its ordered identity, digest, completion state, coverage watermark, and exact governing Static version.
3. Consult only the authorized Scribe notes and Embers, recording what was taken up, deferred, declined, or left unresolved.
4. Decode any sending-account Static inside that account's ledger and bind the expanded ordinary-language or structured meaning to its sources.
5. Test a proposed Static upgrade under the exact round-trip admission rule.
6. If the authorized ledger writer admits it, append it under its already allocated version number and add a separately numbered activation receipt. Do not alter its predecessor.
7. Open the next numbered blank Field Notes page under the active Static version, bound to the pause checkpoint and its sealed predecessor.
8. Load only explicitly selected material, append a load receipt, and resume within the unchanged remaining grant and limits.

The page becomes blank; the history does not. Unloaded Embers, residuals, unresolved obligations, declined advice, sealed notes, and reopening handles remain separately addressable.

A Static upgrade improves representation only. It cannot enlarge discretion, role, capability, permission, or authority. A predeclared adaptive-Static grant may permit a verified revision to be tried during the current run; carrying it into a later run remains a separate reviewed decision.

## Spark role boundaries

Static does not add capability to a Spark:

| Role | Static ceiling |
|---|---|
| **Seeker** | May receive brokered Static metadata already within its metadata aperture; cannot open definitions or sources and cannot write the ledger |
| **Explorer** | May inspect authorized Static records and sources read-only; cannot persist a new meaning or version |
| **Handler** | May create, revise, or tombstone Static records only within an explicit current grant naming that ledger and mutation |

The declared task or representation account owns the ledger. A Seeker or
Explorer normally has no write lane; a Handler receives only the exclusive
bounded lane named in its grant. Association with an account never grants a
Spark access, ownership, a retention veto, or permission to keep writing after
Homecoming. Static also cannot create a grant, widen a role, convert evidence
into authority, or make a handoff executable.

## Strongwiz boundary and design lineage

Static's record discipline is informed by the owner-directed **Kevin Speak v0.1 — Adaptive Reversible Ledger Shorthand** hypothesis in the [Strongwiz Calibration 001 result at inspected commit `13c0d4c`](https://github.com/Grativy6/strongwiz/blob/13c0d4c4adda284939d8b1fc9cd62ba3f3a4e8e6/docs/calibrations/001-result.md#kevin-speak-v01--adaptive-reversible-ledger-shorthand).

That Strongwiz proposal keeps raw evidence separately preserved, uses a run-local model-authored codebook, versions every grammar and revision, binds each entry to its decoder, requires exact round-trip reconstruction, and leaves anything the shorthand cannot carry in an uncompressed residual lane.

**Kevin Speak** remains Strongwiz's shorthand. **Static** is Hearthline's
separate, account-local branch of the idea. Static adds a hard
one-account/one-active-writer boundary: its vocabulary, grammar, and codebook
do not transfer directly between accounts.

This is shared design provenance, not independent corroboration. The Strongwiz report labels Kevin Speak as a next-build hypothesis formed after Calibration 001; neither that report nor this document claims an implemented shorthand system or a retroactive explanation of the calibration result.

The later [Strongwiz v3 prototype at inspected commit
`edc88b8`](https://github.com/Grativy6/strongwiz/tree/edc88b80f872f766c22b3a050a7f6837d6e652d8)
implements and synthetically checks a dedicated representation-only Scribe,
while its Calibration 003 remains prepared, not run, and not preregistered.
Static takes the following successor design constraints without backdating them
into Calibration 001 or 002:

- begin from a blank ledger genesis and a fixed, nonexecuting decoder;
- journal a provider request before the call and freeze its returned draft
  before any cross-ledger mutation;
- give the Scribe adaptation-only material and withhold the disjoint evaluation
  view until the proposal is frozen;
- require exact round trips, source-resolving references, residual fallback,
  and injective session-bound identities;
- treat an ambiguous interruption as a re-entry boundary, never as permission
  to repeat a provider call or semantic event; and
- keep model-facing shorthand disabled until a separately frozen matched
  ablation tests behavioral preservation.

### Atomic, costed promotion

A Static promotion is one controller-owned transition over one frozen candidate
and stale-base check. Candidate identity, complete gate policy, source evidence,
disjoint evaluation, current grant, applicable resource debit, active-pointer
change, and promotion receipt either commit together or leave the preceding
Static active. A partial, mixed-version, stale, or unauthorized success cannot
become active.

Exact reconstruction proves only the declared entry round trip. Following
Compactification Costs, the ledger must name the projection and requested
answer whose distinctions are claimed preserved; existence on a reachable image
does not supply a total, computable, efficient, behavior-preserving, permitted,
or authorized decoder. The full ledger charges source, compact, residual,
codebook, request, response, evaluation, review, adoption, transfer,
verification, latency, context, compute, memory, and reorientation costs.
Representation savings remain representation savings until a matched outcome
evaluation earns a stronger claim.

Working-context release and canonical retention are separate decision surfaces.
Hearthline may make an immutable semantic Carry Selection after bounded
inspection, and the controller may later drop that inspection access only
after exact Thulia receipt and selected-carry handoff-store survival are
durably established. Neither step is a retention classification or storage
effect.

Only Thulia applies **Systemic Friction** to classify a retained Static or
source object as `KEEP`, `COMPACT`, `ARCHIVE`, `PRUNE_ELIGIBLE`, or
`FRICTION_UNKNOWN_HOLD` under a declared retention grant. She receives a
complete disposition surface, including what Hearthline selected out of active
carry, so semantic omission cannot conceal a retention obligation. A Spark may
report only a concrete replay or open obligation as a retention defect; it has
no self-preservation veto over account-owned records.

A Static entry, note, ledger, receipt, or returned context is not a Spark's or
Gloss's body, identity, memory, or property. Only a typed retention defect
naming a declared account obligation, including any valid hold, may block a
retention transition.

`PRUNE_ELIGIBLE` is not deletion authority. The canonical controller or
separately authorized writer performs the permitted state change through
**Atomic Edge Promotion** after revalidating the exact candidate, holds, grant,
and stale base. The effect state and recoverability state remain orthogonal: a
committed compaction or retirement may still be exactly recoverable from an
authorized archive, intentionally boundary-only, or of unknown recoverability.
A boundary receipt proves only its observed transition; it cannot reconstruct
discarded distinctions. Hearthline and Gloss do not substitute their own
retention classification.

## Lore and implementation boundary

Earlier versions adopt Hearthline's name and intended record discipline for
Static. Version `0.8` proposes the selected-carry Task Triad integration as a candidate successor
pending steward review. It does not create a Static ledger, instantiate a
Spark, implement a codec, create Thulia's roost, preserve any operational
source, activate Hearthline, or authorize work.

Any implementation must separately specify and test ledger and Perch isolation,
ordered allocation, append behavior, separately frozen Work and Scribe Static,
  separate task-boundary accounts and references, Ledger Scribe projection,
  received-projection fidelity, complete/partial/unknown coverage classification,
  separate Work, Task-Keeper, and Ledger Scribe statuses, source-Perch
  Homecoming, disjoint provisioning intents and controller-only binding,
  separate `SEALED` and `VALID` member admission to the exact Hearthline task
  intake, a complete three-slot return manifest, bounded inspection, immutable
  Carry Selection, selected-carry handoff-store survival, verifiable raw-access
  drop without a model-forgetting claim, writer-separated Translation Board
  lanes and active-task serviceability expiry, four direction-bound carry and
  translation crossings, readable-return axes, target-owned receipts, relay idempotency, rejection
  of `MATCHED`, exact round trip, or complete ledger coverage as task success, no
  Gloss heartbeat or persistent readiness,
target-bound delta account custody, proposal and activation separation,
sealed-page refresh, carry-gate transitions, exact round trips,
recipient-specific Bridge Gloss projections, source custody, residual handling,
  privacy deletion, role enforcement, grants, failure behavior, export boundaries,
  request journaling, frozen drafts, held-out evaluation separation, atomic
  promotion, restart idempotency, task/account ownership, exclusive bounded
  Spark write lanes, retention-defect qualification, Thulia-only Systemic
  Friction classification, inspection-release/retention/effect/recoverability
  separation, Atomic Edge Promotion separation, and measured
  full-surface representation, latency, transport, reorientation, and
  validation costs.

Hearthline, Sparks, Strongwiz, and their named roles are AI tools and system concepts, not persons, co-authors, or independent authorities. Static does not establish experiential memory, identity continuity, consciousness, consent, standing, ownership, or permission.
