"""Cross-process checkpoint route over the real MCP stdio transport."""
import asyncio
from contextlib import asynccontextmanager
from datetime import timedelta
import json
import os
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from hearthline_mcp.core import digest


def test_checkpoint_survives_restart_and_requires_checkpoint_route(tmp_path):
    async def run():
        source = {"measurement": 12, "baseline": 10, "labels": ["synthetic"]}
        source_hash = digest(source)
        bindings = [{"source_id": "source-1", "version": "1", "hash": source_hash}]
        retrieved = [{"source_id": "source-1", "version": "1", "content": source}]
        tether = {"tether_id": "t1", "task_id": "task-1", "scope": "bounded-comparison", "grant_ref": "grant-1",
                  "finish_condition": "return comparison", "residual": "open", "return_target": "controller",
                  "source_bindings": bindings, "retrieved_sources": retrieved}
        checkpoint = {"checkpoint_id": "checkpoint-1", "task_id": "task-1", "task_version": "v1",
                      "projection_id": "projection-1", "transition_ref": "transition-1",
                      "observation_ref": "observation-1", "horizon": "POINTWISE", "admitted_suffix": ["suffix-1"],
                      "work_state": {"cursor": 2, "answer": 2},
                      "source_bindings": [{"source_id": "source-1", "version": "1", "expected_hash": source_hash}],
                      "requirements": [{"requirement_id": "r1", "field": "baseline", "equals": 10,
                                         "evidence_refs": ["observation-1"]}]}
        requirement = {"unit": "tokens", "epoch": "epoch-1", "boundary": "task-1", "budget": 10, "next_cost": 1}
        grant = {"grant_ref": "grant-1", "task_id": "task-1", "scope": "bounded-comparison",
                 "observed_at": "2026-09-01T00:00:00Z", "expires_at": "2099-01-01T00:00:00Z",
                 "revoked": False, "remaining_budget": 3}
        resource = {"root": {"node_id": "root", "unit": "tokens", "epoch": "epoch-1", "boundary": "task-1",
                              "complete": True, "expected_child_ids": [],
                              "events": [{"event_id": "cost-1", "owner": "root", "amount": 1}], "children": []},
                    "declared_total": 1}

        @asynccontextmanager
        async def connection():
            env = {**os.environ, "HEARTHLINE_STORE_ROOT": str(tmp_path), "HEARTHLINE_STORE_NAMESPACE": "checkpoint-route"}
            params = StdioServerParameters(command=sys.executable, args=["-m", "hearthline_mcp.server"], env=env)
            async with stdio_client(params) as (reader, writer):
                async with ClientSession(reader, writer, read_timeout_seconds=timedelta(seconds=45)) as session:
                    await session.initialize()
                    yield session

        async def call(session, name, request=None, **arguments):
            payload = {"request": request} if request is not None else arguments
            response = await session.call_tool(name, payload)
            assert not response.isError, response
            return json.loads(next(item.text for item in response.content if item.type == "text"))

        history_after_reopen = None
        async with connection() as session:
            assert (await call(session, "bind_persistent_tether", tether))["status"] == "BOUND"
            frozen = await call(session, "freeze_work_checkpoint", {"tether_id": "t1", "checkpoint": checkpoint,
                                                                       "resource_requirement": requirement})
            assert frozen["status"] == "FROZEN"
            assert (await call(session, "read_persistent_records", kind="work.checkpoint"))["records"][0]["id"] == "checkpoint-1"

        async with connection() as session:
            recovered = await call(session, "read_work_checkpoint", checkpoint_id="checkpoint-1")
            assert recovered["status"] == "RECOVERED"
            assert recovered["record"]["checkpoint"] == checkpoint
            legacy = await call(session, "reopen_persistent_tether", {"tether_id": "t1", "current_grant": grant,
                                                                         "retrieved_sources": retrieved})
            assert legacy["status"] == "CHECKPOINT_REVIEW_REQUIRED"
            observed = {**checkpoint, "source_bindings": [{"source_id": "source-1", "version": "1",
                                                           "expected_hash": source_hash, "content": source}]}
            held = await call(session, "reopen_work_checkpoint", {"checkpoint_id": "checkpoint-1", "observed": observed,
                                                                    "current_grant": {**grant, "expires_at": "2020-01-01T00:00:00Z"},
                                                                    "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}},
                                                                    "resource_account": resource})
            assert held["status"] == "HELD_FOR_REVIEW"
            assert held["review"]["predicates"]["current_grant"] == "EXPIRED"
            reopened = await call(session, "reopen_work_checkpoint", {"checkpoint_id": "checkpoint-1", "observed": observed,
                                "current_grant": grant,
                                "facts": {"baseline": {"value": 10, "evidence_refs": ["observation-1"]}},
                                "resource_account": resource})
            assert reopened["status"] == "REOPENED"
            assert reopened["authority_renewal"] == "NONE" and reopened["consumed_resources"] == 0
            history = await call(session, "read_persistent_records")
            assert [row["kind"] for row in history["records"][:2]] == ["tether.bind", "work.checkpoint"]
            assert history["records"][1]["checkpoint"] == checkpoint
            history_after_reopen = history

        # A third process must see the complete append-only prefix, including
        # the held review and the successful review. Reads do not reset the
        # resource account or rewrite the frozen checkpoint.
        async with connection() as session:
            recovered_history = await call(session, "read_persistent_records")
            assert recovered_history["records"][:len(history_after_reopen["records"])] == history_after_reopen["records"]
            assert recovered_history["head"] == history_after_reopen["head"]
            recovered = await call(session, "read_work_checkpoint", checkpoint_id="checkpoint-1")
            assert recovered["record"] == history_after_reopen["records"][1]
            reread = await call(session, "read_persistent_records")
            assert reread["records"] == recovered_history["records"]
            assert reread["head"] == recovered_history["head"]

    asyncio.run(run())
