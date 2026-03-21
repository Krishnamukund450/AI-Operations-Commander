from memory.vector_memory import search_similar_incident

def retrieve_knowledge(metrics):

    result = search_similar_incident(metrics)

    if result:
        print("Similar incident found")

    return result