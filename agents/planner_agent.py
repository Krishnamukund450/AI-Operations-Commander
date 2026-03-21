from agents.llm_reasoning_agent import llm_reasoning

def plan(metrics, decision="analyze"):

    try:
        # ✅ reuse optimized LLM function
        result = llm_reasoning(metrics, decision)

        if result:
            return result

        return "Fallback: System stable"

    except Exception as e:
        print("Planner failed:", e)
        return "Fallback: System stable"