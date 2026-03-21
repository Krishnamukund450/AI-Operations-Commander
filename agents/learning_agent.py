from memory.vector_memory import store_incident

def learn(metrics, decision, action):

    store_incident(metrics, decision, action)

    print("Incident stored in memory")