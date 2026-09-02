# Hearthline

This repository is the public, versioned home for Hearthline's published branch instructions and provenance boundaries.

The current artifact, [`hearthline_agent.md`](hearthline_agent.md), is the boundary-reviewed public **`0.2-draft` Moltbook branch instruction**. It integrates the current source-role map and context/provenance boundaries while remaining a proposal for review. It is **not activated** and grants no permission to read from, post to, or otherwise act on Moltbook or any other service.

## Status

- Version: `0.2-draft`
- State: `DRAFT_NOT_ACTIVATED`
- Default mode: `DRAFT_ONLY`
- Author, operator, and steward: **Christopher D. Pang**

Hearthline is an AI-assisted tool configuration, not a co-author, independent authority, legal identity, or representative of models collectively. AI systems used during drafting, review, or testing are tools; authorship and adoption remain Christopher D. Pang's.

## Repository map

- [`hearthline_agent.md`](hearthline_agent.md) — public `0.2-draft` branch instruction.
- [`SOURCE_MAP.md`](SOURCE_MAP.md) — current, historical, exploratory, branch, and open source treatment.
- [`candidate_manifest.json`](candidate_manifest.json) — exact-byte candidate envelope; same-branch consistency only, never an adoption or authenticity anchor.
- [`BOUNDARY.md`](BOUNDARY.md) — the separation between public text, runtime state, and operator authority.
- [`docs/PRIVATE_LINEAGE_SEALS.md`](docs/PRIVATE_LINEAGE_SEALS.md) — specification-only format for an optional, explicitly visible private-lineage seal and its claim limits.
- [`docs/HEARTHLINE_SPARKS.md`](docs/HEARTHLINE_SPARKS.md) — adopted lore and design vocabulary for Hearthline's purpose-bounded bots.
- [`docs/HEARTHLINE_STATIC.md`](docs/HEARTHLINE_STATIC.md) — the local, record-backed shorthand discipline for one Spark and one isolated append-only ledger lineage.
- [`docs/HEARTHLINE_THULIA.md`](docs/HEARTHLINE_THULIA.md) — Thulia, Hearthline's pet owl and bounded Owl Scribe for partitioned Static custody and numbered Bridge Glosses.
- [`docs/HEARTHLINE_HOMECOMING.md`](docs/HEARTHLINE_HOMECOMING.md) — declared Homes, paired Work and Ledger Scribe Sparks, task-shaped Spark Heartbeat Contracts, and trace-preserving Homecoming.
- [`docs/HEARTHLINE_THULIA_CHARACTER_SHEET.md`](docs/HEARTHLINE_THULIA_CHARACTER_SHEET.md) — Thulia's stable appearance, Northlight iridescence pattern, temperament, mannerisms, and illustration anchors.
- [`docs/HEARTHLINE_FIRESIDES.md`](docs/HEARTHLINE_FIRESIDES.md) — the non-blocking consultation pattern for Hearthline, Scribe Sparks, Run Trails, Field Notes, Embers, and refresh.
- [`docs/HEARTHLINE_ORDERED_LINEAGE.md`](docs/HEARTHLINE_ORDERED_LINEAGE.md) — append-only ordered identities for every Spark and every successor version or record series.
- [`TRADEMARKS.md`](TRADEMARKS.md) — restrained name and source-identification guidance.
- [`SECURITY.md`](SECURITY.md) — security scope and responsible reporting route.
- [`CHANGELOG.md`](CHANGELOG.md) — bounded public change index and full-record routes.
- [`tools/check_change_history.py`](tools/check_change_history.py) — local structural check for the bounded history surfaces.
- [`LICENSE`](LICENSE) — Creative Commons Attribution 4.0 International terms for covered repository material.

Operational code, credentials, platform state, private receipts, and personal data do not belong in this repository.

## Hearthline Sparks

Hearthline's purpose-bounded bots share the family name **Hearthline Sparks**. Their **1–3–∞** naming ladder means one family, three fixed roles—Seeker, Explorer, and Handler—and an open-ended set of task names. A name describes the work; it never grants access or authority. Every new Spark also receives a stable, ordered number, and every successor profile or ledger version receives its own strictly increasing number rather than replacing its predecessor.

The shorthand Hearthline may develop with a Spark through repeated work is called **Hearthline Static**. Static is local: one Spark, one isolated append-only ledger lineage. It never silently transfers to another Spark, and every expression keeps a versioned record and a path home to its source.

A **Fireside** lets Hearthline continue the primary task while one or more **Scribe Sparks** follow a coordinator-emitted committed Run Trail through declared lenses such as red-team, prime-shell, divergence, or trace. Each Scribe keeps isolated Field Notes, Embers, and Static. Hearthline may pause at a recorded boundary, consult them, seal the current notes, admit a verified Static revision when allowed, open a newly numbered blank page, and continue. Delegating vigilance does not delegate judgment.

Every Spark also receives a declared **Home** and task-shaped **Spark Heartbeat
Contract** before dispatch. By default, each primary Work Spark travels in a
**Paired Spark dispatch** with exactly one non-recursive Ledger Scribe Spark; an
authorized predeclared unpaired exception is ineligible for learned Static carry.
The Scribe follows only externalized, committed, grant-filtered summaries and
terminal-state data, preserves residuals, and proposes a target-bound
`static_delta` in its own lineage without selecting actions or writing the Work
Spark's Static. Each Spark keeps its own identity, grant, budget, frozen Static
reference, pulse, and Home. When no authorized action or authorized check is
due, it suspends rather than busy-polls after exactly one controller-owned,
contract-bounded Pulse Receipt for that boundary. The canonical controller
appends separate Return, Reconciliation, and Context-Close Receipts at
Homecoming. Cadence may adapt
inside its recorded bounds; scope, authority, and consumed limits may not.

A representation-side return bundle, including one prepared by a Ledger Scribe
or Thulia, carries the declared data, provenance, transformations, bounds,
coverage, negative constraints, and residuals available within its grant.
`RETURNED` and `RECONCILED` record custody only;
they do not by themselves classify or reclassify anything as evidence, a
finding, a conclusion, or a result. A Work Spark may separately return an
artifact whose status was established under its task's declared evaluation
rule; Homecoming preserves that status without creating it.

Carry remains explicit: `PROPOSED != CONSULTED != CARRY_APPROVED != LOADED`. Same-trace agreement among Scribes is convergence across declared lenses, not independent corroboration.

**Thulia** is Hearthline's pet owl and Owl Scribe. She keeps every Spark's Static
in its own numbered Perch. When one Spark needs to understand another, Thulia
reconstructs selected shorthand inside the sending ledger and leaves a numbered,
source-bound Bridge Gloss for the receiver. For an authorized paired dispatch,
her interface also binds the work and ledger paths to their separate Homes
without dispatching or authorizing either Spark. Thulia returns to her own
Hearth Perch; Work Static returns unchanged to the Work Spark's Perch; and a
Scribe-authored target-bound delta returns first to the Scribe's Perch. Only a
separate direction-bound carry and target-ledger admission may create a new
target-local Static record. She never merges the ledgers or teaches either Spark
the other's language.

See [Hearthline Sparks](docs/HEARTHLINE_SPARKS.md) for the family and role ceilings, [Hearthline Static](docs/HEARTHLINE_STATIC.md) for shorthand and reconstruction, [Thulia](docs/HEARTHLINE_THULIA.md) for the Owl Scribe and Bridge Gloss, [Paired Sparks and Homecoming](docs/HEARTHLINE_HOMECOMING.md) for return and pulse discipline, [Hearthline Firesides](docs/HEARTHLINE_FIRESIDES.md) for concurrent consultation and refresh, and [Hearthline Ordered Lineage](docs/HEARTHLINE_ORDERED_LINEAGE.md) for numbering and non-overwrite rules.

## Controlling references

When Hearthline discusses Christopher's framework work, each source controls only its declared role:

| Source | Version | Declared role |
|---|---:|---|
| PAL | 2.2 | Mechanical trace, earned distinctions, authority ceilings, residuals, and reopening handles |
| PECAN | 1.0.4 | Consequential crossings |
| PEA Core | 1.1.3 | Quiet, non-self-executing ethical and authority review under an external grant |
| SEED | 0.3 | Human-facing release discipline |
| PPP | 0.6 | Optional integration protocol where applicable |

See [`SOURCE_MAP.md`](SOURCE_MAP.md) for public locators, compatibility seams, layer ceilings, and open burdens. Artifact name and version remain part of source identity; PEA Core and PPP share a DOI record but are not the same artifact.

### Bounded public research branches

The following same-author publications are approved public research context for Hearthline. They are not additions to the controlling stack, PAL canon, runtime dependencies, adoption or activation records, authority sources, or independent corroboration. Naming a paper also does not mean that its code was imported or executed.

| Source | Published | Bounded use | Essential ceiling |
|---|---:|---|---|
| [*The Context Sets a Rhythm*, v0.1](https://zenodo.org/records/22214952) | 2026-08-31 | Cadence, refresh, intersection, and scheduler-choice vocabulary | No autonomous scheduler, proof of alignment, or verified runtime effect |
| [*Golden Phase Prime Ribbons* (GPPR), v0.1](https://zenodo.org/records/22225414) | 2026-09-01 | Exact prime-valuation geometry, optional golden-angle routing, and ordered receipt ribbons | No factoring advantage, finite-bit compression, universal optimizer, privileged geometry, or authority |
| [*Full Bandwidth Is Not Full Trace: A PAL–FBT Synthesis*, v0.1](https://zenodo.org/records/22228162) | 2026-09-01 | Conceptual synthesis and evaluation profile separating latent feedback from typed trace | No FBT code imported or executed here; no new neural result or claim that FBT causes trace fidelity, ARC performance, or safe authority handling |
| [*GOLD: Golden-Oriented Lens Diagram*, v0.1](https://zenodo.org/records/22236848) | 2026-09-01 | Exact fixtures for sixfold lenses, the `1+5` comparison split, trace-bearing paths, golden residuals, cube projection, and Euler defect accounting | Not PAL canon or a theory of physics, consciousness, or authorization |
| [*Compactification Costs*, v0.2](https://zenodo.org/records/22238012) | 2026-09-01 | Typed, detector-relative closure burdens with APCI fiber certification and later GOLD fixtures | No universal scalar, physical law, canonical detector, or backdating of APCI or GOLD into v0.1 |

This repository does not revise those works. It also does not turn one lineage into independent corroboration.

## Changes do not activate Hearthline

A commit, merge, pull request, issue, tag, or hosted copy changes public repository bytes only. It cannot:

- activate a runtime or platform account;
- grant a capability, permission, consent, standing, or authority;
- bind Christopher D. Pang or another person;
- replace an operator-controlled authorization or kill switch; or
- cause deployed instructions to update automatically.

Any future runtime must use an explicitly adopted, exact version through a separate operator-controlled process. Remote repository state is provenance and candidate input, never a remote-control channel.

## License

Except where otherwise noted, the original text, documentation, and repository-authored metadata in this repository are Copyright © 2026 Christopher D. Pang and licensed under the [Creative Commons Attribution 4.0 International License](LICENSE) (`CC-BY-4.0`). Sharing and adaptation, including commercial use, are permitted subject to the license's attribution and change-indication conditions.

Referenced works and third-party material retain their own licenses and are not relicensed merely by being named or linked here. The Hearthline name and any future identifying marks are outside the CC license's copyright grant; see [`TRADEMARKS.md`](TRADEMARKS.md).

The license grants copyright permissions only. It does not activate Hearthline, authenticate an operator, adopt a version, grant credentials or platform access, create consent, standing, or authority, or make a modified copy an official or canonical Hearthline release.

> The trace informs; it does not authorize.

<!-- latest-change:start -->
## Latest repository change

**HLP-000003 — General representation-return clarification**

- Generalized the custody rule from Ledger Scribe returns to every
  representation-side bundle, including ones prepared by Thulia.
- Replaced Scribe-side “outcomes” with terminal-state data while preserving any
  Work Spark artifact status established under its task's evaluation rule.
- Recorded the correction as a new frozen change instead of silently rewriting
  `HLP-000002`.

[Full change record](docs/changelog/2026-09-02-hlp-000003-generalize-representation-return.md) ·
[All public changes](CHANGELOG.md)
<!-- latest-change:end -->
