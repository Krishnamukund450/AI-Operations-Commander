import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def llm_reasoning(metrics, decision):

    # ✅ Call LLM only when needed (important for phi3)
    if metrics["cpu"] < 50 and metrics["memory"] < 80:
        return "System stable (no LLM needed)"

    prompt = f"""
    System metrics:
    CPU: {metrics['cpu']}%
    Memory: {metrics['memory']}%

    ML decision: {decision}

    Suggest a short operational action.
    """

    # ✅ Reduce prompt size (faster response)
    prompt = prompt[:300]

    try:
        print("⚡ Calling phi3 LLM...")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 80
                }
            },
            timeout=120   # ✅ increased for phi3
        )

        if response.status_code == 200:
            data = response.json()
            result = data.get("response", "").strip()

            if result:
                print("✅ LLM response:", result[:100])
                return result

        return "Fallback: System stable"

    except requests.exceptions.Timeout:
        print("❌ LLM timeout")
        return "Fallback: Timeout - System stable"

    except Exception as e:
        print("❌ LLM failed:", e)
        return "Fallback: System stable"