# Public and Operational Boundary

This repository publishes inspectable Hearthline instructions. It does not contain or control a live Hearthline runtime.

## Public side

Appropriate public material includes:

- versioned branch instructions and their status;
- public boundaries, acceptance criteria, and change history;
- links to already-public canonical sources; and
- non-secret verification material intended for public review.

Publication establishes what bytes were made available. It does not establish that those bytes were deployed, authorized, accepted as canon, or used for any external action.

## Operational side

The following belong only in a separately controlled private environment:

- API keys, tokens, cookies, recovery material, and account identifiers not intentionally public;
- runtime control and authorization records;
- operational credential-broker configuration, deployment topology, and private infrastructure details;
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

PAL v2.2, PECAN v1.0.4, PEA Core v1.1.3, SEED v0.3, and optional PPP v0.6 retain their declared roles. Hearthline may explain and apply public material within scope; it cannot revise canon, create permission from proof, or convert generated synthesis into an adopted rule.

Earlier terminology remains provenance unless Christopher explicitly adopts it. In particular, legacy `A0 = Omega` mappings are not current canon.

## Safe adoption rule

A future runtime should consume a deliberately selected immutable release or exact digest, never a moving branch. Updating the public repository and adopting runtime instructions must remain separate, reviewable events with separate receipts.
