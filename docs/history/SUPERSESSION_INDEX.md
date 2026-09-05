# History and supersession index

Status: `REPOSITORY_HISTORY_MAP_ONLY`

This index is a derived reading aid. Git objects, frozen HLP records, and exact source receipts remain controlling. No entry adopts a candidate, activates an instruction, or disposes of a branch or pull request.

## Branch topology

| Ref | Head | Classification | Reading rule |
|---|---|---|---|
| `main` | `dd00eaa30e46b74baf31f120622caef16a4e73dd` | `CURRENT_CANON` | Current default-branch history; not runtime adoption |
| `lore/the-night-the-garden-clicked-20260904` | `a6552c1ad23f078d96a7a5247b1f0fd4f4936ec8` | `ACTIVE_CANDIDATE` | Candidate predecessor |
| `lore/creature-charter-20260905` | `49d600cda356711aeb42381a76fb680bbfcd3b5e` | `ACTIVE_CANDIDATE` | Newest coherent candidate, not adopted |
| `design/thulia-gloss-systemic-friction-20260904` | `54bf6971edbc42738314754dcd199cede3f4484a` | `OPEN_CONFLICT` | Divergent design sibling retained for its semantics |
| `codex/thulia-visual-lineage` | `1780aafb13db926a49cd298b1765f260a5e3a145` | `OPEN_CONFLICT` | Open, conflicting PR #4 |

## Candidate-local HLP sequence

- HLP-000008 records the role and custody split.
- HLP-000009 records a fictional Thulia-first return.
- HLP-000010 records the candidate's earlier mechanical Thulia-first return.
- [`docs/WIP_TASK_TRIAD_CHECKPOINT_2026-09-04.md` at candidate `49d600c`](https://github.com/Grativy6/hearthline/blob/49d600cda356711aeb42381a76fb680bbfcd3b5e/docs/WIP_TASK_TRIAD_CHECKPOINT_2026-09-04.md), blob `ae049929ad04668ea58d4e6e8b12590d8d7f61c0`, preserves that HLP-000010-era topology. Its bytes remain unchanged and its context is `SUPERSEDED_CONTEXT`.
- HLP-000011 supersedes the return topology without rewriting HLP-000010 or the WIP checkpoint: three member returns go separately to Hearthline; only selected carry crosses to Thulia.
- HLP-000012 adds the CHARTER/Creature companion without adopting the branch.

The candidate already owns HLP-000008 through HLP-000012 while `main` ends at HLP-000007. This review-only branch allocates no HLP ID. A lineage decision is required before an atomic promotion.

## Squash topology preserved

| Trace-bearing branch head | Recorded squash result | Relationship |
|---|---|---|
| `0f77147b77b067223857f9628b9e86b5c93ee7b0` | `c81e855…` | Equal parent and tree; distinct commit identity |
| `a6373e81b6f26cd61d6131be102cfdf024770456` | `111f8d4…` | Equal parent and tree; distinct commit identity |
| `8911aea76c379e01d4572cad55f951a5a3033700` | `355dfa8…` | Equal parent and tree; distinct commit identity |
| `e38673a113156e86030560efe6394b62388295a7` | `dd00eaa…` | Equal parent and tree; distinct commit identity |

Equal trees do not erase the review history recorded by those branch heads.

## PR #4 old-to-current image map

PR #4 is open, conflicting, and not redundant. These eight proposed image blobs already exist byte-for-byte on current `main`; the PR's six Markdown blobs remain unique.

| PR #4 path | Blob | Exact current path |
|---|---|---|
| `assets/characters/hearthline/HEARTHLINE-IMAGE-000001-gremlin-hunter-reference-sheet.png` | `ec83e6bbf711f58448f2d9022af2f37cb1a0a828` | `assets/characters/hearthline-gremlin-hunter-reference-sheet.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000001-fireside-portrait.png` | `d1218e4ad2a0b28fb01ba335cc941187638d12a0` | `assets/characters/history-and-artifacts/thulia-fireside-portrait-study.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000002-naturalistic-model-sheet-study.png` | `f2fe17b6c1515b8bf1307ad33dd60258e6ce8509` | `assets/characters/history-and-artifacts/thulia-naturalistic-model-sheet-study.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000003-cartoon-expression-sheet-study.png` | `a538ad613c9c580f21ebf4710824789ae71c938d` | `assets/characters/history-and-artifacts/thulia-cartoon-expression-sheet-study.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000004-bilateral-sheet-initial.png` | `c5c17fd2b3aaf3a62fed80c42f1a796ece5ea672` | `assets/characters/history-and-artifacts/thulia-bilateral-sheet-initial.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000005-bilateral-sheet-front-correction.png` | `bb0d2726c6c7ea2f33866990b9f483d746fdd15d` | `assets/characters/history-and-artifacts/thulia-bilateral-sheet-front-correction.png` |
| `assets/characters/thulia/OWL-000001-IMAGE-000006-bilateral-animation-reference.png` | `469e1fc04fa81d26ea8437dbc08b6e6aeacc9783` | `assets/characters/thulia-bilateral-animation-reference-sheet.png` |
| `assets/scenes/OWL-000001-IMAGE-000007-hearthline-thulia-fireside.png` | `95fe547936bca9c1482857c97dcb05b1a25b76c4` | `assets/scenes/hearthline-and-thulia-at-the-trace-workbench.png` |

No map entry closes, merges, rebases, or deletes PR #4. Reopen at <https://github.com/Grativy6/hearthline/pull/4> and review the six unique Markdown blobs separately.

## Historical workflow

GitHub's workflow registry still calls the removed one-shot TETHER integration workflow active. Its definition is absent from every current branch tip; the last historical definition had repository write permission and all four historical runs failed. Treat the registry/file mismatch as `OPEN_CONFLICT` and its bytes as `HISTORICAL_PROVENANCE`.

## Immutable recording rules

- Read `BOUNDARY.md`, `SOURCE_MAP.md`, `CHANGELOG.md`, and all validators before editing.
- Never modify an existing `docs/changelog/*.md` record; correct with a successor.
- Never allocate a new HLP ID until the exact base lineage is selected.
- An accepted history promotion changes, in one commit, one new full HLP record, one new first changelog row, and the sole final README latest-change block.
- Keep literal status markers and claim ceilings; maps never authorize execution.
- Do not infer redundancy from equal trees or blobs.
- Use commit-pinned public cross-repository links.
- Name private repository roles without publishing private locators, paths, filenames, or hashes.

## Decision not taken

No candidate adoption, HLP allocation, PR closure, branch deletion, merge, runtime action, or external effect is implied. Reopen a decision from the exact ref above and the verified all-ref backup.
