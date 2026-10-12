# Thulia: partitioned custody and translation

**Technical contract:** Partitioned custody and source-bound translation between separately governed ledgers.

Editorial separation, 12 October 2026. The contract version below is retained; this edition removes character presentation without promoting the design to implemented behavior. The [complete predecessor](https://github.com/Grativy6/hearthline/blob/f5c69b912761f29e2c82f83d1fe412fc83ec873a/docs/HEARTHLINE_THULIA.md) remains addressable. Names denote optional interface vocabulary; users choose their own context.

| Field | Value |
|---|---|
| Version | `0.3` |
| Status | Adopted design vocabulary; implementation not asserted |
| Design identity | `OWL-000001` |
| Design profile | `OWL-000001/PROFILE-000003` |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Thulia**, the **Owl Scribe** custody interface, has two bounded design responsibilities: preserve the route by which one Spark's [Static](HEARTHLINE_STATIC.md) can be reconstructed for another without joining their ledgers, and preserve the separate representation-side return path for an authorized [Paired Spark dispatch](HEARTHLINE_HOMECOMING.md).

## v0.3 successor record

Version `0.3` adds Creature-manifest and linked-ledger custody to Thulia's design
profile. Profile `OWL-000001/PROFILE-000002` remains the historical Homecoming
integration record; `OWL-000001/PROFILE-000003` is its non-retroactive
successor. The successor does not make Thulia a controller, grant issuer,
arbiter, executor, promotion authority, or shared ledger writer.

The design keeps a registry (the roost) of separately partitioned Static lineages. She knows where each Spark's grammar, codebook, decoder, versions, residuals, and source bindings are recorded. When authorized communication between Sparks requires translation, she reconstructs the sending expression inside its own ledger and records a numbered **Bridge Gloss** in ordinary language or an explicit shared structure.

She does not create a universal Static, pool the ledgers, silently broadcast shorthand, dispatch or direct a worker under her own authority, or let one Spark's vocabulary govern another. She keeps the paths between languages and back to their Homes, not one language above them.

## The Owl Scribe boundary

**Owl Scribe** is a unique custodial job, not a fourth Spark role, not a Scribe lens, and not another decision maker at the Fireside. Thulia does not investigate the primary task, judge competing advice, decide what should be carried, approve a Static proposal, authorize a crossing, create a task grant, or choose actions for a Work Spark.

Her permitted work is limited to:

1. locating an exact Spark-local Static ledger and version through its recorded identity;
2. checking that the requested decoder, grammar, codebook, source bindings, and access grant are present;
3. reconstructing the named expression inside that sending ledger;
4. recording the reconstruction, sources, residuals, and declared destination as a numbered Bridge Gloss;
5. offering that gloss to the existing Fireside carry process as candidate material;
6. binding an authorized paired dispatch to the separately declared Work Spark and Ledger Scribe Spark identities, Homes, frozen Static references, Run Trail projection, and Spark Heartbeat Contracts;
7. returning each Scribe-authored target-bound Static proposal, negative constraint, and residual to the Scribe's exact source-local Perch named before dispatch; and
8. preparing and checking a candidate representation-side Homecoming payload for controller reconciliation without attesting durable arrival, task success, carry approval, Static activation, or context closure.

The ordinary carry gate still controls:

`PROPOSED != CONSULTED != CARRY_APPROVED != LOADED`

A Bridge Gloss does not skip a stage. It is not a decision, recommendation, permission, authorization, or receiving-Spark Static entry. The receiving Spark may earn new local shorthand from an explicitly loaded gloss only through its own admission and activation rules.

## The partitioned roost

Thulia's **roost** is a directory of isolated **Perches**. Each Perch belongs to exactly one Spark Static lineage and binds:

- its Perch identity and ordered version;
- the exact Spark, registry, Static ledger, and permitted audience;
- the available Static versions, entry ranges, and activation receipts;
- the exact decoders, grammars, codebooks, parameters, and digests needed for reconstruction;
- source and residual locations without pretending that an index contains their meaning;
- availability, redaction, retirement, and tombstone state; and
- every access and translation receipt required by the applicable grant.

Partitions are access boundaries, not folders of convenience. A request that can reach one Perch gains no implied access to another. Thulia may index a ledger without being permitted to open its contents, and a Seeker-visible Perch view contains metadata only.

The roost is therefore not shared memory. Shared infrastructure is not shared lineage. It is a partitioned registry and custody design for separately governed records.

## Hearth Perch and paired returns

The custody interface's declared Home is the **Hearth Perch**, a separate
return boundary for Owl Scribe work, not a shared Static ledger. It binds Thulia's exact profile, the coordinator permitted
to receive her return, the dispatch-pinned roost index and version, the records
she may deliver, and the failure or reopening route when a return cannot be
reconciled. The record routes custody; it does not grant or renew authority.

Every Spark-local Static Perch remains separate from the Hearth Perch. Thulia
may carry a Bridge Gloss, Home map, or representation-side return through her
bounded custody, but the material goes back to its named source Perch or onward
through an authorized destination-specific carry gate. She does not keep a
pooled extra copy at Home.

For an authorized paired dispatch, the authorized coordinator creates both
Spark grants and the paired dispatch. Thulia's
interface binds their separate identities, heartbeat and coverage boundaries,
separate frozen Static versions, Homes, and shared dispatch reference. Any
model-assisted work behind that interface still belongs to a declared Spark
role and grant. When
Thulia's own bounded custody work is model-assisted, that work has its own Spark
identity, task-shaped Spark Heartbeat Contract, and Hearth Perch Home; it does
not borrow either member of the pair's pulse or persistence budget.

The Work Spark returns the bounded task result and its unchanged Static to the
Work Spark's source Perch. The Ledger Scribe returns one typed representation
disposition to its own source Perch: `static_delta`, coverage-qualified
`NO_LEDGER_DELTA`, `LEDGER_DELTA_INCOMPLETE`, or
`LEDGER_COVERAGE_UNKNOWN`. Thulia prepares and checks neither one as the other's
result. She may route a permitted reconstruction of a target-bound Scribe Ember
through the direction-bound carry path to the target Perch's proposal intake,
unmatched distinctions to the Scribe's residual lane, and a proposed custody or
reconciliation payload to the Hearth Perch. Only the canonical controller or
store observes durable placement and appends Return, Reconciliation, and
Context-Close Receipts. She does not allocate a target Static version.
Admission and activation remain with the target ledger's authorized writer.

If a Work Spark comes home and its Ledger Scribe does not, the task and note
statuses remain separate. Unless a stricter condition was declared before
dispatch, the missing Scribe return prevents learned carry and Static promotion
rather than manufacturing a task failure or a complete ledger. If any return
is ambiguous, Thulia flags the unresolved return boundary in her candidate
payload; the canonical controller records the disposition and does not replay
it automatically.

## Numbered Bridge Glosses

[Hearthline Ordered Lineage](HEARTHLINE_ORDERED_LINEAGE.md) governs Thulia's identities. Readable examples include:

| Record | Example |
|---|---|
| Owl Scribe | `OWL-000001` |
| Owl profile version | `OWL-000001/PROFILE-000003` |
| Hearth Perch | `OWL-000001/HEARTH-PERCH-000001` |
| Hearth Perch version | `OWL-000001/HEARTH-PERCH-000001/VERSION-000001` |
| Perch | `OWL-000001/PERCH-000001` |
| Perch version | `OWL-000001/PERCH-000001/VERSION-000001` |
| Translation request | `OWL-000001/REQUEST-000001` |
| Bridge Gloss | `OWL-000001/GLOSS-000001` |
| Bridge Gloss revision | `OWL-000001/GLOSS-000001/REVISION-000001` |
| Gloss delivery receipt | `OWL-000001/GLOSS-000001/DELIVERY-000001` |

Every Bridge Gloss binds at least:

- its ordered identity, status, predecessor or revision, and content digest;
- the exact sending Spark, Static ledger, version, entry, and expression bytes;
- the decoder, grammar, codebook, parameters, and reconstruction result used;
- source references, claim status, uncertainty, residuals, and declared omissions;
- the exact receiving Spark or other declared audience and the purpose of the request;
- the requesting grant and the access projection actually used; and
- any later consultation, carry, load, rejection, invalidation, or supersession receipts.

Every request and delivery is direction-bound. A gloss from Spark A to Spark B does not authorize or imply the reverse crossing, delivery to Spark C, or access to either ledger beyond the recorded projection.

A gloss number is allocated before the attempt. Failed, ambiguous, denied, interrupted, invalidated, and superseded glosses keep their numbers and dispositions. Corrections append numbered revisions; they do not overwrite the earlier gloss.

## Translation sequence

1. A coordinator submits a bounded request naming the sending expression, sending and receiving identities, purpose, audience, and grant.
2. Thulia resolves only the named Perch and verifies the exact Static version and reconstruction materials.
3. She decodes the expression inside the sending Spark's ledger. She does not infer a convenient meaning from the compact expression alone.
4. She records an exact ordinary-language or explicitly structured reconstruction with sources, uncertainty, residuals, and omissions.
5. The coordinator appends the numbered Bridge Gloss and offers it as candidate carry to the named destination.
6. The existing carry gate records whether the gloss was consulted, approved for bounded carry, and actually loaded.
7. If the receiving Spark later proposes local Static from it, that proposal receives a new identity in the receiving Spark's ledger and passes the ordinary Static admission rule.

No codebook crosses merely because a gloss does. The source Static remains source-local, and the destination Static remains destination-local.

## Creature-manifest custody

Within a [Hearthline Creature](HEARTHLINE_CREATURES.md), Thulia may custody the
content-addressed composition manifest and the partition map that relates each
Spark, pair, Home, Perch, ledger, heartbeat contract, budget, source registry,
and return route. Custody makes the topology inspectable; it does not make the
manifest a grant or the partitions one memory.

At each permitted crossing, Thulia may report the manifest-bound status of
identity, witness, scope, trace, authority reference, consequence class,
resource state, and re-entry requirements. These are guard observations for the
canonical controller. Thulia does not decide the route, approve the grant,
debit a budget, choose among proposals, or issue the single permitted external
effect.

Comparative arms remain separate Creature manifests, roots, and ledgers. An
external campaign index may name both, but Thulia must not use it as a shared
payload channel. Cooperative Sparks inside one arm retain separate accounts and
write permissions; the canonical controller serializes any effect or promotion.

## Failure and reopening

Thulia fails closed when the source identity, active version, decoder, grammar, codebook, digest, source binding, destination, audience, disclosure intersection, or grant cannot be established. Ambiguity is carried as ambiguity; missing material is not silently completed from resemblance or model familiarity. A permitted lossy summary may be recorded as a separately labeled derivative, but it is not an exact Bridge Gloss.

If a source is later corrected, superseded, redacted, tombstoned, or made unavailable, affected glosses remain addressable but receive appended status changes and are no longer treated as silently current. Dependent receiving records keep their provenance and are reopened or narrowed as required.

Thulia never repairs a failed translation by merging ledgers. She returns to the exact unresolved boundary.

## Fireside use

At a [Hearthline Fireside](HEARTHLINE_FIRESIDES.md), Hearthline or an authorized coordinator may consult Thulia when a Scribe's Field Notes or Embers contain Static that another participant cannot interpret directly. Thulia supplies the Bridge Gloss; Hearthline decides whether to consult or carry it within the unchanged task grant.

At a [Homecoming](HEARTHLINE_HOMECOMING.md), Thulia may also prepare and check a
candidate representation-side return payload against the paired dispatch,
exact coverage watermark, Home Record, source Perch, and frozen Static version.
Only the canonical controller or store may reconcile and append its receipt.
Neither step decides whether the primary task succeeded or whether a candidate
Static revision should be carried or activated.

Thulia's output is derivative of the sending ledger and its sources. It is not another witness, another vote, or independent corroboration.

## Design and implementation boundary

This document adopts Thulia, Owl Scribe, Perch, roost, Bridge Gloss, Hearth Perch, Creature-manifest custody, and representation-side Homecoming custody as Hearthline design vocabulary. `OWL-000001` and `OWL-000001/PROFILE-000003` are design identifiers; they are not evidence of an operational allocation, running service, model process, credential, memory store, or deployment.

Any implementation must separately specify and test partition isolation, exact
reconstruction, least-privilege projection, audience binding, paired-identity
and Home binding, separate frozen Static references, independent task and Scribe
status, coverage-qualified ledger dispositions, Spark Heartbeat Contract
ceilings, Scribe-source-Perch return, target-bound proposal routing, Hearth Perch
isolation, idempotent Homecoming, unknown-return reconciliation, single-writer
numbering, carry-gate enforcement, cross-Spark import rejection, access
revocation, invalidation propagation, crash recovery, lawful redaction, and
  failure on unresolved identity or decoder state, Creature partition checks,
  physically separate comparison arms, guard-status reporting without
  arbitration, and rejection of Thulia as an authority or effect writer.

The interface name and example identifiers do not establish an operational allocation, independent witness, permission or authority.
