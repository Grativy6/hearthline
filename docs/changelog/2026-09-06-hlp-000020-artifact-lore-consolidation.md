# Move the artifact gallery beside its lore

| Field | Value |
|---|---|
| Change ID | `HLP-000020` |
| Record kind | `LORE_ARTIFACT_TOPOLOGY_SUCCESSOR` |
| Recorded date | 2026-09-06 |
| Predecessor | `HLP-000019` |
| Frozen predecessor SHA-256 | `bab3e325d924f465cbef79c9da60dd0748fc6b73f1c5edf9e6cda7b0a7c5ec5d` |
| Branch base | `33ee75f22def49bb42ecf75a37528e5c3acffed5` |
| Branch-base tree | `0e2f5537230f3e59e6088f52004329b22a7c43f0` |
| Scope | `PUBLIC_LORE_PRESENTATION_ONLY` |
| Record authority | `NONE` |
| Record effect | `LORE_ARTIFACT_TOPOLOGY_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Moved the artifact landing page and Holds Nothing Back woodland illustration
  from `assets/artifacts/` into a new [lore artifact branch](../../lore/artifacts/).
- Promoted the exact Rainbow Shell source image from the former nested artifact
  history room into the same lore branch and folded its caption into the branch
  landing page.
- Kept Holds Nothing Back visibly linked as the hero image at the
  [lore entrance](../../lore/README.md).
- Gathered Holds Nothing Back, the Rainbow Shell, Mira's first brass loupe, and
  the Circuit Garden into one object catalog. The loupe and Circuit Garden keep
  their canonical scene files; the catalog references rather than duplicates
  those image bytes.
- Updated the root map, visual-gallery route, artifact-story links, and visual
  index paths to match the new topology.

## Why

These objects are legible because stories give them relationships, uses, and
limits. Keeping their index under `assets/` separated the object pictures from
the lore that explained them and left a one-image gallery branch standing on
its own. The new topology makes artifacts a branch of lore while preserving
Holds Nothing Back as an immediate visual entrance rather than burying it
behind prose.

The consolidation also makes room for an object to carry lore without requiring
every illustration of that object to move or be copied. A scene stays a scene;
the artifact branch can point to it as a visual anchor.

## Preserved boundaries

- The two relocated PNGs retain their exact bytes and existing visual
  identities.
- The loupe and Circuit Garden scene PNGs remain at their existing paths and
  are not duplicated.
- Moving or presenting an image changes no character sheet, operational
  specification, software behavior, permission, credential, grant, identity,
  consent, or authority.
- Holds Nothing Back, the Rainbow Shell, the loupe, and the Circuit Garden are
  fictional lore objects. Their catalog is not a build guide or claim that a
  depicted mechanism exists.
- Earlier HLP records remain frozen and unchanged.

## Compatibility and migration

Repository-relative links now target `lore/artifacts/` instead of the removed
`assets/artifacts/` tree. The Holds Nothing Back story and exact visual registry
follow the relocated images. The general asset gallery now routes readers to
the lore artifact branch while continuing to host character, Creature-form,
and scene files.

The Rainbow Shell keeps `HEARTHLINE/IMAGE-000002`, and the woodland test keeps
`HEARTHLINE/IMAGE-000008`. Reclassification from the former nested history room
to the present artifact branch changes presentation side only; it does not
rewrite either image's bytes or declared provenance status.

## Verification observations

- The relocated Holds Nothing Back PNG has SHA-256
  `734c187bde60c594fcc920e7d02521ca3aaaca7a26dc419c59e73717f092be4c`.
- The relocated Rainbow Shell PNG has SHA-256
  `2ead5044ca62f2920782cb11425d476199a53fc58ce080e75b454c1ae13d3bf1`.
- Git recognized both PNG operations as exact renames, and no image content was
  modified by this successor.
- Every repository-local Markdown link resolves after the move.
- The repository-history, branch-archive, research-station, Return Queue, and
  TETHER checkers pass, as do Python syntax and whitespace checks.

## Open residuals

- External links that name the removed `assets/artifacts/` paths cannot be
  rewritten by this repository; Git history retains the former locations.
- The immediately preceding art-only commit introduced three PNGs not yet
  included in the visual registry count, reused two registered Hearthline image
  ordinals in the scene README, and replaced the bridge bytes without updating
  its registered digest. This pre-existing visual-index repair is deliberately
  not folded into an artifact-topology change.
- The object catalog is intentionally selective. A later object may join it
  only through a separate reviewed change rather than by implication.

## Evidence and exclusions

Public evidence consists of the two exact image digests, Git rename detection,
the updated relative links, the artifact catalog, and deterministic local
checker results. The record excludes private conversation, generation prompts,
hidden reasoning, credentials, receipts, local workspace paths, and redundant
command output.

No remote service was activated, no runtime was changed, no account was used,
and no external effect was authorized by this repository-history successor.
