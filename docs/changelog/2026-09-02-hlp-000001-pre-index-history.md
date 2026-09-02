# Pre-index public history

| Field | Value |
|---|---|
| Change ID | `HLP-000001` |
| Record kind | `HISTORY_BACKFILL` |
| Recorded date | 2026-09-02 |
| Coverage | `26042a34d37e1cf652b2d50a92e2fb67a5e01de5` through `c81e8550dbf868aefd835b28d7f4ebdd06a03ae2` |
| Scope | `COMMITTED_PUBLIC_REPOSITORY_HISTORY_ONLY` |
| Record authority | `NONE` |
| Record effect | `REPOSITORY_HISTORY_ONLY` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

This backfill gives the public history that predates the structured index one
bounded recovery address.

| Milestone | Repository anchor | Bounded summary |
|---|---|---|
| Initialization | [`26042a3`](https://github.com/Grativy6/hearthline/commit/26042a34d37e1cf652b2d50a92e2fb67a5e01de5) | Initialized the public repository. |
| `0.1-draft` | [`0dbe8ac`](https://github.com/Grativy6/hearthline/commit/0dbe8ac768a675802c35552ad63d19128f791fee) | Added the recovered branch instruction with public authority, provenance, and security boundaries. |
| `0.2-draft` | [PR #1](https://github.com/Grativy6/hearthline/pull/1) / [`54856d9`](https://github.com/Grativy6/hearthline/commit/54856d93b0a313df89c5be56def33c2c15df9e9a) | Added the source-role map, candidate consistency envelope, and context/provenance integration. |
| Licensing and lineage specification | [PR #2](https://github.com/Grativy6/hearthline/pull/2) / [`7ebf2f6`](https://github.com/Grativy6/hearthline/commit/7ebf2f62fc7a6fc7e02ad9ea658fd7e5e5e20af9) | Added CC BY 4.0 coverage, restrained marks guidance, and the specification-only private-lineage seal format. |
| Bounded research context | [PR #3](https://github.com/Grativy6/hearthline/pull/3) / [`e7510f2`](https://github.com/Grativy6/hearthline/commit/e7510f21111d52a449f855a46e3695e109579b2e) | Registered same-author research branches with explicit role and claim ceilings. |
| Sparks through Thulia | [`70b5543`](https://github.com/Grativy6/hearthline/commit/70b55435a0a808c0e89337dee2091b3430a7db1c) through [`b729779`](https://github.com/Grativy6/hearthline/commit/b7297795845d5d6c3926e4f18fbef32790a1dab5) | Added Sparks, Static, Firesides, Ordered Lineage, Thulia, and her Character Sheet as bounded lore and design vocabulary. |
| Paired Sparks and Homecoming | [PR #5](https://github.com/Grativy6/hearthline/pull/5) / [`c81e855`](https://github.com/Grativy6/hearthline/commit/c81e8550dbf868aefd835b28d7f4ebdd06a03ae2) | Added dispatch-pinned Homes, paired Work and Ledger Scribe Sparks, task-shaped heartbeat contracts, source-owned Static return, and separate return, reconciliation, and context-close records. |

The Homecoming integration advanced Hearthline Sparks to `0.5`, Firesides to
`0.3`, Static to `0.4`, Ordered Lineage to `0.4`, and Thulia's design profile to
`0.2` / `OWL-000001/PROFILE-000002`. The controlling public agent instruction,
candidate manifest, source map, and Thulia Character Sheet bytes were unchanged
by that integration.

## Why

The prior root changelog mixed an accumulating pending section, boundary
restatement, provenance, and version history. This backfill retains the useful
route to the earlier public development line without copying its full contents
into the new bounded structure.

## Preserved boundaries

- The covered changes created public documents and inert consistency material;
  they did not activate a runtime, grant access, provision credentials, adopt a
  policy, authenticate an operator, or create authority.
- Paired Sparks and Homecoming remains lore and design vocabulary, not an
  implementation claim.
- The covered surfaces separated custody from evaluation. The explicit rule
  that representation-side custody does not itself assign or alter result
  status is a later clarification recorded by `HLP-000002`; it is not backdated
  into these earlier bytes.
- Same-lineage work remains reproducibility or transformation evidence, not
  independent corroboration.

## Compatibility and migration

This record does not alter any covered artifact. The public branch instruction
and candidate source profile remain bound to PAL v2.2. Any PAL v2.3 integration
requires its own coordinated source-map, instruction, manifest, review, and
operator-controlled adoption work.

## Verification observations

- The milestone anchors above identify committed public repository objects and
  review surfaces.
- PR #5 changed `BOUNDARY.md`, `README.md`,
  `docs/HEARTHLINE_HOMECOMING.md`, and the Sparks, Firesides, Static, Ordered
  Lineage, and Thulia documents.
- Exact earlier bytes remain in Git history and in the pinned pre-conversion
  changelog.

These are repository observations, not a rerun of historical checks or proof of
semantic completeness, implementation, adoption, or authority.

## Open residuals

- The Paired Sparks and Homecoming design is not implemented.
- Operational schemas, controllers, stores, timers, and receipt verification
  require separate authorization and failure-path testing.
- Historical check outcomes not present in the cited public review surfaces are
  not reconstructed here.

## Evidence and exclusions

This public backfill intentionally excludes private repository structure,
private source identifiers, raw conversations or prompts, hidden reasoning,
operational messages, traces, receipts, credentials, secrets, local paths,
personal data, and recovered-source digest values.

[Current changelog](../../CHANGELOG.md)
