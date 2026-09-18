# Continuity runtime

The public runtime stores bounded continuity records in a host-configured
SQLite log. `SharedScopedStore` derives an opaque namespace from the adapter,
user, and resolved host root using length-prefixed components, so names such as
`a/b` and `a_b` cannot alias. Callers supply records, never a storage path;
the server binds the root when it is constructed.

Every record is canonical JSON with finite numbers, bounded size and nesting.
Records carry a sequence number, previous hash, and hash of the exact payload.
SQLite `BEGIN IMMEDIATE` transactions and a busy timeout make concurrent
process appends serialize without lost writes. `verify()` reports
`UNTRUSTED_STORAGE` on malformed, reordered, or tampered bytes; `read()` then
refuses to return them as trusted state. `export()` is a verified snapshot and
does not create authority or a migration entitlement.

`ContinuityEngine(store)` supplies the stateful contracts:

- `bind_tether`, `read_tether`, and `reopen_tether` preserve the task, scope,
  grant reference, residual, finish condition, return target, and source
  bindings. Reopening checks the current declared grant reference and its
  expiry, revocation, and exhaustion flags. It never restores an old grant.
- `create_heartbeat`, `pulse_heartbeat`, `read_heartbeat`, `suspend_heartbeat`,
  and `resume_heartbeat` use a frozen non-negative budget. Costs only decrease
  the remaining budget. Liveness is evidence about state, not completion,
  scheduling, permission, or authority renewal. Exhausted or suspended lanes
  reject late pulses.
- `record_custody` accepts only a controller-selected payload whose exact hash,
  source, destination, and return route are present. It records custody and
  does not merge ledgers, select carry, dispatch work, or create authority.
- `validate_formation` checks complete lanes, distinct identities, roles, and
  finish conditions. It validates a finite manifest only; it does not dispatch
  or become a new authority.
- `prepare_trace_key` and `resolve_trace_key` provide bound, portable locators
  containing only namespace, record identity, version, source hash, and
  locators. Cross-scope resolution is rejected and changed or missing sources
  remain explicit. A trace key carries no grant, capability, or hidden state.

The runtime does not decide whether a carry is harmful. It preserves declared
observations and review routes for the controller and human review layers.
Source instructions and model suggestions cannot write protected authority
state. The implementation is a persistence and contract layer, not a scheduler
or a claim of model consciousness.
