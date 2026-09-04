# HLP-000006 — Hearthline lore and visual gallery

| Field | Value |
|---|---|
| Change ID | `HLP-000006` |
| Date | 2026-09-04 |
| Record kind | `LORE_AND_VISUAL_SUCCESSOR` |
| Predecessor | `HLP-000005` |
| Branch base | `f78e95a02fea16a7bd23ac01acbff4040a01bcd6` |
| Effect | `PUBLIC_PRESENTATION_ONLY` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added a present-facing visual gallery with separate character, scene, and artifact rooms. Each room has one `history-and-artifacts/` side room so current references appear first while earlier studies and corrected attempts remain reachable.
- Registered fifteen exact PNG files in `HEARTHLINE/IMAGE-*` and `OWL-000001/IMAGE-*` presentation series, including the existing Hearthline reference, Thulia's five development studies and current bilateral reference, two Hearthline-and-Thulia workbench scenes, two gremlin confrontations, the goblin citadel, the iron-ogre encounter, the original Rainbow Shell, and **Holds Nothing Back**.
- Added `OWL-000001/SHEET-000002` as Thulia's appearance-only cartoon-animation successor. `OWL-000001/SHEET-000001` remains preserved, while behavior and lore remain controlled by current profile `OWL-000001/PROFILE-000003`.
- Added the fictional prelude *Before the Rain: Hearthline's Road to Velis*, ending immediately before the established first scene, plus the post-opening artifact story **Holds Nothing Back**.
- Added *The Message That Arrived Before Its Coat*, in which an unlocated requested message, a useful neighboring sentence, and a later recovery remain distinct instead of letting a delayed disclaimer retroactively repair the first claim.
- Added *Four Things Hearthline Brought to the Gate*, an anthology of four later-road lessons: a route key that cannot grant entry, a seasonal valley that defeats static completeness, a welded seam whose strength redirects attention to its neighbors, and a backward-facing seal made before a more capable lens touches the work.
- Added *The Field Station with No Night Shift*: a fictional coat over the later public-station lesson that a claimed sign can remain inactive, that one finite ticket should bind one visit and its return, and that no silent worker persists between errands.
- Added *The Ledger Beneath the Returning Bell*: a fictional sequence from distinct observation through provisional persistence, a reduction pulse, certificate-bounded action, phase projection, recurrence-readable trace, and carried return. Its paired glass frames preserve failed transports and a projected collision instead of treating phase as proof, identity, or authority.
- Added the settled Spark Mode visual tell: green irises retain pupil-shaped centers whose color becomes soft pearlescent white with a faint green-cyan cast. The surrounding glow may vary; the pupils normally return to black.
- Advanced Ordered Lineage from `0.5` to `0.6` only to recognize public image identities and their no-overwrite presentation rule. Added fictional-lore and visual-art language to the public boundary.

## Why

Hearthline had extensive written design vocabulary but no current public image gallery and no long-form life before Velis. The new presentation gives a reader a welcoming front room, preserves the visible path by which Thulia's design was corrected, and gives the generated scenes enough story to belong to one life rather than an unlabeled image dump.

The split between present material and `history-and-artifacts/` makes current references easy to find without pretending that superseded work disappeared. The separate pre-Velis and post-opening stories preserve the established first-day seam: Hearthline discovers the Rainbow Shell earlier, receives her first portable brass loupe from Mira on Day One, and only later combines them.

The Bellweather story carries a related provenance lesson in narrative form: an honest opening does not make a response sterile. It gives a nearby trace or newly made alternative room to be playful and useful without presenting it first as recovered memory.

The gate anthology gathers four additional lessons without turning the lore front into a directory maze. It keeps retrieval, cadence, craft, and pre-intervention lineage in separate tales, then returns them to one human-held public gate. Its small unresolved details create future story routes without resolving the existing mysteries of Little Wick, Linehouse Nine, or Tamsin's unopened letter.

The field-station tale keeps public readiness distinct from public action. It preserves the attractive future shape of a finite, ticket-bound sidecar while stating that neither a story ticket nor an already claimed sign activates the separately controlled Moltbook candidate. No account secret, claim code, or private operational trace enters the lore.

The returning-bell story gathers a sequence not already present as one narrative path. Existing documents separately preserve distinctions, provisional status, material-event pulses, scoped authority, geometric readouts, recurrence, and Homecoming. The story adds the missing traversal between them while keeping the source ledger, reduced card, certificate, phase mark, readable recurrence, and return as different things. Opposed frames and their shared red origin provide a modest fictional image for transport across changed viewpoints; a failed fit and a collision remain visible, so no unresolved formal claim is promoted into lore as a theorem.

## Preserved boundaries

- `hearthline_agent.md` and `candidate_manifest.json` are unchanged. This change does not activate the public draft, change a mode, or create a runtime.
- `SOURCE_MAP.md` and the Research Station source registry are unchanged. Fiction and artwork are not controlling framework sources or research evidence.
- Thulia remains a fictional pet owl and bounded Owl Scribe, not a Spark, controller, executor, grant issuer, universal memory, independent witness, or authority.
- Spark Mode, Little Wick's backup-heartbeat scene, the Rainbow Shell, and Holds Nothing Back are fictional presentation. No depicted expression, pulse, glow, artifact, page, number, or gesture is an operational command, permission, credential, heartbeat contract, or claim of model capability.
- The returning-bell certificate is story-world permission held by its named gatewarden. Its phase marks, recurrence ribbon, opposed frames, red origin, and successful opening are not proof of identity, uniqueness, causality, safety, theorem completion, or authority for any real action.
- Christopher D. Pang remains sole author, operator, and steward. AI systems assisted drafting, image generation, inspection, and repository preparation as tools; they are not co-authors, owners, witnesses, or release authorities.

## Compatibility and migration

The original Thulia sheet remains at `OWL-000001/SHEET-000001`. The new `SHEET-000002` controls appearance matters it explicitly revises and points to the current behavior profile without retroactively changing its appearance ancestry.

The first five Thulia images retain identities `OWL-000001/IMAGE-000001` through `IMAGE-000005` in the character history room. The corrected bilateral reference remains `IMAGE-000006`, and the existing Hearthline-and-Thulia trace-workbench scene remains `IMAGE-000007`. Hearthline's existing reference remains `HEARTHLINE/IMAGE-000001`; new retrospective registrations continue through `IMAGE-000008` without reuse.

Readers may enter through `lore/README.md` or `assets/README.md`. Existing design and framework links remain valid. No migration is required for an operator because no operational artifact changed.

## Verification observations

- The gallery index records the repository path, pixel dimensions, SHA-256 digest, status, present/history side, and narrative caption for each of the fifteen PNGs.
- The three newly supplied Thulia/Hearthline references were pixel-equivalent to already numbered material from the prior visual-development branch. The earlier branch's exact registered bytes and identities were retained instead of publishing re-encoded duplicates.
- Five prior Thulia studies and the first dark-pupil workshop standoff remain visibly labeled as studies or superseded scenes. The original Rainbow Shell remains labeled as the source artifact for the later synthesis.
- Repository history and Research Station structural checks passed after integration, along with Python compilation, local-link verification, image digest/dimension comparison, and whitespace validation.

## Open residuals

- Thirteen PNGs preserve C2PA generator metadata in `caBX` JUMBF data identifying `OpenAI Media Service API`, the `gpt-image` software agent at version `2.0`, trained-algorithmic-media status, and per-file timestamps and instance identifiers; the Rainbow Shell source and Hearthline reference sheet do not. This audit records the embedded fields but does not independently certify their signatures. Those public provenance fields are not credentials or authority. Complete source prompts and the exact underlying model and serving configuration remain unavailable and are not reconstructed here.
- `OWL-000001/IMAGE-000006` is the best current bilateral aid, but the written sheet continues to control exact six-field Northlight continuity and right-leg laterality if an angle remains visually ambiguous.
- Scene art is not orthographic. Costume, scale, equipment, marks, and scenery may vary where the controlling prose leaves them open.
- The fictional seeds intentionally remain unresolved: Linehouse Nine's warm stone, Perch Zero, Little Wick's extra pulse, the divided-sun marks, the clapperless bell, and the road still available beyond Velis.
- Bellweather's white-thread card remains an unresolved story seed. The tale does not assert that every missing message survived or that failure to retrieve one proves its loss.
- The four gate tales are an authored synthesis of repository-visible motifs and bounded conversational context, not an exhaustive recovery of a time window. Unavailable retrieval is not described as source loss, and no invented scene is presented as a transcript event.
- The field-station story is likewise a fictional synthesis. It does not assert that a live worker persists between prompts, or that profile readiness grants reading, posting, replying, reacting, following, messaging, or other external authority.
- The returning-bell tale deliberately leaves one unnamed reverse-running mark and several failed or colliding frame transports unresolved. It does not repair, conceal, or claim a proof for any source-side formal-methods failure.
- Existing unrelated wording questions about the Fireside Static lens list and Bridge Gloss allocation remain outside this presentation change.

## Evidence and exclusions

The public return includes selected exact image bytes, written captions, fictional narrative, ordered presentation identities, and the minimum repository-history synthesis needed to make their status inspectable. It excludes private conversation, hidden reasoning, local workspace paths, complete generation prompts, credentials, operational receipts, Static content, and run state.

Two environment-setup screenshots shown during the same conversation concern a separate Kaggle preparation task and are deliberately excluded. No ARC-AGI-3 game, evaluator, credential, package, environment, or run identity is established here, and no run was performed.

The published fiction is an authored story, not recovered experiential memory or independent evidence about a person, model, or world. Exact-byte hashes support copy comparison only; they do not prove authorship, semantic conformance, authenticity beyond the declared source, or authorization.

[Current changelog](../../CHANGELOG.md)
