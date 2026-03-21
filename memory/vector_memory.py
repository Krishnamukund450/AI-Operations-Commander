import faiss
import numpy as np
import os
import pickle

# -------------------------------
# CONFIG
# -------------------------------

INDEX_PATH = "memory/faiss_index.bin"
MEMORY_PATH = "memory/incidents.pkl"

dimension = 384

# -------------------------------
# LAZY LOAD MODEL (FIX)
# -------------------------------

model = None

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        print("Loading embedding model...")
        model = SentenceTransformer("paraphrase-MiniLM-L3-v2")  # lighter model
    return model

# -------------------------------
# LOAD OR CREATE INDEX
# -------------------------------

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(dimension)

# -------------------------------
# LOAD OR CREATE MEMORY
# -------------------------------

if os.path.exists(MEMORY_PATH):
    with open(MEMORY_PATH, "rb") as f:
        memory = pickle.load(f)
else:
    memory = []

# -------------------------------
# STORE INCIDENT
# -------------------------------

def store_incident(metrics, decision, action):

    model = get_model()   # ✅ FIX

    text = f"CPU {metrics['cpu']} Memory {metrics['memory']} Decision {decision}"

    embedding = model.encode([text])

    index.add(np.array(embedding))

    memory.append({
        "metrics": metrics,
        "decision": decision,
        "action": action
    })

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save memory
    with open(MEMORY_PATH, "wb") as f:
        pickle.dump(memory, f)

# -------------------------------
# SEARCH INCIDENT
# -------------------------------

def search_similar_incident(metrics):

    if len(memory) == 0:
        return None

    model = get_model()   # ✅ FIX

    query = f"CPU {metrics['cpu']} Memory {metrics['memory']}"

    embedding = model.encode([query])

    D, I = index.search(np.array(embedding), 1)

    idx = I[0][0]

    if idx < len(memory):
        return memory[idx]

    return None