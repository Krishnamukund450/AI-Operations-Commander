from fastapi import FastAPI
from core.agent_graph import agent_graph

app = FastAPI()

# ✅ ADD THIS BLOCK
@app.on_event("startup")
def load_model_once():
    from memory.vector_memory import get_model
    get_model()


@app.get("/run")
def run():
    result = agent_graph.invoke({})
    return result