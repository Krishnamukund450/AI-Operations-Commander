from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest()

history = []

def predict(metrics):

    global history

    cpu = metrics["cpu"]
    memory = metrics["memory"]

    values = [cpu, memory]
    history.append(values)

    if len(history) < 15:
        return "collecting_data"

    try:
        X = np.array(history)

        model.fit(X)

        prediction = model.predict([values])

        if prediction[0] == -1:
            return "anomaly_detected"

        return "normal"

    except Exception as e:
        print("Prediction error:", e)
        return "normal"