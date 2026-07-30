#!/usr/bin/env python3
"""
server.py

FastAPI MCP Bridge server for Toroide tools.
- Exposes POST /mcp which accepts JSON: {"tool": "name", "args": {...}}
- Loads env from .env and environment variables: XAI_API_KEY, SITE_BASE, XAI_URL, HTTP_TIMEOUT
- Dynamically imports tools from the tools/ package and calls run(args)
- Returns MCP-formatted JSON: {"ok": true, "result": {...}} or {"ok": false, "error": "..."}

Notes:
- This file only loads and executes existing tools in tools/ and handles errors gracefully.
- Does not change project architecture or other files.
"""
import os
import importlib
import inspect
import asyncio
import logging
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load .env variables (if present)
load_dotenv()

# Read important environment variables so tools can use them via os.environ
XAI_API_KEY = os.environ.get("XAI_API_KEY")
SITE_BASE = os.environ.get("SITE_BASE")
XAI_URL = os.environ.get("XAI_URL")
HTTP_TIMEOUT = os.environ.get("HTTP_TIMEOUT")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("server")

app = FastAPI(title="Toroide MCP Bridge")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # consider restricting in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Allowed tools — include the tools present in tools/
ALLOWED_TOOLS = {
    "fetch_page",
    "analyze_narrative",
    "enrich_text",
    "summarize",
}


def mcp_ok(result: Any) -> Dict[str, Any]:
    return {"ok": True, "result": result}


def mcp_error(message: str) -> Dict[str, Any]:
    return {"ok": False, "error": str(message)}


async def _invoke_tool(module, args: dict) -> Any:
    """
    Execute module.run(args) supporting sync and async functions.
    """
    if not hasattr(module, "run"):
        raise AttributeError("Tool module has no 'run' function")

    fn = getattr(module, "run")
    if inspect.iscoroutinefunction(fn):
        return await fn(args)
    else:
        # run synchronous function in threadpool to avoid blocking event loop
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: fn(args))


@app.post("/mcp")
async def mcp_endpoint(request: Request):
    """
    MCP HTTP endpoint. Expects JSON body: {"tool": "name", "args": {}}
    Returns MCP response JSON always.
    """
    try:
        payload = await request.json()
    except Exception as e:
        logger.warning("Invalid JSON payload: %s", e)
        return JSONResponse(status_code=400, content=mcp_error("Invalid JSON payload"))

    tool = payload.get("tool")
    args = payload.get("args", {})

    if not tool or not isinstance(tool, str):
        return JSONResponse(status_code=400, content=mcp_error("Missing or invalid 'tool' field"))

    if tool not in ALLOWED_TOOLS:
        return JSONResponse(status_code=404, content=mcp_error(f"Tool '{tool}' not found"))

    module_name = f"tools.{tool}"
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        logger.exception("Failed to import module %s: %s", module_name, e)
        return JSONResponse(status_code=500, content=mcp_error(f"Failed to import tool module '{tool}': {e}"))

    try:
        result = await _invoke_tool(module, args)
    except TypeError as te:
        logger.exception("Tool %s TypeError: %s", tool, te)
        return JSONResponse(status_code=400, content=mcp_error(f"Tool argument error: {te}"))
    except Exception as e:
        logger.exception("Tool %s execution error: %s", tool, e)
        return JSONResponse(status_code=500, content=mcp_error(f"Tool execution error: {e}"))

    # Ensure serializable result
    try:
        return JSONResponse(status_code=200, content=mcp_ok(result))
    except Exception as e:
        logger.exception("Result not JSON serializable: %s", e)
        return JSONResponse(status_code=500, content=mcp_error(f"Result not serializable: {e}"))


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8000"))
    host = os.environ.get("HOST", "0.0.0.0")
    logger.info("Starting Toroide MCP Bridge on %s:%s", host, port)
    uvicorn.run("server:app", host=host, port=port, log_level="info")
