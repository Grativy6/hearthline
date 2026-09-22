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

## Source preservation and receiving-context applicability

Toolkit 0.2.0 adds `review_context_applicability`. Its reduced implementation
profile is drawn from MIND v0.4 section 8.7 and the composition described in
TIES v0.2. It checks **canonical content identity** separately from **declared
conditions of reuse**. It does not assess semantic fidelity or decide what a
claim means. This is one finite comparison mechanism, not an implementation
of the whole MIND framework or the TIES research program.

`read_context_sources` and `hearthline://context-sources` expose exact edition
references, raw-file hashes, source roles, and implementation limits. They do
not download source text, change the shared foundation registry, or adopt
new controlling instructions. Both new tools and the resource belong to the
optional `context` group; hosts selecting only foundation/core/continuity
receive neither. See [source roles](../SOURCE_MAP.md).

### A scoped preference

This runnable package example uses entirely synthetic evidence references:

```python
from hearthline_mcp.applicability import review_applicability
from hearthline_mcp.core import digest

content = {
    "claim": "Keep routine answers short.",
    "applicability_conditions": [{
        "condition_id": "routine-only",
        "field": "question_kind",
        "equals": "routine",
        "evidence_refs": ["synthetic-user:1"],
    }],
    "unresolved": [],
}
request = {
    "source": {
        "source_id": "preference:1", "version": "1",
        "expected_hash": digest(content), "supplied_content": content,
    },
    "target": {
        "context_id": "task:2",
        "facts": {"question_kind": {
            "value": "detailed derivation",
            "evidence_refs": ["synthetic-current-request:2"],
        }},
    },
    "reopen_handle": "tether:preference:1",
}
report = review_applicability(request)
assert report["source_preservation"]["status"] == "MATCH"
assert report["target_applicability"]["status"] == "MISMATCHED"
```

Over MCP, call `review_context_applicability` with `{"request": request}`.
An expected hash should normally come from the previously bound source. The
example computes it locally to illustrate the format; hashing a new caller
assertion does not authenticate that assertion or its provenance.

### Contract and limits

- The source requires `source_id` and `version` strings. Its content carries
  the claim, qualifiers, lineage, optional `unresolved` string list, and
  `applicability_conditions`. These are hashed together. Conditions supplied
  outside the content are rejected. A missing condition list is unresolved.
- Each condition declares a unique `condition_id`, a literal `field` name,
  an `equals` value and `evidence_refs`. The target declares `context_id` and
  a `facts` object whose fields contain `value` and `evidence_refs`. There are
  no expressions, dotted paths, coercions, inferred conditions, or live lookups.
- All conditions are conjunctive exact canonical-JSON comparisons. The
  canonical form is Python JSON with sorted keys, compact separators and UTF-8,
  using `ensure_ascii=False`; non-finite inputs are rejected. `true`, `1` and
  `1.0` stay distinct. These content hashes differ from the **raw file byte**
  hashes in the published-source catalogue.
- Preservation is `MATCH`, `CHANGED`, `MISSING`, `UNVERIFIED` (no expected hash),
  or `STALE` (optional `expected_version` differs). ID/version labels and the
  expected digest remain caller declarations. Authenticity and semantic
  fidelity are explicitly `NOT_ASSESSED`.
- Applicability is `MATCHES_DECLARED_CONDITIONS`, `MISMATCHED`, or `UNRESOLVED`.
  Missing values or evidence references stay unresolved; a present JSON null
  is a supplied value. An unpreserved source cannot yield a match or mismatch.
  One evidenced mismatch is sufficient to fail the conjunction, while other
  unknown conditions remain individually visible. Source unresolveds prevent
  a positive result because this checker cannot establish their irrelevance.
- Evidence references are declarations, not fetched evidence. Duplicate
  references are listed once, never counted as votes. Independence, truth,
  relevance, and sufficiency of the chosen conditions remain unassessed.
- The review binds the exact supplied target and request by hashes and
  retains residuals and a required reopening handle. A later target needs a
  new review. Malformed, unsupported or over-budget inputs return
  `INVALID_INPUT`; limits are 100,000 UTF-8 bytes, depth 24, 10,000 nodes,
  and 256 conditions.
- Every outcome has no authority, execution, admission, or training effect.
  A matching grant-shaped fact cannot renew a grant or substitute for the
  existing current-grant check. A review does not write memory, select a
  model, update weights, or automatically reopen dependencies.

### Carry, correction and restart

Keep the original source and report together in an existing context item or
append-only observation, with its binding and recovery route. Compaction may
retain that item or explicitly omit it; a summary cannot silently replace
the source. Recover omitted material through the existing store/TETHER route,
verify its content, and review the **current** receiving context separately.

When new evidence warrants a correction, append its account with before/after
references. The existing dependency operation can reconsider adopted,
non-provisional, load-bearing dependents; unrelated or provisional edges do
not gain that status through the new review. Heartbeats still report bounded
state only. The review itself is read-only and does not mandate a new loop.

`tests/test_applicability_route.py` exercises this route through three real
MCP processes with synthetic data: a matched preference is omitted during
compaction, recovered after restart, held unresolved for a missing receiving
condition, then found mismatched after a supplied correction. The original
history and the unresolved intermediate observation remain readable after
another restart. This verifies the transport and record boundaries, not an
improvement in model reasoning, semantic adequacy, or learning.
