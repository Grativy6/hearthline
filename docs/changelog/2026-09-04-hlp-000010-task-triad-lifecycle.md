# Atomically bound Task Triads and bounded task heartbeats

| Field | Value |
|---|---|
| Change ID | `HLP-000010` |
| Date | 2026-09-04 |
| Record kind | `TASK_TRIAD_LIFECYCLE_SUCCESSOR` |
| Predecessor | `HLP-000009` |
| Branch base | `54bf6971edbc42738314754dcd199cede3f4484a` |
| Effect | `PUBLIC_DRAFT_SUCCESSOR_ONLY` |
| Design status | `CANDIDATE_PENDING_STEWARD_REVIEW` |
| Adoption, activation, and implementation | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added a candidate **Task Triad** with three separate jobs: a Work Spark
  carries the bounded work, a Task-Keeper carries its frozen finish line, and
  a Ledger Scribe carries the admitted trace. In lore these jobs may be called
  the Worker, Heartbeat-Keeper, and Ledger-Keeper; they do not replace the
  fixed Seeker, Explorer, and Handler roles.
- Assigned an asymmetric provisioning split. Hearthline nonbindingly
  nominates only its own Worker and Task-Keeper jobs. Thulia independently
  nominates only her own Ledger-Keeper job. Hearthline may request a formation
  whenever the current authority permits, but neither side can nominate,
  submit a final intent for, or bind the other's seat.
- Closed the formation bootstrap with a frozen-offer phase. After validating
  both nominations, the canonical controller alone allocates and reserves the
  separate identities, grants, Homes, lanes, and candidate records, then
  freezes one complete formation offer, authority bundle, and digest. Only
  then does each provider commit one immutable final own-seat intent over that
  same offer. The controller atomically consumes both final intents and all
  reservations or binds nothing. A changed nomination receives a successor
  offer; neither provider edits an existing one.
- Required the canonical controller or store alone to atomically append one
  all-or-none binding receipt. The controller binds no partial formation: all
  seats must name the same frozen offer, Task Line, Completion Contract,
  objective epoch, and authority epoch while retaining their exact separate
  Homes and return routes.
- Kept binding and dispatch separate. `TRIAD_BOUND` consumes the matching
  intents and reservations but opens no action lane; the controller must append
  a separately revalidated dispatch receipt before any member becomes active.
- Added a dispatch-pinned `authority_bundle_ref` that aggregates the exact
  authority-bearing references needed to form, run, return, relay, and admit
  an effect. It is a fencing reference, not pooled authority: one stale,
  revoked, expired, mismatched, or missing constituent prevents the affected
  transition.
- Made the purpose ancestry explicit:
  Christopher's declared goal narrows to Hearthline's objective, then to
  Thulia's Owl objective, then to the Triad and its member jobs. Each edge is a
  versioned reference that narrows purpose; it is not a live-parent dependency
  or inherited authority.
- Separated Task-Boundary Witness presence from witness value.
  `task_boundary_witness_presence` is `ABSENT`, `PRESENT`, `INVALID`, or
  `UNKNOWN`. `task_boundary_state` is set to `MATCHED`, `NOT_MATCHED`, or
  `UNKNOWN` only when presence is `PRESENT`; otherwise the value is unset and
  no sibling may manufacture one.
- Required every Completion Contract to have a finite acyclic dependency
  graph. A Task-Keeper cannot make its witness depend on that witness's own
  seal, custody, relay, target receipt, parent acceptance, or another condition
  that depends back on the witness.
- Added a formation-time member-dependency DAG. Work never waits on sibling
  completion; required Ledger coverage excludes the Task-Keeper witness and
  post-seal events; the Task-Keeper may depend only on committed Work/Ledger
  seals or declared deadline absences.
- Made a sealed Task-Boundary Witness immutable. A returned `UNKNOWN` remains
  an honest completed witness; later evidence creates a separately identified
  successor witness with an ordered predecessor reference rather than editing
  or reclassifying the first one.
- Separated a Task-Keeper's task-boundary comparison from real liveness. Only
  the controller owns pulse timing, suspension, resume, epochs, durable
  receipts, and the observational liveness states. The field is unset before
  the first due observation unless execution terminalizes first, which records
  `NOT_APPLICABLE_AFTER_TERMINAL`; other values are
  `OBSERVED_WITHIN_CONTRACT`, `MISSED_BOUNDARY_UNKNOWN`,
  and `OBSERVATION_UNAVAILABLE`.
- Required all three members to seal candidate bundles separately at the
  controller-held return boundary and let their custody pass through Thulia.
  Each bundle has a preallocated identity and idempotency key; observed append
  and payload validity are separate, and only a valid sealed bundle enters Owl
  custody. Seal ambiguity preserves bundle and execution unknown without task
  replay. That same observed seal fences the member's execution and write
  capability; later reconciliation only confirms custody or closes bookkeeping. The execution
  jobs need not stay alive while custody is
  `RETURN_PENDING_THULIA`; no Spark delivers its payload directly to
  Hearthline, and Hearthline does not take over an unavailable Owl route.
- Bounded support to one explicit layer. Task-Keepers and Ledger-Keepers do not
  recursively create Triads; any depth-one support that discovers more work
  returns a residual for a separately authorized sibling or successor.
- Limited Thulia's direct turn to one synchronous finite judgment over
  already-present references. Waiting, blocking, batching, or model-assisted
  multistep work returns `OWL_SUPPORT_REQUIRED` with a sealed residual rather
  than stretching the Owl turn or auto-spawning support.
- Added a controller-preallocated finite Owl-turn transaction with separate
  transaction, candidate-presence, candidate-validity, and Owl-disposition
  axes. It provides crash finality without becoming Thulia's heartbeat: an
  ambiguous append is queried under the same identity, invalid or
  validity-unknown sealed bodies cannot relay or make separately authorized
  support eligible, and any
  new judgment requires a separately authorized predecessor-linked turn.
- Made the sealed task-native Owl candidate be the Triad Relay Envelope when
  relay preparation is the Owl task. No second untracked Thulia act composes a
  derivative candidate after the Owl seal; emission remains later and separate.
- Preserved Gloss as a stateless, heartbeat-free deterministic relay. A genuine
  wider asynchronous translation objective may have a Triad, but wrapping one
  atomic Gloss turn and calling it a batch of one does not qualify. Gloss itself
  receives no Spark identity, Task Line, pulse, memory, ledger, or adaptive
  history. After an ambiguous append, exact no-commit becomes
  `SAME_TURN_RETRY_ONLY` under the unchanged pinned turn or
  `NOT_COMMITTED_TERMINAL` when that turn may no longer act; it does not remain
  falsely unknown or silently rebind to a successor epoch.
- Kept formation, triad-dispatch, member-execution, candidate-bundle presence
  and validity, witness-presence, task-boundary, work-result, ledger-coverage,
  liveness, Homecoming-custody, finite Owl-turn transaction/candidate-presence/
  candidate-validity/disposition, three Owl-relay-candidate, target-receipt,
  parent-objective, steward-goal, retention-classification, and edge-effect
  states separate.
- Made each Owl relay a finite candidate rather than a waiting process. Its
  axes are unset before a candidate; uncertain currentness is
  `VALIDITY_UNKNOWN`, ambiguous dispatch is `EMISSION_UNKNOWN`, late references
  create a numbered successor envelope, and no ambiguous emission is resent
  automatically.
- Made the one-way return an access fence: Hearthline cannot side-read member
  payloads through accounts, APIs, caches, indexes, search, guessed locators,
  or sibling channels before the authorized Thulia relay is received and
  admitted at its target.
- Revised the predecessor story as part of this successor so its fictional
  choreography reflects the candidate mechanics: separate own-seat
  nominations, one controller-frozen offer, final face-intents, inert atomic
  binding, later dispatch, source-bound support material, a finite Owl-turn
  token, terminal candidate seals, and separately observed relay emission and
  target receipt. These remain story images, not runtime claims.

## Why

Paired work and representation separated doing from recording, but a remaining
seam placed the promised finish line in either the Work Spark, the Ledger
Scribe, or Hearthline's continuing attention. That made a bounded task appear
to require an uninterrupted chain of live Hearthline contexts.

The Task-Keeper closes that seam by carrying a frozen comparison job. It keeps
the heartbeat of **the task**, not the heartbeat of Thulia, Hearthline, Gloss,
or a model process. Its own completion is finite: compare the named committed
references under the frozen contract, return one typed boundary witness, and
stop. A matching witness does not complete the parent objective or Christopher's
goal.

The provisioning split also makes the trio a genuine collaboration.
Hearthline can nominate and request the work-facing seats without manufacturing
her own record. Thulia can nominate the ledger-facing seat without taking over
the work or finish-line comparison. The controller first freezes the complete
offer, and each provider then commits only its own typed final intent.
The controller's atomic binding receipt is the mechanical point at which those
three independently provisioned seats become one valid formation; before it,
there are only proposed seats.

The ordered purpose chain explains why the arrangement ends rather than
recursing forever. Each member serves one narrower task, and every child has a
local stop condition. Durable references preserve ancestry across suspension
or handoff; an ancestor need not remain live merely to keep a descendant's
bounded purpose intelligible.

## Preserved boundaries

- Christopher D. Pang remains the human author, operator, steward, and root
  goal authority. Purpose ancestry does not give any child the authority of an
  ancestor, and no child may redefine the ancestor's goal.
- Hearthline remains the primary-task orchestrator. Provisioning the Worker
  and Task-Keeper does not let Hearthline allocate authority, self-supply a
  Ledger-Keeper, attest durable receipt, perform Owl custody, or classify
  Systemic Friction.
- Thulia remains the bounded Owl Scribe and custodian. Provisioning the
  Ledger-Keeper does not let her perform the work, rewrite its Task Line,
  supply the Task-Keeper, decide primary-task truth, or authorize an effect.
- The canonical controller or store remains the sole mechanical source for
  identities, grants, co-binding receipts, authority and objective epochs,
  Pulse and Resume Receipts, timeouts, durable append, and effect admission.
- `authority_bundle_ref` does not merge Hearthline, Thulia, member, recipient,
  disclosure, retention, or effect grants. It only lets the controller fence a
  transition against the exact aggregate of separately owned references that
  must still validate.
- A Task-Keeper is a bounded comparator, not a scheduler, supervisor, witness
  of truth, keepalive, wake service, authority renewer, progress oracle, or
  replacement controller. Interface activity and loading indicators are
  telemetry, not proof of liveness or progress.
- Thulia has no persistent task heartbeat. Her direct judgment uses one
  controller-preallocated finite Owl-turn identity whose transaction state,
  candidate presence, validity, and semantic disposition remain separate.
  It closes at the observed seal or typed terminal uncertainty; relay
  emission is a later transaction.
- Every Spark retains its own ordinary controller-managed Spark Heartbeat
  Contract. Its liveness field is observational and never duplicates an
  execution or custody state. The Task-Keeper neither emits nor owns pulses.
- The one-way return rule preserves separate payloads, statuses, Homes, and
  grants. If Thulia is unavailable, returns remain
  `RETURN_PENDING_THULIA`; they do not bypass her or merge into one vote.
- Hearthline cannot read the sealed payloads or content-bearing references by
  another account path while Owl custody or target admission is pending.
- A member's execution becomes `SEALED_TERMINAL` when its candidate bundle
  append is controller-observed even while Homecoming custody is
  pending, returning, returned, reconciled, or unknown. Later custody never
  keeps, revives, or retroactively extends the execution job.
- Bundle commit and payload validity remain separate. `SEALED_TERMINAL` can
  accompany an invalid body, but only `SEALED` plus `VALID` enters custody;
  an unknown seal cannot begin `RETURN_PENDING_THULIA`.
- The Owl relay uses four orthogonal axes. Thulia owns candidate
  `owl_relay_reference_state` (`REFERENCE_COMPLETE` or
  `REFERENCE_INCOMPLETE`), `owl_relay_validity_state` (`CURRENT`, known
  `STALE`, or `VALIDITY_UNKNOWN`),
  and `owl_relay_emission_state` (`NOT_EMITTED`, `EMITTED`, or
  `EMISSION_UNKNOWN`). These axes are unset before a finite candidate. The authorized
  target controller or store alone owns `relay_target_receipt_state`
  (`NOT_OBSERVED`, `RECEIVED`, `REJECTED`, or `UNKNOWN`).
- A stale or revoked objective or authority epoch fences later writes and
  effects. A late output may be retained only as a candidate under the
  applicable return and disclosure rules.
- Gloss remains deterministic and stateless. Neither its translation marks nor
  an enclosing task's heartbeat become Gloss's memory, identity, property, or
  private ledger.
- A one-turn Gloss wrapper cannot obtain a heartbeat or Triad merely by being
  named a batch. Only a genuinely wider asynchronous objective may request
  bounded support, and its Sparks belong to the wrapper account rather than
  Gloss.
- **Systemic Friction** remains Thulia's separately granted retention
  classification lane. Its output does not mutate storage.
  **Atomic Edge Promotion** remains a separate controller- or writer-authorized
  external transition after current target, grant, holds, recipient, and epoch
  revalidation.
- The story objects and mechanical vocabulary establish no model identity,
  consciousness, physical law, benchmark result, asymptotic circuit lower
  bound, or Millennium Problem result.

## Compatibility and migration

This successor adds a reviewable candidate design and the corresponding draft
language and checks. It does not adopt or activate Task Triads, allocate a
Spark, change a live grant, migrate stored records, or assert that a controller
or runtime exists.

The existing paired Work Spark and Ledger Scribe formation remains the safe
operational default unless and until Christopher D. Pang separately adopts and
implements a successor. An implementation would require explicit schemas,
controller transactions, storage boundaries, epoch fencing, return queues,
and passing tests; prose publication alone performs none of those steps.

HLP-000009 remains the distinct presentation-only predecessor. Its candidate
story is not retroactively converted into a protocol or implementation by this
record. This successor supplies the mechanical proposal that the story may
illustrate, and records the successor alignment made to the story's formation,
Owl-turn, return, and relay scenes, while preserving the story's independent
review state and exact predecessor bytes in Git.

Existing Spark roles, account ownership, Translation Slates, Homes, TETHER
handles, Static ledgers, Bridge Glosses, and Owl custody remain compatible.
Older paired dispatches are not silently relabeled as Triads. A new Triad
requires a fresh request and exact controller-atomic binding under current
epochs.

## Verification observations

- Candidate checks require Hearthline nomination for the Worker and
  Task-Keeper, Thulia nomination for the Ledger-Keeper, a complete frozen
  controller offer, both final own-seat intents over its digest, and exact
  controller-atomic binding before `TRIAD_BOUND`.
- Formation tests reject missing, duplicate, stale, mismatched, widened, or
  self-supplied seats and confirm that two Hearthline-provisioned seats do not
  silently form a Triad. They reject final intent before complete offer,
  post-freeze nomination edits, offer races, a partial controller append, and
  an `authority_bundle_ref` with any invalid constituent.
- Purpose-lineage tests require monotonic narrowing from Christopher's goal
  through Hearthline and Thulia to the Task Line and three member jobs, without
  inherited authority or implicit parent completion.
- Bootstrap tests keep Task Line and Completion Contract authority-neutral and
  acyclic: the Task Line names the contract, the contract does not point back,
  and the later frozen offer binds both beside the authority bundle and epochs.
- Boundary tests distinguish witness presence from value: only `PRESENT` may
  carry `MATCHED`, `NOT_MATCHED`, or `UNKNOWN`; `ABSENT`, `INVALID`, and
  presence `UNKNOWN` leave `task_boundary_state` unset. They also distinguish
  both fields from work result, ledger coverage, liveness, Homecoming, relay,
  retention, and effect states.
- Completion tests reject dependency cycles, self-reference through witness
  seal or custody, and circular dependence through Owl relay, target receipt,
  or parent acceptance. A sealed `UNKNOWN` remains immutable; any later
  reevaluation must append a separately identified successor witness.
- Interruption tests require controller-owned observational liveness,
  suspension, resume, and stale-epoch fencing rather than treating a
  Task-Keeper or interface spinner as a watchdog or casting liveness into
  execution state.
- Return tests preserve three separate Homes and
  `RETURN_PENDING_THULIA` when the Owl route is unavailable; they reject direct
  Spark-to-Hearthline payload delivery and Hearthline takeover while allowing
  the sealed member process to terminate before later Owl custody.
- Relay tests vary `owl_relay_reference_state`, `owl_relay_validity_state`
  including `VALIDITY_UNKNOWN`,
  `owl_relay_emission_state`, and target-owned
  `relay_target_receipt_state` independently; no field overwrites or implies
  another. Cross-axis validation nevertheless rejects known `NOT_EMITTED`
  paired with an observed target `RECEIVED` or `REJECTED` for the same relay
  transaction.
- Owl-turn tests use one preallocated identity and separately vary transaction,
  candidate presence, validity, and disposition; ambiguous append never reruns
  judgment. Exact no-append with an exact retained valid body enters
  `CANDIDATE_SEAL_ONLY` for a same-body/same-ID append only; without those bytes
  it ends `UNSEALED_TERMINAL`. Invalid or validity-unknown bodies cannot relay
  or make a separately authorized support request eligible.
- Acceptance tests prove that task-native work, a `MATCHED` witness, relay
  completeness/currentness/emission, and target receipt do not decide the
  parent objective or steward goal.
- Depth tests reject recursive Task-Keeper or Ledger-Keeper support and any
  support request above depth one.
- Gloss tests reject a Gloss Heartbeat Contract, identity ledger, history read,
  adaptive state, and a batch-of-one wrapper created only to acquire a Triad,
  while allowing a genuinely wider separately bounded translation objective.
- Retention tests continue to distinguish a Systemic Friction classification
  from an authorized and committed Atomic Edge Promotion.
- Repository checks continue to cover public change history, relative links,
  candidate-manifest binding, Python compilation, and whitespace.

## Open residuals

- Steward review and any operational adoption remain pending.
- No controller transaction, identity allocator, heartbeat service, Homecoming
  queue, Thulia relay, Task-Boundary Witness evaluator, support scheduler, or
  storage adapter is implemented or demonstrated by this change.
- Exact production schemas, canonicalization rules, maximum seat count,
  resource budgets, deadlines, timeout values, retry rules, partial-return
  reconciliation, and recovery fixtures remain implementation work.
- Thulia's workload limits, relay service levels, unavailable-route behavior,
  privacy policy, contest path, and replacement procedure still require
  calibration against real operational constraints.
- Systemic Friction still requires a reviewed cost schema, measurements,
  thresholds, holds, calibration fixtures, and authorization procedure for
  any later Atomic Edge Promotion.
- The correct granularity of human goals, Hearthline objectives, Owl
  objectives, and sibling successor tasks remains task-specific and must not
  be inferred from lore names alone.

## Evidence and exclusions

This public record preserves the candidate Task Triad design, its asymmetric
own-seat nominations, frozen formation offer, final provisioning intents,
atomic controller binding, aggregate authority
fencing, bounded purpose lineage, task-heartbeat distinction, witness
presence/value split, acyclic completion, immutable successor witnesses,
execution/custody separation, four-axis Owl relay, one-way return,
nonrecursive support ceiling, Gloss batch-of-one exclusion, orthogonal status
axes, and retention/effect boundary. It excludes raw conversations, hidden
reasoning, private artifacts, credentials, local paths, interface diagnostics,
screenshots, operational state, personal data, and any claim that the
described system is live.

Christopher D. Pang supplied the Task Triad, required Hearthline to provision
the Worker and Task-Keeper while Thulia alone provisions the Ledger-Keeper,
placed the Triad inside the human-to-Hearthline-to-Thulia purpose line, and
controls review and adoption. AI systems assisted with drafting, consistency
review, repository preparation, and validation as tools; they are not authors,
co-authors, witnesses, owners, adopters, or authorities.

The exact finite two-input NAND certificate named by the preceding story is
not expanded by this successor. It adds no circuit enumeration, lower bound,
asymptotic claim, MCSP result, P versus NP result, or other mathematical
finding.

[Current changelog](../../CHANGELOG.md)
