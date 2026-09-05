# Add a retry-rotation release before readiness re-entry

| Field | Value |
|---|---|
| Change ID | `HLP-000017` |
| Record kind | `RETURN_QUEUE_RETRY_ROTATION_SUCCESSOR` |
| Recorded date | 2026-09-05 |
| Predecessor | `HLP-000016` |
| Frozen predecessor SHA-256 | `16a0790ed32cbe66644fbbe02c94405b4224488f77ef38b4f2bd76c11e5fbcff` |
| Branch base | `9dd7e86867f3fe5e93f5d6c5fc3ce891173adac7` |
| Return Queue | `0.2.1` -> `0.3` |
| Ordered Lineage | `0.8` -> `0.9` |
| Scope | `PUBLIC_RETURN_QUEUE_RETRY_ROTATION_DESIGN_ONLY` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DESIGN_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added a controller-owned **Retry Rotation Release Receipt** between a failed
  or unknown pre-admission Service Disposition Receipt and the Readiness Receipt
  that returns the held item to `READY`.
- Required a `FAILED` or `UNKNOWN` disposition `D` to move the selected item
  `x` into `HELD` while preserving its pre/post `overtake_count` as the same
  value `K`. An `UNKNOWN` disposition must be reconciled before release.
- Required exactly one accepted release `Q` for each `(x, D)` failed-attempt
  generation, in exactly one mode: `OTHER_ITEM_SERVICE_ATTEMPTED` or
  `NO_OTHER_ELIGIBLE_READY`.
- Made that mode choice evidence-determined: any qualifying later distinct-item
  service attempt after `D` requires `OTHER_ITEM_SERVICE_ATTEMPTED`; only the
  absence of such an attempt permits `NO_OTHER_ELIGIBLE_READY`.
- Required the Readiness Receipt `R` to bind the unique `Q`, ordinary resolved
  remedy, current revalidation inputs, and `PASS` before moving `x` back to
  `READY`.
- Added one immutable controller-linearized `service_ordinal` to each selected
  service transaction and its typed admission or pre-admission disposition.
- Advanced Ordered Lineage to `0.9` with a distinct readable identity form for
  the new release receipt and preserved the private/public boundary around its
  operational records.

## Why

Return Queue `0.2.1` correctly moved a failed selected head out of `READY`, but
ordinary remedy and a fresh passing check could immediately return the same
high-priority item to the next snapshot. Because failed pre-admission checks do
not consume overtakes, repeated fast failure and re-entry could keep presenting
that item without proving that another eligible return received a service
attempt.

The new receipt closes only that rotation gap. If another eligible item exists,
the failed item cannot reopen until a distinct item receives a later typed
service attempt. If no other eligible item exists, an exact current snapshot
and head may release the retry without manufacturing a fictional neighbor.
Neither mode asserts that an attempt succeeded or that service will continue.

## Preserved boundaries

- `D`, `Q`, and `R` are distinct typed controller receipts. One cannot stand in
  for another, and `Q` is accepted at most once for the pair `(x, D)`.
- `OTHER_ITEM_SERVICE_ATTEMPTED` requires a later typed Service Admission
  Receipt or pre-admission Service Disposition Receipt for a distinct item in
  the same queue, profile and service epoch, a greater `service_ordinal`, and
  proof that `x` remained continuously held from `D` through the release cut.
- `NO_OTHER_ELIGIBLE_READY` requires the exact pre-reopen snapshot digest and
  queue-head digest with controller-derived `other_ready_count = 0`. The release
  and readiness transition compare and swap that head so a stale empty view
  cannot reopen `x` after another item becomes ready.
- Over the typed service receipts after `D` through that bound head,
  `NO_OTHER_ELIGIBLE_READY` also requires controller-derived
  `qualifying_later_attempt_count = 0`. If a qualifying later distinct-item
  attempt exists, `Q` must use `OTHER_ITEM_SERVICE_ATTEMPTED`, even when the
  current `other_ready_count` is zero.
- Evidence for both modes or neither mode is invalid. Mode cannot be relabeled
  from current readiness after its governing attempt history exists, nor
  inferred from the failure, payload, priority, or Morrow output.
- An unresolved `UNKNOWN` disposition cannot source `Q`. Reconciliation to an
  actual admission follows in-service recovery; only reconciliation to failure
  may enter the release path.
- The controller journals idempotency before append. An exact replay returns the
  same `Q`/`R` identities and disposition; changed bindings, a duplicate release
  for `D`, or stale queue state records conflict without mutation. An ambiguous
  append is reconciled before re-entry.
- Ordinary remedy and current `PASS` remain necessary. `Q` is not readiness,
  admission, Homecoming reconciliation, result status, or authority.
- `D`, `Q`, and `R` leave `K` unchanged. `R` changes only queue eligibility
  from `HELD` to `READY`; `Q` and `R` mutate no priority, authority, grant,
  Homecoming or payload custody, result, selected carry, budget, expiry,
  deadline, or external-effect state.
- Morrow receives no retry-release identity, mode, evidence, service ordinal,
  held proof, snapshot or head digest, remedy, or revalidation result. He
  remains deterministic, stateless, and proposal-only.
- Thulia receives none of the release surface and has no channel, state,
  ledger, Perch, custody, invocation, impersonation, or dependency crossing
  with Morrow.
- The design claim is limited to attempt rotation under continued controller
  enforcement. It does not promise wall-clock latency, successful admission,
  controller liveness, or eventual disposition.
- HLP-000015 and HLP-000016 remain byte-for-byte frozen predecessors. This
  successor does not revise their full records.

## Compatibility and migration

Return Queue `0.3` and Ordered Lineage `0.9` are additive design successors.
They require a new queue profile and service epoch before the retry-rotation
rule governs. Existing items may finish under their frozen predecessor profile
or cross through an explicit controller migration receipt that preserves item
identity, arrival evidence, priority history, grant, status, consumed limits,
and `overtake_count`.

A predecessor Service Disposition Receipt without a controller-linearized
`service_ordinal` is not silently upgraded into mode evidence and cannot source
a `0.3` release. A held predecessor item remains governed by its frozen
predecessor rule or receives an explicit bounded handoff. Only a new failed
attempt occurring under the migrated `0.3` profile and service epoch may create
a source `D`; migration cannot fabricate a later service attempt or a past
continuous-held interval. Existing receipt identities are not renumbered or
overwritten.

The change does not alter Homecoming, TETHER, Creature, Morrow, Thulia, Static,
Fireside, source-profile, candidate, or research-station versions.

## Verification observations

- The Return Queue checker binds version `0.3`, the `D -> Q -> R` sequence,
  unchanged `K`, reconciliation-before-release, exclusive release modes,
  uniqueness, exact-retry idempotency, current remedy and `PASS`, and the
  attempt-rotation-only claim ceiling.
- It requires the other-item mode's distinct identity, same queue/profile/epoch,
  greater service ordinal and continuous-held proof, plus the no-other mode's
  exact snapshot/head, derived zero other-ready and qualifying-attempt counts,
  compare-and-swap protection, and mandatory other-item mode whenever a
  qualifying later attempt exists.
- It excludes every release field from Morrow and Thulia and preserves their
  complete surface and availability separation.
- The Ordered Lineage check binds the new typed receipt identity and service
  ordinal without changing earlier receipt identities.
- The bounded-history checker pins the existing HLP-000015 and HLP-000016 full
  record digests while applying ordinary gap-free and latest-record checks to
  HLP-000017.

## Open residuals

- This repository specifies no live queue, controller, scheduler, retry loop,
  store, timer, service worker, or external effect.
- The rule does not guarantee that a service attempt passes. Several failing
  items may continue rotating attempts without producing a successful
  admission or terminal disposition.
- The rule cannot make the controller or host continue, recover, or service an
  item within any wall-clock interval.
- Correct derivation of `other_ready_count`, durable held-interval proof,
  service-ordinal allocation, atomic `Q`/`R` append, compare-and-swap recovery,
  and migration require a separately controlled implementation and fabricated
  prospective tests.
- An implementation must define bounded storage, crash behavior, and retention
  for release idempotency and one-use consumption without widening the public
  claim.

## Evidence and exclusions

The public evidence consists only of repository-authored design text,
structural checks, and Git history. It is not a runtime trace, scheduler test,
fairness measurement, liveness proof, service-level agreement, or operational
receipt.

No private queue state, task or return payload, credential, provider trace,
benchmark data, hidden reasoning, external authorization, or operational
identity is included. AI systems assisted inspection, drafting, adversarial
review, repository preparation, and validation as tools; they are not authors,
co-authors, witnesses, operators, or release authorities.

[Current changelog](../../CHANGELOG.md)
