#!/usr/bin/env python3
"""
test_mcp.py
Pruebas sencillas para el endpoint /mcp.
- Llama a cada herramienta vía HTTP POST a MCP_URL (por defecto http://localhost:8000/mcp)
- Imprime respuestas crudas
- Valida esquema JSON esperado
- Mensajes claros de error
Uso:
  MCP_URL=http://localhost:8000/mcp python test_mcp.py
"""
import os
import sys
import json
import httpx

MCP_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp")
XAI_API_KEY = os.environ.get("XAI_API_KEY")  # para decidir si ejecutar pruebas dependientes de XAI

client = httpx.Client(timeout=30.0)


def call_tool(tool, args):
    payload = {"tool": tool, "args": args}
    try:
        r = client.post(MCP_URL, json=payload)
        r.raise_for_status()
    except Exception as e:
        print(f"[ERROR] HTTP error calling {tool}: {e}")
        return None
    try:
        resp = r.json()
    except Exception:
        print(f"[ERROR] Non-JSON response for {tool}: {r.text}")
        return None
    return resp


def assert_keys(obj, keys):
    missing = [k for k in keys if k not in obj]
    return missing


def test_fetch_page():
    print("==> Test: fetch_page")
    resp = call_tool("fetch_page", {"path": "/"})
    if not resp:
        print("[FAIL] No response")
        return False
    print("Raw response:", json.dumps(resp, indent=2, ensure_ascii=False))
    if not resp.get("ok"):
        print("[FAIL] Tool returned error:", resp.get("error"))
        return False
    result = resp.get("result", {})
    missing = assert_keys(result, ["url", "text"])
    if missing:
        print("[FAIL] Missing keys in result:", missing)
        return False
    print("[OK] fetch_page returned url and text (length text):", len(result.get("text", "")))
    return True


def test_analyze_narrative():
    print("==> Test: analyze_narrative")
    if not XAI_API_KEY:
        print("[SKIP] XAI_API_KEY not set; skipping analyze_narrative")
        return True
    sample = "Texto de prueba breve para análisis narrativo."
    resp = call_tool("analyze_narrative", {"text": sample})
    if not resp:
        print("[FAIL] No response")
        return False
    print("Raw response:", json.dumps(resp, indent=2, ensure_ascii=False))
    if not resp.get("ok"):
        print("[FAIL] Tool returned error:", resp.get("error"))
        return False
    result = resp.get("result", {})
    # either keys present or 'raw'
    expected = ["tone", "clarity", "structure", "coherence", "style", "opportunities"]
    missing = [k for k in expected if k not in result]
    if "raw" in result:
        print("[WARN] analyze_narrative returned raw content; inspect manually.")
        return True
    if missing:
        print("[FAIL] analyze_narrative missing expected keys:", missing)
        return False
    print("[OK] analyze_narrative returns expected keys")
    return True


def test_enrich_text():
    print("==> Test: enrich_text")
    if not XAI_API_KEY:
        print("[SKIP] XAI_API_KEY not set; skipping enrich_text")
        return True
    sample = "Esto es una oración de ejemplo para mejorar."
    resp = call_tool("enrich_text", {"text": sample, "goal": "Hazlo más claro y conciso."})
    if not resp:
        print("[FAIL] No response")
        return False
    print("Raw response:", json.dumps(resp, indent=2, ensure_ascii=False))
    if not resp.get("ok"):
        print("[FAIL] Tool returned error:", resp.get("error"))
        return False
    result = resp.get("result", {})
    if "enriched" in result:
        print("[OK] enrich_text returned enriched text (length):", len(result.get("enriched") or ""))
        return True
    if "raw" in result:
        print("[WARN] enrich_text returned raw content; inspect manually.")
        return True
    print("[FAIL] enrich_text missing 'enriched' in result")
    return False


def test_summarize():
    print("==> Test: summarize")
    if not XAI_API_KEY:
        print("[SKIP] XAI_API_KEY not set; skipping summarize")
        return True
    sample = "Este es un texto de ejemplo para generar un resumen técnico o ejecutivo sobre su contenido y estructura."
    resp = call_tool("summarize", {"text": sample, "mode": "executive"})
    if not resp:
        print("[FAIL] No response")
        return False
    print("Raw response:", json.dumps(resp, indent=2, ensure_ascii=False))
    if not resp.get("ok"):
        print("[FAIL] Tool returned error:", resp.get("error"))
        return False
    result = resp.get("result", {})
    if "summary" in result:
        print("[OK] summarize returned summary (length):", len(result.get("summary") or ""))
        return True
    if "raw" in result:
        print("[WARN] summarize returned raw content; inspect manually.")
        return True
    print("[FAIL] summarize missing 'summary' in result")
    return False


if __name__ == "__main__":
    all_ok = True
    all_ok &= test_fetch_page()
    all_ok &= test_analyze_narrative()
    all_ok &= test_enrich_text()
    all_ok &= test_summarize()
    if all_ok:
        print("\nALL TESTS OK")
        sys.exit(0)
    else:
        print("\nSOME TESTS FAILED or WARNED")
        sys.exit(2)
