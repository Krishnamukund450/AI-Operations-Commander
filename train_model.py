import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv("data/incidents.csv")

X = df[["cpu", "memory"]]
y = df["decision"]

model = DecisionTreeClassifier()

model.fit(X, y)

joblib.dump(model,"models/decision_model.pkl")

print("Training accuracy:", model.score(X,y))

print("Model trained successfully")