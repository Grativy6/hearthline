# Software mechanisms

This public profile contains bounded mechanisms that preserve trace and expose
limits. It does not load Hearthline lore, select a model, grant permission, or
perform an external action.

`software.fbt` implements the finite boundary between mutable computation,
append-only trace, and constructor-bound operator policy. `TRACE_ONLY` records
events, `SHADOW` compares a proposal without applying it, and `GOVERNING`
requires an explicit policy reference and a finite allowlist of internal state
actions supplied when the engine is constructed. A model or request cannot
change the mode or write the authority record. Governing transitions can only
change the engine's bounded internal state; they cannot send, schedule,
authorize, or alter an external system.

Computation state is explicitly volatile: a successful durable trace append is
the commit point, the in-memory update follows it, and a new engine starts
with empty computation state while retaining the trace. A failed append leaves
the computation unchanged.

`software.a0bk` is an adapter for the proposed A0BK v0.10.0 PAL 2.2-oriented
grammar. It routes a named ROOT, APPEND, CHILD, VERSION, or SUCCESSOR operation
through the maintained foundation check when available and labels the result
as an adaptation to PAL 2.3. It does not duplicate PAL or claim blanket
conformance. The source version and residual lineage stay visible.

`software.p3la` composes finite typed edges. Each edge carries input and output
hashes, schema, domain, and disagreement state. Optional supplied values can
be checked against their hashes; otherwise hashes remain declared rather than
verified. Disagreement remains an alternative. With an explicit
`EXPLICIT_INTERSECTION` policy, compatible schemas and domains produce only the
finite intersection of supplied terminal output claims. No consensus is
inferred.

`software.carrier_contract` records the separate carrier, operator, write,
transport/effect, and readout fields from the One Carrier, Many Blocks
diagnostic direction. Matching shapes do not establish semantic equivalence.
`software.c2c_capability` reports whether a declared local host exposes the
model internals and KV-cache access needed for a real experiment. API-only
hosts are reported unavailable; local prerequisites are only
`PREREQUISITES_DECLARED_NOT_VERIFIED` until a learned bridge and compatible
experiment actually exist. Experiments are `NOT_RUN`, so no latency, fidelity,
compression, or reasoning claim is made.

All operations return `effects: []`, and all persisted FBT trace records use the
shared hash-chained store. The trace is an account of recorded operations; it
does not make the operation true or authorized.
