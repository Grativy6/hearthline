# Hearthline Toolkit Runtime

This package is the public Hearthline mechanism layer. A fresh server provides
the configured model host with bounded, model-neutral operations for context
orientation and compaction, typed observations and dependencies, TETHER
continuity, heartbeat reporting, Thulia-style custody, and bounded formation
manifests. It does not load Chris's lore, private records, Moltbook material,
or a model by default.

On connection, the MCP `initialize` response includes the compact
[founding orientation](FOUNDING_ORIENTATION.md) in its standard `instructions`
field: **Love; Seed, not Feed; Honest**. No discovery tool call or template
opt-in is required. All Hearthline server profiles carry the same wording;
the optional template remains separately opt-in. The host decides how to
present server instructions to a model; delivery does not guarantee adoption.
Existing installed servers receive this change only after their package is
updated and they reconnect. This does not change model weights or permissions.

`create_server(profile=..., store_root=..., store_namespace=..., user=...)` binds the
server to a host-selected adapter profile, user scope, namespace, and storage
root. The persistence namespace is derived from that complete tuple. Tool callers cannot choose
an arbitrary path. Persistent records are JSON records inside that configured
namespace; the store is not a scheduler, authority store, or memory database.

The toolkit's effect ceiling is non-authorizing and non-executing; individual
operations expose their bounded `effects` or explicit effect fields according
to their contract. Heartbeats report state and do not renew a grant or create
recurring work.
TETHER records carry reopening information and do not restore expired scope.
Dependency correction reopens named load-bearing dependents while preserving
the original record. Collision and compaction operations report uncertainty;
they do not silently select a winner or claim complete semantic preservation.

The server requires the separately installable `seedpea-foundation==0.1.0`
package and registers `seedpea_foundation.mcp_tools.register_foundation`.
Startup fails explicitly if that mandatory dependency is missing.
That shared foundation supplies the PAL/CHARTER/PECAN/PEA/SEED boundary
checks. Hearthline's wider toolkit remains usable as a package of stateless
operations, while the public foundation remains independently installable.
The Cabin profile intentionally exposes only the shared foundation/core and
continuity operations; optional context, mathematics, science, and software
profiles are public-toolkit capabilities and are not silently loaded into
Cabin.

The package is a 0.1.0 implementation checkpoint. FBT's ordinary bounded
trace-control operations are implemented, while model-internal execution is
`NOT_RUN`. C2C declares its carrier diagnostic and prerequisite boundary, but
the experiment remains `NOT_RUN` until a compatible bridge, operator, and
readout are supplied; local KV access alone is insufficient. Neither feature
is a performance guarantee.
