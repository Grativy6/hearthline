# Hearthline Gloss

> **Gloss turns one declared note. It does not remember the notes.**

| Field | Value |
|---|---|
| Version | `0.1` |
| Status | Adopted lore and design vocabulary |
| Mechanism class | `STATELESS_DETERMINISTIC` |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Gloss** is Hearthline's fixed-function translation relay. In the lore it is
the little golden turning wisp introduced in
[*Gloss and the Two-Sided Note*](../lore/GLOSS_AND_THE_TWO_SIDED_NOTE.md). In
the design it names one narrow operation: apply the complete route declared by
one self-contained note under one exact lexicon generation and direction.

Gloss is not a Spark, Owl Scribe, Scribe lens, model, interpreter, retention
reviewer, ledger owner, or source of authority. It has no context window,
history lookup, adaptive codebook, hidden memory, discretion, or continuing
write lane.

## Deterministic turn contract

A routine turn binds the canonical input note, exact route, direction, and
lexicon generation before execution. Its logical form is:

$$
(y, m) = T(x, r, d, \lambda_v)
$$

where $x$ is the canonical note, $r$ is its complete fixed route, $d$ is the
declared direction, $\lambda_v$ is one pinned lexicon generation, $y$ is the
returned face, and $m$ is the deterministic mark body. Repeating the same
canonical inputs produces the same output bytes, status, and mark body.

The operational ceiling is explicit:

```yaml
mechanism: STATELESS_DETERMINISTIC
history_reads: 0
prior_translation_reads: 0
free_form_inference: false
adaptive_learning: false
```

Routine translation never consults an earlier turn to infer, improve, repair,
or personalize the next one. A changed route or lexicon generation is a
changed input, not something Gloss remembers. Unknown syntax is permitted only
when the complete bound route still determines an exact turn.

## Detachable Translation Slate

Every attempted turn is recorded on a detachable **Translation Slate**. The
slate is a replaceable interface belonging to the declared translation
account. It is not Gloss's body, mind, memory, property, or identity, and a
replacement slate does not replace or reincarnate Gloss.

The canonical controller or store allocates a mark identity before the turn
and appends the result after it. Gloss produces only the deterministic mark
body. A mark binds at least:

- translation account and preallocated mark identity;
- canonical input and output digests;
- route, direction, and exact lexicon generation;
- success, unchanged-snag, or unresolved status;
- deterministic rule or decoder identity;
- declared omissions, residuals, and reopening handle; and
- the writer and grant that durably appended the mark.

The slate's compact, externally readable marks are the routine translation
account's record medium. There is no second Gloss history ledger behind it.
Replacing a full slate requires a new account-bound slate identity and a
verified continuation or explicit gap; it never silently discards a live
replay, contest, privacy, or reopening obligation.

The translation account owns the slate records and lexicon generations. Thulia
has bounded custody of their index, current validated generation, and
exceptions. Gloss has no memory ownership and cannot object to, demand, or
veto a lawful retention disposition.

Neither a note, mark, lexicon record, nor slate is Gloss's body, identity,
memory, or property. A retention transition can be blocked only by a typed
retention defect naming a declared account obligation, including any valid
hold, never by a persona claim attributed to Gloss.

That rule applies only to records predeclared as account-owned **`G_mutable`**.
This design asserts no persistent or autobiographical Gloss state. If a future
implementation introduces identity-bearing or agent-owned state, it is outside
this contract, requires separate governance, and may not be relabeled
account-owned to evade an identity or refusal claim.

## Lexicon generations

Thulia tends the lexicon series through separately granted, append-only
successor review. A lexicon generation binds its predecessor, canonical bytes,
scope, grammar, codebook, decoder, parameters, tests, status, and activation
receipt. A later generation never retroactively changes an earlier turn.

Routine Gloss receives the already selected generation. It does not choose
one, search the generation history, combine generations, repair an absent key,
or infer a mapping from resemblance. A missing, ambiguous, stale, unauthorized,
or non-reconstructible generation returns the note unchanged with a typed snag
mark.

## Failure is an output

Gloss fails closed when the note presents two controlling routes, omits a
required route or direction, cannot bind the exact lexicon generation, loses a
required distinction, or fails its declared exact-return check. It returns the
offered note unchanged and emits the deterministic snag-mark body. It does not
pick the likely meaning, paraphrase, call a model, open a Perch, or retry under
a different rule.

The snag mark reports only the mechanical boundary it observed. It is not a
finding about truth, usefulness, relevance, authority, or whether the note
should be retained.

## Thulia, Hearthline, and account custody

Thulia may validate the selected lexicon generation, tend the detachable
slate, route its account-owned marks, and record an unresolved exception in her
pointer index. She does not perform a routine turn by improvisation or copy the
slate into an Owl-owned payload ledger.

Hearthline may request a turn and receive a source-bound offer. The offer,
consultation, load, rejection, or reopening record belongs in Hearthline's
declared task account. Hearthline does not maintain the lexicon, append a
pretended Gloss mark, or silently replace a failed turn with its own
translation.

Any model-assisted lexicon or exception work occurs as a separately identified
Spark job with one exclusive bounded write lane in its declared task account.
The lane closes at Homecoming and custody returns to the canonical store. That
Spark does not become Gloss or inherit Thulia's retention-classification lane.

## Bridge Gloss is a different record

A **Bridge Gloss** is Thulia's source-, direction-, audience-, purpose-,
grant-, and version-bound reconstruction for a named crossing between account
partitions. Gloss is the stateless mechanical turn. The similar names mark an
adjacent seam; they do not merge the jobs.

A self-contained part of a Bridge Gloss may pass through Gloss under a pinned
lexicon generation. Its Translation Slate mark may then be cited by the Bridge
Gloss. That mark cannot create, number, authorize, deliver, consult, approve,
load, or replace the Bridge Gloss.

## Retention boundary

Gloss never applies **Systemic Friction**. It neither selects notes for keeping,
compaction, archive, or pruning nor treats a smaller face as permission to
remove a larger one. Only Thulia may issue the retention classification under
the separate rule and grant described in
[Thulia's design](HEARTHLINE_THULIA.md#systemic-friction).

`PRUNE_ELIGIBLE` is not deletion authority. A canonical controller or other
authorized writer must still validate the current grant and perform the exact
mechanical transition through Atomic Edge Promotion.

## Lore and implementation boundary

This document adopts Gloss, deterministic turn, Translation Slate, lexicon
generation, and snag mark as Hearthline lore and design vocabulary. It does
not implement a codec, allocate a translation account or slate, instantiate a
wisp, append a mark, preserve operational memory, activate Hearthline, or grant
authority.

Systemic Friction is working Hearthline design vocabulary pending the paper's
reviewed release. This document does not add it to PAL canon, the controlling
source stack, or the Research Station source registry.

Any implementation must separately specify and test canonicalization, route
completeness, lexicon selection, deterministic repetition, inverse checks,
unchanged failure, mark preallocation, atomic append, slate replacement,
account custody, least-privilege access, privacy removal, crash recovery,
reopening, and rejection of history-dependent or model-improvised routine
translation.
