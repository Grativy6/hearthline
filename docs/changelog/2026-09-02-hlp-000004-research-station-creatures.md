# Install the Research Station and Creature design successor

| Field | Value |
|---|---|
| Change ID | `HLP-000004` |
| Record kind | `SOURCE_PROFILE_AND_DESIGN_SUCCESSOR` |
| Recorded date | 2026-09-02 |
| Predecessor | `HLP-000003` |
| Branch base | `355dfa8202abd04f22a17c6c023e16358c0d9dc4` |
| Prior public draft | `0.2-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_1` |
| Successor public draft | `0.3-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2` |
| Scope | `PUBLIC_RESEARCH_CONTEXT_AND_DESIGN` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DRAFT_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Advanced the current public draft and source profile to PAL v2.3 while
  preserving PAL v2.2-era records under their original identities and leaving
  the candidate `DRAFT_NOT_ACTIVATED` in `DRAFT_ONLY` mode.
- Registered BRRRT v2.0 and Single Cut Transport Lemma v0.2 as bounded public
  branches, and reaffirmed the already-registered Compactification Costs v0.2
  without counting it twice.
- Added the Hearthline Research Station with DOI, version, license, role,
  ceiling, inspected-artifact, and hash-domain records.
- Recorded the repaired BRRRT live PDF match and retained the earlier
  C2PA-wrapped loose-file identity only as superseded audit history.
- Inspected Strongwiz at commit
  `edc88b80f872f766c22b3a050a7f6837d6e652d8` and separated that repository head
  from the v3 mechanism freeze at
  `300fd0b9ae1183e582bb834e17ff02bf80189fd8`.
- Added Hearthline Creatures and advanced Sparks to `0.6`, Homecoming to `0.4`,
  Static to `0.5`, Ordered Lineage to `0.5`, and Thulia to profile
  `OWL-000001/PROFILE-000003`.
- Added controller-owned open objective windows so independently scoped Sparks
  or Creatures may suspend, accept later objectives, return out of order, and
  aggregate into one response without sharing grants, budgets, ledgers, or
  statuses.
- Added CI-backed, fail-closed structural verification for source, successor,
  candidate-text, BRRRT-resolution, and Creature-boundary consistency.

## Why

PAL v2.3, BRRRT v2.0, Single Cut v0.2, and Compactification Costs v0.2 were
complete public sources that needed explicit, versioned Hearthline roles before
future ARC-AGI-3 preparation. Strongwiz v3 also supplied a concrete but still
unrun design surface for separating task action from representation work. A
single public Research Station keeps those inputs discoverable without
converting them into one undifferentiated authority or imported codebase.

Creature names the requested composition: task-shaped bundles of Sparks with
Thulia and linked ledgers. The design makes the bundle inspectable while
preserving one-Spark/one-ledger Static, separate Homes and grants, controller-
admitted effects through a separately authorized broker or domain writer, and a
non-governing Thulia custody interface.

The open objective window makes the Homecoming distinction operationally
load-bearing in the design: each objective retains its own return and result
status even when several branches share one outward conversational cadence. The
heartbeat marks a safe interrupt boundary; it does not create the host lifecycle
or scheduler that would keep the exchange available.

## Preserved boundaries

- The five PAL v2.3 faces retain separate roles. This source-profile successor
  is not a claim of complete Hearthline or Strongwiz conformance.
- PEA Core v1.1.3 and optional PPP v0.6 remain explicit PAL v2.2 compatibility
  seams; no v2.3 adapter is inferred.
- BRRRT, Single Cut, Compactification Costs, and the other Pang sources share
  one author-led lineage and are not independent corroboration.
- No source text, Strongwiz code, model output, game data, holdout, credential,
  private ledger, or operational path is imported into the public repository.
- A Creature is not a fourth Spark role, one merged mind, a shared Static
  ledger, an authority aggregator, an executor, or a self-spawning process.
- Thulia may custody manifests, Perches, and Bridge Glosses. External
  authenticated operator control remains the only grant/revocation source. The
  canonical controller—not Thulia—tracks those grants and owns allocation,
  promotion, reconciliation, and effect admission/serialization; a separately
  authorized broker or domain writer performs the admitted effect.
- A heartbeat is a projection over durable state. It does not keep a process or
  workspace alive, renew a grant or budget, prove progress, or replace the
  controller-owned Pulse Receipt required before suspension.
- This repository promotion activates no runtime, platform account, ARC
  environment, competition entry, publication action, or external authority.

## Compatibility and migration

PAL v2.3 is a successor source for new records, not a rewrite of PAL v2.2
history. Single Cut v0.2 succeeds the v0.1 research context while retaining the
older row as historical. Compactification Costs v0.2 was already current public
research context and is carried forward unchanged.

The Strongwiz source is pinned as `0.4.0.dev0` exploratory design evidence, not
a tagged or published v0.4 release. Calibration 001 and 002 remain their
historical `PARTIAL` results, and Calibration 003 remains prepared, not run, and
not preregistered. No Hearthline component is backdated into those runs.

The public Moltbook instruction advances to `0.3-draft`; its normalized LF text
hash is bound in the candidate manifest. Updating repository bytes is not the
separate operator-controlled adoption of those bytes by a runtime.

## Verification observations

- Zenodo's live API reported PAL v2.3, BRRRT v2.0, Single Cut v0.2, and
  Compactification Costs v0.2 under the recorded DOIs, versions, dates, author,
  open access, and CC BY 4.0 license.
- A fresh live download of the repaired BRRRT PDF was 1,251,146 bytes with
  SHA-256
  `f9e699ad4a8541506ecc6678c3296bdf4fbe4dd249a0dd6759c7fd0d22837e0a`
  and MD5 `79462822b3895d2e02d0aff26279a8af`, matching the package PDF's SHA ledger.
- The PAL package, BRRRT package, Single Cut verification bundle, and
  Compactification Costs documents were independently hashed; the exact
  identities are in the Research Station registry.
- Strongwiz's GitHub CI run
  [`33696382045`](https://github.com/Grativy6/strongwiz/actions/runs/33696382045)
  completed successfully at inspected head `edc88b8`. This is bounded software
  evidence, not an ARC or Scribe-benefit result.
- The repository structural checks validate JSON uniqueness, source roles,
  pinned Git-blob hashes, source-profile consistency, candidate policy bytes,
  BRRRT live resolution plus superseded history, Creature ceilings, local links,
  bounded change history, and whitespace integrity.

## Open residuals

- Hearthline's Sparks, Static, Thulia, Creatures, ledgers, controller, and
  runtime remain designs rather than an implemented or evaluated system.
- Strongwiz's v3 evidence-yield gate is retained for later runner integration;
  it is not yet an ARC campaign scheduler. Its heartbeat is caller-driven and
  cannot itself supervise or preserve a process.
- Strongwiz's in-process Scribe is trusted application code, not a
  confidentiality sandbox. A future untrusted provider requires an actual
  process and capability boundary.
- One Strongwiz raw registry-file hash is LF-byte-specific, and its local
  exact-lock test recipe omits optional calibration dependencies that CI
  installs explicitly. These portability/documentation seams remain visible.
- Strongwiz's package metadata says `0.4.0.dev0`/pre-alpha while its citation
  and notice surfaces still say `0.2.0`/v0.2. Its wheel and source distribution
  also omit the repository-local Calibration 003 harness. No tagged v0.4 release
  or package-installed calibration is inferred.
- Strongwiz's semantic source-registry reference binds its own 14-source set; it
  does not contain BRRRT v2.0, the new Single Cut v0.2 record, or
  Compactification Costs v0.2. Hearthline does not backdate this intake into
  Strongwiz's development provenance.
- Exact current ARC-AGI-3 source, package, environment, game, evaluator,
  model/runtime, budget, credential, Kaggle, and acceptance identities remain
  unbound. No run is authorized by this record.
- Multi-Creature cooperation, arbitration, and any performance effect remain
  unimplemented hypotheses. Matched arms must be separate Creature instances
  and cannot share payload ledgers.
- Dynamic objective admission and out-of-order Homecoming remain unimplemented.
  The A-suspend/B+C-admit/C-B-A-return scenario is a prospective synthetic
  conformance test, not a completed workspace-lifecycle result.

## Evidence and exclusions

The public registry contains locators, hashes, versions, roles, ceilings, and a
bounded synthesis. It excludes manuscript bytes, private material, raw audit
conversations, hidden reasoning, operational state, game content, credentials,
and run payloads. AI systems assisted inspection, synthesis, drafting, and
checking as tools; they are not authors, co-authors, witnesses, release
authorities, or independent corroborators.

[Current changelog](../../CHANGELOG.md)
