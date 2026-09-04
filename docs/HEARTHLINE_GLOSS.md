# Hearthline Gloss

> **Gloss turns one declared note. It does not remember the notes.**

| Field | Value |
|---|---|
| Version | `0.3` |
| Status | Candidate design successor — pending steward review |
| Adoption effect | None |
| Mechanism class | `STATELESS_DETERMINISTIC` |
| Implementation | Not asserted by this document |
| Author and steward | Christopher D. Pang |

**Gloss** is Hearthline's fixed-function translation transform. In the lore it is
the little golden turning wisp introduced in
[*Gloss and the Two-Sided Note*](../lore/GLOSS_AND_THE_TWO_SIDED_NOTE.md). In
the design it names one narrow operation: apply the complete route declared by
one self-contained note under one exact lexicon generation and direction.

Gloss is not a Spark, Owl Scribe, Scribe lens, model, interpreter, retention
reviewer, ledger owner, or source of authority. It has no context window,
history lookup, adaptive codebook, hidden memory, discretion, or continuing
write lane.

## v0.3 Translation-Board candidate successor

Version `0.3` preserves version `0.2`'s atomic-turn and no-heartbeat boundary
while moving every note, serviceability decision, deterministic result, and
relay receipt onto an external task-scoped Translation Board with
writer-separated lanes. Version `0.2` remains preserved candidate ancestry;
this successor is a candidate pending steward review.

Gloss does not receive a Spark identity, Task-Keeper, Ledger-Keeper, Heartbeat
Contract, Pulse Receipt, Home, Homecoming, liveness state, or private ledger.
There is no continuing Gloss task to keep alive between turns. One turn is a
pinned transaction performed against a task-scoped external Translation Board;
the transaction either acquires an externally committed disposition, enters an
exact no-commit recovery or terminal state, or remains honestly unknown.

For each proposed turn, `gloss_readiness_state` is unset before the controller
checks the turn, then `READY_FOR_EXACT_TURN`, `NOT_READY`, or
`READINESS_UNKNOWN`. Readiness is derived only from the exact currently pinned
request, lexicon generation, route, grants, epochs, and required Board lanes.
It opens one atomic attempt; it is not a heartbeat, persistent availability,
inherited liveness, or promise that a later turn will be ready. Gloss neither
maintains nor observes this state.

Before execution, the canonical controller or store preallocates one mark and
pins its transaction key, task-scoped Translation Board, exact Thulia-to-Gloss
request-lane receipt, canonical input bytes and digest, complete route,
direction, lexicon-generation identity and digest, writer grant,
`objective_epoch`, `authority_bundle_ref`, and aggregate `authority_epoch`.
Only `READY_FOR_EXACT_TURN` may enter execution. Gloss receives those fixed
inputs and produces the deterministic output and rule-trace body. The store
then performs one compare-and-append in the Board's dedicated Gloss-output lane
under the preallocated mark identity. Gloss neither allocates the mark nor
observes durable placement.

A transaction has one externally recorded state:

| Transaction state | Meaning |
|---|---|
| `PREALLOCATED` | The exact turn identity and inputs are pinned; no output commit is yet attested |
| `COMMITTED_SUCCESS` | The exact success body was durably appended once |
| `COMMITTED_SNAG` | The exact deterministic unchanged-note snag body was durably appended once |
| `OUTCOME_UNKNOWN` | Timeout, crash, store ambiguity, or an unobserved acknowledgement prevents a truthful claim about whether the body committed |
| `SAME_TURN_RETRY_ONLY` | An exact query proved that no body committed while the complete original inputs, grants, and epochs remain current; only the same deterministic turn under the same identity may be attempted |
| `NOT_COMMITTED_TERMINAL` | An exact query proved that no body committed and the old turn may no longer act; any further translation requires a separately authorized successor |

These are controller-facing transaction states, not extra Gloss outputs. Only a
`COMMITTED_*` state attests that an outcome body reached the Gloss-output lane.
`PREALLOCATED` attests only the durable reservation, while
`OUTCOME_UNKNOWN` characterizes the controller's observation boundary. Any
control receipt remains translation-account infrastructure, not a second Gloss
history ledger.

`OUTCOME_UNKNOWN` carries a typed cause such as `TIMEOUT`, `CRASH`, or
`COMMIT_UNOBSERVED`. None means that Gloss is still alive, failed semantically,
or definitely did not execute. Recovery first queries the preallocated mark. If
the exact expected body is already present, the store returns that existing
commit. If an exact query proves no body is present and the complete original
inputs, pinned epochs, grant, and limits remain current, the controller records
`SAME_TURN_RETRY_ONLY`. That state permits only recomputing the same
deterministic body and compare-appending it under the same identity and
transaction key; it opens no choice of rule or fresh task. An identical
concurrent body is idempotent success; a different body under that identity is
an integrity fault. An unavailable read remains `OUTCOME_UNKNOWN`.

A retry never allocates a replacement mark to hide ambiguity and never selects
a newer lexicon, route, slate, grant, or epoch. If any pinned authority or
objective epoch is stale, the old transaction is not rebound or silently
completed under current state. When an exact query proves no body committed
and any pinned authority or objective epoch is stale, exact inputs are
unavailable, or another frozen limit forbids retry, the controller records
`NOT_COMMITTED_TERMINAL`. If the entire pinned turn remains current, the
query instead records `SAME_TURN_RETRY_ONLY` as described above. If the parent
purpose still authorizes more work after a terminal result, it may allocate a
separately identified successor turn under current authority. A
still-unresolved commit observation remains `OUTCOME_UNKNOWN`. Deterministic
same-turn retry is replay of one canonical transaction, not history-dependent
learning.

Only an independently identified enclosing asynchronous, genuinely multistep
batch, lexicon-maintenance, or translation objective may receive a
[Task Triad](HEARTHLINE_TASK_TRIADS.md). Its identity and purpose must exist
independently of a Gloss turn. Its Worker may request translation routing only
through the exact Hearthline task intake and the separately authorized
Hearthline-to-Thulia handoff; only Thulia may invoke a `T_TO_GLOSS_TURN`. Its
Task-Keeper may compare the wrapper's frozen Task Line and Completion Contract,
and its Ledger-Keeper may preserve the admitted mark references and coverage.
The triad belongs to the enclosing objective. It does not belong to Gloss,
invoke Gloss directly, create Gloss liveness, read a hidden Gloss history, or
recursively give Gloss another trio.

Calling one atomic turn a “batch of one,” wrapper, relay job, or persistent
task solely to obtain a heartbeat, ledger, Homecoming, or history is invalid.
Schema validation rejects that disguise. Any wrapper heartbeat or account
belongs only to the independently justified enclosing task and never becomes
per-turn memory on or for Gloss.

## Deterministic turn contract

A routine turn binds the canonical input note, exact route, direction, and
lexicon generation before execution. Its logical form is:

$$
(y, m) = T(x, r, d, \lambda_v)
$$

where $x$ is the canonical note, $r$ is its complete fixed route, $d$ is the
declared direction, $\lambda_v$ is one pinned lexicon generation, $y$ is the
returned face, and $m$ is the deterministic mark body. Repeating the same
canonical inputs produces the same output bytes, transformation status, and
mark body. The external transaction may still be `OUTCOME_UNKNOWN`; pure
determinism cannot attest storage.

The operational ceiling is explicit:

```yaml
mechanism: STATELESS_DETERMINISTIC
history_reads: 0
prior_translation_reads: 0
free_form_inference: false
adaptive_learning: false
spark_identity: none
heartbeat_contract: none
liveness_state: none
homecoming: none
owned_ledger: none
readiness_owner: controller
readiness_scope: one_exact_turn
```

Routine translation never consults an earlier turn to infer, improve, repair,
or personalize the next one. A changed route or lexicon generation is a
changed input, not something Gloss remembers. `READY_FOR_EXACT_TURN` expires
with its pinned turn and cannot be carried forward as Gloss liveness. Unknown
syntax is permitted only when the complete bound route still determines an
exact turn.

## External Translation Board and detachable marks

Every attempted turn receives a preallocated identity for a detachable
**Translation Slate** mark on the task-scoped **Translation Board**. The Board
is an external account, not a surface belonging to Gloss. Only a
controller-observed `COMMITTED_SUCCESS` or `COMMITTED_SNAG` attests that a
result body reached the Gloss-output lane. The detachable mark medium is
replaceable; it is not Gloss's body, mind, memory, property, or identity.

The Board separates ownership and write authority:

| Lane | Writer or effect owner |
|---|---|
| Hearthline request | Hearthline under the current task grant |
| Thulia request relay | Thulia under the exact direction-bound relay grant |
| Gloss output and rule trace | Canonical store from the deterministic turn body |
| Thulia return relay | Thulia under the reverse direction-bound relay grant |
| Hearthline serviceability | Hearthline under the current task grant |

No mark in one lane manufactures a mark or receipt in another. In particular,
a deterministic output does not make shorthand serviceable, and a relay
receipt does not attest the output's semantic fitness.

The Board's `shorthand_service_state` is `CANDIDATE`, `SERVICEABLE`,
`NOT_SERVICEABLE`, `SERVICEABILITY_UNKNOWN`, or `RETIRED_AT_TASK_CLOSE`.
Only Hearthline authors the semantic assessment states. The controller may derive
`RETIRED_AT_TASK_CLOSE`
from the root-task close receipt, but cannot turn it into a new semantic
decision.

The canonical controller or store allocates a mark identity before the turn
and appends the result after it. Gloss produces only the deterministic mark
body. A mark binds at least:

- task-scoped Translation Board, Gloss-output lane, and preallocated mark identity;
- pinned transaction key, `objective_epoch`, and `authority_epoch`;
- canonical input and output digests;
- route, direction, and exact lexicon generation;
- the committed success or committed unchanged-snag body;
- deterministic rule or decoder identity;
- declared omissions, residuals, and reopening handle; and
- retry and idempotency references, if any; and
- the writer, grant, and store receipt that durably appended the mark when a
  commit is actually observed.

The separate controller transaction record carries `PREALLOCATED`,
`COMMITTED_SUCCESS`, `COMMITTED_SNAG`, `OUTCOME_UNKNOWN`,
`SAME_TURN_RETRY_ONLY`, or `NOT_COMMITTED_TERMINAL` and any typed timeout,
crash, commit-observation, no-commit, or stale-authority cause.
`OUTCOME_UNKNOWN` is not an appended slate outcome body or store receipt. It
remains on the controller record until a same-identity query can establish
what, if anything, committed. `SAME_TURN_RETRY_ONLY` permits only the exact
pinned deterministic turn; `NOT_COMMITTED_TERMINAL` permits no further action
under that turn identity.

The Board's compact, externally readable marks are the routine translation
account's record medium. There is no second Gloss history ledger behind it.
Replacing a full slate requires a new account-bound slate identity and a
verified continuation or explicit gap; it never silently discards a live
replay, contest, privacy, or reopening obligation.

The translation account owns the Board records and lexicon generations. Thulia
has bounded custody only of exact relay lanes, their index, the current
validated generation pointer, and exceptions. Hearthline owns the task-scoped
request and serviceability decisions. Gloss has no memory ownership and cannot
object to, demand, or veto a lawful retention disposition.

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

The translation account preserves the lexicon series through separately
granted, append-only successor review. Thulia tends its identity, custody, and
route; Hearthline alone may declare a mapping semantically
`SERVICEABLE` for the active root task. A lexicon generation binds its predecessor,
canonical bytes, scope, grammar, codebook, decoder, parameters, tests, status,
serviceability source, and activation receipt. A later generation never
retroactively changes an earlier turn.

Routine Gloss receives the already selected generation. It does not choose
one, search the generation history, combine generations, repair an absent key,
or infer a mapping from resemblance. A missing, ambiguous, stale, unauthorized,
or non-reconstructible generation returns the note unchanged with a typed snag
mark.

The active serviceability map exists only for the root task that admitted it.
Task close ends that active map. A later revisit must explicitly reload a
retained exact lexicon generation and receipts under a current grant; neither
Gloss readiness nor Thulia's pointer carries semantic serviceability across the
closure.

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

A timeout, crash, or missing store acknowledgement is not a snag mark. It is a
transaction-observation failure and remains `OUTCOME_UNKNOWN` until the
preallocated identity can be checked. Exact no-commit moves to
`SAME_TURN_RETRY_ONLY` only while the entire pinned turn remains current, or to
`NOT_COMMITTED_TERMINAL` otherwise. The caller must not return the note
unchanged as though Gloss had
reported a semantic snag, infer success from determinism, or infer nonexecution
from silence.

## Thulia, Hearthline, and account custody

Hearthline writes the exact request on her Board lane, including a proposed
meaning when she is creating or revising shorthand, or otherwise the
source-bound expression and requested output face.
After the request is durably handed to Thulia, Thulia routes only the permitted
projection on the separately preallocated `T_TO_GLOSS_TURN` lane. Thulia is the
only interface permitted to invoke that turn; Gloss performs the pinned
deterministic transform and owns no custody relay. Thulia does not perform a
routine turn by improvisation, supply a likely meaning, or copy the Board into
an Owl-owned payload ledger.

The committed deterministic output and rule trace stay on the dedicated
Gloss-output lane. Their separately preallocated `GLOSS_TO_T_RESULT`
transaction and target receipt are distinct from the input turn. Thulia then
uses a different `T_TO_H_READABLE` transaction to relay the exact result. A
receipt in one direction proves nothing about another direction, and none can
be inferred from deterministic computation alone.

Hearthline's offer, consultation, load, Carry Selection, rejection,
serviceability, or reopening record belongs in her declared task account.
Hearthline may append only her authorized request and semantic
task-scoped `SERVICEABLE` decisions; she cannot append a pretended Gloss
output or silently replace a failed turn with her own translation.

Any model-assisted lexicon or exception work occurs as a separately identified
Spark job or enclosing Task Triad with exclusive bounded write lanes in its
declared accounts. Hearthline nominates only the Worker and Task-Keeper jobs;
Thulia independently nominates only Ledger-Keeper. The controller allocates
the separate records and freezes one complete offer; each provider then
commits only its final own-seat intent over the same digest, and the controller
atomically binds all three or none. Each execution/write
lane closes atomically at its controller-observed candidate seal. Each
controller-observed `SEALED` and separately `VALID` member bundle returns under
its own identity to Hearthline's task intake, using
`RETURN_PENDING_HEARTHLINE` until its target receipt is observed. It does not
return to Thulia or wait for an Owl-composed member envelope. None of
those Sparks becomes Gloss, gives Gloss a heartbeat, or inherits Thulia's Owl
routing or retention-classification lane.

If a Gloss mark is available but the exact Thulia profile, relay grant, or
objective epoch is unavailable, the mark stays in the translation account and
the appropriate directional relay state remains `REJECTED` or `UNKNOWN`.
Hearthline may not route in Thulia's place or turn the deterministic mark into
a serviceability decision without its required admitted return. A later relay
must revalidate the same pinned epoch; a successor epoch receives a successor
objective rather than inheriting the earlier return.

## Bridge Gloss is a different record

A **Bridge Gloss** is Thulia's source-, direction-, audience-, purpose-,
grant-, and version-bound relay record for a named crossing between account
partitions. It cites an exact committed Gloss output and rule trace; Thulia
does not originate the reconstruction. Gloss is the stateless mechanical turn.
The similar names mark an adjacent seam; they do not merge the jobs.

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

`PRUNE_ELIGIBLE` is not deletion authority. Thulia alone applies the
classification and opens the exact custody gate under a current retention
grant; the canonical store still performs Atomic Edge Promotion and emits the
effect receipt. Unknown or absent store outcome cannot be reported as deletion,
compaction, archive, or durable keep.

## Lore and implementation boundary

This document preserves the adopted Gloss, deterministic turn, Translation
Slate, lexicon generation, and snag-mark vocabulary from version `0.1`, plus
the atomic transaction and unknown-outcome recovery from candidate version
`0.2`. Version `0.3` proposes the external Translation Board,
writer-separated lanes, controller-observed one-turn readiness, Hearthline-only
task-scoped serviceability, and exact-generation reload boundary pending
steward review. It does not implement a codec, allocate a translation account
or Board, instantiate a wisp, append a mark, preserve operational memory,
activate Hearthline, or grant authority.

Systemic Friction is working Hearthline design vocabulary pending the paper's
reviewed release. This document does not add it to PAL canon, the controlling
source stack, or the Research Station source registry.

Any implementation must separately specify and test canonicalization, route
completeness, lexicon selection, deterministic repetition, inverse checks,
unchanged failure, mark preallocation, atomic append, slate replacement,
account custody, least-privilege access, privacy removal, timeout and crash
ambiguity, commit observation, transaction-key uniqueness, compare-and-append
idempotency, mismatched-body rejection, exact-epoch retry, stale-epoch refusal,
unknown-outcome reopening, wrapper-only Task Triads, absence of Gloss liveness
and Homecoming, exact no-commit retry-only and terminal transitions, rejection
of batch-of-one heartbeat disguises, per-turn readiness expiry, rejection of
inherited or persistent readiness, Translation Board writer-lane isolation,
direction-separated relay identities and receipts, Hearthline-only task-scoped
`SERVICEABLE`, direct member return to Hearthline, root-task map
closure, retained exact-generation reload, and rejection of history-dependent
or model-improvised routine translation.
