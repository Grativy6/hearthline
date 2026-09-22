# Separate preserved context from its applicability

| Field | Value |
|---|---|
| Change ID | `HLP-000031` |
| Record kind | `MCP_CONTEXT_SUCCESSOR` |
| Recorded date | 2026-09-21 |
| Predecessor | `HLP-000030` |
| Frozen predecessor SHA-256 | `034449e6481e610a84d5cf91b988679021bc154a4de7c68d659ed6fc108f573d` |
| Predecessor hash domain | Git object content bytes |
| Branch base | `73b85bad9fdb2269aa99738518e4e24bae5c6a98` |
| Branch-base tree | `c6ad9b10961e6294e0b402e01304b50c6c232606` |
| Scope | `MIND_TIES_CONTEXT_APPLICABILITY` |
| Record authority | `NONE` |
| Record effect | `REPOSITORY_HISTORY_ONLY` |
| Operational effect | `NONE` |
| Author and steward | Christopher D. Pang |

## What changed

Toolkit 0.2.0 adds a reference-only catalogue for the published MIND v0.4 and
TIES v0.2 editions, with raw-file hashes, roles, source sections and explicit
implementation limits. A context-group tool and resource expose that catalogue.
The read-only `review_context_applicability` tool separately reports canonical
source-content preservation and exact declared receiving-condition comparisons.
Conditions are bound inside the content; absent evidence stays unresolved.

The existing observation, compaction, TETHER and selective-correction surfaces
carry the result. No additional persistence engine is introduced. Documentation
includes a runnable synthetic example, the finite contract, migration boundary,
and the distinction between source reference and runtime implementation.

## Why

Christopher requested the Hearthline MCP update after publishing TIES and MIND.
A faithfully recovered record may not apply to the current question. Keeping
these checks separate prevents a successful retrieval from silently becoming
an applicability claim, and gives missing conditions an explicit reopening path.

## Preserved boundaries

The shared PAL/CHARTER/PECAN/PEA/SEED foundation is unchanged. MIND contributes
a reduced implementation profile, and TIES a bounded composition account;
neither is promoted to a new controlling source. Same-author references do
not become independent confirmations. Repeated references do not become votes.
Founding orientation, optional templates, historical records, current-grant
checks, dependency adoption and heartbeat limits remain intact.

## Compatibility and migration

This is an additive 0.2.0 package update with no stored-record migration. The
foundation dependency stays at 0.1.0. Hosts restricting tools to foundation,
core and continuity do not expose the new context tools or resource. A running
installation needs an explicit package update and reconnection; a repository
change does not update it automatically.

## Verification observations

The local Windows/Python 3.12 toolkit suite passed **93 tests**, including 30
new checks. The real MCP route spans three server processes: retain a scoped
preference, omit it during compaction, recover it, preserve an unknown target
condition, append a correction, and selectively reconsider one adopted
load-bearing dependent. Original and intermediate records remain unchanged
after another restart. Unit fixtures cover content changes, removed qualifiers,
missing source/evidence, stale editions, strict equality, malformed/bounded
inputs, duplicate evidence, and context-group filtering.

All five repository structural checks passed. The wheel built successfully;
an isolated installation exposed version 0.2.0, the packaged catalogue and
resource, and the read-only review over actual MCP stdio. These observations
use synthetic data and establish only the named finite contracts. Platform CI
results belong to their exact checked commit.

## Open residuals

The checker compares supplied declarations. It does not authenticate evidence,
judge semantic fidelity, find all relevant conditions, or decide whether a
claim is true or useful. Source unresolveds block a positive result unless a
revised account resolves them. A target change requires a fresh review.
No learning improvement or end-to-end TIES conformance has been established.

## Evidence and exclusions

Source identities are recorded in `hearthline_mcp/context_sources.json` and
the source map. The context contract specifies the distinct canonical-JSON and
raw-file hash domains. The code performs no source download, model call,
training, weight update, scheduler activation, automatic admission, or external
action. Installed adapters and private records are outside this change.
Earlier history records retain their original bytes and meanings.
