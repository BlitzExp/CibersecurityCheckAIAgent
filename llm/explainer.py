import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def generate_explanation(assessment: dict) -> str:
    """
    Uses a local LLM to explain the risk and provide recommendations.
    """
    prompt = f"""
You are a cybersecurity assistant.

Library: {assessment['library']}
Version: {assessment['version']}
Risk level: {assessment['risk']}

Reason (from vulnerability analysis):
{assessment['reason']}

Number of CVEs found: {len(assessment.get('cves', []))}

Explain in clear technical terms:
1. Why this library is risky (or safe)
2. What a developer should do next

Be concise and factual. Do not invent vulnerabilities.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f" LLM explanation unavailable: {e}"
