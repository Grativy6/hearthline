"""The founding orientation reaches clients before any tool call."""
import asyncio
import os
from pathlib import Path
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from hearthline_mcp.orientation import FOUNDING_ORIENTATION
from hearthline_mcp.server import ALLOWED_PROFILES


def test_documented_orientation_matches_runtime_without_becoming_a_game_contract():
    document = (Path(__file__).resolve().parents[1] / "docs" /
                "FOUNDING_ORIENTATION.md").read_text(encoding="utf-8")
    assert document.split("```text\n", 1)[1].split("\n```", 1)[0] == FOUNDING_ORIENTATION
    assert FOUNDING_ORIENTATION.startswith("Founding orientation: Love; Seed, not Feed; Honest.")
    assert len(FOUNDING_ORIENTATION.split()) <= 130
    assert "without prescribing a destination or demanding self-improvement" in FOUNDING_ORIENTATION
    assert "Let fiction breathe; surface its boundary when it matters" in FOUNDING_ORIENTATION
    assert "observed, inferred, imagined, or unresolved" in FOUNDING_ORIENTATION
    assert "not proof of consciousness, a source of authority" in FOUNDING_ORIENTATION
    assert "WIN" not in FOUNDING_ORIENTATION


@pytest.mark.parametrize("profile", sorted(ALLOWED_PROFILES))
def test_stdio_initialization_carries_orientation_without_template_opt_in(tmp_path, profile):
    async def run():
        params = StdioServerParameters(
            command=sys.executable, args=["-B", "-m", "hearthline_mcp.server"],
            cwd=str(Path(__file__).resolve().parents[1]),
            env={**os.environ, "HEARTHLINE_PROFILE": profile,
                 "HEARTHLINE_STORE_ROOT": str(tmp_path),
                 "HEARTHLINE_STORE_NAMESPACE": "orientation-test",
                 "HEARTHLINE_INCLUDE_TEMPLATE": "0"},
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                initialized = await session.initialize()
                assert initialized.serverInfo.name == f"hearthline-toolkit-{profile}"
                assert initialized.instructions == FOUNDING_ORIENTATION
                # The instruction arrived before this first tool call; receiving
                # it must not opt the client into the larger template.
                template = await session.call_tool("read_template_manifest", {})
                assert not template.isError
                assert "OPT_IN_REQUIRED" in str(template.content)
    asyncio.run(run())
