# Science and mathematics capabilities

This module provides bounded, deterministic ordinary-software helpers for the
public Hearthline toolkit. Each call accepts one JSON-compatible object and
returns one JSON-compatible object with `status` and `effects: []`. It is a
capability surface, not a proof assistant, scientific instrument, or model
benchmark.

The observation contract requires a question, raw input, baseline, method,
aperture/window, calibration, and uncertainty before it reports a declared
contract check. Channels are typed as observed, interpretation, or simulation;
the status is structural evidence rather than a truth claim. It
keeps observation, interpretation, simulation, alternatives, and human review
distinct. It reports missing channels and declared detection limits without
inferring a unique cause. Finite endpoint/readout and side-trace repair preserve
residuals; side-trace repair explicitly does not claim answer or full-object
recovery. APCI is represented only as a protected-query collision witness:
equal retained packets with different protected answers require a side trace;
missing evidence is insufficient and no universal scalar cost is claimed.

The exact arithmetic helpers use bounded `Fraction` values for GOLD channels and
GPPR factor/exponent events. GOLD reconstructs six channels from their mean and
six zero-sum differences (five independent, sixth determined), and validates an
eight-vertex, twelve-edge cube under the Eisenstein projection
`(x1-x3, x2-x3)`. Only `000` and `111` collide; the central repair bit retains
which preimage was present. Optional endpoint-compatible paths report the
exact signed area difference for closed piecewise-linear paths with shared
endpoints; this is the finite polygonal realization of the second-level
signature area. Sector/residual data remains separately visible.
GOLD's bounded turn record uses an integer inequality check for the exact symbolic
`beta=(3-sqrt(5))/2`, `K=floor(6n beta+1/2)`, `j=K mod 6`, and epsilon turns.
GPPR validates declared natural prime valuations (it never factors an arbitrary
target), product consistency, ordered event ribbons, multiplicity, an integrity
chain, and symbolic `zeta^j` endpoint terms using a bounded prime registry. Its
arithmetic status is `FINITE_ARITHMETIC_CHECKED`: a bounded check of supplied
factors, not a claim about an external certificate. Its enclosure router requires
a named partition, precision, source endpoint, and two-dimensional rectangular
enclosures. Only enclosures wholly inside one declared partition cell route;
the result is `ROUTED_UNDER_SUPPLIED_ENCLOSURE`, and a supplied hash or boolean
is never called a verified certificate. Boundary, cross-cell, endpoint-mismatch,
and malformed cases remain unresolved and use fallback.

## Tool register

| Name | Purpose |
|---|---|
| `science.observation_contract` | Required observation/interpretation/simulation channels |
| `science.compare_prerequisites` | Added, removed, and common finite prerequisites |
| `science.detection_limit` | Declared value versus declared finite limit |
| `science.simulation_vs_observation` | Preserve data kind; no causal claim |
| `science.residual_alternatives` | Carry alternatives and missing discriminators |
| `math.finite_endpoint` | Validate bounded exact-rational endpoint and side trace |
| `math.readout_binding` | Bind a readout while retaining endpoint identity |
| `math.side_trace_repair` | Predecessor-backed side trace repair |
| `math.apci_cost` | Protected-query collision witness; no scalar cost |
| `math.bridge_repair` | Finite source/readout fibers and protected-answer repair |
| `math.gold_channels` | Exact common+five-difference channels and cube-fiber check |
| `math.gppr_factor_events` | Bounded factors, product, ordered events, integrity chain |
| `math.gppr_partition` | Versioned enclosure-in-cell routing with certificate fallback |

Every result is advisory evidence. These functions do not grant authority,
consent, standing, or permission, and do not classify harmfulness. Authority
and ethical review remain in the foundation adapter. FBT/C2C latent state
transfer, neural performance, and unfinished Hodge claims are intentionally
unsupported here; their reopening route is an explicitly bound model/runtime or
mathematical proof contract.

## Source boundary

The capability names and distinctions are mapped from the local workflow and
source inventory, including PAL v2.3, CHARTER, BRIDGE, GOLD, GPPR, APCI and
A0BK-related ordinary-software clauses. The exact published source, version,
locator, and license must be attached by the source-contract work before any
claim of conformance. This repository stores no private corpus or full paper
copy; use the source inventory and public links for attribution.
