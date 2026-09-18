from pathlib import Path
import asyncio
import json
import os
import shutil
import uuid

from hearthline_mcp.server import create_server


def test_server_constructs_without_lore_or_private_inputs(tmp_path):
    server = create_server(profile="public", store_root=tmp_path, store_namespace="test")
    names = {tool.name for tool in server._tool_manager.list_tools()}
    assert "math.apci_cost" in names
    assert "bind_persistent_tether" in names
    assert "hearthline_foundation_status" in names or any("foundation" in name for name in names)


def test_allowed_tools_filters_math_surface_before_registration(tmp_path):
    server = create_server(profile="cabin", store_root=tmp_path, store_namespace="test", user="cabin-user", allowed_tools={"math.apci_cost"})
    names = {tool.name for tool in server._tool_manager.list_tools()}
    assert "math.apci_cost" in names
    assert "math.gppr_partition" not in names


def test_stdio_tether_survives_server_restart():
    # Exercise the real MCP transport twice against one configured store.
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    async def run() -> None:
        root = Path(os.environ.get("LOCALAPPDATA", Path.cwd())) / "Hearthline" / f"test-{uuid.uuid4().hex}"
        env = {**os.environ, "HEARTHLINE_STORE_ROOT": str(root), "HEARTHLINE_STORE_NAMESPACE": "stdio"}
        params = StdioServerParameters(command=str(Path(os.sys.executable)), args=["-m", "hearthline_mcp.server"], env=env)
        request = {"tether_id": "stdio-tether", "task_id": "task", "scope": "test", "grant_ref": "g1", "finish_condition": "done", "residual": "none", "return_target": "test"}
        try:
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    response = await session.call_tool("bind_persistent_tether", {"request": request})
                    assert not response.isError
                    for source_id, dependent_id, load_bearing in (("s", "d1", True), ("d1", "d2", True), ("s", "side", False)):
                        response = await session.call_tool("record_typed_dependency", {"request": {
                            "dependency_id": f"{source_id}-{dependent_id}", "source_id": source_id,
                            "dependent_id": dependent_id, "relation": "depends_on",
                            "adopted": True, "provisional": False, "adoption_ref": f"human-{dependent_id}", "load_bearing": load_bearing}})
                        assert not response.isError
                    response = await session.call_tool("reopen_load_bearing_dependents", {"request": {"source_id": "s", "correction_id": "corr-1"}})
                    correction = json.loads(response.content[0].text)
                    assert not response.isError and correction["reconsider"] == ["d1", "d2"]
                    response = await session.call_tool("create_persistent_heartbeat", {"request": {"heartbeat_id": "hb", "tether_id": "stdio-tether", "finish_condition": "done", "budget": 1}})
                    assert not response.isError
                    response = await session.call_tool("pulse_persistent_heartbeat", {"request": {"heartbeat_id": "hb", "event_id": "e1", "cost": 1, "state": "changed"}})
                    assert not response.isError and "EXHAUSTED" in str(response.content)
                    response = await session.call_tool("pulse_persistent_heartbeat", {"request": {"heartbeat_id": "hb", "event_id": "e2", "cost": 1}})
                    assert not response.isError and "LATE_PULSE_REJECTED" in str(response.content)
                    response = await session.call_tool("check_compaction_collision", {"request": {"left_retained_packet": {"x": 1}, "right_retained_packet": {"x": 1}, "left_protected_answers": ["A"], "right_protected_answers": ["B"], "protected_questions": ["q"]}})
                    assert not response.isError and "COLLISION_REVIEW_REQUIRED" in str(response.content)
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    response = await session.call_tool("read_persistent_tether", {"tether_id": "stdio-tether"})
                    assert not response.isError
                    assert "BOUND" in str(response.content)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    asyncio.run(run())
