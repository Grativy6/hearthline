# WIP checkpoint — Task Triads and *The Night the Garden Clicked*

| Field | Value |
|---|---|
| Date | 2026-09-04 |
| Branch | `lore/the-night-the-garden-clicked-20260904` |
| Pre-checkpoint HEAD | `3085d857e8f71671935bdcd1d8bb34a2e81673fe` |
| State | Deliberately paused; candidate work in progress |
| Adoption or implementation effect | None |

This file records an intentional pause requested by Christopher D. Pang before
the working context became crowded. The checkpoint commit containing this file
is the authoritative byte snapshot. Nothing in this checkpoint is adopted,
merged, activated, or represented as fully validated.

## Frozen design decision

A Task Triad has three separate Spark jobs:

1. **Worker** — provisioned from Hearthline's side;
2. **Task-Keeper / Heartbeat-Keeper** — provisioned from Hearthline's side,
   carrying only the frozen task boundary rather than runtime liveness; and
3. **Ledger-Keeper** — provisioned independently from Thulia's side.

Hearthline may request a Triad whenever her current authority permits. She
supplies only the nonbinding Worker and Task-Keeper nomination and later her
own-seat intent. Thulia supplies only the nonbinding Ledger-Keeper nomination
and later her own-seat intent. Neither selects, binds, replaces, or inherits
the other side's seat or grant. The controller freezes one complete offer,
matches the two immutable own-seat intents, and atomically binds all three or
none. Binding is inert; a separately revalidated dispatch starts the jobs.

The purpose lineage remains:

`Christopher's goal -> Hearthline objective -> Thulia objective -> Triad jobs`

That lineage communicates purpose only. Every grant is independently narrowed.
All member results seal separately, validate separately, and return to Thulia;
Thulia prepares the bounded relay to Hearthline. Gloss remains deterministic,
stateless, heartbeat-free, and ledger-free. Only Thulia applies Systemic
Friction.

## Work present in this snapshot

- Expanded, fully fictional story: `lore/THE_NIGHT_THE_GARDEN_CLICKED.md`.
- Candidate Task-Triad design: `docs/HEARTHLINE_TASK_TRIADS.md`.
- Candidate HLP-000010 change record and v0.6-draft agent propagation.
- Cross-document updates for Thulia, Gloss, Sparks, Homecoming, TETHER,
  Ordered Lineage, Static, Firesides, and Creatures.
- Expanded repository validators. The candidate manifest is intentionally
  still stale at this checkpoint and full validation has not been claimed.

## Known unresolved audit findings

Resume from these findings before updating the candidate manifest or claiming
the candidate clean:

1. Reconcile when member candidate-bundle identities become reserved. Task
   Triads and agent prose place reservation before offer freeze; some TETHER
   schema currently leaves the reference unset until `TRIAD_BOUND`.
2. Make Ordered Lineage suspension/reopening requirements stage-conditional so
   requested, pending, offered, bound-undispatched, and dispatched states do not
   require records that cannot yet exist.
3. State explicitly in Ordered Lineage that `TRIAD_BOUND` is inert until a
   separate controller dispatch receipt.
4. Separate the always-required same-identity query route from the conditional
   retained-body seal route in Ordered Lineage; preserve “digest **or**
   validation rule,” and add the exact Owl query route.
5. Require `triad_relay_envelope_ref` once Relay-Envelope axes are set.
6. Require both controller-observed `SEALED` and separately `VALID` before any
   custody continuation; explicitly bar `VALIDITY_UNKNOWN` as well as
   `INVALID`.
7. Normalize the story's exact Owl disposition token from `COMPLETE` to
   `CANDIDATE_COMPLETE`, or declare a display alias without collapsing status.
8. Reconcile Homecoming's two legitimate `RETURN_ONLY` entrances: live
   cancellation/revocation/staleness, and exact-no-append same-body/same-ID
   candidate sealing after `EXECUTION_UNKNOWN`.
9. Resolve old-epoch terminal return authority. The likely design is to keep
   the old task authority stale while requiring a separate current
   terminal-return/custody grant to move an already sealed valid bundle,
   without rebinding or reviving it. Encode the exact reference in TETHER and
   align all prose.
10. Finish the remaining `RETURN_PENDING_THULIA` wording and tests so only a
    `SEALED` plus `VALID` bundle can enter that custody state.
11. Refresh validator literals only after the documents stabilize, then update
    `candidate_manifest.json` to `0.6-draft` and the final normalized policy
    digest.

## Resume sequence

1. Inspect this checkpoint commit and working branch before editing.
2. Resolve the audit findings above with `apply_patch`.
3. Ask the adversarial scan to check the final snapshot again.
4. Run diff, schema, link, README-bound, fictionalization, certificate, and
   all repository validators.
5. Update the candidate manifest only after every content edit is complete.
6. Commit the reviewed candidate successor, publish its branch, and report it
   as pending steward review rather than adopted.

