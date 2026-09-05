# Hearthline TETHER

## Trace Externalization Through Handle-bound Exact Reopening

```yaml
document: HEARTHLINE_TETHER
version: 0.2-draft
status: PUBLIC_DESIGN_PROPOSAL
author_and_steward: Christopher D. Pang
repository_role: HEARTHLINE_CONTINUITY_TECHNIQUE
activation_effect: NONE
```

> **Keeper.** Externalize recoverable trace through whatever reliable carrier is available. Carry a compact, identity-bound handle. Never carry a material unresolved state without also carrying a concrete route by which it could be reopened.

## v0.2-draft Homecoming Priority Mark successor

Version `0.2-draft` permits a task TETHER to carry a compact **Homecoming
Priority Mark** assigned by Hearthline at commissioning and recorded by the
canonical controller before dispatch. The mark is a projection of a durable
Homecoming Priority Assignment Receipt, not an editable priority field. It
avoids a self-hash: the controller first freezes the priority-envelope-free
TETHER core and computes `task_tether_core_digest` under
`HEARTHLINE_TASK_TETHER_CORE_V1`. The Assignment Receipt binds that digest,
dispatch, destination queue profile and epoch, finite policy and class,
controller-frozen ceiling and revision budget, controller-readable basis
reference, and dispatch epoch. Only then does the final envelope carry the
core, mark, and Assignment Receipt reference. A separate envelope digest may be
computed afterward; neither digest includes itself.

The mark routes scheduling intent home without carrying task cargo into the
scheduler. It cannot verify the carrier, establish importance or result status,
grant access, widen authority, or make a return ready. The dispatched Spark or
Creature, its return payload, Morrow, an evaluator, and Thulia cannot author,
edit, inherit, or promote it. A new dispatch requiring priority stops if the
assignment receipt or exact TETHER binding is missing, invalid, conflicting, or
ambiguous.

A later class change is not an edit to the TETHER. Hearthline proposes it and
the controller appends a separate Homecoming Priority Revision Receipt with an
exact predecessor, monotonic ordinal, compare-and-swap head, remaining finite
revision budget, named queue epoch, current priority-ledger head, and observed
snapshot head. Revision append and snapshot cut share one controller-linearized
surface. The revision first applies in the later snapshot whose frozen
`priority_ledger_cut` includes it; stale-head compare-and-swap cannot backdate
it. Invalid, stale, forked, no-op, or non-exact replay attempts under a new key
do not change the last valid head; an ambiguous append has no effect until
reconciled from durable state. A revision can never renew or expand the
TETHER's source task, scope,
grant, authority, Home, access, privacy, retention, expiry, deadline,
capabilities, consumed limits, or budgets.

Typed idempotency lookup precedes current lifecycle, predecessor, and head
validation for both assignment and revision. A byte-identical same-key retry
returns the original receipt identity and latest durable disposition even after
later state advances; a same-key changed binding conflicts. Only an unseen key
undergoes fresh validation, and a non-exact replay under a new key cannot alter
the valid head.

This successor does not make TETHER a queue, scheduler, priority ledger, or
permission channel. Morrow sees only the controller-attested effective rank
in a separate frozen Queue Scheduling View; he receives neither the task TETHER
nor its receipt chain or basis. Thulia receives none of the mark, assignment,
revision, view, proposal, order, or admission surfaces. Morrow receives none of
her Perches, ledgers, Bridge Glosses, selected carry, or custody records. They
have no direct channel or shared state.

## 1. Purpose

TETHER is Hearthline's carrier-neutral continuity technique for work that must survive a context boundary, process boundary, session change, long interruption, or selective return. It names a bounded motion:

```text
externalize -> bind -> carry -> retrieve -> verify -> selectively reopen -> return
```

The technique does not require one archive format, compression method, storage provider, or software stack. A Git commit, immutable blob, workflow artifact, ordinary file, versioned document, folder plus manifest, database snapshot, object-store item, transcript range, or another adequately identified carrier may be used when the current environment can lawfully and reliably reopen it.

The goal is not total memory. The goal is exact or honestly bounded reopening.

## 2. Relation to MAPS TraceKey

MAPS TraceKey v0.1 defines a TraceKey as a scoped routing handle rather than the memory itself and gives the project the phrase **small keys back to large traces**. TETHER is a compatible Hearthline-side technique built at that seam:

- **TraceKey names the key.**
- **TETHER names the motion performed with a bound key.**

The relationship is lineage and reuse, not independent corroboration. TETHER does not replace MAPS TraceKey or silently adopt every future TraceKey feature.

Primary publication: [*MAPS TraceKey v0.1: An Offline-First Trace-Routing Ledger for AI-Assisted Work*](https://doi.org/10.5281/zenodo.21245399).  
Implementation repository: [Grativy6/maps-tracekey](https://github.com/Grativy6/maps-tracekey).

## 3. What a TETHER carries

A complete TETHER handle should carry the smallest fields needed to identify, constrain, and reopen the trace honestly:

```yaml
tether_id: stable local identifier
source_identity: originating project, account, document, run, or record
carrier_kind: git_commit | artifact | file | versioned_document | snapshot | other
locator: exact route the authorized retrieval layer can use
version_or_integrity: commit, blob, version ID, digest, ETag, manifest, or declared absence
scope: what part of the source the handle addresses
provenance: who or what supplied, produced, transformed, or observed it
claim_status: source-side status carried without promotion
coverage: what the carrier is known to include and omit
residuals: material uncertainty, missing coverage, conflicts, or open burdens
reopening_route: concrete retrieval, query, comparison, reproduction, or review step
access_requirements: grant, privacy, credential, tool, or environment constraints
authority_ceiling: what the handle and payload cannot authorize
do_not_claim: especially likely overreads
staleness_or_expiry: change conditions that require revalidation
```

Not every carrier exposes every field natively. Missing material fields remain explicit rather than being guessed. A mutable locator without a stable version or integrity binding is a **lead**, not an exact TETHER.

A content hash is useful when available, but it binds bytes only. It does not authenticate the human source, establish chronology by itself, grant access, authorize disclosure, certify truth, or widen the payload's claim status.

## 4. Exact reopening

`Exact` describes the relation between the handle and the reopened object. It does not promise that the externalized trace was complete, adequate, true, or sufficient for every later question.

A TETHER reopening is exact when the retrieval layer can establish that it reopened the bound carrier or the declared projection of that carrier under the recorded identity rule. When exact identity cannot be established, the result must be typed more narrowly, for example:

- `RETRIEVED_UNVERIFIED` — content was retrieved, but identity or integrity is not established;
- `STALE` — the named source changed beyond the bound version or expiry rule;
- `ACCESS_UNAVAILABLE` — the source may still exist, but the present grant or tool cannot reach it;
- `SOURCE_MISSING` — the bound source cannot presently be located;
- `SCOPE_INSUFFICIENT` — the carrier is real, but it does not cover the question;
- `CONTENT_UNRESOLVED` — the source was reopened and still does not decide the issue.

Retrieval failure is not source loss. Source loss is not proof that the underlying event never occurred. A nearby reconstruction may be useful, but it must be labeled as a reconstruction before it is presented.

## 5. Selective reopening

Reopening should admit only what the current task requires. The retrieval layer may search, index, filter, or read a bounded region instead of flooding the active context with the full carrier.

A selective reopening records:

1. the TETHER handle used;
2. the identity or integrity check performed;
3. the portion actually reopened;
4. material exclusions or unread regions;
5. the claim status inherited from the source;
6. any new interpretation added in the present pass; and
7. the next reopening route for what remains unresolved.

Selective reopening must not make an omitted region disappear from the coverage account. A summary may route attention; it does not silently become the source.

## 6. The unresolved-route rule

A TETHER may carry an unresolved state forward. It may not turn the word `UNRESOLVED` into a dead end. **An unresolved state without a reopening route is an incomplete TETHER.**

For every material unresolved item, retain at least one concrete reopening route, such as:

- retrieve the exact source version;
- request the missing access or disclosure decision from the authorized person;
- compare the bound version with the current version;
- inspect a named file, range, table, receipt, or artifact;
- rerun a declared procedure under fixed inputs;
- ask a named specialist to attack a named theorem, assumption, or priority question;
- obtain an independent measurement or witness; or
- state that no presently known route exists and preserve the search terms and stopping reason.

A route need not be guaranteed to succeed. It must be specific enough that a later worker can tell what reopening was intended and why it could change the status.

## 7. Authority, privacy, and capability boundary

A TETHER handle is not permission to retrieve its carrier. A locator does not grant credentials. A successful reopening does not authorize publication, disclosure, execution, spending, messaging, or any other consequence.

Reopening uses only the current grant, current tools, current privacy boundary, and current scope. Resuming from a TETHER cannot create, renew, widen, transfer, or infer authority. Consumed limits remain consumed. A stale or inaccessible grant leaves the handle intact and the content unopened.

Private material should remain in the least exposed adequate carrier. Public handles must not leak private filenames, local paths, secrets, personal data, hidden prompts, or the existence of material whose disclosure was not authorized.

## 8. What TETHER is not

TETHER is not:

- a way to evade or enlarge a model's context window;
- preservation of hidden chain-of-thought or private model state;
- a claim of continuous model identity or experiential memory;
- a requirement to compress, archive, or use a particular file format;
- proof that externalized material is complete, truthful, current, or adequate;
- a permission, authorization, authenticity, or authorship mechanism;
- a substitute for backups, version control, access control, encryption, or retention policy; or
- a reason to keep unnecessary data.

The active context carries a handle and whatever bounded material is reopened. The larger trace remains external.

## 9. Hearthline integration

Hearthline may use TETHER during directly authorized work when continuity would otherwise depend on fragile conversational recall.

- A **Work Spark** may emit a TETHER handle for its exact artifact, receipts, open burdens, and next route.
- A **Ledger Scribe Spark** may record or validate a handle within its own grant, but it cannot use the handle to select actions or read outside its access boundary.
- **Thulia** may custody or translate a handle between declared Perches only when the direction, source, and target are authorized. She does not merge the underlying ledgers or reopen private content merely because she carries the key.
- **Homecoming** may return a TETHER handle as representation-side data. `RETURNED` and `RECONCILED` remain custody states; they do not verify the payload or manufacture its result status.
- **Hearthline Static** may retain shorthand pointing to a TETHER, but the shorthand remains local and cannot replace the source trace.

TETHER complements suspension: before a long pause or context boundary, externalize the material trace, bind the handle, record the residuals and reopening route, then suspend. On return, revalidate the grant and handle before reopening anything.

## 10. Minimal conformance examples

### Git or repository carrier

Bind repository, commit, path, and blob or content digest. Reopen the exact file or range needed. Branch names alone are mutable and do not establish exact identity.

### Workflow or computation artifact

Bind run identity, artifact identity, source commit, procedure version, declared inputs, and digest when available. A successful download establishes retrieval; the artifact's own tests and claim ceiling control what its contents support.

### Versioned document

Bind document identity and version or immutable revision. If only a mutable shared link exists, carry `RETRIEVED_UNVERIFIED` or `STALE` as appropriate rather than claiming byte continuity.

### Database or object store

Bind snapshot or transaction identity, schema/query version, object version, and relevant partition. Reading today's current row is not reopening yesterday's snapshot unless the store establishes that relation.

### Conversation or transcript

Bind exact message, turn, export, or transcript-range identity when available. A summary is a projection and must carry its omissions. If the exact prior wording cannot be recovered, lead with that status before offering a reconstruction.

## 11. Compact operating rule

> **Externalize what must survive. Bind the smallest honest handle. Reopen only what the present task needs. Carry every unresolved item with its route home.**

## 12. Status and authorship

This document is a public design proposal for the Hearthline repository. It adds no runtime, storage provider, credential, persistent memory, external connection, task grant, or authority. Implementation and adoption are separate acts.

Christopher D. Pang is the author and steward of TETHER. AI systems assisted with extraction, naming refinement, adversarial review, drafting, repository preparation, and validation as tools. They are not authors, co-authors, owners, witnesses, or authorities.
