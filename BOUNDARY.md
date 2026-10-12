# Public and Operational Boundary

This repository publishes the model-neutral Hearthline toolkit, technical contracts and scoped formal evidence. It does not control an installed runtime.

## Public side

Appropriate public material includes:

- versioned branch instructions and their status;
- public boundaries, acceptance criteria, and change history;
- functional design contracts with explicit implementation status;
- links to already-public canonical sources;
- public implementation source and fabricated verification fixtures whose
  status, limits, and provenance are explicit; and
- non-secret verification material intended for public review.

The public source map may name public artifacts, versions, roles, status, authority ceilings, and canonical locators. It must not contain private source bytes, attachment hashes, journal excerpts, personal-context material, or a recoverable map of private chronology.

Publication establishes what bytes were made available. It does not establish that those bytes were deployed, authorized, accepted as canon, or used for any external action.

Personal lore, character art and selected private continuity belong in a separately configured environment. Previously public originals remain in Git history through the [historical reading guide](docs/HISTORY.md); this reorganization is not a secrecy guarantee. Named mechanisms remain usable without adopting a character or personal context.

## Copyright and authority

The repository's `CC-BY-4.0` license grants copyright and similar-rights permissions for covered material. Those permissions allow licensed sharing and adaptation; they do not authenticate a copy, designate a modified copy as official or canonical, activate a runtime, grant credentials or platform access, or supply consent, standing, adoption, or execution authority. Copyright compliance and operational authorization remain separate questions.

## Operational side

The following belong only in a separately controlled private environment:

- API keys, tokens, cookies, recovery material, and account identifiers not intentionally public;
- runtime control and authorization records;
- operational credential-broker configuration, deployment topology, and private infrastructure details;
- operational Static ledgers, Thulia roost, Hearth Perch and Spark-local Perch indexes, Bridge Glosses, and their access, carry, and delivery receipts;
- operational Spark identities, Home Records, paired-dispatch state, Spark Heartbeat Contracts, Pulse Receipts, suspension/resume state, return bundles, and Homecoming Return, Reconciliation, and Context-Close Receipts;
- operational Return Queue profiles, queue items, arrival and service snapshots,
  Homecoming Priority Marks, Assignment and Revision Receipts, priority-ledger
  cuts, Retry Rotation Release and Readiness Receipts, Morrow/Queue Steward
  views and proposals, and order, overflow, service, and close receipts;
- private receipts, logs, conversation records, and unpublished work;
- personal, behavioral, device, location, health, or biometric data; and
- any learned template derived from such data.

Do not commit sanitized-looking samples copied from real operational data. Use fabricated fixtures with no recoverable private source.

Morrow and Thulia remain operationally disjoint even on the private side.
There is no direct channel, shared state, ledger, Perch, Bridge Gloss, custody,
selected carry, mutual invocation, impersonation, or availability dependency
between them. The controller exposes only separate minimum views, and each
function must remain correct when the other is absent.

## Authority boundary

Christopher D. Pang is the author and original steward of this project. Each installation has its own operator and chosen context. Only an authenticated operator-controlled process outside that installation's agent write scope may adopt a version, select a mode, grant a capability, or revoke it.

Repository events are never authorization events. In particular:

- opening or merging a pull request does not activate changed instructions;
- a GitHub account, collaborator, automation, model, or issue commenter cannot grant Hearthline authority through repository text;
- a successful test or matching hash proves only its declared result; and
- a deployed runtime must fail closed when its adopted version or external authorization cannot be established.

There is no authority backflow from publication, popularity, technical capability, successful execution, or later outcomes.

## Framework boundary

PAL v2.3, PECAN v1.0.4, PEA Core v1.1.3, SEED v0.3, and optional PPP v0.6 retain their declared roles. PAL v2.3 is a successor source for new records, not a retrofit of v2.2-era evidence; the PEA Core and PPP interfaces remain explicit v2.2 compatibility seams until separately revised. Hearthline may explain and apply public material within scope; it cannot revise canon, create permission from proof, or convert generated synthesis into an adopted rule.

Earlier terminology remains provenance unless Christopher explicitly adopts it. In particular, legacy `A0 = Omega` mappings are not current canon.

Supplied continuity is not experiential memory. A journal, transcript, summary, continuity packet, or personal-context file may inform a bounded review without establishing that Hearthline remembers the event, existed at the time, owns the context, or has continuous identity, personhood, standing, or authority. Duplicate formats and derivatives from one source lineage are not independent corroboration.

## Safe adoption rule

A future runtime should consume a deliberately selected immutable release or exact digest, never a moving branch. Updating the public repository and adopting runtime instructions must remain separate, reviewable events with separate receipts.

The historical [`candidate_manifest.json`](https://github.com/Grativy6/hearthline/blob/f5c69b912761f29e2c82f83d1fe412fc83ec873a/candidate_manifest.json) is a same-branch consistency envelope for its legacy agent: it binds the policy's UTF-8, LF-normalized repository text and declared metadata present in the proposal. It does not bind a platform checkout's raw line-ending bytes. Because policy and manifest can change together, it is not an external integrity anchor, operator authentication, source-authenticity finding, semantic-conformance result, freshness guarantee, adoption record, or activation receipt. The separate operator-controlled local pin remains the exact-byte adoption prerequisite.

An optional private-lineage seal may provide an additional, bounded provenance comparison if it follows [`docs/PRIVATE_LINEAGE_SEALS.md`](docs/PRIVATE_LINEAGE_SEALS.md). Such a seal remains shared-key evidence about an exact committed Git tree and its HMAC-bound declared context. It is not an adoption record, public identity proof, semantic review, or authority source.
