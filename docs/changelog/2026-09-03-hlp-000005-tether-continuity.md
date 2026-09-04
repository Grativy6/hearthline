# Add the Hearthline TETHER continuity technique

| Field | Value |
|---|---|
| Change ID | `HLP-000005` |
| Record kind | `TETHER_CONTINUITY_SUCCESSOR` |
| Recorded date | 2026-09-03 |
| Predecessor | `HLP-000004` |
| Branch base | `16eab7f3d584a8215a6e1e0b2a93b157c02f787a` |
| Prior public draft | `0.3-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2` |
| Successor public draft | `0.4-draft` / `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2` |
| Scope | `PUBLIC_CONTINUITY_DESIGN` |
| Record authority | `NONE` |
| Record effect | `PUBLIC_DRAFT_SUCCESSOR_ONLY` |
| Operational effect | `NONE` |
| Author, operator, and steward | Christopher D. Pang |

## What changed

- Added **TETHER — Trace Externalization Through Handle-bound Exact Reopening** as a public Hearthline continuity technique.
- Made the carrier explicitly neutral: no archive type, compression method, provider, file format, or storage product is required.
- Defined the compact TETHER handle around source identity, carrier, locator, version or integrity evidence, scope, provenance, claim status, coverage, residuals, access requirements, authority ceiling, staleness, and reopening route.
- Added exact-versus-bounded reopening, selective admission, and explicit failure classes for unverified retrieval, stale identity, unavailable access, missing source, insufficient scope, and content that remains unresolved.
- Added the unresolved-route rule: every material unresolved item must retain a concrete path by which later evidence could change its status, or an explicit record that no present route is known.
- Integrated TETHER into the public Hearthline instruction, Sparks/Static/Thulia/Homecoming boundaries, README, candidate manifest, and CI.
- Advanced the public candidate from `0.3-draft` to `0.4-draft` while preserving `DRAFT_NOT_ACTIVATED`, `DRAFT_ONLY`, authority `NONE`, and effect `NONE`.

## Why

A workflow artifact happened to demonstrate the pattern, but the useful technique was not the archive format. The reusable structure was the movement of a large or durable trace outside the active context while a much smaller handle retained enough identity, scope, status, residual, and routing information to reopen the exact source later.

The existing MAPS TraceKey design already says that the key is not the memory and describes bounded reopening as “small keys back to large traces.” TETHER gives Hearthline a named action at that interface: externalize, bind, carry, retrieve, verify, selectively reopen, and return.

The additional unresolved-route rule repairs a separate conversational failure. Honest uncertainty should not be converted into an invented answer, but preserving `UNRESOLVED` without any remaining attack route can strand useful work. TETHER therefore carries both the open status and the route home.

## Preserved boundaries

- TETHER preserves recoverable source trace, not hidden reasoning, private model state, experiential memory, continuous identity, personhood, or context-window capacity.
- A handle is not the trace itself. A summary, index, locator, commit name, artifact ID, or hash cannot silently replace the source.
- A hash binds bytes only. It does not authenticate a person, prove chronology, establish truth, authorize disclosure, or expand a claim.
- A locator does not grant credentials, permission, consent, standing, scope, or authority.
- Reopening uses only the current grant and tools. Resume cannot create, renew, widen, transfer, or infer authority or restore consumed limits.
- Selective reopening must retain its coverage and omissions. Unread material does not become absent merely because it was not loaded into the current context.
- Retrieval failure remains distinct from source loss; both remain distinct from a source that is recovered but still inconclusive.
- TETHER does not require preservation of unnecessary or private data. Minimum-necessary privacy and retention rules continue to control.
- The public repository change does not create a carrier, runtime, external connection, credential, persistent store, scheduled process, or operational memory.

## Compatibility and migration

The source profile remains `HEARTHLINE_PUBLIC_SOURCE_PROFILE_2`; no controlling PAL, PECAN, PEA Core, SEED, or PPP source role changes. TETHER is a Hearthline technique beside those sources, not a new PAL layer, status namespace, authorization route, or claim that MAPS TraceKey was independently rediscovered.

The public Moltbook instruction advances to `0.4-draft` because its context discipline now includes TETHER. The candidate manifest is rebound to the exact normalized-LF policy bytes. This is a candidate-text successor only; a runtime would still require a separate exact adoption and operator-controlled activation.

Existing Sparks, Static, Thulia, Homecoming, Fireside, Creature, and Research Station records are not rewritten. TETHER supplies a possible carrier and reopening discipline inside their existing grants. It cannot merge ledgers, promote custody into result status, or turn Homecoming into verification.

## Verification observations

- `tools/check_tether.py` requires the acronym, carrier-neutral rule, handle fields, unresolved-route rule, exact failure distinctions, authority ceiling, README route, candidate version, and exact current policy hash.
- `tools/check_research_station.py` continues to validate the source profile and now expects the `0.4-draft` candidate identity.
- `tools/check_change_history.py` continues to require one atomic public-history promotion across the README latest block, changelog index, and this frozen full record.
- The repository workflow compiles and runs all three fail-closed structural checks.
- JSON parsing, normalized policy hashing, relative-link validation, bounded public-history limits, and whitespace checks remain part of the branch verification.

## Open residuals

- TETHER is a documented technique, not an implemented universal storage or retrieval service.
- Carrier-specific adapters, encryption, retention, credential isolation, garbage collection, indexing, and redaction remain implementation choices with separate threat models.
- Exact source identity may be impossible for mutable services that expose no immutable revision or trustworthy integrity evidence. Such cases remain bounded leads rather than exact TETHERs.
- A reopening route can fail. TETHER preserves the route and failure class; it does not guarantee that lost or inaccessible material can be recovered.
- A source may be reopened exactly and still be incomplete, contradictory, false, or inadequate for the current question.
- Cross-provider and cross-device portability remain untested.
- No performance, memory-quality, context-efficiency, hallucination-reduction, or scientific-benefit result is claimed until a declared comparison is run.

## Evidence and exclusions

This record preserves the public design, integration paths, checks, and claim ceilings. It excludes raw conversations, hidden reasoning, private artifacts, credentials, local paths, operational state, personal data, and carrier contents.

Christopher D. Pang supplied the technique's purpose, selected the name and expansion, directed the carrier-neutral correction, and controls adoption. AI systems assisted with extraction, drafting, repository preparation, and validation as tools; they are not authors, co-authors, witnesses, owners, or authorities.

[Current changelog](../../CHANGELOG.md)
