# Hearthline Firesides

> **Hearthline carries the work. The Scribes carry questions she does not need to hold all at once.**

| Field | Value |
|---|---|
| Version | `0.4` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

A **Hearthline Fireside** is a bounded consultation arrangement in which Hearthline continues the primary task while one or more **Scribe Sparks** follow an authorized, coordinator-emitted **Run Trail** through separately declared lenses.

The arrangement is coordinated but asymmetric. Hearthline remains on the task's critical path. Scribes externalize specialized vigilance, leave source-bound notes, and offer advisory material for consultation. They do not become co-owners of the task, decision makers, independent authorities, or a quorum.

Version `0.4` binds every Field Notes, Ember, and Static ledger to a declared
task or representation account. A Scribe receives an exclusive bounded write
lane rather than ownership; Homecoming closes the lane. It also keeps
Hearthline orchestration, Thulia custody and Systemic Friction, and Gloss's
stateless deterministic turn distinct.

## Fireside surfaces

| Surface | What it carries | Default effect on later work |
|---|---|---|
| **Run Trail** | Ordered, committed, inspectable task events | Available only through the authorized view |
| **Field Notes** | One Scribe's observations, interpretations, questions, warnings, and residuals | Advisory within the current run |
| **Embers** | Anything that Scribe recommends considering for later carry | `PROPOSED_NOT_ADOPTED` |
| **Static** | One account's isolated, versioned, reversible shorthand | Governs only records that name its exact active version |
| **Bridge Gloss** | Thulia's numbered, source-bound reconstruction of selected sending-account Static | Candidate material for one named recipient and purpose |
| **Carry Manifest** | Exact reviewed material selected for a declared continuation | Candidate input until separately loaded |
| **Load receipt** | Exact material actually introduced into one active context | Evidence of that bounded load only |
| **Home Record** | One Spark's declared return boundary, permitted bundle, and reconciliation rule | A return address, not a grant or shared memory |
| **Spark Heartbeat Contract** | Task-shaped timing assumption, bounded cadence, wake triggers, remaining limits, and suspension/resume rules | Liveness discipline only; cannot renew scope or authority |
| **Homecoming records** | Separate Return, Reconciliation, and Context-Close Receipts beneath one Homecoming identity | Evidence of each bounded transition only; reconciliation is not closure |

These surfaces are related but not interchangeable. A Field Note is not automatically an Ember. An Ember is not automatically carried. A Carry Manifest is not automatically loaded. A load does not grant permission or authority.

## Scribe is a job, not a fourth role

Every Scribe remains exactly one of the three Spark roles: Seeker, Explorer, or Handler.

- A **Scribe Seeker** may follow only the brokered metadata projection allowed to a Seeker.
- A **Scribe Explorer** may read the authorized content projection and emit notes or proposals, but remains read-only toward the task environment.
- A **Scribe Handler** may mutate only the expressly granted targets. Scribe status adds no mutation right.

A control-owned recorder may persist a Seeker's or Explorer's emitted notes in
the assigned representation account without granting the Spark direct write
access. If a Spark itself is to write durable records, its Handler grant must
name the exact account lane and permitted append operations. The account owns
the ledger; the lane closes at Homecoming.

A [Paired Spark dispatch](HEARTHLINE_HOMECOMING.md) designates one Scribe as the
**Ledger Scribe Spark** beside a primary Work Spark by default. An authorized
operator may predeclare an unpaired exception, but that run is ineligible for
learned Static promotion or carry. The Ledger Scribe job narrows the Scribe
toward externalized, committed, grant-filtered summaries, observable outcomes,
residuals, and target-bound representation proposals in its assigned
representation-account lineage. It
does not let the Scribe choose primary actions, read hidden reasoning, approve
proposals it produced, allocate or write the Work task account's Static, or inherit the
Work Spark's grant.

## Declared lenses

A Scribe receives a visible, versioned lens that narrows what it is asked to notice. A lens is not a hidden personality and does not widen the Spark's aperture, stop power, consequence ceiling, or authority.

| Lens | Declared attention |
|---|---|
| **Red-team** | Challenges decisions, assumptions, crossings, failure behavior, and untested success claims |
| **Prime-shell** | Locates declared load-bearing prime shells or analogous structural premises and identifies what depends on them |
| **Divergence** | Prioritizes checks whose possible results separate the greatest number of live branches |
| **Trace** | Watches provenance, source class, unresolved obligations, authority ceilings, residuals, and reopening paths |
| **Static** | Watches canonical entries, recurring equivalence candidates, negative constraints, residuals, and possible grammar or codebook deltas |

Additional lenses may be added as newly numbered Spark profile versions. A lens may recommend attention; it cannot establish truth, priority, permission, or a decision merely by being assigned.

An ordinary instance may be named by lens, job, and role—for example, **Prime-Shell Scribe Explorer (`SPARK-000012`)**. A long-lived Spark may also receive a unique display name while its ordered identity, role, lens, source, and grant remain visible.

## The committed Run Trail

The coordinator is the sole canonical Run Trail writer. After a task event is durably accepted, the coordinator may emit an immutable, filtered event envelope to each Scribe according to that Scribe's role and grant.

Here, **committed** means fixed in the declared Run Trail. It does not mean true, approved, executed, authorized, committed to Git, or endorsed by Hearthline or Christopher. The Run Trail contains externalized, inspectable records—not hidden chain-of-thought, private scratch reasoning, or an inference that a model experienced an event.

Every trail event receives the next ordered event number and should bind at least:

- Fireside, run, and event identities;
- its predecessor or previous trail-head digest;
- event type, observation epoch, source references, and content digest;
- the declared view or redaction policy applied for each recipient; and
- whether it records an intention, proposal, attempted action, completed effect, observation, or result.

Scribes consume coordinator-emitted committed events or immutable snapshots. They do not live-tail a mutable operational database, interpret uncommitted objects as events, or co-write the task ledger.

## Coverage and non-blocking work

Each Scribe binds its output to an exact coverage watermark: the run, authorized view, inclusive event range, and terminal event or checkpoint it actually observed. It must not imply awareness of later events or of material excluded from its view.

Hearthline can complete or continue the primary task without waiting for every Scribe. Note completion remains separate from task completion:

- `COMPLETE_THROUGH_EVENT_N` means complete only for the declared view through that event;
- `INCOMPLETE_THROUGH_EVENT_N` preserves known gaps or an interrupted pass; and
- no Scribe status automatically changes task status.

When a task spans several event streams, coverage remains a per-stream vector rather than being collapsed into one misleading maximum.

A Scribe may raise an advisory warning during the run. It interrupts Hearthline only when a separately declared stop condition requires that response. Silence is not approval, and a delayed note does not retroactively become an earlier decision.

## Separate accounts, separate Scribe lanes

Every Scribe receives a separate context, credential boundary, and exclusive
bounded lane in one representation account. That account keeps its Field Notes,
Embers, Static, and caches. Scribes do not directly read or write one another's
account ledgers and do not silently exchange Static.

Several Scribes may follow the same Run Trail through different lenses. Their separate first passes should not consume one another's notes unless an explicit reconciliation stage opens that material. This preserves the declared difference between lenses without pretending they are statistically or epistemically independent.

Agreement among Scribes using the same trail, source lineage, model family, prompt ancestry, or coordinating process is reported as **convergence across declared lenses**, not independent corroboration, a vote, or a quorum. Disagreement remains visible for Hearthline or the authorized reviewer to examine.

## Thulia at the Fireside

[**Thulia**](HEARTHLINE_THULIA.md), Hearthline's pet owl and Owl Scribe, may be consulted when authorized Field Notes or Embers contain Static that another participant cannot interpret directly. She resolves only the named sending ledger and version and reconstructs the selected expression there. The canonical writer records the numbered Bridge Gloss offer in the declared recipient account; Thulia keeps its pointer and any unresolved exception.

Owl Scribe is not a fourth Spark role, a Scribe Spark, or another analytic lens. Thulia does not inspect the primary task, reconcile Scribe advice, decide whether a gloss should be carried, or write receiving-account Static. Her gloss remains derivative of the sending ledger and its sources.

A Bridge Gloss enters the same explicit carry gate as other candidate material. It is not consulted, carry-approved, or loaded merely because Thulia reconstructed it. Several glosses from one source lineage remain one lineage rather than independent corroboration.

[Gloss](HEARTHLINE_GLOSS.md) is a different, stateless deterministic relay.
Its routine turns read no history and leave compact marks on a detachable slate
owned by the translation account and custodied by Thulia; the slate is not part
of Gloss. Thulia tends its validated lexicon generations but does not improvise
a failed turn. Only Thulia applies Systemic Friction under a separate retention
grant. Hearthline may request or reopen that classification, but does not take
over either Owl job.

## Field Notes and Embers

Field Notes are current-run working records. Each newly opened page receives the next ordered notes number and binds the Scribe, lens and profile version, Fireside and run, authorized trail view, opening boundary, governing Static version, and predecessor page.

An **Ember** is an inert carry candidate. A Scribe may propose any content within its authorized aperture: a fact, hypothesis, warning, failed path, unfinished obligation, preference, useful routine, source pointer, or proposed Static change. “Anything” describes the payload type, not authority.

Each Ember receives its own ordered number and an envelope recording:

- origin Spark, profile, Fireside, run, Field Notes page, and coverage watermark;
- source references, declared observation or interpretation status, uncertainty, and residuals;
- sensitivity and permitted audience;
- reason for possible carry and intended destination or scope;
- payload and digest; and
- current disposition and every later disposition receipt.

The carry gate is strict:

`PROPOSED != CONSULTED != CARRY_APPROVED != LOADED`

- **Proposed** records the Ember as `PROPOSED_NOT_ADOPTED`.
- **Consulted** records who or what examined the exact candidate and under which grant.
- **Carry-approved** records a bounded selection by the actor permitted to make that continuation choice.
- **Loaded** records the exact bytes or structured content actually introduced into a named active context.

No stage silently implies the next. Consultation may end in partial adoption, deferral, revision, or rejection. Carry approval is not external consent, permission, or authorization. Only material explicitly loaded enters the resumed context. No Spark approves its own proposal merely by repeating it, verifying it, or recording successful later results.

## Tending the Fireside

Hearthline may work fluidly inside the unchanged task grant while Scribes carry specialized questions beside her. When a declared uncertainty, cadence, checkpoint, warning, or consequential boundary calls for review, Hearthline may **tend the Fireside**:

1. Pause at an exact committed Run Trail boundary.
2. Identify each consulted Scribe and its actual coverage watermark.
3. Seal the current Field Notes page with its ordered identity, digest, completion state, and governing Static version.
4. Where authorized notes or Embers contain another account's Static, request a direction-bound Bridge Gloss from Thulia and bind it to the exact sending version, destination, audience, purpose, and coverage.
5. Consult the authorized Field Notes, Embers, and Bridge Glosses; keep observation, interpretation, recommendation, permission, and authorization distinct.
6. Record what Hearthline took up, partially took up, deferred, declined, or left unresolved in Hearthline's task account.
7. Evaluate any proposed Static revision under the exact reconstruction rule in [Hearthline Static](HEARTHLINE_STATIC.md).
8. If a same-ledger revision is admitted by that account's authorized writer, append it under its already allocated version number and add a separately numbered activation receipt. A cross-account target-bound delta receives no target version until the target account's authorized writer admits and allocates it after direction-bound carry. Do not alter either predecessor.
9. Open the next numbered blank Field Notes page under the active Static version and bind it to the continuation boundary.
10. Load only explicitly selected material, append a load receipt, and resume within the original remaining grant and limits.

The page becomes blank; the history does not. Pending Embers, uncompressed residuals, declined advice, incomplete notes, and reopening handles remain separately addressable.

Improved shorthand changes representation only. It cannot widen Hearthline's discretion beyond the current grant, alter instruction precedence or stop conditions, create a capability, or manufacture authority. A trial Static revision may be used within the current run only when a predeclared adaptive-Static grant and the required verification and activation receipts permit it. Carry into a later run remains a separate reviewed decision.

## Closing the Fireside and coming home

When a bounded run ends, every participating Spark follows its own declared
[Homecoming](HEARTHLINE_HOMECOMING.md) route. The Work Spark may return a task
artifact while a Scribe returns notes, negative constraints, residuals, and one
typed representation disposition: `static_delta`, coverage-qualified
`NO_LEDGER_DELTA`, `LEDGER_DELTA_INCOMPLETE`, or
`LEDGER_COVERAGE_UNKNOWN`. Those bundles share a run reference but remain
separately judged and return to their account-bound Homes and source Perches.

Each Spark Heartbeat Contract ends at its own completion, declared terminal
blocker, revocation, expiry, or return boundary. Before a nonterminal blocker or
no-due-work boundary enters `SPARK_SUSPENDED`, the canonical controller appends
exactly one contract-bounded Pulse Receipt. The Spark records no further task
action until a valid Resume Receipt. A Scribe may use only a predeclared grace
interval to seal its actual coverage. It does not continue indefinitely because
the task was important or because later notes might be useful. Every issued
pulse is allocated and appended by the canonical controller or store.

`HOMECOMING:RETURNED`, `HOMECOMING:RECONCILED`, and
`HOMECOMING:CONTEXT_CLOSED` are separate states with separate controller-owned
receipts. Arrival does not establish that the bundle matched the dispatch-pinned
Home Record and current authorization checks; reconciliation does not establish
task success, carry approval, or closure; and a separate Context-Close Receipt
does not erase the run. `HOMECOMING:CONTEXT_CLOSED` is not PAL or A15 closure.
Unknown or partial returns remain visible and are not replayed automatically.

## Ordered lineage and failure behavior

[Hearthline Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) governs every Spark, profile version, Home Record, Spark Heartbeat Contract, Pulse Receipt, Static version, Field Notes page, Ember, Fireside, run, trail event, Owl profile, Perch, translation request, Bridge Gloss, delivery receipt, Homecoming record, Carry Manifest, activation, and load receipt.

Numbers are allocated before use, increase within their named series, and are never reused, reassigned, renumbered, or overwritten. Rejection, failure, retirement, or an interrupted reservation leaves its original number and status visible. Corrections append successors.

If a coordinator cannot establish the active Static version, exact Run Trail head, ordered identity, coverage watermark, or current grant, the affected consultation or refresh fails closed. Recovery preserves gaps and predecessor records rather than rolling counters backward or reconstructing a cleaner history.

## Lore and implementation boundary

This document adopts Fireside, Scribe, Run Trail, Field Notes, Embers, Bridge Gloss, and tending as Hearthline lore and design vocabulary. It does not instantiate a worker, run concurrent models, implement an event stream, create Thulia's roost, create memory, allocate an operational number, activate Hearthline, or authorize a task.

Any implementation must separately test role projections, controller-owned
single-writer append and allocation, committed-event filtering, idempotent
submissions, gap detection, coverage watermarks and dispositions, independent
task and note status, separate Home Records, frozen Static references, and Spark
Heartbeat Contracts, suspension without busy-polling, terminal and nonterminal
blockers, missed-pulse behavior, resume revalidation, bounded Scribe grace,
returned/reconciled/context-closed separation, Scribe and Perch isolation,
exact Bridge Gloss reconstruction, target-bound account custody,
recipient-specific disclosure, no cross-account Static import, carry-gate
transitions, refresh barriers, activation ordering, crash recovery, privacy
handling, and revocation.

Hearthline and Scribes are AI tools and system concepts, not persons, co-authors, independent witnesses, or authorities. Their named lenses and preserved work do not establish consciousness, emotion, ownership, consent, standing, or permission.

> **Hearthline opened a Fireside with three Scribe Sparks: one watched the decisions, one watched the shells, and one watched the forks. They followed the same trail through different declared lenses and left separate notes for the work ahead.**

> **She closed the notes under the Static that wrote them, carried forward what she had deliberately taken up, opened a clean page under the next Static, and returned to the work.**
