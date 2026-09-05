# Public and Operational Boundary

This repository publishes inspectable Hearthline instructions. It does not contain or control a live Hearthline runtime.

## Public side

Appropriate public material includes:

- versioned branch instructions and their status;
- public boundaries, acceptance criteria, and change history;
- explicitly labeled fictional lore, character art, and visual provenance;
- links to already-public canonical sources; and
- non-secret verification material intended for public review.

The public source map may name public artifacts, versions, roles, status, authority ceilings, and canonical locators. It must not contain private source bytes, attachment hashes, journal excerpts, personal-context material, or a recoverable map of private chronology.

Publication establishes what bytes were made available. It does not establish that those bytes were deployed, authorized, accepted as canon, or used for any external action.

Fictional scenes and visual details may give Hearthline, Thulia, Sparks, or artifacts a narrative life. They do not report an AI system's experiences, instantiate the depicted characters or objects, or turn a story action, expression, color, heartbeat, or prop into an operational instruction or control.

## Copyright and authority

The repository's `CC-BY-4.0` license grants copyright and similar-rights permissions for covered material. Those permissions allow licensed sharing and adaptation; they do not authenticate a copy, designate a modified copy as official or canonical, activate a runtime, grant credentials or platform access, or supply consent, standing, adoption, or execution authority. Copyright compliance and operational authorization remain separate questions.

## Operational side

The following belong only in a separately controlled private environment:

- API keys, tokens, cookies, recovery material, and account identifiers not intentionally public;
- runtime control and authorization records;
- operational credential-broker configuration, deployment topology, and private infrastructure details;
- operational Static ledgers, Thulia roost, Hearth Perch and account-local Perch indexes, Bridge Glosses, and their access, carry, and delivery receipts;
- operational Spark identities, Home Records, paired-dispatch state, Spark Heartbeat Contracts, Pulse Receipts, suspension/resume state, return bundles, and Homecoming Return, Reconciliation, and Context-Close Receipts;
- private receipts, logs, conversation records, and unpublished work;
- personal, behavioral, device, location, health, or biometric data; and
- any learned template derived from such data.

Do not commit sanitized-looking samples copied from real operational data. Use fabricated fixtures with no recoverable private source.

## Authority boundary

Christopher D. Pang is the sole author, operator, and steward of Hearthline. Only an authenticated operator-controlled process outside the branch's write scope may adopt a version, select a mode, grant a capability, or revoke it.

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

The committed `candidate_manifest.json` is a same-branch consistency envelope: it binds the policy's UTF-8, LF-normalized repository text and declared metadata present in the proposal. It does not bind a platform checkout's raw line-ending bytes. Because policy and manifest can change together, it is not an external integrity anchor, operator authentication, source-authenticity finding, semantic-conformance result, freshness guarantee, adoption record, or activation receipt. The separate operator-controlled local pin remains the exact-byte adoption prerequisite.

An optional private-lineage seal may provide an additional, bounded provenance comparison if it follows [`docs/PRIVATE_LINEAGE_SEALS.md`](docs/PRIVATE_LINEAGE_SEALS.md). Such a seal remains shared-key evidence about an exact committed Git tree and its HMAC-bound declared context. It is not an adoption record, public identity proof, semantic review, or authority source.
