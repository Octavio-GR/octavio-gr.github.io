#!/usr/bin/env bash
# curl_tests.sh
# Ejemplos curl para probar /mcp en localhost:8000 o en la URL pública.
# Uso:
#   MCP_URL=http://localhost:8000/mcp ./curl_tests.sh

MCP_URL=${MCP_URL:-http://localhost:8000/mcp}
echo "Using MCP_URL=$MCP_URL"
echo

echo "==> fetch_page (path=/)"
curl -s -X POST "$MCP_URL" -H "Content-Type: application/json" -d '{"tool":"fetch_page","args":{"path":"/"}}' | jq || true
echo
echo

echo "==> analyze_narrative (short sample)"
curl -s -X POST "$MCP_URL" -H "Content-Type: application/json" -d '{"tool":"analyze_narrative","args":{"text":"Texto de prueba para análisis narrativo."}}' | jq || true
echo
echo

echo "==> enrich_text (short sample)"
curl -s -X POST "$MCP_URL" -H "Content-Type: application/json" -d '{"tool":"enrich_text","args":{"text":"Esto es una oración de ejemplo para mejorar.","goal":"Hazlo más claro."}}' | jq || true
echo
echo

echo "==> summarize (executive)"
curl -s -X POST "$MCP_URL" -H "Content-Type: application/json" -d '{"tool":"summarize","args":{"text":"Breve texto de ejemplo para resumir.","mode":"executive"}}' | jq || true
echo
