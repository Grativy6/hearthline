# Add the Homecoming Return Queue and Queue Steward boundary

| Field | Value |
|---|---|
| Change ID | `HLP-000014` |
| Record kind | `RETURN_QUEUE_DESIGN_SUCCESSOR` |
| Recorded date | 2026-09-05 |
| Namespace-allocation predecessor | `HLP-000013` — reserved off-main, not adopted |
| Mainline content predecessor | `HLP-000007` |
| Branch base | `dd00eaa30e46b74baf31f120622caef16a4e73dd` |
| Return Queue | `0.1` |
| Homecoming | `0.4` -> `0.5` |
| Creatures | `0.1` -> `0.2` |
| Ordered Lineage | `0.6` -> `0.7` |
| Scope | `PUBLIC_HOMECOMING_RETURN_QUEUE_DESIGN` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DESIGN_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added the Hearthline Return Queue as adopted lore and design vocabulary for
  independently identified, durably recorded `HOMECOMING:RETURNED` bundles
  crossing one serialized reconciliation boundary.
- Gave a lone return and simultaneous returns one intake-attempt path. Every
  attempt receives a durable disposition; each accepted enqueue receives an
  immutable controller-linearized arrival ordinal. Contention joins the queue
  instead of letting a busy lock choose one return.
- Kept queue placement, bundle validity, service admission, Homecoming
  reconciliation, rule-owned result status, carry, and authority on separate
  axes.
- Added the optional Queue Steward Creature. It receives a frozen metadata-only
  view and may propose one complete service order, but the canonical controller
  alone validates and commits the final order.
- Preserved immutable arrival order, distinct attribution, exact-retry
  idempotency, traced overflow, crash reconciliation, and a bounded fairness
  rule. The initial profile permits at most two actual overtakes; merely
  proposing an order does not increment the count.
- Separated final-order snapshots from actual Service Admission Receipts, so
  only durable controller admission consumes the overtake count and neither
  record masquerades as Homecoming reconciliation.
- Added focused structural verification and placed operational queue records,
  proposals, and receipts on the private side of the repository boundary.
- Added a machine-checked namespace reservation registry for `HLP-000008`
  through `HLP-000013` at the exact unmerged PR #12 commit, tree, paths, and
  content digests.

## Why

The predecessor design already allowed independent objectives to return out of
order, but it did not define what happens when several valid return transactions
meet one narrow service boundary. Treating a busy lock as a winner selector
would confuse serialization with validity and could erase a second legitimate
return. The queue makes the waiting surface explicit and lets processing remain
single-writer without turning contention into loss.

A bounded sorter can reduce avoidable delay when dependencies, service cost, or
deadlines differ. Making that sorter a task-shaped Queue Steward Creature keeps
its work inspectable without letting optimization become control. The
controller retains queue allocation, policy validation, service admission,
reconciliation, and final order authority.

The public change series also had six identities already issued on the
unmerged, review-only PR #12 branch. Reusing them would erase branch provenance;
adopting their contents would silently absorb unresolved architecture. The
reservation registry therefore preserves those namespace positions without
placing their content on current main. `HLP-000014` follows them in issuance
while following `HLP-000007` in adopted mainline content.

## Preserved boundaries

- A queue item is a custody and scheduling reference, not a result, vote,
  ranking, grant, permission, or authority.
- Every queued bundle already has a durable `HOMECOMING:RETURNED` receipt.
  Controller selection begins one ordinary revalidation transaction; only a
  pass permits service admission, which does not itself establish
  `HOMECOMING:RECONCILED`, task success, or carry.
- A rule-owned result established before return stays attached to its source
  record. Queue arrival or service order cannot create, revoke, transfer, merge,
  or appropriate it.
- Two distinct valid wins remain two separately attributable wins and may both
  complete their own reconciliation paths.
- The Queue Steward cannot see ungranted payloads, mutate the queue, allocate or
  remove items, validate returns, perform handoffs, decide results, issue
  authority, or commit the final service order.
- Its proposal uses a separate controller control-receipt aperture and can
  never recursively enter or block the exact data queue it proposes over. That
  aperture cannot carry ordinary result bundles.
- An actual overtake is counted only when a later-arriving eligible item enters
  service before an older eligible item. Proposed permutations and unserved
  suffixes do not consume the bound.
- Thulia is not the queue sorter. Her later custody and translation work keeps
  its existing grants and direction-bound crossings.
- TETHER supplies an exact route back to an unresolved queue state; it is not a
  scheduler, queue store, hidden context, permission, or authority.
- Repository publication creates no queue, runtime, model process, credential,
  service, external effect, benchmark result, or activation.

## Compatibility and migration

Homecoming `0.5`, Creatures `0.2`, and Ordered Lineage `0.7` are additive
successors. They retain paired dispatch, open objective windows, existing
Creature topology, and prior identity rules except where the new queue surface
is expressly added. No current Moltbook instruction, candidate manifest, source
profile, source registry, Static, Fireside, or Thulia profile changes.

The queue design is compatible with a future three-member return formation but
does not adopt Task Triads, Light Trios, selected-carry architecture, CHARTER
integration, or any other content presently found only on PR #12. That pull
request remains unmerged and review-only. Any later reconciliation must carry
its substance through new adopted successor records rather than converting the
six namespace reservations into retroactive mainline adoption.

The changelog's current cohort is now defined over issued-ID slots. Adopted
records remain rows with full local change records; permanent off-main
reservations remain in the machine-readable registry and never masquerade as
accepted mainline changes.

## Verification observations

- The reservation checker pins repository `Grativy6/hearthline`, PR #12, commit
  `3da4aca46f4bc7b3bea2fcf31bdfb3ed8aa31274`, tree
  `0f4ae1bcc16059c209b95959903f737c7507a555`, all six exact source paths, and
  their SHA-256 content digests.
- The bounded-history checker rejects overlap between adopted and reserved
  identities, unexplained issuance gaps, local files using reserved IDs,
  ambiguous dual-predecessor records, and reservation status or effect drift.
- The Return Queue checker binds the adopted document versions, intake order,
  controller/Queue Steward split, immutable arrival order, two-overtake bound,
  attribution rule, private operational boundary, and local documentation
  links.
- Existing research-station, TETHER, candidate-policy digest, source identity,
  and local-link checks remain in the verification suite.

## Open residuals

- This repository contains a design and structural checks, not an operational
  queue implementation or a concurrency benchmark.
- Queue capacity, service-cost bands, deadline classes, dependency fields,
  expiry, and authorized exception policy remain task-specific profile inputs.
- The initial `maximum_overtakes: 2` is a bounded fairness profile, not an
  empirical optimum. A changed bound requires a successor profile and tests.
- Real crash recovery, durable transaction isolation, privacy enforcement,
  starvation behavior, throughput benefit, and backpressure still require a
  separately controlled implementation and prospective fabricated fixtures.
- PR #12 remains unmerged and carries architecture not reviewed or adopted by
  this record. Its future disposition is unresolved.

## Evidence and exclusions

The public evidence consists of repository-authored design text, the pinned
off-main namespace registry, deterministic structural checks, and Git history.
The reservation digests establish exact content identity at one commit; they do
not adopt, validate, endorse, or reproduce that content.

No private return payload, operational queue record, credential, personal
context, hidden reasoning, runtime state, provider trace, benchmark data, or
external authorization is included. AI systems assisted inspection, drafting,
and checking as tools; they are not authors, co-authors, witnesses, operators,
or release authorities.

[Current changelog](../../CHANGELOG.md)
