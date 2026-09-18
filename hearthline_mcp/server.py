"""FastMCP entry point for the public Hearthline toolkit."""
from __future__ import annotations

import json
import os
from importlib.resources import files
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from . import __version__
from .orientation import FOUNDING_ORIENTATION
from .core import (collision_check, compact, dependency_correction, dependency_record,
                   finite_packet, inspect_context, observation, repair_context,
                   status_manifest)
from .context import orient, source_status, transport_capsule
from .store import ScopedStore
from .continuity import ContinuityEngine
from .science_math import TOOLS as MATH_TOOLS, TOOL_DESCRIPTIONS
from .software import TOOLS as SOFTWARE_TOOLS, TOOL_DESCRIPTIONS as SOFTWARE_TOOL_DESCRIPTIONS, SoftwareEngine, fbt_operation


ALLOWED_PROFILES = {"public", "cabin", "seedpea-bridge"}


def create_server(*, profile: str = "public", store_root: str | Path | None = None, store_namespace: str = "public", user: str = "default", include_template: bool = False, allowed_tools: list[str] | set[str] | None = None) -> FastMCP:
    """Create an isolated server bound to one configured profile and store.

    Caller input may select records, but cannot select an arbitrary filesystem
    root.  A host application supplies the root during server construction.
    """
    if profile not in ALLOWED_PROFILES:
        raise ValueError(f"unsupported profile {profile!r}; choose one of {sorted(ALLOWED_PROFILES)}")
    allowed = set(allowed_tools) if allowed_tools is not None else None
    if allowed is not None:
        unknown = sorted(allowed - set(MATH_TOOLS) - set(SOFTWARE_TOOLS) - {"foundation", "core", "context", "continuity", "math", "software"})
        if unknown:
            raise ValueError(f"unknown tool groups or names in allowed_tools: {unknown}")
    if store_root is None:
        appdata = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        store_root = appdata / "Hearthline" / "toolkit"
    mcp = FastMCP(f"hearthline-toolkit-{profile}", instructions=FOUNDING_ORIENTATION)
    store = ScopedStore(store_root, store_namespace, adapter=f"hearthline:{profile}", user=user)
    continuity = ContinuityEngine(store)
    software = SoftwareEngine(store, mode="TRACE_ONLY", operator_id=f"hearthline:{user}")

    def _tool(*, group: str, **kwargs: Any):
        def decorate(function: Any) -> Any:
            if allowed is not None and group not in allowed and function.__name__ not in allowed:
                return function
            return mcp.tool(**kwargs)(function)
        return decorate

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def toolkit_status() -> dict[str, Any]:
        enabled_math = sorted(name for name in MATH_TOOLS if allowed is None or "math" in allowed or name in allowed)
        enabled_software = sorted(name for name in SOFTWARE_TOOLS if allowed is None or "software" in allowed or name in allowed)
        return {**status_manifest(), "profile": profile, "template_available": include_template,
                "math_tools": enabled_math, "math_catalogue": sorted(MATH_TOOLS),
                "software_tools": enabled_software, "software_catalogue": sorted(SOFTWARE_TOOLS),
                "template_reference": "public Hearthline template is opt-in; no lore or private content is loaded by this server",
                "foundation_required": True}

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def read_template_manifest() -> dict[str, Any]:
        if not include_template:
            return {"status": "OPT_IN_REQUIRED", "default_loaded": False, "authority_effect": "NONE"}
        return {"status": "AVAILABLE", "manifest": json.loads(files("hearthline_mcp").joinpath("template_manifest.json").read_text()), "authority_effect": "NONE"}

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def list_capabilities() -> dict[str, Any]:
        return json.loads(files("hearthline_mcp").joinpath("capabilities.json").read_text())

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def make_finite_packet(items: list[dict[str, Any]], purpose: str = "") -> dict[str, Any]:
        return finite_packet(items, purpose=purpose)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def inspect_context_packet(request: dict[str, Any]) -> dict[str, Any]: return inspect_context(request)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def orient_context(request: dict[str, Any]) -> dict[str, Any]: return orient(request)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def report_source_status(request: dict[str, Any]) -> dict[str, Any]: return source_status(request)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def compact_context_packet(request: dict[str, Any]) -> dict[str, Any]: return compact(request)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def check_compaction_collision(request: dict[str, Any]) -> dict[str, Any]: return collision_check(request)

    @_tool(group="context", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def repair_compacted_context(request: dict[str, Any]) -> dict[str, Any]: return repair_context(request)

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def record_observation_event(request: dict[str, Any]) -> dict[str, Any]: return store.append(observation(request))

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def read_persistent_records(kind: str = "", offset: int = 0, limit: int = 100) -> dict[str, Any]:
        """Read a bounded page from this server's configured scope."""
        if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= 256:
            return {"status":"INVALID_INPUT", "authority_effect":"NONE"}
        snapshot = store.read()
        rows = [r for r in snapshot["records"] if not kind or r.get("kind") == kind]
        page = rows[offset:offset + limit]
        return {"status":"READ", "records":page, "next_offset":offset + len(page) if offset + len(page) < len(rows) else None,
                "head":snapshot["head"], "namespace":snapshot["namespace"], "authority_effect":"NONE"}

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def record_typed_dependency(request: dict[str, Any]) -> dict[str, Any]:
        record = dependency_record(request)
        if record.get("status") != "VALID":
            return record
        return store.append(record)

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def reopen_load_bearing_dependents(request: dict[str, Any]) -> dict[str, Any]:
        stored = store.read()["records"]
        edges = [r.get("dependency", {}) for r in stored if r.get("kind") == "dependency_record" and r.get("status") == "VALID"]
        known = {str(x) for e in edges for x in (e.get("source_id"), e.get("dependent_id")) if x is not None}
        correction = dependency_correction({"source_id": request.get("source_id"), "edges": edges, "known_nodes": sorted(known)})
        return store.append({**correction, "kind": "dependency_correction", "id": str(request.get("correction_id", correction.get("source_id", "correction")))})

    @_tool(group="core", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def validate_transport_capsule(request: dict[str, Any]) -> dict[str, Any]: return transport_capsule(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def bind_persistent_tether(request: dict[str, Any]) -> dict[str, Any]: return continuity.bind_tether(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def prepare_trace_key(request: dict[str, Any]) -> dict[str, Any]: return continuity.prepare_trace_key(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def resolve_trace_key(request: dict[str, Any]) -> dict[str, Any]: return continuity.resolve_trace_key(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def read_persistent_tether(tether_id: str) -> dict[str, Any]: return continuity.read_tether(tether_id)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def reopen_persistent_tether(request: dict[str, Any]) -> dict[str, Any]: return continuity.reopen_tether(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def create_persistent_heartbeat(request: dict[str, Any]) -> dict[str, Any]: return continuity.create_heartbeat(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def read_persistent_heartbeat(heartbeat_id: str) -> dict[str, Any]: return continuity.read_heartbeat(heartbeat_id)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def pulse_persistent_heartbeat(request: dict[str, Any]) -> dict[str, Any]: return continuity.pulse_heartbeat(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def suspend_persistent_heartbeat(request: dict[str, Any]) -> dict[str, Any]: return continuity.suspend_heartbeat(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def resume_persistent_heartbeat(request: dict[str, Any]) -> dict[str, Any]: return continuity.resume_heartbeat(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False))
    def record_persistent_custody(request: dict[str, Any]) -> dict[str, Any]: return continuity.record_custody(request)

    @_tool(group="continuity", annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False))
    def validate_persistent_formation(request: dict[str, Any]) -> dict[str, Any]: return continuity.validate_formation(request)

    @mcp.resource("hearthline://status")
    def status() -> str: return json.dumps(toolkit_status(), indent=2, sort_keys=True)

    @mcp.resource("hearthline://capabilities")
    def capabilities() -> str: return files("hearthline_mcp").joinpath("capabilities.json").read_text()

    try:
        from seedpea_foundation.mcp_tools import register_foundation
    except ImportError as exc:
        raise RuntimeError("hearthline-toolkit requires seedpea-foundation==0.1.0; install the shared foundation before starting the MCP server") from exc
    register_foundation(mcp, include_institution=False)
    def _math_wrapper(function: Any):
        def math_tool(request: dict[str, Any]) -> dict[str, Any]:
            return function(request)
        return math_tool
    for tool_name, function in MATH_TOOLS.items():
        if allowed is not None and tool_name not in allowed and "math" not in allowed:
            continue
        mcp.tool(name=tool_name, description=TOOL_DESCRIPTIONS[tool_name])(_math_wrapper(function))
    for tool_name, function in SOFTWARE_TOOLS.items():
        if allowed is not None and "software" not in allowed and tool_name not in allowed:
            continue
        def _software_factory(operation: Any):
            def software_tool(request: dict[str, Any]) -> dict[str, Any]:
                if operation is fbt_operation:
                    return operation(request, engine=software)
                return operation(request)
            return software_tool
        mcp.tool(name=tool_name, description=SOFTWARE_TOOL_DESCRIPTIONS[tool_name], annotations=ToolAnnotations(readOnlyHint=tool_name not in {"software.fbt"}, destructiveHint=False))(_software_factory(function))
    return mcp


def main() -> None:
    root = os.environ.get("HEARTHLINE_STORE_ROOT")
    namespace = os.environ.get("HEARTHLINE_STORE_NAMESPACE", "public")
    user = os.environ.get("HEARTHLINE_STORE_USER", "default")
    profile = os.environ.get("HEARTHLINE_PROFILE", "public")
    include_template = os.environ.get("HEARTHLINE_INCLUDE_TEMPLATE", "").strip().lower() in {"1", "true", "yes", "on"}
    create_server(profile=profile, store_root=root, store_namespace=namespace, user=user, include_template=include_template).run()


if __name__ == "__main__":
    main()
