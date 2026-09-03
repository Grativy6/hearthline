# Hearthline Research Station

| Field | Value |
|---|---|
| Version | `0.1` |
| Status | Public research-context and provenance registry |
| Runtime effect | `NONE` |
| Author and steward | Christopher D. Pang |

The Research Station is Hearthline's bounded shelf for public sources that may
inform a design or an experiment without becoming runtime dependencies,
independent corroboration, or authority. Its machine-readable source record is
[`research-station/source-identities.json`](research-station/source-identities.json).

## September 2026 intake

| Source | Hearthline use | Claim ceiling |
|---|---|---|
| [PAL v2.3](https://doi.org/10.5281/zenodo.22240134) | Current mechanical source for typed boundaries, projections, transport, grants, residuals, and reopening | The five faces keep separate authority; registration is not whole-system conformance or external authority |
| [BRRRT v2.0](https://doi.org/10.5281/zenodo.22261831) | Transition and readability ledger; benchmark crossings; release-ready versus authorized promotion | A reading is not a mechanism, readability is not decoding, and verification does not manufacture a grant |
| [Single Cut Transport Lemma v0.2](https://doi.org/10.5281/zenodo.22239108) | Finite pairwise fixtures, action-trace lift, exact checkpoints, heartbeat stutter, and re-entry | Finite verification is not a universal proof; heartbeat is not progress; recoverability is not authority |
| [Compactification Costs v0.2](https://doi.org/10.5281/zenodo.22238012) | Detector-relative loss, reachable-image decoders, totalization seams, and full representation-cost questions | No universal scalar, canonical detector, automatic decoder, physical law, or authority |
| [Strongwiz v3 prototype](https://github.com/Grativy6/strongwiz/tree/edc88b80f872f766c22b3a050a7f6837d6e652d8) | Design evidence for representation-only scribes, material-event cadence, restart integrity, matched controls, and cost ledgers | Prepared but not run or preregistered; no demonstrated scribe or ARC benefit; no code imported here |

Compactification Costs v0.2 was already present in Hearthline's public research
map. This intake confirms it rather than claiming a second source. PAL v2.3 is a
successor source for new Hearthline records; it does not relabel PAL v2.2-era
records. Single Cut v0.2 succeeds the previously listed v0.1 context. BRRRT and
the Strongwiz inspection are new bounded entries.

### Resolved BRRRT artifact identity

A first audit observed a 1,276,294-byte C2PA-wrapped loose PDF at
`806d7cda4ffb186d21f7797917c99c22ff29452af12de36aa597ed37fe4d3236`,
while the release package and its ledger bound a 1,251,146-byte canonical PDF at
`f9e699ad4a8541506ecc6678c3296bdf4fbe4dd249a0dd6759c7fd0d22837e0a`.
The author replaced the loose record file in place. A fresh live-record query
and byte download on 2 September 2026 now confirm that the loose PDF is
1,251,146 bytes at `f9e699…37e0a`, matching the package and SHA ledger; its
current Zenodo MD5 is `79462822b3895d2e02d0aff26279a8af`. The earlier wrapper
identity remains historical audit evidence, not a current DOI-file variant.

The Strongwiz inspection also preserves two smaller upstream reproducibility
seams: one raw source-registry file hash is specific to LF Git-blob bytes while
an ordinary Windows checkout transforms that file, and Strongwiz's local
exact-lock full-test recipe omits optional calibration dependencies that its CI
installs explicitly. The semantic registry reference and green pinned-commit CI
remain separately identifiable; neither seam is treated as an ARC failure or
silently erased.

Two distribution identities remain deliberately separate as well. Strongwiz's
package metadata names `0.4.0.dev0` with pre-alpha status, while its
`CITATION.cff` and `NOTICE.md` still carry `0.2.0`/v0.2 labels; this Station uses
the package version but does not promote it into a tagged v0.4 release. The
reproducible wheel and source distribution contain the general kernel, not the
repository-local `calibration_003` harness, so installing the package is not a
reproduction of Calibration 003.

Strongwiz's semantic `source_registry_ref` identifies its own 14-entry source
registry, not this Station. It includes PAL v2.3 and an older Single Cut source,
but it does not include BRRRT v2.0, the v0.2 Single Cut record, or
Compactification Costs v0.2. Their present Hearthline registration is later
research intake, not retroactive Strongwiz development provenance.

## Design extraction

The Station carries the following questions into Hearthline's tool design:

1. **What is the declared projection?** A return, heartbeat, equality, or
   checkpoint statement names the included and excluded coordinates and its
   comparator.
2. **What became unreadable?** Any summary, shorthand, or shared view records
   which distinctions its detector preserves, loses, or leaves ambiguous.
3. **What crossed the boundary?** Release, retention, transformation,
   transport, readability, recommendation, promotion, and authorization remain
   different typed transitions.
4. **What did the representation cost?** Count source, residual, compact,
   codebook, request, response, evaluation, transfer, verification, latency,
   context, compute, and human reorientation costs before claiming a saving.
5. **What survives restart?** Freeze the work state and trace; revalidate every
   non-work coordinate; never restore spent resources, expired grants, or
   authority.
6. **What comparison could falsify the design?** A representation feature earns
   reasoning or play credit only through a matched evaluation at the relevant
   outcome, not from architecture resemblance or a smaller ledger alone.
7. **What shares cadence without sharing scope?** An open objective window may
   aggregate separately identified, out-of-order Homecomings, but every
   objective retains its own grant, limits, ledger, status, and receipts.
8. **What actually keeps the work surface available?** The outer host and
   controller own lifecycle and scheduling. A heartbeat is an interrupt and
   evidence boundary, not a keepalive or scheduler.

## Additional ARC-preparation context

Five earlier public sources remain useful at narrower apertures: [The Context
Sets a Rhythm](https://doi.org/10.5281/zenodo.22214952) for replaceable cadence,
[Golden Phase Prime Ribbons](https://doi.org/10.5281/zenodo.22225414) for exact
identity encodings and separate canonical/event ribbons,
[Full Bandwidth Is Not Full Trace](https://doi.org/10.5281/zenodo.22228162) for
latent-versus-trace separation, [GOLD](https://doi.org/10.5281/zenodo.22236848)
for a `1+5` common/comparison lens fixture, and [The Context Draws a
Map](https://doi.org/10.5281/zenodo.21831000) for local context maps and
reopening handles. Their exact roles and ceilings are in the registry. They are
optional design sources, not a recipe for ARC success.

## Provenance and redistribution boundary

The Station records public locators, inspected byte identities, versions,
roles, and ceilings. It does not vendor manuscripts, private journals, run
state, credentials, game data, hidden reasoning, or Strongwiz code. Matching a
published file checksum identifies bytes only; it does not establish semantic
truth, authorship beyond the public record, independent review, adoption, or
authority.

All Pang works named here share one author-led lineage. Cross-citation, model
review, regenerated files, and repeated tests may add transformation or
reproducibility evidence but do not turn that lineage into independent
corroboration.

## Implementation boundary

This registry does not activate Hearthline, instantiate a Spark or Creature,
contact an ARC environment, consume a holdout, preregister an experiment, or
authorize a run. A later implementation must bind exact source, code, model,
runtime, domain, evaluator, budget, grant, and stop-rule identities in a new
receipt-backed record.
