"""
MCP Gateway Server

Aggregates multiple backend MCP servers (configured via backends.json or
BACKENDS_CONFIG env var) and exposes them as a single SSE-based MCP server.

Each backend entry:
  { "name": "names", "command": "python", "args": ["/servers/names/server.py"] }
"""

import asyncio
import json
import logging
import os
from contextlib import AsyncExitStack
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("gateway")

mcp = FastMCP("mcp-gateway", host=os.getenv("FASTMCP_HOST", "127.0.0.1"), port=int(os.getenv("FASTMCP_PORT", "8000")))

# tool_name -> ClientSession
_registry: dict[str, ClientSession] = {}
_exit_stack = AsyncExitStack()


def _load_backends() -> list[dict]:
    raw = os.getenv("BACKENDS_CONFIG")
    if raw:
        return json.loads(raw)
    config_path = os.path.join(os.path.dirname(__file__), "backends.json")
    if os.path.exists(config_path):
        with open(config_path) as f:
            return json.load(f)
    return []


async def _connect_backends():
    backends = _load_backends()
    if not backends:
        log.warning("No backends configured — gateway will have no tools")
        return

    await _exit_stack.__aenter__()

    for cfg in backends:
        name = cfg.get("name", cfg["command"])
        params = StdioServerParameters(
            command=cfg["command"],
            args=cfg.get("args", []),
            env=cfg.get("env"),
        )
        log.info("Connecting to backend '%s'", name)
        try:
            read, write = await _exit_stack.enter_async_context(stdio_client(params))
            session = await _exit_stack.enter_async_context(ClientSession(read, write))
            await session.initialize()
            result = await session.list_tools()
            for tool in result.tools:
                _registry[tool.name] = session
                log.info("  registered tool '%s' from '%s'", tool.name, name)
        except Exception as exc:
            log.error("Failed to connect to backend '%s': %s", name, exc)


async def _call_backend(tool_name: str, arguments: dict[str, Any]) -> str:
    session = _registry.get(tool_name)
    if session is None:
        raise ValueError(f"Unknown tool: {tool_name}")
    result = await session.call_tool(tool_name, arguments)
    parts = []
    for content in result.content:
        if isinstance(content, TextContent):
            parts.append(content.text)
        else:
            parts.append(str(content))
    return "\n".join(parts)


@mcp.tool()
async def gateway_call(tool_name: str, arguments: str = "{}") -> str:
    """
    Call any tool registered from a backend MCP server.

    Args:
        tool_name: Name of the tool to invoke.
        arguments: JSON-encoded arguments to pass to the tool.
    """
    args = json.loads(arguments)
    return await _call_backend(tool_name, args)


@mcp.tool()
async def list_tools() -> str:
    """List all tools available across all connected backend MCP servers."""
    if not _registry:
        return "No tools registered (no backends connected)."
    return "\n".join(f"- {name}" for name in sorted(_registry))


async def main():
    await _connect_backends()
    log.info("Gateway ready — %d tool(s) registered", len(_registry))
    await mcp.run_sse_async()


if __name__ == "__main__":
    asyncio.run(main())
