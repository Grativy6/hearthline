# Changelog

This is the bounded index of accepted changes to Hearthline's public repository
artifacts. It records repository history only; it is not an adoption,
activation, implementation, authorization, or identity record.

## Current cohort

The current cohort covers at most 25 issued-ID slots. Adopted records appear
newest first; permanently reserved off-main slots remain in the separate
registry below. On the next promotion after the cohort fills, its adopted rows
move to a fixed-range index named
`docs/changelog/index/hlp-NNNNNN-to-hlp-NNNNNN.md`; only their relative record
links are adjusted for the archive location. Full records keep their stable
paths, and the next cohort begins here.

| ID | Date | Disposition | Summary | Full record |
|---|---|---|---|---|
| `HLP-000026` | 2026-09-10 | `LORE_SUCCESSOR` | Establish the Cooperative for Auditable Provenance as Hearthline's canonical fictional common record beyond any one task, without sovereignty or operational authority. | [Record](docs/changelog/2026-09-10-hlp-000026-cooperative-for-auditable-provenance.md) |

## Archived cohorts

- [HLP-000001 through HLP-000025](docs/changelog/index/hlp-000001-to-hlp-000025.md)

## Issued off-main namespace reservations

`HLP-000008` through `HLP-000013` were issued on unmerged PR #12 at one exact
commit but were never adopted on `main`. They remain permanent namespace
reservations with status `RESERVED_OFF_MAIN_NOT_ADOPTED` and effect
`NAMESPACE_ONLY_NO_ADOPTION`. Their content is neither copied into nor endorsed
by this index. Exact commit, tree, path, and digest bindings are in the
[machine-readable reservation registry](docs/changelog/branch-reservations.json).
The separate [branch archive ledger](docs/changelog/branch-archive.json) keeps
the complete PR #4 and PR #12 reopening handles without copying their contents.

## Recording contract

- `README.md` contains exactly one replace-in-place **Latest repository
  change** block at its end: at most five bullets and 120 prose words, plus one
  full-record link and one link to this index.
- Each accepted repository-history promotion adds one bounded full record under
  `docs/changelog/`, prepends one matching row here, and replaces the README
  block in the same commit. A mismatch blocks promotion.
- An identity issued on an unmerged branch may be preserved permanently in the
  reservation registry. Reserved IDs remain absent from adopted rows and local
  full records; adopted and reserved IDs together must be gap-free and neither
  status nor content may silently cross between them.
- A retired review lane remains branch-local. Its exact commit/tree handle and
  selected path pointers preserve a reopening route, not content adoption.
- Full records are frozen after addition. Corrections and supersessions receive
  a new record; an earlier record is not silently rewritten.
- Public history receives only an authorized public synthesis. Raw fragments,
  conversations, prompts, hidden reasoning, private paths or identifiers,
  credentials, operational state, receipts, and redundant command output are
  excluded.
- A representation-side return bundle, including one prepared by a Ledger
  Scribe or Thulia, may carry changed paths, observations, checks, compatibility
  signals, and unresolveds as data.
  `RETURNED` and `RECONCILED` do not by themselves classify or reclassify it as
  evidence, a finding, a conclusion, a result, Static, or authority.
- `REPOSITORY_HISTORY_PROMOTION` has effect `REPOSITORY_HISTORY_ONLY`. “Atomic
  promotion” here means that the three history surfaces change together; it
  does not mean policy adoption, runtime activation, implementation, release
  authorization, or Static admission.

The preceding accumulated changelog remains available at its
[pinned pre-conversion state](https://github.com/Grativy6/hearthline/blob/c81e8550dbf868aefd835b28d7f4ebdd06a03ae2/CHANGELOG.md).
Git remains the byte-level source for commit history.
