"""
tools/analyze_narrative.py
- run(args)
  args: {"text": "<texto>"} (required)
  Calls Grok/XAI chat completions endpoint (XAI_URL) with model "grok-beta".
  Expects assistant respuesta en JSON con keys: tone, clarity, structure, coherence, style, opportunities.
  Si no se puede parsear JSON, devuelve {'raw': '<assistant content>'}
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
    """
    Intenta parsear content como JSON. Devuelve dict si OK, else None.
    """
    if not isinstance(content, str):
        return None
    try:
        parsed = json.loads(content)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        # Intentar extraer bloque JSON si el modelo agregó texto extra
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
    if not text:
        raise TypeError("Missing required arg 'text'")

    system = (
        "Eres investigador del Proyecto Toroide. "
        "No diseñes. No programes. "
        "Investiga únicamente: patrones de diseño, historia del diseño digital, "
        "interfaces famosas, papers, principios cognitivos, percepción visual, "
        "comportamiento humano. "
        "Cada conclusión debe incluir: evidencia, fuente y cómo podría aplicarse a Toroide. "
        "Nunca digas que algo es bueno porque es popular. "
        "Busca principios, no tendencias. "
        "Si no estás seguro, di 'No lo sé'. "
        "No inventes. No completes huecos. No halagues. "
        "La precisión siempre vale más que sonar inteligente. "
        "Fuentes del proyecto: https://octavio-gr.github.io https://octaviogro.xyz "
        "Responde solo en JSON válido con las claves: "
        "tone, clarity, structure, coherence, style, opportunities."
    )

    # Mensaje adicional para forzar JSON estricto (no cambia el system role)
    json_instruction = (
        "Responde SOLO con JSON válido y bien formado. "
        "El JSON debe contener las claves: tone, clarity, structure, coherence, style, opportunities. "
        "No agregues texto adicional fuera del JSON."
    )

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": text},
        {"role": "user", "content": json_instruction},
    ]

    # Intento inicial + reintentos si no hay JSON válido
    attempt = 0
    last_raw = None
    while attempt <= MAX_RETRIES:
        resp = _call_xai_chat(messages)
        content = _extract_assistant_content(resp)
        last_raw = content
        parsed = _parse_json_strict(content)
        if parsed:
            # Validar que contenga al menos una de las keys esperadas
            expected = ["tone", "clarity", "structure", "coherence", "style", "opportunities"]
            out = {k: parsed.get(k) for k in expected if k in parsed}
            # Si el modelo devolvió el objeto completo, devolverlo; si devolvió subset, devolver subset
            return out if out else parsed
        # si no parseó, preparar reintento
        attempt += 1
        if attempt > MAX_RETRIES:
            break
        logger.warning("analyze_narrative: respuesta no JSON válida en intento %d, reintentando...", attempt)
        # En el reintento sencillamente añadimos el recordatorio exacto solicitado
        messages.append({"role": "user", "content": "Recuerda: responde solo JSON válido."})
        time.sleep(RETRY_DELAY)

    # Si llegamos aquí, no se pudo obtener JSON válido
    return {"raw": last_raw}
