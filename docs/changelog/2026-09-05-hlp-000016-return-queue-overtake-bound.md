# Narrow the maximum-overtake claim

| Field | Value |
|---|---|
| Change ID | `HLP-000016` |
| Record kind | `RETURN_QUEUE_CLAIM_NARROWING` |
| Recorded date | 2026-09-05 |
| Predecessor | `HLP-000015` |
| Frozen predecessor SHA-256 | `3c9620320309573023e0f3659dba00d3cd52328999be2edab7fd4ab6d2dd2ae1` |
| Branch base | `aa2bcbd855dbd8cadc90bbd985925811cae12153` |
| Return Queue | `0.2` -> `0.2.1` |
| Scope | `PUBLIC_RETURN_QUEUE_CLAIM_NARROWING_ONLY` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DESIGN_CLAIM_NARROWING_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Advanced the governing Hearthline Return Queue document from `0.2` to
  `0.2.1` without changing its queue state machine, priority policy, receipt
  identities, or controller boundary.
- Defined `maximum_overtakes` as a count of successful admissions of
  later-arriving eligible items ahead of a continuously `READY` item while
  controller service continues.
- Replaced language that could be read as promising starvation freedom or
  eventual disposition with an explicit claim ceiling: the bound is not a
  wall-clock latency bound, controller-liveness promise, or
  eventual-disposition guarantee.
- Narrowed the Morrow-availability statement to queue correctness, dispatch
  priority, and fairness-rule computation. The controller fallback remains
  available, but its existence does not compel the controller or host to run.
- Updated the public changelog, latest-change pointer, Return Queue checker,
  and bounded-history checker as one release-discipline successor.

## Why

The `0.2` text correctly counted an overtake only when a later-arriving
eligible item was successfully admitted first. Its phrase “cannot be
indefinitely starved,” however, could be read as a wall-clock or eventual
service guarantee. The nearby statement that eventual disposition did not
depend on Morrow could likewise be read as promising disposition even if the
controller stopped servicing the queue.

The mechanism establishes a conditional admission-count bound, not an event
source. If controller service stops, no scheduling rule can establish when it
will resume or whether a pending return will eventually receive a disposition.
The narrower statement preserves the useful fairness invariant without
claiming liveness the design does not supply.

## Preserved boundaries

- The counter still increments only for a successful admission of a
  later-arriving eligible item ahead of the older item. A proposal, final order,
  failed admission, or unserved suffix does not consume an overtake.
- The claim applies to an item that remains continuously `READY` and is
  conditional on controller service continuing. Held, terminal, unknown,
  expired, revoked, or otherwise non-ready intervals do not become latency
  evidence.
- Reaching the bound still makes the item fairness-due under the frozen base
  rule, subject to the already declared, separately authorized and receipted
  exception path.
- Dispatch priority still cannot overtake a fairness-due item under the
  ordinary rule. It creates no result status, permission, authority, grant,
  budget, deadline extension, or service admission.
- Morrow remains optional, deterministic, stateless, proposal-only, and
  formally without authority. Only the controller computes the fallback,
  persists counts, commits order, and admits service.
- HLP-000015 remains the unchanged, frozen predecessor. This successor does
  not rewrite its full record or silently alter its recorded claim surface.
- Publication does not create a queue, scheduler, controller, service loop,
  timer, runtime, task, result, effect, or authority.

## Compatibility and migration

Return Queue `0.2.1` is a claim-narrowing documentation successor to `0.2`. It
does not change queue state, ordering, receipts, authority, or runtime behavior.
No queue item, priority assignment, revision, arrival ordinal, overtake count,
snapshot, proposal, order, admission, disposition, or Homecoming record is
migrated or rewritten.

An implementation conforming to the `0.2` mechanism may adopt the narrower
claim without changing its data. Any separate implementation or service-level
statement that promises wall-clock latency, controller availability, or
eventual disposition requires its own assumptions, authority, evidence, and
versioned record.

## Verification observations

- The Return Queue checker requires governing version `0.2.1`, the conditional
  successful-admission bound, and the explicit latency, liveness, and
  eventual-disposition exclusions.
- The bounded-history checker covers HLP-000016 through the ordinary gap-free
  index, latest-record, full-record, heading, link, and size rules.
- The bounded-history checker pins the byte digest of HLP-000015 so this
  successor cannot silently revise its predecessor record.
- Existing Research Station and TETHER checks remain applicable and unchanged.

## Open residuals

- This documentation does not measure scheduler fairness, throughput, service
  latency, availability, recovery time, or eventual disposition.
- “Controller service continuing” would require an implementation-specific
  operational definition before it could support a measured service claim.
- Aging and maximum-overtake policy values remain bounded design choices, not
  demonstrated universal optima.
- The separately authorized exception route can defer a fairness-due item only
  under its recorded blocker, duration, remedy, and reopening conditions; a
  future implementation must test that path independently.

## Evidence and exclusions

The public evidence is limited to the changed governing prose, this bounded
successor record, deterministic structural checks, and Git history. It is not
an execution trace, queue run, fairness measurement, latency observation,
liveness proof, or operational receipt.

No private payload, queue state, credential, provider trace, benchmark result,
hidden reasoning, external authorization, or runtime behavior is included. AI
systems assisted inspection, drafting, adversarial review, repository
preparation, and validation as tools; they are not authors, co-authors,
witnesses, operators, or release authorities.

[Current changelog](../../CHANGELOG.md)
