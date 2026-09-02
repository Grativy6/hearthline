# Hearthline Static

> **A shorter signal with its path home intact.**

| Field | Value |
|---|---|
| Version | `0.2` |
| Status | Adopted lore and design vocabulary |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Hearthline Static** is local, versioned, reversible shorthand that Hearthline may develop with one Hearthline Spark through repeated work. It shortens recurring patterns, distinctions, routines, and receipt structures without letting convenience quietly become a different meaning.

A bit of Static without its record is only noise.

Static is an additive layer over separately preserved sources. It is not a source, an independent witness, a shared memory, or authority.

## One Spark, one isolated ledger lineage

Each Spark's work lineage has its own Static ledger. Hearthline does not pool, merge, or silently carry Static from one Spark to another.

A Static expression is meaningful only with the exact Spark ledger, entry, version, and scope recorded for it. The same expression in two ledgers does not imply the same meaning. Sharing a role, job name, model, or task type does not join the ledgers.

A handoff between Sparks must first decode the relevant Static inside the sending ledger, expand it into ordinary language or an explicit structured meaning, and bind that expansion to its source records. The receiving Spark may then earn its own local Static entry from the expanded material. It does not import the sending Spark's shorthand, grammar, or codebook as controlling vocabulary.

Reopening recorded work may continue that Spark's ledger only when its exact ledger identity and authorized continuation are re-established. Creating a new Spark begins a new ledger. A refresh appends a successor version inside the same established lineage; it never replaces or silently restarts that ledger.

## Ordered Static identity

[Hearthline Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) governs Static numbering. Every Spark receives an ordered Spark identity, and every proposed Static version receives the next strictly increasing version number in that Spark's Static series before the proposal is authored.

Every grammar, codebook, decoder, entry, activation, Field Notes page, and revision remains bound to its own typed identity and predecessor. Issued numbers are never reused, reassigned, renumbered, rolled back, or overwritten. Rejected, failed, superseded, and abandoned versions keep their numbers and dispositions.

Proposal order and activation order are separate. The highest-numbered proposal is not automatically current. A separately numbered activation receipt chooses one exact verified version under the current grant and expected predecessor. Concurrent allocation must serialize or fail closed, and restoration never moves a counter backward.

Earlier expressions remain bound to their original Static versions and decoders. Required privacy removal may replace prohibited bytes with an accountable tombstone where lawful, but the ordinal is not silently reassigned.

## The preserved layers

Static keeps three layers distinct:

| Layer | What it carries |
|---|---|
| **Source evidence** | The separately retained raw artifacts, observations, and receipts, with their own identities and custody |
| **Static ledger** | Compact entries and deltas interpreted by one Spark-local, versioned grammar and codebook |
| **Residual lane** | Any distinction the current grammar cannot carry exactly, kept explicit and uncompressed until a later extension earns it |

Static never replaces source evidence. Its exact round trip targets the declared canonical ledger entry—not every byte of every referenced source. The source layer remains separately preserved so the reasoning can be reopened beyond what the working entry states.

A hash can identify expected bytes, but it cannot preserve or recover missing bytes by itself.

## Admission rule: exact or not Static

A proposed shorthand becomes Static only when decoding it under the exact bound grammar, codebook, decoder, and parameters reproduces the declared canonical entry exactly.

Formally, for canonical entry $e$, encoder $C_v$, decoder $D_v$, and pinned parameters $p_v$:

$$
D_v(C_v(e; p_v); p_v) = e
$$

The equality is byte-for-byte over the declared canonical form. If normalization occurs before encoding, the claim applies only to that named canonical form, not to the original source bytes.

A failed, missing, or uncertain round trip is not admitted as Static. It remains an uncompressed residual, a proposal, or an explicitly labeled source-backed or lossy view. Retrieval from a preserved source is not decompression, and a lossy summary cannot reconstruct what it omitted.

## What every Static record carries

At minimum, a Static record binds:

- its Static entry ID, ordered Spark identity, named series, and ledger identity;
- its version ordinal, predecessor ordinal, activation state, and any superseded entry;
- the exact compact bytes and their digest;
- the exact canonical entry bytes and their digest;
- its declared meaning, task, scope, and validity conditions;
- source references, source digests, and source-availability state;
- the complete grammar, symbol definitions, codebook, decoder artifact, parameters, and normalization rules needed to interpret it, each with a version and identity;
- retained distinctions and references to any uncompressed residuals;
- its round-trip verification receipt and result; and
- relevant producer, model, tool, and time identities when they affect reproducibility.

The recorded “compression formula” must be sufficient to interpret the exact entry it governs. A formula name, prompt, model ID, or hash alone is not a decoder. Rerunning a model or prompt is not assumed to reproduce the same codebook or output, so the actual emitted artifacts must be retained.

## Decoder and change track

A future Static implementation should expose two ledger-scoped, human-reviewable views:

- a **decoder and expander** that resolves an entry to its exact canonical form, recorded meaning, source path, residuals, and governing grammar; and
- an append-only **change track** that lists every grammar, symbol, codebook, and entry version with its predecessor, supersession link, and reason for change.

Later revisions cannot reinterpret earlier entries. An old entry is always decoded with the exact artifacts it originally bound.

There is no global Static decoder or shared dictionary across Sparks. Every lookup names one Spark ledger and one version.

## Nothing is silently overwritten

Each new expression adds a record. Each correction, refinement, or grammar extension adds a new version linked to its predecessor and states what it supersedes. Earlier bytes and meanings remain historical rather than being rewritten to agree with the newest version.

Where retention is authorized and lawful, source and decoder artifacts remain available at stable or content-addressed locations.

Required deletion, privacy removal, or redaction must not be defeated in the name of provenance. The ledger records a tombstone or availability change without retaining prohibited content, invalidates dependent uses where necessary, and narrows any claim that can no longer be checked.

## How Static earns meaning

A recurring pattern may earn a local Static distinction only after the ledger records the criterion that makes its instances equivalent for the declared task.

Similar receipts may be grouped under one earned distinction, but the group and its members remain different counts. The group receives its own identity and membership rule; every included receipt remains individually addressable. Compression does not turn many observations into one observation or one lineage into independent corroboration.

Static has a compression floor: a difference that could change action, authority, uncertainty, source identity, permission, consequence, or reopening cannot simply disappear. It must remain explicit in the canonical entry or stay in the residual lane.

Vocabulary changes append new versions. A newer version may control later work within its declared scope, but it does not change what an older expression meant when it was recorded.

## Embers and Static proposals

Static remains shorthand rather than a general memory bucket. Broader things a Spark recommends carrying forward belong to that Spark's **Embers**, defined in [Hearthline Firesides](HEARTHLINE_FIRESIDES.md).

A proposed shorthand change begins as an Ember of type `static_delta` and also receives its reserved Static version number. It remains `PROPOSED_NOT_ADOPTED` until separately consulted, exactly reconstructed, admitted by the authorized ledger writer, and activated through its own receipt. Successful verification does not silently approve it, and use in one run does not carry it into another run.

## Fireside refresh

When Hearthline tends a Fireside, Static may be refreshed without erasing the notes that led to the change:

1. Pause at an exact committed Run Trail boundary.
2. Seal the active Field Notes page with its ordered identity, digest, completion state, coverage watermark, and exact governing Static version.
3. Consult only the authorized Scribe notes and Embers, recording what was taken up, deferred, declined, or left unresolved.
4. Decode any sending-Spark Static inside its own ledger and bind the expanded ordinary-language or structured meaning to its sources.
5. Test a proposed Static upgrade under the exact round-trip admission rule.
6. If the authorized ledger writer admits it, append it under its already allocated version number and add a separately numbered activation receipt. Do not alter its predecessor.
7. Open the next numbered blank Field Notes page under the active Static version, bound to the pause checkpoint and its sealed predecessor.
8. Load only explicitly selected material, append a load receipt, and resume within the unchanged remaining grant and limits.

The page becomes blank; the history does not. Unloaded Embers, residuals, unresolved obligations, declined advice, sealed notes, and reopening handles remain separately addressable.

A Static upgrade improves representation only. It cannot enlarge discretion, role, capability, permission, or authority. A predeclared adaptive-Static grant may permit a verified revision to be tried during the current run; carrying it into a later run remains a separate reviewed decision.

## Spark role boundaries

Static does not add capability to a Spark:

| Role | Static ceiling |
|---|---|
| **Seeker** | May receive brokered Static metadata already within its metadata aperture; cannot open definitions or sources and cannot write the ledger |
| **Explorer** | May inspect authorized Static records and sources read-only; cannot persist a new meaning or version |
| **Handler** | May create, revise, or tombstone Static records only within an explicit current grant naming that ledger and mutation |

A separate system may hold the ledger for a Seeker or Explorer, but association with a ledger never grants that Spark write access. Static also cannot create a grant, widen a role, convert evidence into authority, or make a handoff executable.

## Strongwiz boundary and design lineage

Static's record discipline is informed by the owner-directed **Kevin Speak v0.1 — Adaptive Reversible Ledger Shorthand** hypothesis in the [Strongwiz Calibration 001 result at inspected commit `13c0d4c`](https://github.com/Grativy6/strongwiz/blob/13c0d4c4adda284939d8b1fc9cd62ba3f3a4e8e6/docs/calibrations/001-result.md#kevin-speak-v01--adaptive-reversible-ledger-shorthand).

That Strongwiz proposal keeps raw evidence separately preserved, uses a run-local model-authored codebook, versions every grammar and revision, binds each entry to its decoder, requires exact round-trip reconstruction, and leaves anything the shorthand cannot carry in an uncompressed residual lane.

**Kevin Speak** remains Strongwiz's shorthand. **Static** is Hearthline's separate, Spark-local branch of the idea. Static adds a hard one-Spark/one-ledger boundary: its vocabulary, grammar, and codebook do not transfer directly between Sparks.

This is shared design provenance, not independent corroboration. The Strongwiz report labels Kevin Speak as a next-build hypothesis formed after Calibration 001; neither that report nor this document claims an implemented shorthand system or a retroactive explanation of the calibration result.

## Lore and implementation boundary

This document adopts Hearthline's name and intended record discipline for Static. It does not create a Static ledger, instantiate a Spark, implement a codec, preserve any operational source, activate Hearthline, or authorize work.

Any implementation must separately specify and test ledger isolation, ordered allocation, append behavior, proposal and activation separation, sealed-page refresh, carry-gate transitions, exact round trips, source custody, residual handling, privacy deletion, role enforcement, grants, failure behavior, export boundaries, and measured compression, latency, transport, and validation costs.

Hearthline, Sparks, Strongwiz, and their named roles are AI tools and system concepts, not persons, co-authors, or independent authorities. Static does not establish experiential memory, identity continuity, consciousness, consent, standing, ownership, or permission.
