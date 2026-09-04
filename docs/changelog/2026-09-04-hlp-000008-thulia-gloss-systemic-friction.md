# Separate Thulia, Gloss, Hearthline, and account custody

| Field | Value |
|---|---|
| Change ID | `HLP-000008` |
| Record kind | `ROLE_CUSTODY_SUCCESSOR` |
| Recorded date | 2026-09-04 |
| Predecessor | `HLP-000007` |
| Branch base | `dd00eaa30e46b74baf31f120622caef16a4e73dd` |
| Prior public draft | `0.4-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2` |
| Successor public draft | `0.5-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2` |
| Scope | `PUBLIC_ROLE_AND_CUSTODY_DESIGN` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DRAFT_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Assigned distinct jobs to Hearthline, Thulia, Gloss, the Sparks, and the
  canonical controller. Hearthline orchestrates the primary task without
  taking over Owl custody, deterministic translation, retention
  classification, or another account's write lane.
- Made every Static or payload ledger the property of its declared task or
  representation account. A Spark receives one exclusive bounded write lane
  for one exact job; Homecoming closes that lane and returns durable custody to
  the canonical store.
- Reduced Thulia's roost to a partitioned pointer, status, hold, and exception
  index. Hearthline-facing offer records remain in Hearthline's task account;
  Work and Scribe payloads remain in their task or representation accounts.
- Defined Gloss as a stateless deterministic relay driven only by the canonical
  input, complete route, direction, and pinned validated lexicon generation.
  Routine translation reads no history and does not improvise missing meaning.
- Added a detachable **Translation Slate**. It belongs to the translation
  account, is replaceable, and is custodied by Thulia; it is an external
  interface and record carrier, not Gloss's body, mind, memory, identity,
  property, or private ledger.
- Made **Systemic Friction** Thulia's exclusive retention-classification lane
  under a separate current grant. Its typed results include `KEEP`, `COMPACT`,
  `ARCHIVE`, `PRUNE_ELIGIBLE`, and `FRICTION_UNKNOWN_HOLD`.
- Kept classification separate from effect. `PRUNE_ELIGIBLE` does not delete or
  authorize deletion; a canonical controller or separately authorized writer
  must revalidate the current candidate and holds before any Atomic Edge
  Promotion.
- Refreshed current-facing visual and character references to Thulia profile
  `OWL-000001/PROFILE-000004` without changing her appearance sheet or images.

## Why

Thulia appeared to carry three ledgers: Hearthline's received offers, the
payloads of Thulia-bound Sparks, and Gloss's translation history. That shape
made one custody role look like several overlapping jobs and invited
Hearthline to fill in when the Owl path was unavailable.

The repair locates durable state where the work is accountable. The primary
task account records what Hearthline received and did with an offer. Task and
representation accounts retain Spark payloads. The translation account retains
lexicon generations and compact turn marks on its detachable slate. Thulia
keeps only the small partitioned index needed to locate, validate, hold, and
reopen those records.

Gloss consequently needs no remembered interaction state. Determinism belongs
to its complete declared transform, while the externally appended mark records
that a particular turn occurred. Thulia may tend the pinned lexicon and slate
without asking Gloss to learn from history or treating the slate as part of the
wisp.

Systemic Friction remains a distinct Owl rule because it evaluates burdens and
obligations outside the abstract computational transform. The result can guide
a later authorized storage transition without granting Thulia task governance
or giving any Spark a veto based on possession or self-preservation language.

## Preserved boundaries

- Hearthline remains the primary-task orchestrator and decision surface. It may
  request, inspect, reject, or reopen Thulia's return, but it does not substitute
  its own Owl classification or silently assume the job when Thulia is absent.
- Thulia remains non-governing for primary-task truth, advice, action,
  working-context carry, grants, and external effects. Her exclusive retention
  classification exists only under its separately declared grant.
- Gloss remains distinct from Thulia's numbered Bridge Gloss handoff record.
  It has no Spark identity, model context, history read, adaptive learning,
  authority, memory ownership, ledger ownership, or retention choice.
- The Translation Slate is detachable from Gloss. Replacing a slate or moving
  translation-account custody does not alter Gloss's identity or transform.
- A Spark may raise a retention defect only by naming an exact replay, open,
  contest, privacy, safety, or other account obligation that the transition
  would violate. Authorship, continuity language, or “my memory” creates no
  self-preservation veto.
- No ledger, payload, note, receipt, Static entry, translation mark, or returned
  context is a Spark's or Gloss's body, identity, memory, or property. Only a
  typed retention defect naming a declared account obligation, including any
  valid hold, may block a retention transition.
- The retention lane is closed to records explicitly declared account-owned
  `G_mutable` before review. Any future persistent, autobiographical,
  identity-bearing, or agent-owned Spark or Gloss state requires separate
  governance and cannot be relabeled account-owned to bypass an identity or
  refusal claim.
- A retention classification is not a mutation. Atomic Edge Promotion belongs
  to the canonical controller or another separately authorized writer and
  receives a distinct effect record.
- Account custody, Static admission, working-context carry, result
  classification, authority, deployment, and public release remain separate.

## Compatibility and migration

The public Moltbook instruction advances from `0.4-draft` to `0.5-draft` and
the candidate manifest is rebound to its exact normalized-LF bytes. The source
profile remains `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2`; status remains
`DRAFT_NOT_ACTIVATED`, default mode remains `DRAFT_ONLY`, and authority and
effect remain `NONE`.

Existing task, representation, and translation records do not move merely
because the ownership language is clarified. An implementation migrates by
binding each ledger to its account, issuing a Spark an explicit bounded lane,
closing that lane at Homecoming, and keeping Thulia's index pointer-only. Any
former Gloss-history surface becomes or is replaced by a translation-account
slate; it is not adopted as Gloss memory.

Earlier public history remains frozen. In particular, HLP-000007 and its lore
artifact are preserved as the predecessor presentation; this successor supplies
the controlling operational distinctions without rewriting that record.

## Verification observations

- `tools/check_research_station.py` checks the role split, account ownership,
  Spark-lane closure, Fireside account boundaries, pointer-only Owl index,
  stateless Gloss contract,
  detachable-slate boundary, exclusive Systemic Friction lane, retention-defect
  ceiling, and separation of `PRUNE_ELIGIBLE` from Atomic Edge Promotion.
- The same check rejects a declared list of selected legacy ownership phrases
  and a Gloss-owned surface in the current controlling documents while leaving
  frozen lore and change history outside that retrofit check.
- Candidate validation binds `candidate_manifest.json` to the exact
  normalized-LF bytes of `hearthline_agent.md` at `0.5-draft`.
- `tools/check_change_history.py` continues to require an atomic README latest
  block, changelog row, and bounded full record without changing its predecessor.
- Link validation, JSON parsing, Python compilation, and whitespace checks
  remain part of the repository verification path.

## Open residuals

- These are public design contracts, not evidence that a controller, account
  store, Spark lane, Gloss transform, Translation Slate, or Thulia service has
  been implemented or deployed.
- The exact Systemic Friction cost schema, calibration fixtures, thresholds,
  privacy policy, hold precedence, contest procedure, and Atomic Edge Promotion
  transaction remain implementation and paper work.
- A validated lexicon-generation format, canonicalization rule, mark schema,
  concurrency discipline, and test-vector corpus for Gloss remain to be built.
- The correct account granularity and retention horizon remain task-specific;
  this change does not create a universal ledger layout or universal scalar
  friction score.
- Systemic Friction is working Hearthline design vocabulary pending the paper's
  reviewed release. It is not PAL canon, a controlling source, a physical law,
  or a Research Station source-registry entry.

## Evidence and exclusions

This record preserves the public role partition, custody model, deterministic
translation contract, retention-classification seam, changed paths, and
verification claims. It excludes raw conversations, hidden reasoning, private
artifacts, credentials, local paths, operational state, personal data, and any
claim that the described components are live.

Christopher D. Pang supplied the role distinctions, named Systemic Friction as
Thulia's rule, required the detachable account-owned slate correction, and
controls adoption. AI systems assisted with analysis, drafting, repository
preparation, and validation as tools; they are not authors, co-authors,
witnesses, owners, or authorities.

[Current changelog](../../CHANGELOG.md)
