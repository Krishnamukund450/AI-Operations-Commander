import joblib
import os
import pandas as pd

MODEL_PATH = "models/decision_model.pkl"

model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

def decide(metrics):

    cpu = metrics["cpu"]
    memory = metrics["memory"]

    if model is None:
        return "ignore"

    features = pd.DataFrame([[cpu, memory]], columns=["cpu","memory"])

    prediction = model.predict(features)

    return prediction[0]