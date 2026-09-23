# PAL 2.4 work checkpoints

Hearthline's checkpoint tools provide a bounded, append-only bridge for
carrying declared work across an interruption. They preserve the work fields
that the caller names and review the next episode's observations separately.
They do not restore hidden model state, authenticate a source or grant,
execute a task, consume a resource budget, or renew authority.

The route has three operations:

* `freeze_work_checkpoint` records a named checkpoint beneath an existing
  TETHER. The checkpoint contains `work_state`, `task_id`, `task_version`,
  `projection_id`, `transition_ref`, `observation_ref`, a `POINTWISE` horizon,
  an admitted suffix, source bindings, and an explicit requirements list.
  Resource accounting is separately named by `unit`, `epoch`, `boundary`,
  `budget`, and `next_cost`.
* `read_work_checkpoint` recovers the exact declared record. Reading is
  side-effect free and does not perform a resume check.
* `reopen_work_checkpoint` appends a review receipt containing observed work,
  current facts, a caller-supplied grant report, and a finite nested resource
  account. It returns `REOPENED` only when all declared predicates match. Any
  expired, missing, changed, or unknown predicate remains unresolved and is
  reported as `HELD_FOR_REVIEW`.

Successor checkpoints must identify their predecessor and carry an explicit
adoption reference. Rebinding an existing checkpoint with different bytes is
preserved as `CONFLICTING_REBIND`; it does not overwrite the earlier record.
The older `reopen_persistent_tether` route detects a checkpoint and returns
`CHECKPOINT_REVIEW_REQUIRED`, so a checkpoint cannot be bypassed through the
legacy TETHER path.

## Minimal synthetic example

The following uses an initialized local MCP `session`. Values are synthetic;
the digest binds canonical JSON (UTF-8, sorted keys, compact separators), not
the raw publication-file hash domain. The executable three-process example is
also covered by [the route test](../tests/test_checkpoint_route.py).

```python
from datetime import datetime, timedelta, timezone
from hearthline_mcp.core import digest

source = {"baseline": 10}
await session.call_tool("bind_persistent_tether", {"request": {
    "tether_id": "t1", "task_id": "task-1", "scope": "bounded-comparison",
    "grant_ref": "grant-1", "finish_condition": "return comparison",
    "residual": "review current baseline", "return_target": "controller",
    "source_bindings": [{"source_id": "source-1", "version": "1", "hash": digest(source)}],
    "retrieved_sources": [{"source_id": "source-1", "version": "1", "content": source}],
}})
checkpoint = {
    "checkpoint_id": "checkpoint-1",
    "task_id": "task-1",
    "task_version": "v1",
    "projection_id": "projection-1",
    "transition_ref": "transition-1",
    "observation_ref": "observation-1",
    "horizon": "POINTWISE",
    "admitted_suffix": ["suffix-1"],
    "work_state": {"cursor": 2, "answer": 2},
    "source_bindings": [{
        "source_id": "source-1", "version": "1",
        "expected_hash": digest(source),
    }],
    "requirements": [{
        "requirement_id": "r1", "field": "baseline", "equals": 10,
        "evidence_refs": ["observation-1"],
    }],
}

await session.call_tool("freeze_work_checkpoint", {"request": {
    "tether_id": "t1",
    "checkpoint": checkpoint,
    "resource_requirement": {
        "unit": "tokens", "epoch": "epoch-1", "boundary": "task-1",
        "budget": 10, "next_cost": 1,
    },
}})

await session.call_tool("read_work_checkpoint", {
    "checkpoint_id": "checkpoint-1",
})

now = datetime.now(timezone.utc)
await session.call_tool("reopen_work_checkpoint", {"request": {
    "checkpoint_id": "checkpoint-1",
    "observed": {**checkpoint, "source_bindings": [{
        **checkpoint["source_bindings"][0], "content": source,
    }]},
    "current_grant": {"grant_ref": "grant-1", "task_id": "task-1",
                       "scope": "bounded-comparison", "observed_at": now.isoformat(),
                       "expires_at": (now + timedelta(minutes=5)).isoformat(), "revoked": False,
                       "remaining_budget": 3},
    "facts": {"baseline": {"value": 10,
                             "evidence_refs": ["observation-1"]}},
    "resource_account": {"root": {
        "node_id": "root", "unit": "tokens", "epoch": "epoch-1",
        "boundary": "task-1", "complete": True,
        "expected_child_ids": [], "events": [], "children": [],
    }, "declared_total": 0},
}})
```

The final operation is a review of declared evidence. Even a `REOPENED`
result carries `authority_renewal: NONE`, `consumed_resources: 0`, and the
finite-profile notice. A resource event marked `UNKNOWN`, an incomplete child
manifest, or a missing current fact cannot be treated as zero, complete, or
true. The append-only history remains the record of what was declared and
when; it is not a claim that the underlying work or grant is authentic.

Resource observations have their own continuity rule. Once an event amount,
owner, attribution, or containing node has been observed for a TETHER and
resource boundary, a later account must retain those declared values. Omitting an
event or lowering a known amount is held for review. A new event may be added
when the resulting account remains within the frozen budget. An earlier
`UNKNOWN` amount may later become known only by retaining the same event and
its surrounding history. A changed unit, epoch, or boundary belongs in an
explicit successor checkpoint with a predecessor and adoption reference.
