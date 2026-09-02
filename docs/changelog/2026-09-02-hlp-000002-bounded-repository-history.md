# Bounded public history and return-data clarification

| Field | Value |
|---|---|
| Change ID | `HLP-000002` |
| Record kind | `REPOSITORY_HISTORY_PROMOTION` |
| Recorded date | 2026-09-02 |
| Predecessor | `HLP-000001` |
| Conversion base | `c81e8550dbf868aefd835b28d7f4ebdd06a03ae2` |
| Scope | `PUBLIC_REPOSITORY_HISTORY_AND_DESIGN_CLARIFICATION` |
| Record authority | `NONE` |
| Record effect | `REPOSITORY_HISTORY_ONLY` |
| Containing documentation effect | `HOMECOMING_0.2_CLARIFICATION` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Replaced the accumulating root changelog with a navigation index capped at
  one current 25-record cohort and fixed-range archive indexes.
- Added one frozen full record for each accepted repository-history promotion
  and one bounded backfill for pre-index history.
- Added one marked, replace-in-place **Latest repository change** block at the
  end of `README.md`.
- Added a standard-library-only structural validator for the README, index, and
  full-record topology.
- Preserved the former accumulated changelog through an exact pinned link
  instead of retransmitting or duplicating it.
- Advanced Paired Sparks and Homecoming from `0.1` to `0.2` to state that a
  Ledger Scribe's representation-side return carries declared data;
  `RETURNED` and `RECONCILED` do not themselves classify or reclassify it as
  evidence, a finding, a conclusion, or a result.

## Why

The README should orient; the root changelog should route; full records should
carry detail. Separating those jobs keeps the root surfaces bounded while
preserving a durable recovery path for decisions, scope, verification
observations, compatibility, and unresolveds. The design clarification keeps
transport distinct from interpretation: data comes home before any separately
governed evaluation.

## Preserved boundaries

- Git remains the byte-level history. Markdown records are curated navigation
  and declared interpretation.
- Public history contains an authorized public synthesis only.
- Representation-side observations and checks remain data unless a separately
  declared evaluation rule, evaluator, and authority boundary make a narrower
  evidence or result claim. An already-evaluated Work Spark artifact keeps its
  status; Homecoming neither creates nor erases it.
- No change-history record activates Hearthline, adopts policy, implements a
  design, admits Static, grants access, or creates authority.

## Compatibility and migration

Paired Sparks and Homecoming advances from `0.1` to `0.2`; its implementation
status and authority ceiling do not change. No controlling instruction,
candidate manifest, source profile, license, or operational boundary changed.
Earlier history remains available through Git and the pinned pre-conversion
changelog.

For each future accepted change, the same commit adds exactly one full record,
prepends exactly one matching index row, and replaces the single marked README
block. A mismatch blocks promotion. This atomic promotion is repository-history
bookkeeping only.

## Verification observations

Run from the repository root:

```sh
python3 tools/check_change_history.py
```

The validator checks the unique EOF marker block; README, index, archive, and
note size ceilings; current and archived cohort topology; global ID sequence;
newest-record alignment; index-to-record closure; required headings; row-to-file
date, ID, and kind agreement; repository-confined relative links; and forbidden
public-history text forms.

## Open residuals

- Validation is local and non-authoritative; no hosted workflow or background
  automation was added.
- GitHub object links identify repository objects but do not authenticate a
  person or prove local adoption.
- This first promotion has no containing-commit value in its own record; Git
  history identifies the commit that introduced it without a self-reference.

## Evidence and exclusions

The conversion base and predecessor record establish the declared input
boundary. No private source link, identifier, hash, transcript, prompt, hidden
reasoning, operational state, receipt, credential, or raw log is carried into
this public record.

[Current changelog](../../CHANGELOG.md)
