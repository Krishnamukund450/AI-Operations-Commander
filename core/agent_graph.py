from langgraph.graph import StateGraph
from typing import TypedDict

from agents.monitoring_agent import monitor
from agents.prediction_agent import predict
from agents.decision_agent import decide
from agents.knowledge_agent import retrieve_knowledge
from agents.llm_reasoning_agent import llm_reasoning
from agents.alert_agent import send_alert
from agents.action_agent import act
from agents.learning_agent import learn
from agents.planner_agent import plan


class AgentState(TypedDict, total=False):

    metrics:dict
    prediction:str
    plan: str
    decision:str
    knowledge:str
    llm:str
    action:str


def monitoring_node(state):

    state["metrics"] = monitor()

    metrics = state["metrics"]

    # 🚨 Telegram Alerts
    if metrics["cpu"] > 70:
        send_alert(f"🚨 High CPU: {metrics['cpu']}%")

    if metrics["memory"] > 80:
        send_alert(f"🚨 High Memory: {metrics['memory']}%")

    return state


def prediction_node(state):

    state["prediction"] = predict(state["metrics"])

    return state


def planner_node(state):

    plan_result = plan(state["metrics"])

    state["plan"] = plan_result

    return state


def decision_node(state):

    state["decision"] = decide(state["metrics"])

    return state


def knowledge_node(state):

    state["knowledge"] = retrieve_knowledge(state["metrics"])

    return state


def llm_node(state):

    if state["decision"] == "ignore":
        return state

    # If knowledge found, skip LLM
    if state.get("knowledge"):
        return state

    suggestion = llm_reasoning(state["metrics"], state["decision"])

    if suggestion:
        state["llm"] = suggestion

    return state


def action_node(state):

    final = state.get("llm") or state["decision"]

    state["action"] = act(final)

    return state


def learning_node(state):

    learn(state["metrics"], state["decision"], state["action"])

    return state



graph = StateGraph(AgentState)

graph.add_node("monitor", monitoring_node)
graph.add_node("predict", prediction_node)
graph.add_node("planner", planner_node)
graph.add_node("decision", decision_node)
graph.add_node("knowledge", knowledge_node)
graph.add_node("llm", llm_node)
graph.add_node("action", action_node)
graph.add_node("learning", learning_node)

graph.set_entry_point("monitor")

graph.add_edge("monitor","predict")
graph.add_edge("predict", "planner")
graph.add_edge("planner", "decision")
graph.add_edge("decision","knowledge")
graph.add_edge("knowledge","llm")
graph.add_edge("llm","action")
graph.add_edge("action","learning")

agent_graph = graph.compile()