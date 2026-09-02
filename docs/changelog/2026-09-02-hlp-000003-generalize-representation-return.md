# Generalize representation-side return custody

| Field | Value |
|---|---|
| Change ID | `HLP-000003` |
| Record kind | `REPOSITORY_HISTORY_CORRECTION` |
| Recorded date | 2026-09-02 |
| Predecessor | `HLP-000002` |
| Correction base | `111f8d47ef9aa67cb3676bc0eb1faf4ed808d9f6` |
| Scope | `PUBLIC_DESIGN_CLARIFICATION` |
| Record authority | `NONE` |
| Record effect | `REPOSITORY_HISTORY_ONLY` |
| Containing documentation effect | `HOMECOMING_0.3_CLARIFICATION` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Advanced Paired Sparks and Homecoming from `0.2` to `0.3`.
- Generalized the representation-side custody rule from a Ledger Scribe return
  to any representation-side return bundle, including one prepared by a Ledger
  Scribe or Thulia.
- Replaced Scribe-side “outcomes” with terminal-state data in the current
  orientation and controlling Homecoming document.
- Preserved the separate rule that a Work Spark artifact may retain status
  already established under its task's declared evaluation rule.
- Replaced the README latest-change block and prepended the matching root-index
  row without altering the frozen `HLP-000002` full record.

## Why

The `0.2` wording correctly prevented Homecoming custody from creating result
status, but named only Ledger Scribes. Thulia may also perform separately bounded
representation work. The generalized rule closes that scope seam without
erasing status established upstream by a Work Spark's declared evaluation.

## Preserved boundaries

- A representation-side bundle carries declared data; custody alone neither
  assigns nor removes evidence, finding, conclusion, or result status.
- An already-evaluated Work Spark artifact keeps its status. Homecoming neither
  creates nor erases it.
- The earlier `HLP-000002` record remains frozen and historically accurate as a
  narrower statement.
- No history record activates Hearthline, implements a design, admits Static,
  grants access, or creates authority.

## Compatibility and migration

Paired Sparks and Homecoming advances from `0.2` to `0.3`. No Spark, Fireside,
Static, Ordered Lineage, Thulia, controlling instruction, candidate manifest,
source profile, license, or operational boundary changes. Implementations do
not exist in this repository and therefore receive no runtime migration.

## Verification observations

The local structural validator closed the README, current index, and three full
records; checked their caps, identifiers, kinds, dates, links, sequence, and
required sections; and returned `CHANGE_HISTORY_OK`. Python compilation and
`git diff --check` completed without error before promotion.

## Open residuals

- The design remains unimplemented and unevaluated.
- This correction does not define a task-specific evaluation rule or decide the
  status of any future Work Spark artifact.
- The containing commit is not embedded in its own record; Git supplies that
  anchor without a circular self-reference.

## Evidence and exclusions

This record contains public repository-change data only. It excludes private
source links or identifiers, raw conversations or prompts, hidden reasoning,
operational state, receipts, credentials, local paths, and unreviewed payloads.

[Current changelog](../../CHANGELOG.md)
