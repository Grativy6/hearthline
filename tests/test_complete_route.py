"""Synthetic end-to-end source/carry/correction route over actual MCP stdio."""
import asyncio
from contextlib import asynccontextmanager
from datetime import timedelta
import json
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from hearthline_mcp.core import digest

def test_complete_source_to_reopening_route(tmp_path):
    @asynccontextmanager
    async def connection():
        env = {**os.environ, "HEARTHLINE_STORE_ROOT":str(tmp_path), "HEARTHLINE_STORE_NAMESPACE":"complete-route"}
        params = StdioServerParameters(command=sys.executable, args=["-m","hearthline_mcp.server"], env=env)
        async with stdio_client(params) as (reader,writer):
            async with ClientSession(reader, writer, read_timeout_seconds=timedelta(seconds=45)) as session:
                await session.initialize()
                yield session
    async def call(session, name, request=None, **arguments):
        response = await session.call_tool(name, {"request":request} if request is not None else arguments)
        assert not response.isError, response
        return json.loads(next(x.text for x in response.content if x.type == "text"))
    async def run():
        source = {"measurement":12,"baseline":10}
        source_hash = digest(source)
        bindings = [{"source_id":"source1","version":"1","hash":source_hash}]
        retrieved = [{"source_id":"source1","version":"1","content":source}]
        grant = {"grant_ref":"g","task_id":"task","scope":"comparison","observed_at":"2026-09-17T00:00:00Z","expires_at":"2099-01-01T00:00:00Z","revoked":False,"remaining_budget":3}
        async with connection() as session:
            assert (await call(session,"read_template_manifest"))["status"] == "OPT_IN_REQUIRED"
            selected = await call(session,"report_source_status", {"source_id":"source1","supplied_content":source,"expected_hash":source_hash,"version":"1","expected_version":"1"})
            assert selected["state"] == "AVAILABLE"
            orientation = await call(session,"orient_context", {"profile":"scientific","purpose":"compare","selected":["source1"],"supplied":["source1"],
                "source_bindings":[{"source_id":"source1","version":"1","content_hash":source_hash}]})
            assert orientation["status"] == "VALID"
            observation = {"id":"observation1","question":"Difference from baseline?","raw":[12],"baseline":[10],"method":"subtraction",
                "aperture":"single synthetic observation","calibration":"integer fixture","uncertainty":"no physical claim",
                "channels":[{"name":"observation","kind":"observed"},{"name":"interpretation","kind":"interpretation"}],
                "alternatives":["baseline may change"],"source":"source1"}
            recorded = await call(session,"record_observation_event", observation)
            assert recorded["status"] == "DECLARED_CONTRACT_CHECKED"
            compacted = await call(session,"compact_context_packet", {"items":[{"id":"observation1","value":12},{"id":"baseline1","value":10}],
                "max_items":1,"protected_questions":["difference"],"model_profile":"synthetic/no-model",
                "source_bindings":bindings,"alternatives":["baseline may change"],"purpose":"reopen comparison",
                "recovery_limits":{"full_object":False},"recovery_route":"retrieve source1"})
            assert compacted["packet"]["omitted_ids"] == ["baseline1"]
            tether = {"tether_id":"t","task_id":"task","scope":"comparison","grant_ref":"g","finish_condition":"return corrected comparison",
                "residual":"baseline remains reopenable","return_target":"controller","source_bindings":bindings,"retrieved_sources":retrieved}
            assert (await call(session,"bind_persistent_tether", tether))["status"] == "BOUND"
            for source_id, dependent_id, load in [("baseline1","comparison1",True),("comparison1","conclusion1",True),("baseline1","unrelated",False)]:
                saved = await call(session,"record_typed_dependency", {"dependency_id":source_id+"-"+dependent_id,"source_id":source_id,"dependent_id":dependent_id,
                    "relation":"depends_on","adopted":True,"provisional":False,"adoption_ref":"synthetic-controller1","load_bearing":load})
                assert saved["status"] == "VALID"
            collision = await call(session,"check_compaction_collision", {"left_retained_packet":{"value":12},"right_retained_packet":{"value":12},
                "left_protected_answers":{"difference":2},"right_protected_answers":{"difference":3},"protected_questions":["difference"]})
            assert collision["status"] == "COLLISION_REVIEW_REQUIRED"
            repair = {"source_map":{"a":{"protected_answer":2},"b":{"protected_answer":3}},"readout_map":{"a":"12","b":"12"},
                "side_trace_map":{"a":"same","b":"same"},"protected_query":["a","b"],"domain_complete":True}
            assert (await call(session,"math.bridge_repair",repair))["answer_recovered"] is False
            repair["side_trace_map"]["b"] = "baseline9"
            repaired = await call(session,"math.bridge_repair",repair)
            assert repaired["answer_recovered"] is True and repaired["full_object_recovered"] is True
            repair["source_map"]["b"]["protected_answer"] = 2
            repair["side_trace_map"]["b"] = "same"
            answer_only = await call(session,"math.bridge_repair",repair)
            assert answer_only["answer_recovered"] is True and answer_only["full_object_recovered"] is False
        async with connection() as session:
            assert (await call(session,"read_persistent_tether",tether_id="t"))["status"] == "BOUND"
            assert (await call(session,"reopen_persistent_tether", {"tether_id":"t","current_grant":grant,"retrieved_sources":retrieved}))["status"] == "REOPENED"
            missing = await call(session,"reopen_persistent_tether", {"tether_id":"t","current_grant":grant})
            assert missing["reopened"] is False and missing["source_errors"]
            for changed in [[], [{"source_id":"source1","version":"2","content":source}], [{"source_id":"source1","version":"1","content":{"measurement":12,"baseline":9}}]]:
                assert (await call(session,"reopen_persistent_tether", {"tether_id":"t","current_grant":grant,"retrieved_sources":changed}))["reopened"] is False
            correction = await call(session,"reopen_load_bearing_dependents", {"source_id":"baseline1","correction_id":"correct1"})
            assert correction["reconsider"] == ["comparison1","conclusion1"] and "unrelated" not in correction["reconsider"]
            preserved = await call(session,"read_persistent_records",kind="observation")
            assert preserved["records"][0]["observation"] == observation
            assert (await call(session,"create_persistent_heartbeat", {"heartbeat_id":"h","tether_id":"t","finish_condition":"return corrected comparison","budget":1}))["status"] == "ACTIVE"
            assert (await call(session,"pulse_persistent_heartbeat", {"heartbeat_id":"h","event_id":"e","cost":1,"state":"progress","material_change":"correction routed"}))["status"] == "EXHAUSTED"
            assert (await call(session,"pulse_persistent_heartbeat", {"heartbeat_id":"h","event_id":"later","cost":0}))["status"] == "LATE_PULSE_REJECTED"
    asyncio.run(run())
