# Hearthline TETHER

## Trace Externalization Through Handle-bound Exact Reopening

```yaml
document: HEARTHLINE_TETHER
version: 0.3-draft
status: CANDIDATE_PUBLIC_DESIGN_PROPOSAL_PENDING_STEWARD_REVIEW
author_and_steward: Christopher D. Pang
repository_role: HEARTHLINE_CONTINUITY_TECHNIQUE
change_lineage_ref: HLP-000011
agent_contract_successor_ref: hearthline_agent.md@0.7-draft
activation_effect: NONE
```

> **Keeper.** Externalize recoverable trace through whatever reliable carrier is available. Carry a compact, identity-bound handle. Never carry a material unresolved state without also carrying a concrete route by which it could be reopened.

## v0.3 inspected-carry successor

Version `0.2-draft` remains candidate ancestry. Candidate version `0.3-draft`
is the TETHER companion to `HLP-000011` and the candidate
[`hearthline_agent.md`](../hearthline_agent.md) `0.7-draft` successor. It adds
the two-stage return boundary: three separately sealed and validated member
bundles enter Hearthline's task intake; Hearthline inspects them under a bounded
grant and freezes one immutable Carry Selection plus any Translation Board
requests; only that selected handoff then crosses to Thulia. Hearthline's
inspection context may close only after the exact handoff has a durable Thulia
receipt and the selected carry has committed to its separate custody store.
Closing withdraws active inspection access; optional Gloss work and the
readable return proceed from that custody copy. Thulia's later Systemic
Friction classification and any canonical retention effect remain different,
later edges. No one of those edges claims erasure of model memory or deletion
of an external source.

The successor also keeps the Hearthline-to-Thulia, Thulia-to-Gloss,
Gloss-to-Thulia, and Thulia-to-Hearthline lanes distinct. It makes Gloss
readiness a controller-observed fact of one finite turn rather than a heartbeat
or inherited persistence, and binds task-scoped shorthand serviceability to
Hearthline's explicit decision and one exact lexicon generation.

The state names in this successor are the state families defined by
[Task Triads](HEARTHLINE_TASK_TRIADS.md): `RETURN_PENDING_HEARTHLINE`,
Carry Selection coverage, `carry_handoff_emission_state`,
`carry_handoff_state`, `inspection_context_state`, Gloss readiness and
transaction states, readable-carry axes and store outcome, selected-carry
store outcome, retention classification, canonical-store effect, and
recoverability. Phrases
such as “first stage,” “selected-carry phase,” and “later retention phase” are
explanatory orderings, not additional state axes.

## v0.2 task-bound suspension predecessor

Version `0.1-draft` remains the predecessor. Candidate version `0.2-draft`
adds the exact reopening bundle when one or more
[Task Triad](HEARTHLINE_TASK_TRIADS.md) member executions are suspended or the
coordinated objective is apparently stuck. It binds the frozen
Goal, Task Line, Completion Contract, three member and Home references, last
committed boundaries, ancestor states, remaining limits, objective epoch, and
controller-owned immutable authority bundle and aggregate authority epoch
needed to test whether work may resume without silently becoming a different
task.

The successor also binds the bootstrap-safe formation request, two nonbinding
own-seat nominations, controller-frozen offer and digest, two final intents,
and atomic binding receipt. It preserves per-member execution, candidate-bundle
existence and validity, liveness, and custody as separate axes; makes a boundary
witness optional and presence-qualified; and carries the four independent Owl
relay/target axes with an idempotent emission transaction and numbered
late-reference succession.

It also separates interface telemetry from externally witnessed lifecycle.
A spinner or `Working` indicator is not a pulse or evidence of progress. A
Task-Keeper sharing the watched host's failure domain cannot watchdog that
host. Timeout, wake, and resume remain actions of an external canonical
controller or durable store.

## 1. Purpose

TETHER is Hearthline's carrier-neutral continuity technique for work that must survive a context boundary, process boundary, session change, long interruption, or selective return. It names a bounded motion:

```text
externalize -> bind -> carry -> retrieve -> verify -> selectively reopen -> return
```

The technique does not require one archive format, compression method, storage provider, or software stack. A Git commit, immutable blob, workflow artifact, ordinary file, versioned document, folder plus manifest, database snapshot, object-store item, transcript range, or another adequately identified carrier may be used when the current environment can lawfully and reliably reopen it.

The goal is not total memory. The goal is exact or honestly bounded reopening.

## 2. Relation to MAPS TraceKey

MAPS TraceKey v0.1 defines a TraceKey as a scoped routing handle rather than the memory itself and gives the project the phrase **small keys back to large traces**. TETHER is a compatible Hearthline-side technique built at that seam:

- **TraceKey names the key.**
- **TETHER names the motion performed with a bound key.**

The relationship is lineage and reuse, not independent corroboration. TETHER does not replace MAPS TraceKey or silently adopt every future TraceKey feature.

Primary publication: [*MAPS TraceKey v0.1: An Offline-First Trace-Routing Ledger for AI-Assisted Work*](https://doi.org/10.5281/zenodo.21245399).  
Implementation repository: [Grativy6/maps-tracekey](https://github.com/Grativy6/maps-tracekey).

## 3. What a TETHER carries

A complete TETHER handle should carry the smallest fields needed to identify, constrain, and reopen the trace honestly:

```yaml
tether_id: stable local identifier
source_identity: originating project, account, document, run, or record
carrier_kind: git_commit | artifact | file | versioned_document | snapshot | other
locator: exact route the authorized retrieval layer can use
version_or_integrity: commit, blob, version ID, digest, ETag, manifest, or declared absence
scope: what part of the source the handle addresses
provenance: who or what supplied, produced, transformed, or observed it
claim_status: source-side status carried without promotion
coverage: what the carrier is known to include and omit
residuals: material uncertainty, missing coverage, conflicts, or open burdens
reopening_route: concrete retrieval, query, comparison, reproduction, or review step
access_requirements: grant, privacy, credential, tool, or environment constraints
authority_ceiling: what the handle and payload cannot authorize
do_not_claim: especially likely overreads
staleness_or_expiry: change conditions that require revalidation
```

Not every carrier exposes every field natively. Missing material fields remain explicit rather than being guessed. A mutable locator without a stable version or integrity binding is a **lead**, not an exact TETHER.

A content hash is useful when available, but it binds bytes only. It does not authenticate the human source, establish chronology by itself, grant access, authorize disclosure, certify truth, or widen the payload's claim status.

## 4. Exact reopening

`Exact` describes the relation between the handle and the reopened object. It does not promise that the externalized trace was complete, adequate, true, or sufficient for every later question.

A TETHER reopening is exact when the retrieval layer can establish that it reopened the bound carrier or the declared projection of that carrier under the recorded identity rule. When exact identity cannot be established, the result must be typed more narrowly, for example:

- `RETRIEVED_UNVERIFIED` — content was retrieved, but identity or integrity is not established;
- `STALE` — the named source changed beyond the bound version or expiry rule;
- `ACCESS_UNAVAILABLE` — the source may still exist, but the present grant or tool cannot reach it;
- `SOURCE_MISSING` — the bound source cannot presently be located;
- `SCOPE_INSUFFICIENT` — the carrier is real, but it does not cover the question;
- `CONTENT_UNRESOLVED` — the source was reopened and still does not decide the issue.

Retrieval failure is not source loss. Source loss is not proof that the underlying event never occurred. A nearby reconstruction may be useful, but it must be labeled as a reconstruction before it is presented.

## 5. Selective reopening

Reopening should admit only what the current task requires. The retrieval layer may search, index, filter, or read a bounded region instead of flooding the active context with the full carrier.

A selective reopening records:

1. the TETHER handle used;
2. the identity or integrity check performed;
3. the portion actually reopened;
4. material exclusions or unread regions;
5. the claim status inherited from the source;
6. any new interpretation added in the present pass; and
7. the next reopening route for what remains unresolved.

Selective reopening must not make an omitted region disappear from the coverage account. A summary may route attention; it does not silently become the source.

## 6. The unresolved-route rule

A TETHER may carry an unresolved state forward. It may not turn the word `UNRESOLVED` into a dead end. **An unresolved state without a reopening route is an incomplete TETHER.**

For every material unresolved item, retain at least one concrete reopening route, such as:

- retrieve the exact source version;
- request the missing access or disclosure decision from the authorized person;
- compare the bound version with the current version;
- inspect a named file, range, table, receipt, or artifact;
- rerun a declared procedure under fixed inputs;
- ask a named specialist to attack a named theorem, assumption, or priority question;
- obtain an independent measurement or witness; or
- state that no presently known route exists and preserve the search terms and stopping reason.

A route need not be guaranteed to succeed. It must be specific enough that a later worker can tell what reopening was intended and why it could change the status.

## 7. Authority, privacy, and capability boundary

A TETHER handle is not permission to retrieve its carrier. A locator does not grant credentials. A successful reopening does not authorize publication, disclosure, execution, spending, messaging, or any other consequence.

Reopening uses only the current grant, current tools, current privacy boundary, and current scope. Resuming from a TETHER cannot create, renew, widen, transfer, or infer authority. Consumed limits remain consumed. A stale or inaccessible grant leaves the handle intact and the content unopened.

That stale bound grant cannot authorize its own inspection. A separately
issued, current read-only inspection grant may authorize retrieval and
verification of the historical carrier without authorizing resume, effect, or
silent rebasing.

Private material should remain in the least exposed adequate carrier. Public handles must not leak private filenames, local paths, secrets, personal data, hidden prompts, or the existence of material whose disclosure was not authorized.

## 8. What TETHER is not

TETHER is not:

- a way to evade or enlarge a model's context window;
- preservation of hidden chain-of-thought or private model state;
- a claim of continuous model identity or experiential memory;
- a heartbeat, scheduler, host watchdog, wake service, or process keepalive;
- evidence of liveness or progress merely because an interface displays a
  spinner, `Working`, or another activity indicator;
- a requirement to compress, archive, or use a particular file format;
- proof that externalized material is complete, truthful, current, or adequate;
- a permission, authorization, authenticity, or authorship mechanism;
- a substitute for backups, version control, access control, encryption, or retention policy; or
- a reason to keep unnecessary data.

The active context carries a handle and whatever bounded material is reopened. The larger trace remains external.

## 9. Task-bound suspension and exact reopening

A task-bound TETHER is complete only when it can reopen the same frozen task
*and* determine whether that task remains resumable. A locator back to the last
artifact is not enough. Before one or more
[Task Triad](HEARTHLINE_TASK_TRIADS.md) member executions enter suspension—or
before the controller suspends the coordinated objective at a context,
session, process, or host boundary—the canonical controller or durable store
commits a bundle equivalent to:

```yaml
goal_binding:
  goal_version_ref: exact ordered identity and digest
  purpose_projection_refs: ordered NARROWS edge identities and digests
  purpose_projection_dag_validation_ref: required with a frozen offer or bound task; otherwise exact when already appended or unset; cycles fail formation
  ancestor_states_at_suspend: explicit state for every traversed goal or task
task_binding:
  task_line_version_ref: exact ordered identity and digest
  objective_epoch_ref: exact dispatch-pinned epoch when DISPATCHED; before dispatch, exact request- or offer-pinned Task Line epoch
  completion_contract_version_ref: exact ordered identity and digest
  task_triad_ref: required only when triad_formation_state is TRIAD_BOUND; otherwise unset
  task_triad_dispatch_ref: unset until controller allocates a dispatch attempt; thereafter exact identity and digest
  triad_dispatch_state: unset before TRIAD_BOUND; thereafter exact one of [NOT_DISPATCHED, DISPATCHED, DISPATCH_REFUSED, DISPATCH_STALE]
  dispatch_receipt_ref: required for an appended dispatch decision; unset before that decision
provisioning_binding:
  formation_request_ref: unset before request creation; thereafter exact ordered identity and digest
  triad_formation_state: unset before request creation; thereafter exact one of [TRIAD_FORMATION_REQUESTED, TRIAD_FORMATION_PENDING, TRIAD_FORMATION_OFFERED, TRIAD_FORMATION_REFUSED, TRIAD_FORMATION_STALE, TRIAD_BOUND]
  hearthline_nomination_ref: required whenever formation_request_ref exists; request creation atomically includes Hearthline's nonbinding own-seat nomination
  thulia_nomination_ref: required once Thulia's nonbinding own-seat nomination is appended; otherwise unset
  formation_offer_ref: required in TRIAD_FORMATION_OFFERED or TRIAD_BOUND; unset in REQUESTED or PENDING
  terminal_offer_rule: REFUSED or STALE preserves formation_offer_ref iff an offer was already frozen
  formation_offer_digest: required exactly when formation_offer_ref exists; otherwise unset
  member_reservation_refs: required with a frozen offer; otherwise unset
  hearthline_intent_ref: present iff Hearthline's final own-seat intent was appended; required in TRIAD_BOUND
  thulia_intent_ref: present iff Thulia's final own-seat intent was appended; required in TRIAD_BOUND
  controller_binding_receipt_ref: required iff TRIAD_BOUND; otherwise unset
controller_binding:
  controller_ref: required once formation_request_ref exists; otherwise unset
  authority_bundle_ref: required once allocated for the frozen offer and in TRIAD_FORMATION_OFFERED or TRIAD_BOUND; otherwise unset
  terminal_authority_rule: REFUSED or STALE preserves authority_bundle_ref iff the bundle was already allocated
  authority_epoch_ref: required exactly when authority_bundle_ref exists; otherwise unset
  authority_epoch_stage_rule: offer-pinned before dispatch and dispatch-pinned afterward
  authority_epoch_semantics: when present, aggregate over the exact authority bundle
  authority_components:
    presence_rule: required exactly when authority_bundle_ref exists; otherwise unset
    hearthline_provisioning_grant_ref: exact separate grant
    thulia_provisioning_grant_ref: exact separate grant
    work_member_grant_ref: exact separate grant
    task_keeper_member_grant_ref: exact separate grant
    ledger_keeper_member_grant_ref: exact separate grant
    recipient_and_effect_limits_ref: exact audience, disclosure, consequence, and effect limits
terminal_return_authority:
  historical_task_authority_state: exact current, stale, revoked, expired, or unknown state of the dispatch-pinned authority; never rewritten
  current_terminal_return_custody_grant_ref: required before moving an already SEALED and VALID old-epoch bundle; otherwise exact current reference when applicable or unset
  current_terminal_return_custody_epoch_ref: required exactly when current_terminal_return_custody_grant_ref exists; otherwise unset
  terminal_return_recipient_ref: exact Hearthline task-intake account when the current grant exists; otherwise unset
  authority_ceiling: custody and admission of the exact already sealed body only; no task action, reseal, semantic rewrite, rebinding, or epoch renewal
members:
  presence_rule: absent before controller member allocation; reserved-only at offer; fully bound and state-bearing only in TRIAD_BOUND
  work:
    member_reservation_ref: required with frozen offer; otherwise unset
    candidate_bundle_reservation_ref: required with frozen offer and binds exact future identity, idempotency key, expected digest or validation rule, and query route; otherwise unset
    member_binding_ref: required in TRIAD_BOUND; otherwise unset
    spark_profile_grant_refs: reserved exact identities and digests with offer; binding-effective only in TRIAD_BOUND
    home_ref: reserved with offer; exact dispatch-pinned Home Record after dispatch
    heartbeat_ref: reserved with offer; binding-effective only in TRIAD_BOUND
    member_execution_state: unset before TRIAD_BOUND; thereafter exact one of [NOT_DISPATCHED, ACTIVE, SPARK_SUSPENDED, RETURN_ONLY, SEALED_TERMINAL, UNSEALED_TERMINAL, EXECUTION_UNKNOWN]
    candidate_bundle_ref: required in TRIAD_BOUND and must consume the exact identity named by candidate_bundle_reservation_ref; otherwise unset
    candidate_bundle_idempotency_key: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_expected_digest_or_validation_rule: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_exact_query_route: required exactly when candidate_bundle_ref exists; queries that same canonical identity without replay
    retained_candidate_body_reopening_route: exact authorized locator, body retrieval, integrity check, and same-ID RETURN_ONLY seal route only when an exact body is known retained; otherwise unset with unavailability or uncertainty in unresolveds
    member_candidate_bundle_state: unset before candidate_bundle_ref exists; thereafter exact one of [NOT_PRODUCED, SEALED, UNKNOWN]
    member_candidate_bundle_validity_state: unset unless bundle SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
    liveness_state: unset before dispatch and first due observation unless execution terminalizes first; terminalization sets NOT_APPLICABLE_AFTER_TERMINAL; otherwise thereafter exact one of [OBSERVED_WITHIN_CONTRACT, MISSED_BOUNDARY_UNKNOWN, OBSERVATION_UNAVAILABLE]
    last_committed_boundary_ref: unset before any committed member boundary; thereafter exact pulse, suspension, artifact, or absence observation
  task_keeper:
    member_reservation_ref: required with frozen offer; otherwise unset
    candidate_bundle_reservation_ref: required with frozen offer and binds exact future identity, idempotency key, expected digest or validation rule, and query route; otherwise unset
    member_binding_ref: required in TRIAD_BOUND; otherwise unset
    spark_profile_grant_refs: reserved exact identities and digests with offer; binding-effective only in TRIAD_BOUND
    home_ref: reserved with offer; exact dispatch-pinned Home Record after dispatch
    heartbeat_ref: reserved with offer; binding-effective only in TRIAD_BOUND
    member_execution_state: unset before TRIAD_BOUND; thereafter exact one of [NOT_DISPATCHED, ACTIVE, SPARK_SUSPENDED, RETURN_ONLY, SEALED_TERMINAL, UNSEALED_TERMINAL, EXECUTION_UNKNOWN]
    candidate_bundle_ref: required in TRIAD_BOUND and must consume the exact identity named by candidate_bundle_reservation_ref; otherwise unset
    candidate_bundle_idempotency_key: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_expected_digest_or_validation_rule: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_exact_query_route: required exactly when candidate_bundle_ref exists; queries that same canonical identity without replay
    retained_candidate_body_reopening_route: exact authorized locator, body retrieval, integrity check, and same-ID RETURN_ONLY seal route only when an exact body is known retained; otherwise unset with unavailability or uncertainty in unresolveds
    member_candidate_bundle_state: unset before candidate_bundle_ref exists; thereafter exact one of [NOT_PRODUCED, SEALED, UNKNOWN]
    member_candidate_bundle_validity_state: unset unless bundle SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
    liveness_state: unset before dispatch and first due observation unless execution terminalizes first; terminalization sets NOT_APPLICABLE_AFTER_TERMINAL; otherwise thereafter exact one of [OBSERVED_WITHIN_CONTRACT, MISSED_BOUNDARY_UNKNOWN, OBSERVATION_UNAVAILABLE]
    last_committed_boundary_ref: unset before any committed member boundary; thereafter exact pulse, suspension, witness, or absence observation
  ledger_keeper:
    member_reservation_ref: required with frozen offer; otherwise unset
    candidate_bundle_reservation_ref: required with frozen offer and binds exact future identity, idempotency key, expected digest or validation rule, and query route; otherwise unset
    member_binding_ref: required in TRIAD_BOUND; otherwise unset
    spark_profile_grant_refs: reserved exact identities and digests with offer; binding-effective only in TRIAD_BOUND
    home_ref: reserved with offer; exact dispatch-pinned Home Record after dispatch
    heartbeat_ref: reserved with offer; binding-effective only in TRIAD_BOUND
    member_execution_state: unset before TRIAD_BOUND; thereafter exact one of [NOT_DISPATCHED, ACTIVE, SPARK_SUSPENDED, RETURN_ONLY, SEALED_TERMINAL, UNSEALED_TERMINAL, EXECUTION_UNKNOWN]
    candidate_bundle_ref: required in TRIAD_BOUND and must consume the exact identity named by candidate_bundle_reservation_ref; otherwise unset
    candidate_bundle_idempotency_key: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_expected_digest_or_validation_rule: required exactly when candidate_bundle_ref exists; otherwise unset
    candidate_bundle_exact_query_route: required exactly when candidate_bundle_ref exists; queries that same canonical identity without replay
    retained_candidate_body_reopening_route: exact authorized locator, body retrieval, integrity check, and same-ID RETURN_ONLY seal route only when an exact body is known retained; otherwise unset with unavailability or uncertainty in unresolveds
    member_candidate_bundle_state: unset before candidate_bundle_ref exists; thereafter exact one of [NOT_PRODUCED, SEALED, UNKNOWN]
    member_candidate_bundle_validity_state: unset unless bundle SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
    liveness_state: unset before dispatch and first due observation unless execution terminalizes first; terminalization sets NOT_APPLICABLE_AFTER_TERMINAL; otherwise thereafter exact one of [OBSERVED_WITHIN_CONTRACT, MISSED_BOUNDARY_UNKNOWN, OBSERVATION_UNAVAILABLE]
    last_committed_boundary_ref: unset before any committed member boundary; thereafter exact pulse, suspension, ledger, or absence observation
task_boundary_binding:
  task_boundary_witness_presence: unset before the Completion Contract's declared observation boundary; at that boundary exact one of [ABSENT, PRESENT, INVALID, UNKNOWN]
  task_boundary_witness_ref: unset before the boundary; afterward optional exact reference and required when presence PRESENT
  task_boundary_state: unset before the boundary and unless presence PRESENT; then exact one of [MATCHED, NOT_MATCHED, UNKNOWN]
owl_turn_binding:
  owl_turn_ref: optional exact controller-preallocated finite-turn identity
  owl_candidate_ref: exact preallocated candidate identity when owl_turn_ref exists; otherwise unset
  owl_candidate_idempotency_key: required exactly when owl_candidate_ref exists; otherwise unset
  owl_candidate_expected_digest_or_validation_rule: required exactly when owl_candidate_ref exists; otherwise unset
  owl_candidate_exact_query_route: required exactly when owl_candidate_ref exists; queries that same canonical identity without rerunning the Owl act
  owl_retained_candidate_body_digest: exact digest only when an exact Owl candidate body is known retained; otherwise unset
  owl_retained_candidate_body_reopening_route: exact authorized locator, retrieval, integrity check, and same-ID CANDIDATE_SEAL_ONLY route sufficient to recover that digest-bound body only when it is known retained; otherwise unset with unavailability or uncertainty in unresolveds
  owl_turn_transaction_state: when turn exists, exact one of [PREALLOCATED, ACTIVE, SEALED_TERMINAL, OUTCOME_UNKNOWN, CANDIDATE_SEAL_ONLY, UNSEALED_TERMINAL]
  owl_candidate_state: when turn exists, exact one of [NOT_PRODUCED, SEALED, UNKNOWN]
  owl_candidate_validity_state: unset unless candidate SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
  owl_turn_disposition: unset unless candidate SEALED and VALID; then exact one of [CANDIDATE_COMPLETE, OWL_SUPPORT_REQUIRED]
  owl_predecessor_turn_ref: exact predecessor or declared absence
  owl_input_reference_digest: exact digest when turn exists; otherwise unset
custody_binding:
  member_homecoming_refs:
    work:
      return_receipt_ref: unset until the Work Return Receipt is appended; thereafter exact
      reconciliation_receipt_ref: unset until the Work Reconciliation Receipt is appended; thereafter exact
      context_close_receipt_ref: unset until the Work Context-Close Receipt is appended; thereafter exact
    task_keeper:
      return_receipt_ref: unset until the Task-Keeper Return Receipt is appended; thereafter exact
      reconciliation_receipt_ref: unset until the Task-Keeper Reconciliation Receipt is appended; thereafter exact
      context_close_receipt_ref: unset until the Task-Keeper Context-Close Receipt is appended; thereafter exact
    ledger_keeper:
      return_receipt_ref: unset until the Ledger-Keeper Return Receipt is appended; thereafter exact
      reconciliation_receipt_ref: unset until the Ledger-Keeper Reconciliation Receipt is appended; thereafter exact
      context_close_receipt_ref: unset until the Ledger-Keeper Context-Close Receipt is appended; thereafter exact
  homecoming_custody_state:
    work: unset before custody begins; thereafter exact current value
    task_keeper: unset before custody begins; thereafter exact current value
    ledger_keeper: unset before custody begins; thereafter exact current value
  hearthline_task_intake_ref: exact controller-owned intake account when the first member return becomes admissible; otherwise unset
  member_task_intake_receipt_refs:
    work: unset until the separate SEALED and VALID Work bundle is durably admitted; thereafter exact
    task_keeper: unset until the separate SEALED and VALID Task-Keeper bundle is durably admitted; thereafter exact
    ledger_keeper: unset until the separate SEALED and VALID Ledger-Keeper bundle is durably admitted; thereafter exact
  intake_admission_rule: each bundle enters RETURN_PENDING_HEARTHLINE and is admitted separately only after controller-observed SEALED plus separately observed VALID; INVALID, VALIDITY_UNKNOWN, UNKNOWN, and NOT_PRODUCED do not enter intake custody
hearthline_inspection_binding:
  inspection_context_ref: exact bounded root-task inspection context once any member intake receipt exists; otherwise unset
  inspection_grant_ref: exact current read grant for only the admitted member bundles; otherwise unset
  return_manifest_ref: exact controller-sealed three-slot manifest at the declared inspection boundary; otherwise unset
  return_manifest_state: unset before manifest candidate allocation; thereafter exact one of [NOT_PRODUCED, SEALED, UNKNOWN]
  return_manifest_validity_state: unset unless return_manifest_state is SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
  carry_selection_ref: controller-preallocated exact candidate identity once a SEALED plus VALID Return Manifest permits the selection act; otherwise unset; after seal it also binds the immutable body digest
  carry_selection_idempotency_key: required exactly when carry_selection_ref is preallocated; otherwise unset
  carry_selection_expected_digest_or_validation_rule: required exactly when carry_selection_ref is preallocated; otherwise unset
  carry_selection_exact_query_route: required exactly when carry_selection_ref is preallocated; queries the same canonical identity without replay
  carry_selection_state: exact one of [NOT_PRODUCED, SEALED, UNKNOWN] after candidate preallocation; otherwise unset
  carry_selection_validity_state: unset unless carry_selection_state is SEALED; then exact one of [VALID, INVALID, VALIDITY_UNKNOWN]
  carry_selection_coverage_state: unset before the inspection universe is frozen; thereafter exact one of [COMPLETE, INCOMPLETE, COVERAGE_UNKNOWN]
  carry_item_selection_by_item: unset until a SEALED and VALID Carry Selection; thereafter every candidate item has exactly one of [SELECT_KEEP, SELECT_CONDENSE, SELECT_LOSE]
  carry_selection_admission_rule: Carry Selection may be sealed only from a SEALED plus VALID return manifest, and only SEALED plus VALID plus COMPLETE Carry Selection may enter H_TO_T_CARRY
  carry_selection_authority_rule: Hearthline alone originates the semantic carry choice; Thulia may classify retention friction but cannot add, delete, or reinterpret selected meaning
  translation_board_request_refs: ordered exact Hearthline-authored requests or declared empty set once Carry Selection is frozen
  shorthand_serviceability_receipt_refs: exact Hearthline-authored, controller-appended serviceability decisions or declared empty set; Thulia and Gloss may record or apply a mapping but cannot mark it task-serviceable
  inspection_context_state: unset before its state family is allocated; thereafter exact one of [NOT_OPENED, OPEN_BOUNDED, CLOSE_PENDING, RAW_ACCESS_DROPPED, CLOSE_OUTCOME_UNKNOWN]
  inspection_close_receipt_ref: required exactly when inspection_context_state is RAW_ACCESS_DROPPED; otherwise unset
carry_handoff_binding:
  hearthline_to_thulia_lane_ref: exact one-way lane and grant before an offer; otherwise unset
  carry_handoff_transaction_ref: exact independently preallocated H_TO_T_CARRY identity before any emission attempt; otherwise unset
  carry_handoff_idempotency_key: exact key when carry_handoff_transaction_ref exists; otherwise unset
  carry_handoff_emission_state: unset before transaction preallocation; thereafter exact one of [NOT_EMITTED, EMITTED, EMISSION_UNKNOWN]
  carry_handoff_state: unset before transaction preallocation; thereafter exact one of [NOT_OBSERVED, ACCEPTED_BY_THULIA, REJECTED_BY_THULIA, HANDOFF_UNKNOWN]
  carry_handoff_admission_rule: only carry_selection_state SEALED plus carry_selection_validity_state VALID plus carry_selection_coverage_state COMPLETE under a current Thulia lane grant may reach ACCEPTED_BY_THULIA
  thulia_durable_receipt_ref: required exactly when carry_handoff_state is ACCEPTED_BY_THULIA; otherwise unset
predecessor_relay_compatibility_binding:
  applicability: only a TETHER reopening an already allocated v0.2-draft Triad Relay Envelope family; never allocated for the v0.3 selected-carry route
  triad_relay_envelope_ref: required exact predecessor reference whenever any owl_relay axis or relay_target_receipt_state is set; otherwise unset
  owl_relay_reference_state: unset before finite Triad Relay Envelope candidate; then exact one of [REFERENCE_COMPLETE, REFERENCE_INCOMPLETE]
  owl_relay_validity_state: unset before finite Triad Relay Envelope candidate; then exact one of [CURRENT, STALE, VALIDITY_UNKNOWN]
  owl_relay_emission_state: unset before finite Triad Relay Envelope candidate; then exact one of [NOT_EMITTED, EMITTED, EMISSION_UNKNOWN]
  relay_target_receipt_ref: unset before relay candidate and transaction; afterward exact separately numbered target receipt or declared absence
  relay_target_receipt_state: unset before relay candidate and transaction; initialized NOT_OBSERVED afterward, then exact one of [NOT_OBSERVED, RECEIVED, REJECTED, UNKNOWN]
translation_binding:
  thulia_to_gloss_lane_ref: exact one-way lane when translation is requested; otherwise unset
  gloss_to_thulia_lane_ref: exact distinct one-way lane when translation is requested; otherwise unset
  thulia_to_hearthline_lane_ref: exact distinct one-way lane for final readable carry; otherwise unset
  gloss_turn_ref: exact finite deterministic translation-turn identity when used; otherwise unset
  gloss_readiness_observation_ref: exact controller observation for this gloss_turn_ref after observation; otherwise unset; Gloss supplies no heartbeat or persistent readiness claim
  gloss_readiness_state: unset before the per-turn observation or when no gloss_turn_ref exists; thereafter exact one of [READY_FOR_EXACT_TURN, NOT_READY, READINESS_UNKNOWN]
  gloss_transaction_state: unset before a gloss_turn_ref exists; thereafter exact one of [PREALLOCATED, COMMITTED_SUCCESS, COMMITTED_SNAG, OUTCOME_UNKNOWN, SAME_TURN_RETRY_ONLY, NOT_COMMITTED_TERMINAL]
  active_shorthand_map_ref: exact immutable root-task-scoped map reference when activated; otherwise unset
  active_shorthand_map_digest: required exactly when active_shorthand_map_ref exists; otherwise unset
  active_shorthand_root_task_ref: required exactly when active_shorthand_map_ref exists; otherwise unset
  active_lexicon_generation_ref: required exactly when active_shorthand_map_ref exists; otherwise unset
  shorthand_service_state_by_mapping: exact one of [CANDIDATE, SERVICEABLE, NOT_SERVICEABLE, SERVICEABILITY_UNKNOWN, RETIRED_AT_TASK_CLOSE] for every referenced mapping
  revisit_rule: a later task reloads an exact retained lexicon generation under new access and serviceability review; it does not inherit serviceability from the earlier root-task map
  final_readable_carry_ref: exact Thulia-to-Hearthline result after any authorized Gloss turn, or exact no-translation carry; otherwise unset
  readable_return_transaction_ref: exact independently preallocated identity before any Thulia-to-Hearthline emission; otherwise unset
  readable_return_idempotency_key: required exactly when readable_return_transaction_ref exists; otherwise unset
  readable_carry_reference_state: unset before the Readable Carry Envelope candidate exists; then exact one of [REFERENCE_COMPLETE, REFERENCE_INCOMPLETE]
  readable_carry_validity_state: unset before that candidate exists; then exact one of [CURRENT, STALE, VALIDITY_UNKNOWN]
  readable_carry_emission_state: unset before that candidate exists; then exact one of [NOT_EMITTED, EMITTED, EMISSION_UNKNOWN]
  readable_carry_receipt_state: unset before transaction allocation; thereafter exact one of [NOT_OBSERVED, RECEIVED, REJECTED, UNKNOWN]
  readable_carry_store_outcome_ref: exact readable-carry store/controller receipt after a valid Readable Carry Envelope seal; otherwise unset
  readable_carry_store_outcome_state: unset before a valid envelope seal; thereafter exact one of [NOT_ATTEMPTED, COMMITTED, FAILED, OUTCOME_UNKNOWN]
  readable_return_admission_rule: only readable_carry_store_outcome_state COMMITTED plus owl_candidate_state SEALED plus owl_candidate_validity_state VALID plus owl_turn_disposition CANDIDATE_COMPLETE may feed T_TO_H_READABLE emission
  readable_return_receipt_ref: exact Hearthline target receipt when observed; otherwise unset
custody_close_and_retention_binding:
  selected_carry_store_outcome_ref: exact carry-store/controller receipt for durable custody of the accepted Carry Selection and every exact input still required by its declared translation and readable-return path; otherwise unset
  selected_carry_store_outcome_state: unset before that custody operation is admitted; thereafter exact one of [NOT_ATTEMPTED, COMMITTED, FAILED, OUTCOME_UNKNOWN]
  close_gate: inspection_context_state may enter CLOSE_PENDING only when carry_handoff_state is ACCEPTED_BY_THULIA and selected_carry_store_outcome_state is COMMITTED for the same carry_selection_ref; FAILED, OUTCOME_UNKNOWN, and NOT_ATTEMPTED do not satisfy the gate
  close_effect: RAW_ACCESS_DROPPED ends Hearthline's active access to the inspected Spark-return bodies; it does not assert hidden-state erasure, delete the external sources, or remove reopening handles
  systemic_friction_classification_ref: later Thulia-only classification over the immutable Carry Selection after required Gloss turns are terminal and readable_carry_store_outcome_state is COMMITTED and, when return is required, readable_carry_receipt_state is RECEIVED, or after an explicit no-translation/no-readable-return branch; unset until issued and never a substitute for Hearthline's selection
  retention_classification: unset before classification; thereafter exact one of [KEEP, COMPACT, ARCHIVE, PRUNE_ELIGIBLE, FRICTION_UNKNOWN_HOLD]
  canonical_store_effect_ref: exact later Atomic Edge Promotion transaction and receipt over the named canonical source boundary; otherwise unset
  canonical_store_effect_state: unset before that later edge is requested; thereafter exact one of [NOT_REQUESTED, AUTHORIZED, ATTEMPTED, COMMITTED, FAILED, OUTCOME_UNKNOWN]
  source_recoverability_state: unset before observation; thereafter exact one of [PRESERVED_EXACT, RECOVERABLE_FROM_AUTHORIZED_ARCHIVE, BOUNDARY_ONLY_UNRECOVERABLE, RECOVERABILITY_UNKNOWN] within one named recovery boundary
limits:
  consumed: exact time, actions, cost, context, disclosure, and other use
  remaining: exact remainder or explicit unknown for every declared limit
unresolveds: coverage gaps, blockers, holds, missing returns, source-loss versus access-failure status, and open burdens
next_wake_condition: externally observable predicate and observation route
handoff_binding:
  next_authorized_action: exact action or explicit none
  required_reviewer: exact identity or explicit none
  expiry_and_revocation_state: exact state at suspension
  purpose_guard_text: minimum canonical text needed to reject a mismatched successor
epoch_fence:
  require_exact_objective_epoch: true
  require_exact_authority_bundle: true
  require_bound_aggregate_authority_epoch_match: true
  require_current_aggregate_authority_epoch_for_resume_or_effect: true
  require_each_component_grant_valid_for_resume_or_effect: true
  separately_authorized_read_only_stale_inspection_permitted: true
  old_epoch_terminal_custody_exception_requires_separate_current_grant: true
  silent_rebase_permitted: false
reopening_route: exact retrieval, verification, revalidation, and return steps
```

The representation may differ, but none of those material relations may be
replaced by mutable labels such as `current task`, `latest contract`, `same
Hearthline`, or `the Spark that was working`. Each of the three members and
each of their three Homes remains separately addressable. At a declared
observation boundary, an absent member return or Task-Boundary Witness is
recorded as absent or unknown; proximity to the other two does not fill it.

Task-boundary presence is its own controller/store observation. The optional
`task_boundary_witness_ref` is required when
`task_boundary_witness_presence` is `PRESENT`, and only then may
`task_boundary_state` hold `MATCHED`, `NOT_MATCHED`, or `UNKNOWN`. For
`ABSENT`, `INVALID`, or presence `UNKNOWN`, the boundary state remains unset;
no Work, Ledger, Homecoming, liveness, or relay record may supply it by
inference. Before the Completion Contract's declared observation boundary,
presence, reference, and boundary state are all unset. Premature unset is not
`ABSENT` and is not a Task-Keeper return.

`member_execution_state`, `member_candidate_bundle_state`,
`member_candidate_bundle_validity_state`, `liveness_state`, and
`homecoming_custody_state` answer five different questions for each member.
They must not be collapsed into one another or into a Triad-wide liveness or
completion state. Liveness never establishes execution, progress, completion,
bundle existence, validity, or custody; execution never implies liveness. A
member may be `SEALED_TERMINAL`, have a `SEALED` and `VALID` candidate bundle,
show `NOT_APPLICABLE_AFTER_TERMINAL` for liveness, and still be
`RETURN_PENDING_HEARTHLINE` on its custody axis.

Predispatch or pre-observation silence is not a liveness result. Each member's
`liveness_state` remains unset until dispatch and the first contract-defined
due observation, unless execution becomes terminal first; terminalization sets
`NOT_APPLICABLE_AFTER_TERMINAL`. Otherwise, only after the first due boundary
may the controller record `OBSERVED_WITHIN_CONTRACT`,
`MISSED_BOUNDARY_UNKNOWN`, or `OBSERVATION_UNAVAILABLE`; it does not backfill an
observation into the inert formation or bound-but-not-dispatched interval.

An observed candidate append atomically commits bundle `SEALED` and execution
`SEALED_TERMINAL`; validity and custody are later, separate observations. A
sealed body classified `INVALID` remains `SEALED` and `SEALED_TERMINAL` but is
barred from Hearthline task-intake custody; `VALIDITY_UNKNOWN` is barred too,
and invalidity does not mean the body was not produced. An
ambiguous append or acknowledgement records bundle `UNKNOWN`, execution
`EXECUTION_UNKNOWN`, leaves validity and custody unset, and reconciles only the
same preallocated identity without replay. The member branch therefore carries
the controller-preallocated `candidate_bundle_ref`, its idempotency key, and its
expected digest or exact validation rule, plus the canonical same-identity
query route, whenever that identity exists.
`EXECUTION_UNKNOWN` is not resumable: the only permitted continuation is an
exact query of that candidate identity until the controller establishes an
observed seal or authoritative absence. If a later authoritative query proves
no append, a successor observation records the bundle transition `UNKNOWN` to
`NOT_PRODUCED` without rewriting the earlier observation.

A retained-body reopening route is conditional evidence, not presumed storage
and not authority. It is present only when the handle can name an authorized
locator, retrieval step, and integrity check sufficient to recover the exact
body governed by the candidate's expected digest or validation rule. If the
body was not retained, cannot be located, or retention is uncertain, the route
remains unset and that fact is recorded in `unresolveds`; neither `UNKNOWN` nor
a preallocated candidate identity implies that bytes survive. The member may
enter `RETURN_ONLY` only when the exact retained body remains valid, available,
and authorized for one same-body, same-identity seal attempt; no task action is
permitted. That attempt must also use the preallocated candidate's exact
idempotency key and pass its bound digest or validation rule. Otherwise the
member enters `UNSEALED_TERMINAL`. Either terminal execution state fixes
liveness at `NOT_APPLICABLE_AFTER_TERMINAL` and cannot be resumed.

`RETURN_ONLY` has two entrances and neither is a resume. A live `ACTIVE` or
`SPARK_SUSPENDED` member may enter it after cancellation, revocation, or
staleness solely to prepare the bounded terminal body allowed by the frozen
return rule. Separately, an `EXECUTION_UNKNOWN` member may enter it only after
the exact candidate query authoritatively proves no append and the retained
same body remains available, current, authorized, and bound to the original
identity and idempotency key. The first route may yield a zero-content typed
terminal return; the second permits only the one same-body seal attempt. No
route permits renewed task reasoning.

On the separate relay-validity axis, `STALE` requires an established mismatch,
supersession, revocation, expiry, or other failed validity condition. An
inability to establish current validity records `VALIDITY_UNKNOWN`, not
`STALE`.

A finite Owl act has its own preallocated transaction and candidate identities.
`owl_turn_transaction_state`, `owl_candidate_state`, candidate validity, and
the optional Owl disposition are separate. An observed candidate append
atomically records candidate `SEALED` and turn `SEALED_TERMINAL`; only a
`SEALED` and `VALID` candidate may carry `CANDIDATE_COMPLETE` or
`OWL_SUPPORT_REQUIRED`. Ambiguous append records candidate `UNKNOWN` and turn
`OUTCOME_UNKNOWN`; it permits only an exact query of the preallocated identity,
never another judgment, a resume, or automatic replay. If that query finds the
existing body, the controller records candidate `SEALED` and turn
`SEALED_TERMINAL` and validates it separately. Authoritative no-append records
the successor existence observation `NOT_PRODUCED`. If the exact candidate
body, digest, inputs, grant, and epochs remain retained and current, the turn
becomes `CANDIDATE_SEAL_ONLY`.
`CANDIDATE_SEAL_ONLY` permits only that same body under the same candidate
identity and idempotency key to attempt compare-and-append; it permits no new
judgment or rerun. Observed success atomically records candidate `SEALED` and
turn `SEALED_TERMINAL`. If no exact valid body remains, or its authority or
inputs are stale, the authoritative absence still records candidate
`NOT_PRODUCED` and the ended act becomes `UNSEALED_TERMINAL`; any new judgment
needs a separately authorized predecessor-linked Owl turn.

That Owl seal-only route is available only when the TETHER carries the
preallocated Owl candidate identity and idempotency key, its expected digest or
validation rule, its same-identity query route, the exact retained-body digest,
and an authorized reopening route that recovers the body matching that digest.
Those fields may instead be bound through one immutable reference that
explicitly contains all of them.
When exact retained bytes or their integrity cannot be established, the body
digest and route remain unset and the uncertainty is carried in `unresolveds`;
the handle does not infer retention from `OUTCOME_UNKNOWN`, candidate
preallocation, or the existence of an Owl turn.

The `owl_relay_*` axes and **Triad Relay Envelope** belong only to the preserved
`0.2-draft` candidate route. A TETHER reopening an already allocated
predecessor relay family must keep those axes unset until the exact
`triad_relay_envelope_ref` exists; setting any legacy relay axis or its target
receipt without that reference is invalid. Reference completeness, reference
validity, source emission, and the target receipt remain orthogonal, and an
ambiguous legacy transaction reconciles only its original preallocated
identity. Version `0.3-draft` does not mint or repurpose that envelope. Its
current selected-carry route uses the independent `H_TO_T_CARRY` transaction
and states below.

The return path therefore has two deliberate stages. First, each
controller-observed `SEALED` plus separately `VALID` member bundle returns
independently to the named Hearthline task intake as
`RETURN_PENDING_HEARTHLINE`; no aggregate envelope is needed to make the other
two readable. At the inspection boundary, the controller seals a three-slot
Return Manifest that accounts for each exact member with either its admitted
body or a typed absence, invalidity, or unknown exception. Only a manifest
whose state is `SEALED` and validity is separately `VALID` permits Hearthline
to freeze one immutable Carry Selection. Every candidate item is marked
exactly `SELECT_KEEP`, `SELECT_CONDENSE`, or `SELECT_LOSE`; the latter two
carry an explicit account of distinctions preserved and loss accepted. An
empty selection is still an explicit selection. Only a Carry Selection that is
itself `SEALED`, separately `VALID`, and coverage `COMPLETE` may enter the
Thulia handoff. An omitted item makes coverage `INCOMPLETE`; it is never
silently recast as `SELECT_LOSE`. Neither Thulia, Gloss, a Spark, nor the
controller may silently enlarge or rewrite the selection.

Second, the selected carry crosses the one-way Hearthline-to-Thulia lane under
its own preallocated transaction and idempotency key. Source
`carry_handoff_emission_state` is independently `NOT_EMITTED`, `EMITTED`, or
`EMISSION_UNKNOWN`; target `carry_handoff_state` is independently
`NOT_OBSERVED`, `ACCEPTED_BY_THULIA`, `REJECTED_BY_THULIA`, or
`HANDOFF_UNKNOWN`. Only a durable receipt bound to the same Carry Selection
establishes `ACCEPTED_BY_THULIA`. The carry store must then durably commit the
immutable selection and every exact input its declared downstream route still
needs. That `selected_carry_store_outcome_state: COMMITTED` is custody storage,
not a Systemic Friction classification or canonical retention effect.

Only after that custody commit and
`inspection_context_state: RAW_ACCESS_DROPPED` may Thulia route exact
Translation Board requests over distinct Thulia-to-Gloss and
Gloss-to-Thulia lanes. Gloss has no
heartbeat, continuing context, ledger, or inherited readiness. The controller
observes readiness for each finite deterministic turn;
`READY_FOR_EXACT_TURN` for one turn says nothing about the next. Thulia returns
the final readable carry through a fourth, distinct Thulia-to-Hearthline lane,
but only after the Readable Carry Envelope is itself `SEALED`, separately
`VALID`, `CANDIDATE_COMPLETE`, and durably stored with
`readable_carry_store_outcome_state: COMMITTED`. No direction may be inferred
from another lane's receipt. Its separate Hearthline receipt may seed a new
bounded planning context; it does not reopen the closed raw-return inspection
context. Only after every required Gloss turn is terminal, readable-carry
storage is `COMMITTED`, and any required Hearthline receipt is `RECEIVED`—or
the frozen selection expressly requires neither translation nor readable
return—may Thulia issue the later Systemic Friction classification. Any
canonical retention effect is later still and separately authorized.

Hearthline alone may mark a shorthand mapping task-serviceable. That decision
binds the root task, exact mapping, direction, lexicon generation, limits, and
serviceability receipt. Thulia may custody it and Gloss may apply it
deterministically; neither can make it serviceable by repetition or successful
translation. The active shorthand map closes when its originating root task
ends. A later revisit must reopen the exact retained lexicon generation and
obtain current access and a current Hearthline serviceability decision rather
than inheriting the former active map.

The bounded Hearthline inspection context cannot close merely because a Carry
Selection exists or emission was attempted. It remains `OPEN_BOUNDED` until
both `carry_handoff_state: ACCEPTED_BY_THULIA` and
`selected_carry_store_outcome_state: COMMITTED` bind that exact selection.
The controller may then enter `CLOSE_PENDING`; only a successful, separately
receipted access-drop transition establishes `RAW_ACCESS_DROPPED`. That state
withdraws Hearthline's active access to the raw Spark-return bodies, making the
reasoned omissions operational. It does not assert deletion of external
sources, erase ordered identities, or claim provider/model forgetting. A
failed custody store leaves the inspection context `OPEN_BOUNDED`; an
ambiguous access-drop leaves `CLOSE_OUTCOME_UNKNOWN` and reopens only the same
closure transaction.

Every branch has an explicit non-success disposition. A Carry Selection that
is `UNKNOWN`, `INVALID`, `VALIDITY_UNKNOWN`, `INCOMPLETE`, or
`COVERAGE_UNKNOWN` stays outside handoff and uses its same-identity query or
successor route. An unavailable Thulia leaves target receipt `NOT_OBSERVED`
and source emission separately exact; ambiguous acknowledgement leaves
`HANDOFF_UNKNOWN`; neither closes inspection. Selected-carry custody records `FAILED` or
`OUTCOME_UNKNOWN` without being recast as a retention decision. Gloss records
`NOT_READY`, `READINESS_UNKNOWN`, `COMMITTED_SNAG`, `OUTCOME_UNKNOWN`, or
`NOT_COMMITTED_TERMINAL` at the appropriate independent boundary. Readable
carry keeps reference, validity, emission, and receipt axes separate, so a
receipt `UNKNOWN` never becomes a resend instruction; readable-carry storage
`FAILED` or `OUTCOME_UNKNOWN` never permits emission. Missing retention
evidence becomes `FRICTION_UNKNOWN_HOLD`; canonical-store or recoverability
uncertainty remains `OUTCOME_UNKNOWN` or `RECOVERABILITY_UNKNOWN`. These are
holds or reconciliation routes, not additional TETHER state families and not
permission to infer success, prune, or preserve raw inspection access forever.

Homecoming receipts are likewise per member and per stage. A member's appended
Return Receipt does not imply its Reconciliation Receipt or Context-Close
Receipt, and one member's stage does not fill another member's missing stage.
Each of the nine stage references remains unset until its owning receipt is
actually appended; a later stage preserves rather than replaces the earlier
exact reference.

The provisioning records preserve a bootstrap-safe formation sequence. The
request carries Hearthline's nonbinding nomination for only the Work and
Task-Keeper seats; Thulia independently contributes a nonbinding nomination for
only the Ledger-Keeper seat. The controller validates them, reserves the
separate identities, grants, Homes, lanes, and exact candidate-bundle
identities and keys, and freezes a
complete Triad Formation Offer under one exact `formation_offer_ref` and
`formation_offer_digest`, including the authority bundle. Neither nomination
is authority or a seat binding, and `TRIAD_FORMATION_OFFERED` starts no member.

Only after seeing its authorized projection of that same frozen offer does each
provider submit a final own-seat intent. Hearthline's intent names the Work and
Task-Keeper selections; Thulia's intent names the Ledger-Keeper selection. Both
must name the same frozen Goal, Purpose Projection, Task Line, Completion
Contract, objective epoch, formation offer and digest, authority bundle, and
aggregate authority epoch. The canonical controller or store alone allocates
and appends those records and atomically compare-and-swaps both final intents,
the offer, reservations, authority components, and expected predecessors into
one binding receipt or nothing. A stale predecessor, mismatched frozen
reference, refusal, or changed component yields no partial binding and no
rewritten nomination, offer, or intent; a successor attempt receives new
ordered identities.

`triad_formation_state` and `triad_dispatch_state` remain separate. Even
`TRIAD_BOUND` is inert until the controller independently revalidates the
frozen bundle and appends the exact dispatch receipt that establishes
`DISPATCHED`; an offered or bound record never supplies its own dispatch.

The schema is stage-conditional, not a demand that future records already
exist. Before request creation, the formation reference and state are unset.
`TRIAD_FORMATION_REQUESTED` and `TRIAD_FORMATION_PENDING` always carry the
Hearthline nomination atomically included in the request, while only the
Thulia nomination and other records actually appended are conditional. They do not require an offer,
authority bundle, member reservation, final intent, binding receipt, Triad, or
dispatch. `TRIAD_FORMATION_OFFERED` requires the offer identity and digest,
reserved member records, reserved candidate-bundle identities and keys, and its
aggregate authority bundle, while either final intent may still be absent.
Those candidate identities are reservations only: no bundle state exists and
no append is permitted yet. `TRIAD_BOUND` additionally requires both final
intents, all three binding records, the exact consumed candidate reservations,
and the controller binding receipt. A
terminal refused or stale formation preserves every earlier-stage record that
already exists and leaves later-stage fields unset; it neither deletes a
frozen offer nor fabricates one. The member execution, bundle-existence,
validity, liveness, and custody fields shown in the schema apply only to its
fully bound state-bearing branch; an offered reservation names the future
candidate identity but leaves those later observations unset. Binding remains
inert until the separately revalidated dispatch receipt.

The authority bundle is an aggregate reference, not an aggregate grant. Its
digest binds Hearthline's provisioning grant, Thulia's provisioning grant,
the three separately issued member grants, and the recipient, audience,
disclosure, consequence, and effect limits. Any component change requires a
successor immutable bundle and advances the aggregate authority epoch. The old
bundle and epoch remain addressable but fenced.

On reopening, the external controller or store:

1. retrieves and verifies the exact TETHER and bound source records;
2. compares the frozen Goal ancestry, Task Line, Completion Contract, and
   ancestor states against the current objective decision;
3. verifies that the handle binds the exact historical dispatch-pinned
   `objective_epoch`, `authority_bundle_ref`, and aggregate `authority_epoch`,
   without treating that old epoch as current or selecting a convenient
   successor;
4. checks each member's separate execution, candidate-bundle existence,
   candidate-bundle validity, liveness, and Homecoming custody states before
   deciding which kind of continuation is possible, without casting one axis
   into another;
5. before any resume or task effect, requires the current aggregate authority
   epoch and revalidates both provisioning grants, each resumable member
   continuation and grant, recipient and effect limits, revocations, Homes,
   Heartbeat Contracts, and remaining limits while preserving consumed use;
   for custody of an already `SEALED` and `VALID` old-epoch body, it instead
   requires the separate current `terminal_return_custody_grant_ref`, exact
   body identity, and exact Hearthline task-intake recipient without making the
   historical task grant current;
6. appends an authorized Resume Receipt only for a member whose execution is
   `SPARK_SUSPENDED`, before that member takes another task action; and
7. reopens only the minimum source regions needed for the next declared
   boundary.

`SEALED_TERMINAL` and `UNSEALED_TERMINAL` refuse task-action resume. For
`SEALED_TERMINAL`, the controller may continue only the separately authorized
custody, Homecoming, carry-handoff, or target-receipt path for an already
`SEALED` and `VALID` candidate bundle. When its dispatch-pinned objective or
authority epoch is stale, that movement requires a separate current
terminal-return/custody grant naming the exact historical bundle, Hearthline
intake, permitted disclosure, and expiry. It cannot authorize task action,
resealing, semantic rewriting, rebinding, or epoch renewal. `RETURN_ONLY`
forbids task action and custody; it permits only
the exact bounded terminal-body preparation and same-identity seal attempt
declared by its return rule. Only an observed atomic seal may move execution to
`SEALED_TERMINAL`, after which separately authorized custody may begin.
The controller does not wake a terminal member, append a Resume Receipt for it,
or reinterpret pending custody as live execution.

A stale objective or authority epoch fails closed. A stale authority bundle,
component grant, recipient limit, effect limit, or aggregate authority epoch
does the same for task action and external effect. Either stops further work
and returns the
candidate Task Triad disposition
`STALE_OBJECTIVE_EPOCH` or `STALE_AUTHORITY_EPOCH`, and preserves a TETHER
route by which an authorized controller may inspect, reframe, or redispatch
the work. These names are candidate design vocabulary, not adopted PAL or
repository-wide status values. Reopening never silently rebases an old Triad
onto new wording, uses a meaningful parent-purpose edge as permission, or
turns a successor dispatch into continuation of the predecessor.

This fail-closed rule does not strand a body that sealed and validated before
the task epoch went stale. A separately issued, current terminal-return/custody
grant may move only that exact immutable body into the named Hearthline intake
and onward through the already bounded return route. Its receipt records the
historical stale epoch and the independent current custody grant together.
Failure to validate that grant leaves custody pending or rejected; it never
revives the Spark or silently admits the body under the old authority.

That fail-closed rule fences continuation and effects; it does not make the
historical handle forbidden to inspect. A separately authorized, current
read-only inspection grant may retrieve and verify the stale TETHER, its exact
old bundle, and its old epoch for diagnosis. Such inspection neither resumes
the member nor makes the old authority current. Reframing or redispatch then
requires a separately authorized successor objective and new ordered records;
the stale handle remains ancestry, not authority.

### Late evidence does not revise an old witness

A TETHER may route evidence that becomes available after a Task-Keeper has
sealed `UNKNOWN`. It may not use that evidence to mutate the old witness,
remove its missing-reference account, or pretend the evidence was present at
the earlier boundary. The old numbered witness remains `UNKNOWN`.

If the controller authorizes a reopened or successor objective, it first pins
the then-current exact Task Line, Completion Contract, objective epoch,
authority bundle, aggregate authority epoch, and component grants. It then
admits a new bounded Task-Keeper evaluation. The Task-Keeper proposes a witness
against the newly admitted references; the controller allocates and appends its
new number. That witness names the old witness as predecessor and binds the
late-evidence and reopening receipts. A different successor value records a
new evaluation boundary; it does not rewrite history or revive a closed
predecessor context.

### Telemetry is not a pulse

A spinner, `Working` label, animated loading surface, periodically refreshed
page, or other interface indicator is presentation telemetry. It may show what
one interface most recently rendered. It does not establish that the task host
is running, that a model or process is advancing, that bytes have committed,
that a Pulse Receipt exists, or that any completion boundary was reached. When
the last durable boundary is old and the host cannot be independently queried,
the honest liveness and progress status remains unknown.

A Task-Keeper—called a Heartbeat-Keeper only as a lore alias—keeps the Task
Line and Completion Contract visible. It owns no pulse series. When it shares
the process, session, context window, transport, or host failure domain of the
Worker, it stops being observable when that domain fails and therefore cannot
watchdog the domain. Adding another same-domain Spark repeats the dependency;
it does not make the observation external.

The canonical controller or durable store across the watched failure boundary
owns the clock, maximum-pulse deadline, timeout observation, suspension or
revocation transition, wake-condition observation, and Resume Receipt. Missing
a boundary establishes only what the Heartbeat Contract declares—normally
unknown liveness followed by suspension or revocation. It does not prove that
the underlying work failed, completed, or never happened.

## 10. Hearthline integration

Hearthline may use TETHER during directly authorized work when continuity would otherwise depend on fragile conversational recall.

- A **Work Spark** may emit a TETHER handle for its exact artifact, receipts, open burdens, and next route.
- A **Task-Keeper Spark** may check that a handle pins the declared Goal, Task
  Line, Completion Contract, objective epoch, authority bundle, aggregate
  authority epoch, and boundary evidence. It cannot allocate a pulse, change
  the task, self-supply a result, watchdog its own host, or schedule, wake,
  resume, or revoke a member.
- A **Ledger Scribe Spark** may record or validate a handle within its own grant, but it cannot use the handle to select actions or read outside its access boundary.
- **Hearthline task intake** receives the Work, Task-Boundary Witness, and
  Ledger bundles separately through controller-observed Homecoming. Admission
  requires `SEALED` plus `VALID` for that member and creates
  `RETURN_PENDING_HEARTHLINE`; no member or aggregate may fill a missing bundle.
- **Hearthline inspection** freezes the immutable Carry Selection and any
  Translation Board requests. Hearthline alone originates the semantic carry
  choice and marks a shorthand mapping task-serviceable.
- **Thulia** may custody or translate only the selected handle between declared
  lanes when direction, source, target, and grant are current. She alone may
  classify Systemic Friction, but she cannot originate or rewrite Hearthline's
  semantic Carry Selection.
- **Selected-carry storage** is a custody prerequisite for dropping
  Hearthline's raw inspection access. It preserves the exact downstream inputs
  but performs no Systemic Friction classification or canonical retention
  effect.
- The current **Hearthline-to-Thulia handoff** uses one selected-carry
  transaction with separate `carry_handoff_emission_state` and target-owned
  `carry_handoff_state`. The older **Triad Relay Envelope** and `owl_relay_*`
  axes remain predecessor-only; if reopened, every populated legacy axis must
  name its exact `triad_relay_envelope_ref`.
- **Gloss** performs only one pinned deterministic translation turn. It is
  stateless and heartbeat-free; readiness is observed by the controller per
  turn and is never inherited from a prior successful turn.
- A **Readable Carry Envelope** is the exact finite Owl candidate. It must be
  sealed, valid, `CANDIDATE_COMPLETE`, and durably stored before its independent
  return transaction may emit.
- **Canonical retention** occurs only after the readable-return prerequisites
  are satisfied. Thulia classifies; a separately authorized writer performs
  and receipts any Atomic Edge Promotion; recoverability remains an
  independent observation inside a named boundary.
- **Homecoming** may return a TETHER handle as representation-side data. `RETURNED` and `RECONCILED` remain custody states; they do not verify the payload or manufacture its result status.
- **Hearthline's active shorthand map** may retain a task-scoped handle under
  an exact lexicon generation, but the shorthand cannot replace the source
  trace. The active map closes with the root task; a revisit reopens the exact
  retained generation under new access and serviceability review.

TETHER complements suspension: before a long pause or context boundary,
externalize the material trace, bind the task and epoch fence, record the
residuals and reopening route, then append the applicable per-member or
coordinated-objective suspension. On return, revalidate the grant, objective
epoch, immutable authority bundle, aggregate authority epoch, every component
grant, and handle before any continuation or effect. A separate current
read-only inspection grant may verify a stale handle without reviving it.

## 11. Minimal conformance examples

### Git or repository carrier

Bind repository, commit, path, and blob or content digest. Reopen the exact file or range needed. Branch names alone are mutable and do not establish exact identity.

### Workflow or computation artifact

Bind run identity, artifact identity, source commit, procedure version, declared inputs, and digest when available. A successful download establishes retrieval; the artifact's own tests and claim ceiling control what its contents support.

### Versioned document

Bind document identity and version or immutable revision. If only a mutable shared link exists, carry `RETRIEVED_UNVERIFIED` or `STALE` as appropriate rather than claiming byte continuity.

### Database or object store

Bind snapshot or transaction identity, schema/query version, object version, and relevant partition. Reading today's current row is not reopening yesterday's snapshot unless the store establishes that relation.

### Conversation or transcript

Bind exact message, turn, export, or transcript-range identity when available. A summary is a projection and must carry its omissions. If the exact prior wording cannot be recovered, lead with that status before offering a reconstruction.

### Stalled interface or host

Bind the last externally committed task boundary and exact affected-member and
coordinated-objective reopening bundle. Record the observed spinner or
`Working` label only as interface telemetry, never as a Pulse Receipt. An
external controller or store compares each member's last committed pulse with
that member's frozen maximum boundary, records `MISSED_BOUNDARY_UNKNOWN` or
`OBSERVATION_UNAVAILABLE` on the liveness axis as the evidence warrants, and
fences affected execution into `SPARK_SUSPENDED` or `RETURN_ONLY` only as its
contract authorizes. It derives no aggregate Triad liveness. When the
return path itself cannot deliver the frozen handoff, the controller may record
the candidate triad disposition `HOST_HANDOFF_BLOCKED` with the exact TETHER
route rather than inferring success or loss. Current
`carry_handoff_emission_state` and `carry_handoff_state` remain unchanged
unless their owning boundary separately commits a transition. If the TETHER
also reopens a preserved predecessor relay, its `owl_relay_*` axes and
`relay_target_receipt_state` likewise remain unchanged and must keep their exact
`triad_relay_envelope_ref`. Interface telemetry cannot manufacture
`EMITTED`, `ACCEPTED_BY_THULIA`, `REFERENCE_COMPLETE`, `CURRENT`, or
`RECEIVED`. An affected member resumes only if its execution state is
`SPARK_SUSPENDED` and the objective epoch, authority bundle, aggregate
authority epoch, component grants, member continuation, Home, remaining
limits, and wake condition are revalidated. A replacement host receives a
successor dispatch unless exact continuation is established.

## 12. Compact operating rule

> **Externalize what must survive. Bind the smallest honest handle. Reopen only what the present task needs. Carry every unresolved item with its route home.**

## 13. Status and authorship

This document is a public design proposal for the Hearthline repository. It adds no runtime, storage provider, credential, persistent memory, external connection, task grant, or authority. Implementation and adoption are separate acts.

Christopher D. Pang is the author and steward of TETHER. AI systems assisted with extraction, naming refinement, adversarial review, drafting, repository preparation, and validation as tools. They are not authors, co-authors, owners, witnesses, or authorities.
