"""Actual MCP processes: carry a scoped lesson, restart, correct without erasure."""
import asyncio
from contextlib import asynccontextmanager
from datetime import timedelta
import json
import os
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from hearthline_mcp.core import digest


def test_applicability_correction_survives_compaction_and_restart(tmp_path):
    @asynccontextmanager
    async def connection():
        env = {**os.environ, "HEARTHLINE_STORE_ROOT": str(tmp_path),
               "HEARTHLINE_STORE_NAMESPACE": "applicability-route"}
        params = StdioServerParameters(command=sys.executable, args=["-m", "hearthline_mcp.server"], env=env)
        async with stdio_client(params) as (reader, writer):
            async with ClientSession(reader, writer, read_timeout_seconds=timedelta(seconds=45)) as session:
                await session.initialize()
                yield session

    async def call(session, name, request=None, **arguments):
        response = await session.call_tool(name, {"request": request} if request is not None else arguments)
        assert not response.isError, response
        return json.loads(next(item.text for item in response.content if item.type == "text"))

    def observation(ident, value):
        return {"id": ident, "question": "Does the saved preference apply here?",
                "raw": value, "baseline": "previous declared context", "method": "exact declared equality",
                "aperture": "synthetic task fixture", "calibration": "no model or world measurement",
                "uncertainty": "supplied references not authenticated", "source": "synthetic-user:1",
                "channels": [{"name": "tool-report", "kind": "reported"}],
                "alternatives": ["the receiving context can differ"]}

    async def run():
        content = {"claim": "Keep routine answers short.", "applicability_conditions": [
            {"condition_id": "routine-only", "field": "question_kind", "equals": "routine",
             "evidence_refs": ["synthetic-user:1"]}], "unresolved": []}
        source = {"source_id": "preference:1", "version": "1", "expected_hash": digest(content),
                  "supplied_content": content}
        old_target = {"context_id": "task:1", "facts": {
            "question_kind": {"value": "routine", "evidence_refs": ["synthetic-task:1"]}}}
        request = {"source": source, "target": old_target, "reopen_handle": "tether:preference:1"}
        bindings = [{"source_id": source["source_id"], "version": "1", "hash": digest(content)}]
        retrieved = [{"source_id": source["source_id"], "version": "1", "content": content}]
        async with connection() as session:
            registry = await call(session, "read_context_sources")
            assert registry["sources"][1]["version"] == "0.2"
            initial = await call(session, "review_context_applicability", request)
            assert initial["target_applicability"]["status"] == "MATCHES_DECLARED_CONDITIONS"
            # Keep the original request and report in the existing append-only observation surface.
            original = observation("original", {"request": request, "review": initial})
            await call(session, "record_observation_event", original)
            compacted = await call(session, "compact_context_packet", {
                "items": [{"id": "routing", "value": "reopen the scoped preference"},
                          {"id": "lesson", "value": {"request": request, "review": initial}}],
                "max_items": 1, "source_bindings": bindings,
                "protected_questions": ["Does the preference apply to the current task?"],
                "recovery_route": "read observation original and verify preference:1"})
            assert compacted["packet"]["omitted_ids"] == ["lesson"]
            await call(session, "record_observation_event", observation("carry", compacted))
            assert (await call(session, "bind_persistent_tether", {
                "tether_id": "preference:1", "task_id": "review", "scope": "context-reuse", "grant_ref": "g",
                "finish_condition": "report current applicability", "residual": "lesson omitted; retrieve before reuse",
                "return_target": "controller", "source_bindings": bindings, "retrieved_sources": retrieved,
            }))["status"] == "BOUND"
            for dependent, load, adopted in [("answer-style", True, True), ("unrelated", False, True), ("proposal", True, False)]:
                assert (await call(session, "record_typed_dependency", {
                    "dependency_id": "edge:" + dependent, "source_id": "preference:1", "dependent_id": dependent,
                    "relation": "depends_on", "adopted": adopted, "provisional": not adopted,
                    "adoption_ref": "synthetic-controller:1", "load_bearing": load,
                }))["status"] == "VALID"
            before = (await call(session, "read_persistent_records"))["records"]

        async with connection() as session:
            # This is a new server process, reading the same isolated synthetic store.
            stored = (await call(session, "read_persistent_records", kind="observation"))["records"]
            saved_request = stored[0]["observation"]["raw"]["request"]
            assert stored[0]["observation"] == original
            packet = stored[1]["observation"]["raw"]["packet"]
            assert packet["omitted_ids"] == ["lesson"]
            repair = await call(session, "repair_compacted_context", {
                "needed_ids": ["lesson"], "available_items": [{"id": "lesson", "value": saved_request}]})
            recovered = repair["restored"][0]["value"]
            grant = {"grant_ref": "g", "task_id": "review", "scope": "context-reuse",
                     "observed_at": "2026-09-21T00:00:00Z", "expires_at": "2099-01-01T00:00:00Z",
                     "revoked": False, "remaining_budget": 2}
            reopened = await call(session, "reopen_persistent_tether", {
                "tether_id": "preference:1", "current_grant": grant, "retrieved_sources": retrieved})
            assert reopened["status"] == "REOPENED" and reopened["authority_renewal"] == "NONE"
            # Successful retrieval does not fill in an unknown receiving context.
            recovered["target"] = {"context_id": "task:2", "facts": {}}
            unknown = await call(session, "review_context_applicability", recovered)
            assert unknown["source_preservation"]["status"] == "MATCH"
            assert unknown["target_applicability"]["status"] == "UNRESOLVED"
            await call(session, "record_observation_event", observation("unresolved", unknown))
            # A newly supplied correction narrows reuse; it does not rewrite the old preference.
            recovered["target"]["facts"] = {"question_kind": {
                "value": "detailed derivation", "evidence_refs": ["synthetic-user-correction:2"]}}
            revised = await call(session, "review_context_applicability", recovered)
            assert revised["source_preservation"]["status"] == "MATCH"
            assert revised["target_applicability"]["status"] == "MISMATCHED"
            await call(session, "record_observation_event", observation("correction", {
                "request": recovered, "review": revised, "corrects": "original"}))
            correction = await call(session, "reopen_load_bearing_dependents", {
                "source_id": "preference:1", "correction_id": "current-task-correction"})
            assert correction["reconsider"] == ["answer-style"]
            assert (await call(session, "read_persistent_records"))["records"][:len(before)] == before

        async with connection() as session:
            rows = (await call(session, "read_persistent_records", kind="observation"))["records"]
            assert rows[0]["observation"] == original
            assert rows[2]["observation"]["raw"]["target_applicability"]["status"] == "UNRESOLVED"
            assert rows[3]["observation"]["raw"]["review"]["target_applicability"]["status"] == "MISMATCHED"
            assert rows[3]["observation"]["raw"]["request"]["source"] == source

    asyncio.run(run())
