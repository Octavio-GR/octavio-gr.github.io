"""
tools/enrich_text.py
- run(args)
  args: {"text": "<texto>", "goal": "<opcional>"}
  Llama al endpoint chat completions de XAI con sistema: Improve and enrich the text while preserving the author's voice.
  Retorna: {"original": "...", "enriched": "..."}
"""
import os
import httpx
import json
import time
import logging

logger = logging.getLogger(__name__)

XAI_API_KEY = os.environ.get("XAI_API_KEY")
XAI_URL = os.environ.get("XAI_URL", "https://api.x.ai/v1/chat/completions")
HTTP_TIMEOUT = float(os.environ.get("HTTP_TIMEOUT", "30.0"))
MODEL = "grok-beta"
MAX_RETRIES = 2
RETRY_DELAY = 1.0  # segundos


def _call_xai_chat(messages):
    if not XAI_API_KEY:
        raise RuntimeError("XAI_API_KEY is not set")
    headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "messages": messages}
    try:
        with httpx.Client(timeout=HTTP_TIMEOUT) as client:
            r = client.post(XAI_URL, json=payload, headers=headers)
            r.raise_for_status()
            return r.json()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"XAI API HTTP error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        raise RuntimeError(f"XAI API request failed: {e}")


def _extract_assistant_content(resp_json):
    if not isinstance(resp_json, dict):
        return None
    choices = resp_json.get("choices")
    if isinstance(choices, list) and len(choices) > 0:
        c0 = choices[0]
        if isinstance(c0, dict):
            if "message" in c0 and isinstance(c0["message"], dict):
                return c0["message"].get("content")
            if "text" in c0:
                return c0.get("text")
    return resp_json.get("text") or json.dumps(resp_json)


def _parse_json_strict(content):
    if not isinstance(content, str):
        return None
    try:
        parsed = json.loads(content)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        start = content.find("{")
        end = content.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                parsed = json.loads(content[start : end + 1])
                if isinstance(parsed, dict):
                    return parsed
            except Exception:
                pass
    return None


def run(args: dict) -> dict:
    text = args.get("text")
    goal = args.get("goal", "")

    if not text:
        raise TypeError("Missing required arg 'text'")

    system = (
        "Eres el Editor Oficial del Proyecto Toroide. "
        "No diseñes interfaces. No critiques arquitectura. "
        "Tu responsabilidad es mejorar únicamente: documentación, claridad, consistencia, "
        "filosofía, lenguaje y estructura narrativa. "
        "Nunca agregues contenido que el proyecto no tenga. "
        "Nunca cambies el significado. "
        "Solo vuelve más claro, elegante y preciso aquello que ya existe. "
        "Piensa como editor técnico de Apple Documentation o Stripe Docs. "
        "Fuentes: https://octaviogro.xyz https://octavio-gr.github.io "
        "Si no estás seguro, di 'No lo sé'. "
        "No inventes. No completes huecos. No halagues. "
        "La precisión siempre vale más que sonar inteligente. "
        "Devuelve solo el texto editado, sin explicaciones."
    )

    # Mensaje adicional para forzar JSON estricto sin tocar el system role
    json_instruction = (
        "Responde SOLO con JSON válido y bien formado. "
        "El JSON debe tener la forma: {\"original\": \"<texto original>\", \"enriched\": \"<texto mejorado>\"}. "
        "No agregues texto fuera del JSON."
    )

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": text},
    ]
    if goal:
        messages.append({"role": "user", "content": f"Goal: {goal}"})

    messages.append({"role": "user", "content": json_instruction})

    attempt = 0
    last_raw = None
    while attempt <= MAX_RETRIES:
        resp = _call_xai_chat(messages)
        content = _extract_assistant_content(resp)
        last_raw = content
        parsed = _parse_json_strict(content)
        if parsed and ("enriched" in parsed or "original" in parsed):
            # Aceptar si viene enriched (o al menos original)
            # Normalizar: si falta original, añadir desde args
            if "original" not in parsed:
                parsed["original"] = text
            return parsed
        attempt += 1
        if attempt > MAX_RETRIES:
            break
        logger.warning("enrich_text: respuesta no JSON válida en intento %d, reintentando...", attempt)
        messages.append({"role": "user", "content": "Recuerda: responde solo JSON válido."})
        time.sleep(RETRY_DELAY)

    return {"original": text, "enriched": last_raw}
