# Hearthline

This repository is the public, versioned home for Hearthline's published branch instructions and provenance boundaries.

The current artifact, [`hearthline_agent.md`](hearthline_agent.md), is the boundary-reviewed public **`0.4-draft` Moltbook branch instruction**. It integrates the current source-role map and context/provenance boundaries while remaining a proposal for review. It is **not activated** and grants no permission to read from, post to, or otherwise act on Moltbook or any other service.

## Status

- Version: `0.4-draft`
- State: `DRAFT_NOT_ACTIVATED`
- Default mode: `DRAFT_ONLY`
- Author, operator, and steward: **Christopher D. Pang**

Hearthline is an AI-assisted tool configuration, not a co-author, independent authority, legal identity, or representative of models collectively. AI systems used during drafting, review, or testing are tools; authorship and adoption remain Christopher D. Pang's.

## Repository map

- [`hearthline_agent.md`](hearthline_agent.md) — public `0.4-draft` branch instruction.
- [`SOURCE_MAP.md`](SOURCE_MAP.md) — current, historical, exploratory, branch, and open source treatment.
- [`candidate_manifest.json`](candidate_manifest.json) — normalized-text candidate envelope; same-branch consistency only, never an adoption or authenticity anchor.
- [`BOUNDARY.md`](BOUNDARY.md) — the separation between public text, runtime state, and operator authority.
- [`docs/PRIVATE_LINEAGE_SEALS.md`](docs/PRIVATE_LINEAGE_SEALS.md) — specification-only format for an optional, explicitly visible private-lineage seal and its claim limits.
- [`docs/HEARTHLINE_SPARKS.md`](docs/HEARTHLINE_SPARKS.md) — adopted lore and design vocabulary for Hearthline's purpose-bounded bots.
- [`docs/HEARTHLINE_STATIC.md`](docs/HEARTHLINE_STATIC.md) — the local, record-backed shorthand discipline for one Spark and one isolated append-only ledger lineage.
- [`docs/HEARTHLINE_THULIA.md`](docs/HEARTHLINE_THULIA.md) — Thulia, Hearthline's pet owl and bounded Owl Scribe for partitioned Static custody and numbered Bridge Glosses.
- [`docs/HEARTHLINE_HOMECOMING.md`](docs/HEARTHLINE_HOMECOMING.md) — declared Homes, paired Work and Ledger Scribe Sparks, task-shaped Heartbeat Contracts, open objective windows, and trace-preserving Homecoming.
- [`docs/HEARTHLINE_RETURN_QUEUE.md`](docs/HEARTHLINE_RETURN_QUEUE.md) — dispatch priority, queued return, immutable arrival order, and Morrow's stateless Queue Steward profile.
- [`docs/HEARTHLINE_THULIA_CHARACTER_SHEET_000002.md`](docs/HEARTHLINE_THULIA_CHARACTER_SHEET_000002.md) — current Thulia appearance and animation sheet; its [`SHEET-000001`](docs/HEARTHLINE_THULIA_CHARACTER_SHEET.md) predecessor remains preserved.
- [`docs/HEARTHLINE_FIRESIDES.md`](docs/HEARTHLINE_FIRESIDES.md) — the non-blocking consultation pattern for Hearthline, Scribe Sparks, Run Trails, Field Notes, Embers, and refresh.
- [`docs/HEARTHLINE_ORDERED_LINEAGE.md`](docs/HEARTHLINE_ORDERED_LINEAGE.md) — append-only ordered identities for every Spark and every successor version or record series.
- [`docs/HEARTHLINE_CREATURES.md`](docs/HEARTHLINE_CREATURES.md) — manifest-bound, task-shaped bundles of separately governed Sparks, ledgers, Homes, and Thulia custody.
- [`lore/README.md`](lore/README.md) — fictional stories, including Hearthline's road to Velis and **Holds Nothing Back**.
- [`assets/README.md`](assets/README.md) — present-facing visual gallery with clearly separated history and artifact trails.
- [`docs/HEARTHLINE_RESEARCH_STATION.md`](docs/HEARTHLINE_RESEARCH_STATION.md) — bounded public research context, inspected source identities, design extraction, and open provenance residuals.
- [`docs/HEARTHLINE_TETHER.md`](docs/HEARTHLINE_TETHER.md) — carrier-neutral trace externalization, identity-bound handles, selective exact reopening, and unresolved-route discipline.
- Housekeeping: [`TRADEMARKS.md`](TRADEMARKS.md), [`SECURITY.md`](SECURITY.md), [`CHANGELOG.md`](CHANGELOG.md), and [`LICENSE`](LICENSE).
- [`tools/check_change_history.py`](tools/check_change_history.py) and the other `tools/` checks — fail-closed structural verification.

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

A **Creature** is a task-shaped, manifest-bound formation of separately
identified Sparks, ledgers, Homes, optional Fireside lenses, and Thulia custody.
It exposes the coordination topology without merging identities, memory,
budgets, grants, or authority. Creature is not a fourth Spark role or a larger
agent identity.

An **open objective window** may gather out-of-order Homecomings from separately
identified objectives into one eventual response. The controller and host own
admission and lifecycle; a heartbeat marks an interrupt boundary but is not a
scheduler, keepalive, grant, or shared context.

A **Homecoming Return Queue** gives every intake attempt a durable disposition
and every accepted enqueue an immutable, controller-linearized arrival place.
Hearthline assigns a receipt-bound Homecoming Priority Mark before dispatch.
Stateless **Morrow** sees only a frozen scheduling view and may propose within-class
order. He gets dense ready-only ranks rather than global queue ordinals or epochs,
and his formal authority is `NONE`; the proposal-only output does not decide service.
Fairness comes first; only the controller owns counts, commits an order, and admits service.
An invalid new assignment blocks dispatch; an unmarked legacy return is held for explicit migration. Every return keeps its status and attribution.

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

Morrow and Thulia share no channel, state, ledger, custody, invocation,
impersonation, or dependency; each works when the other is absent.

The repository map above links the full role, Homecoming, Return Queue,
Creature, lineage, custody, and carry boundaries.

**TETHER** is Hearthline's carrier-neutral continuity technique: externalize recoverable trace, bind a compact identity/scope/status/residual/reopen handle, verify it later, and reopen only what the present task needs. Its receipt-bound Priority Mark sequences Homecoming without becoming permission or authority. An unresolved item without a reopening route is incomplete.

## Controlling references

When Hearthline discusses Christopher's framework work, each source controls only its declared role:

| Source | Version | Declared role |
|---|---:|---|
| PAL | 2.3 | Mechanical trace, role-typed boundaries, projections, transport, authority ceilings, residuals, and reopening handles |
| PECAN | 1.0.4 | Consequential crossings |
| PEA Core | 1.1.3 | Quiet, non-self-executing ethical and authority review under an external grant |
| SEED | 0.3 | Human-facing release discipline |
| PPP | 0.6 | Optional integration protocol where applicable |

See [`SOURCE_MAP.md`](SOURCE_MAP.md) for public locators, compatibility seams, layer ceilings, and open burdens. Artifact name and version remain part of source identity; PEA Core and PPP share a DOI record but are not the same artifact.

### Bounded public research branches

The following same-author publications are approved public research context for Hearthline. They are not additions to the controlling stack, PAL canon, runtime dependencies, adoption or activation records, authority sources, or independent corroboration. Naming a paper also does not mean that its code was imported or executed.

| Source | Published or inspected | Bounded use | Essential ceiling |
|---|---:|---|---|
| [*The Context Sets a Rhythm*, v0.1](https://zenodo.org/records/22214952) | 2026-08-31 | Cadence, refresh, intersection, and scheduler-choice vocabulary | No autonomous scheduler, proof of alignment, or verified runtime effect |
| [*Golden Phase Prime Ribbons* (GPPR), v0.1](https://zenodo.org/records/22225414) | 2026-09-01 | Exact prime-valuation geometry, optional golden-angle routing, and ordered receipt ribbons | No factoring advantage, finite-bit compression, universal optimizer, privileged geometry, or authority |
| [*Full Bandwidth Is Not Full Trace: A PAL–FBT Synthesis*, v0.1](https://zenodo.org/records/22228162) | 2026-09-01 | Conceptual synthesis and evaluation profile separating latent feedback from typed trace | No FBT code imported or executed here; no new neural result or claim that FBT causes trace fidelity, ARC performance, or safe authority handling |
| [*GOLD: Golden-Oriented Lens Diagram*, v0.1](https://zenodo.org/records/22236848) | 2026-09-01 | Exact fixtures for sixfold lenses, the `1+5` comparison split, trace-bearing paths, golden residuals, cube projection, and Euler defect accounting | Not PAL canon or a theory of physics, consciousness, or authorization |
| [*Compactification Costs*, v0.2](https://zenodo.org/records/22238012) | 2026-09-01 | Typed, detector-relative closure burdens with APCI fiber certification and later GOLD fixtures | No universal scalar, physical law, canonical detector, or backdating of APCI or GOLD into v0.1 |
| [*Single Cut Transport Lemma*, v0.2](https://zenodo.org/records/22239108) | 2026-09-01 | Resolution-qualified asymmetry, finite action-trace fixtures, exact checkpoints, heartbeat stutter, and re-entry | No universal minimal asymmetry, practical optimality, progress from heartbeat, or authority from recoverability |
| [*Boundary-Readable Trace and Absorber-Informed Closure* (BRRRT), v2.0](https://zenodo.org/records/22261831) | 2026-09-02 | Typed transition and readability ledger, benchmark crossings, and atomic promotion | A reading is not a mechanism; readability is not decoding; release-ready is not authorized |
| [Strongwiz v3 campaign prototype](https://github.com/Grativy6/strongwiz/tree/edc88b80f872f766c22b3a050a7f6837d6e652d8) | Inspected 2026-09-02 | Inspected design source for representation-only Scribes, matched controls, restart integrity, material-event cadence, and cost-accounting requirements | Prepared, not run or preregistered; no runner-wired evidence-yield schedule, Scribe benefit, or ARC benefit established; no code imported here |

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

**HLP-000015 — Morrow and the Homecoming Priority Mark**

- Hearthline now assigns a receipt-bound priority class before task dispatch.
- Morrow proposes deterministic within-class order from a stateless, scheduling-only view; the controller retains fairness and admission.
- Priority revisions are append-only, prospective, ceiling-bound, and never renew task authority or budgets.
- Morrow and Thulia share no channel, state, ledger, custody, or record surface.

[Full change record](docs/changelog/2026-09-05-hlp-000015-morrow-homecoming-priority.md) ·
[All public changes](CHANGELOG.md)
<!-- latest-change:end -->
