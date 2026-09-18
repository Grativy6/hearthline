# Context and transport contracts

The public context layer records bounded context decisions and re-entry
materials. It does not retrieve a source, expose hidden model state, execute a
program, establish truth, or renew permission.

`orient` accepts the working profiles `mathematical`, `scientific`,
`philosophical`, and `game`. It returns a provisional orientation with
disjoint sets for `supplied`, `selected`, `available_unread`, `inferred`,
`omitted_for_budget`, `unavailable`, and `corrected` material. An unknown
profile or an item appearing in two material-state sets is invalid. `selected`
is an orthogonal load decision and may name supplied material. An orientation
with a purpose but no purpose-specific profile is explicitly `UNFORCED`.
Optional actionable
guidance is short data attached to that orientation; it is not a corpus dump
or an instruction authority. Optional source bindings carry source ID, version,
and content hash; selected sources must be bound when bindings are supplied.

`source_status` computes the digest of supplied content itself. Caller-provided
`observed_hash` and state labels are retained nowhere as verification. Missing
content is `MISSING`; a hash mismatch is `CHANGED`; a version or fingerprint
mismatch is `STALE`; only matching supplied content is `AVAILABLE`.

`transport_capsule` binds a program, cursor, schedule, dependency versions,
comparator identity, finite budget, and linked receipt chain. It returns no
execution effect. A changed comparator, dependency set, schedule, budget, or
receipt chain relative to a prior capsule is `REASSESSMENT_REQUIRED` and keeps
the prior capsule hash visible. Receipt-link and canonical-hash errors are
invalid. A valid capsule is a bounded restart record, not proof of semantic
equivalence or permission.
