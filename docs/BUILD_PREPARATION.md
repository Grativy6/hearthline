# Prepare the four-part toolkit build

Status: **DESIGN AND BUILD PREPARATION — ADAPTER INTEGRATION NOT COMPLETE**

This public note records the selected product boundaries and the evidence
needed from the build. It is not an execution grant or a substitute for the
versioned contracts. An initial working slice is a checkpoint toward the full
selected build, not completion of every toolkit module.

## Four deliverables

| Deliverable | Responsibility |
|---|---|
| seedPEA MCP | Minimal PAL, CHARTER, PECAN, PEA, SEED and PEACHES preparation/checking functions for people building their own systems. |
| Public Hearthline MCP | The same foundation plus the full supported context, continuity, reasoning, custody and orchestration toolkit. Lore is separately selectable. |
| Cabin MCP | Private extensions and selected continuity. A family workspace alongside personal agents is a later possibility. |
| Book of Peaches | The common stamp specification, separate Branchline book profile, verifier, checker rules and book infrastructure. |

The [public toolkit profile](PUBLIC_TOOLKIT.md) is the general entrance.
The [Moltbook profile](LEGACY_MOLTBOOK.md) is legacy and optional. Its root
agent file and candidate manifest remain historical compatibility artifacts;
they are not the source manifest or default instructions for the new build.

## Dependency direction and existing work

Use an independently installable foundation package in both seedPEA and
Hearthline. The full toolkit may depend on that foundation; the foundation
must not require the full toolkit, a task scheduler, research dependencies,
lore, or private repositories. Book verification has its own versioned
interface; shared verifier code does not distribute checker keys.

The public adapter must install without a second seedPEA service or private
checkout. Select the distribution artifact and record its applicable license
before publishing executable packages. Cabin selects shared modules without
making its records shared or public.

Inspect exact current repositories before extending an older local checkout.
The [public SeedPEA preview](https://github.com/Grativy6/seedpea-mcp-adapter/tree/ee4ee83c351d63b9d082cc41fd53cfdcdaef8c10)
already contains structured read-only checks, tests and Python packaging. Its
declared PAL 2.2 profile is a compatibility input, not a PAL 2.3 conformance
result. Preserve useful existing code and tests while mapping the selected
foundation. A historical echo/keyword prototype is not the same baseline.

Reuse the existing Python MCP and JavaScript app starting points where their
verified state supports that choice. Freeze actual repository heads,
working-tree state, dependency versions and source profiles at build start.
Keep record contracts language-neutral so interfaces do not drift across the
two runtimes. Installation and smoke evidence must support host claims.

## First contracts to make concrete

Names below describe responsibilities, not final API names:

1. Source identity, version, locator, inclusion/adoption status and applicable
   compatibility mapping, with retrieval or an explicit missing state.
2. Typed account/receipt records, provenance, residuals, and declared
   load-bearing dependencies; model-proposed relations remain provisional.
3. A scoped foundation check naming its predicate, inputs, evidence,
   limitations and unresolved result. Review, grant and execution stay distinct.
4. A Hearthline context/compaction packet, protected questions, preserved
   alternatives, source binding, and an honest reopen result.
5. TETHER and heartbeat records preserving current scope, spent limits,
   finish conditions and return route without renewing authority.
6. A PEACHES registration request and verification result, distinct from an
   issued stamp and from any separately referenced permission.

The applicable framework scope is preserved even when the interface is
small. Missing evidence cannot become approval. A declared mechanical check
does not decide general ethical acceptability or establish that the host
faithfully mediates every consequential operation.

Source-to-clause records should grow alongside the implementation: each
operative rule names its source or explicit design decision, scope,
transformation, residual and reopening condition. Complete and review the
applicable Founding Basis before real Genesis. A literature synthesis alone
does not adopt book rules or establish software conformance.

## First integrated checkpoint

Exercise the foundation independently, then this Hearthline route with
synthetic records:

**source selection → context and observation → compact packet → TETHER →
restart/reopen → dependency correction → bounded heartbeat report**.

The same foundation inputs and pinned configuration must produce equivalent
foundation results through seedPEA and Hearthline. The broader route belongs
to Hearthline. A minimal Cabin configuration uses selected synthetic private
records; family functionality is not required for this checkpoint.

Required distinguishing cases include:

- a missing or altered source produces an explicit retrieval/binding failure;
- two sources compact to one packet but require different protected answers,
  so an extra field or retrieved source is needed;
- correcting a necessary premise reopens the affected comparison while
  leaving unrelated records and the old observation readable;
- a heartbeat cannot satisfy completion or renew an exhausted grant;
- separate synthetic users/roots cannot obtain one another's private records;
- public defaults load neither personal history nor Moltbook instructions.

Read-only capability discovery and foundation binding connect to the app
first. Context and continuity extensions are separately selected capabilities;
they do not enlarge seedPEA's default catalogue. Preserve model attribution,
cancellation and existing private-note exclusions during integration.

## Early offline PEACHES work

Draft the common stamp specification and Branchline profile separately.
Bind book identity, exact stamp identity, exact object identity and request
identity as different values. Freeze the initial encoding, schema and
algorithms for each fixture set and label them provisional/test-only.

Specify retry behavior before writing an append path: an unchanged retry,
intentional second registration, changed payload under the same request,
delayed submission and replay of an old stamp are different cases. A repeated
request must not silently create an event or invent a receipt after an
unknown outcome.

Test canonical bytes, invalid signatures, wrong previous heads, incompatible
signed continuations, missing history and stale mirrors. A valid prefix does
not establish freshness; conflicting continuations remain visible. Include
an external book and an institutional stamp recorded as a separate Branchline
event, with neither stamp absorbing the other's claims.

Test export/import and compatible schema transitions while preserving old
bytes and verification context. An incompatible continuation needs a named
successor route; changing a label cannot repair history. Public fields and
commitment-only options must not require private grants, memories or chats as
public payloads. Also check avoidable metadata linkability.

Use fabricated objects, segregated test keys and unmistakable test-book
identities. Offline vectors must never become real Genesis or registration
events. A historical stamp and a referenced grant's present usability have
separate statuses.

## Work that remains separately staged

- Final founding-package bytes, permanent book identity, checker designation,
  live key custody, succession, compromise recovery and operational hosting
  are required for real Genesis readiness. They need not block the offline
  toolkit. Fixture choices do not silently settle them.
- FBT, cache-to-cache and other model-internal experiments retain their own
  instrumentable-model requirements, baselines, resource scope and evidence.
  They are optional research modules, not claimed general performance gains.
- Real private-source selection, family sharing, institutional onboarding and
  live external effects require their applicable scope and records.

## What a build return must show

Report exact code/source/dependency versions, the implemented capability
matrix, reproducible checks and results, unsupported cases and residuals.
Demonstrate clean installation, selected-host operation, isolation, recovery
and export for the functionality claimed. Keep synthetic evidence,
documentation readiness, working adapter behavior and a live book distinct.

The future build prompt should name the complete intended deliverables,
milestones, effect limits and completion criteria. Routine implementation
choices and local repairs can remain with the implementer; unresolved human
choices must not be silently decided by defaults or test success.
