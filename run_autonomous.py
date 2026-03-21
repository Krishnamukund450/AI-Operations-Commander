import time
from core.agent_graph import agent_graph

def run_autonomous():

    state = {}

    while True:

        result = agent_graph.invoke(state)

        print("\n--- Agent Cycle ---")
        print(result)

        time.sleep(5)

if __name__ == "__main__":
    run_autonomous()