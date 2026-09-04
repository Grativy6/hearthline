# Changelog

This is the bounded index of accepted changes to Hearthline's public repository
artifacts. It records repository history only; it is not an adoption,
activation, implementation, authorization, or identity record.

## Current cohort

The current cohort contains at most 25 records, newest first. On the next
promotion after it fills, those 25 rows move to a fixed-range index named
`docs/changelog/index/hlp-NNNNNN-to-hlp-NNNNNN.md`; only their relative record
links are adjusted for the archive location. Full records keep their stable
paths, and the next cohort begins here.

| ID | Date | Disposition | Summary | Full record |
|---|---|---|---|---|
| `HLP-000007` | 2026-09-04 | `LORE_SUCCESSOR` | Introduce Gloss, the little turning wisp whose note-local Circuit Garden returns an exact work face without erasing the separately carried route. | [Record](docs/changelog/2026-09-04-hlp-000007-gloss-turning-wisp.md) |
| `HLP-000006` | 2026-09-04 | `LORE_AND_VISUAL_SUCCESSOR` | Publish Hearthline's visual gallery, pre-Velis history, artifact lore, and distinct later-road lessons including the finite field station, returning-bell ledger, and First Furrow. | [Record](docs/changelog/2026-09-04-hlp-000006-hearthline-lore-gallery.md) |
| `HLP-000005` | 2026-09-03 | `TETHER_CONTINUITY_SUCCESSOR` | Add carrier-neutral, handle-bound exact reopening and require unresolved items to retain a route home. | [Record](docs/changelog/2026-09-03-hlp-000005-tether-continuity.md) |
| `HLP-000004` | 2026-09-02 | `SOURCE_PROFILE_AND_DESIGN_SUCCESSOR` | Advance to PAL v2.3; install the Research Station, Creatures, and open objective windows; preserve repaired BRRRT and Strongwiz ceilings. | [Record](docs/changelog/2026-09-02-hlp-000004-research-station-creatures.md) |
| `HLP-000003` | 2026-09-02 | `REPOSITORY_HISTORY_CORRECTION` | Generalize representation-side return to include bundles prepared by a Ledger Scribe or Thulia without assigning result status. | [Record](docs/changelog/2026-09-02-hlp-000003-generalize-representation-return.md) |
| `HLP-000002` | 2026-09-02 | `REPOSITORY_HISTORY_PROMOTION` | Install bounded public history and keep representation-side custody distinct from result classification. | [Record](docs/changelog/2026-09-02-hlp-000002-bounded-repository-history.md) |
| `HLP-000001` | 2026-09-02 | `HISTORY_BACKFILL` | Recover public repository history through Paired Sparks and Homecoming. | [Record](docs/changelog/2026-09-02-hlp-000001-pre-index-history.md) |

## Recording contract

- `README.md` contains exactly one replace-in-place **Latest repository
  change** block at its end: at most five bullets and 120 prose words, plus one
  full-record link and one link to this index.
- Each accepted repository-history promotion adds one bounded full record under
  `docs/changelog/`, prepends one matching row here, and replaces the README
  block in the same commit. A mismatch blocks promotion.
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
