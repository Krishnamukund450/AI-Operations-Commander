# 🚀 AI Operations Commander

An intelligent multi-agent system that monitors system health, detects anomalies, makes decisions, and executes actions autonomously using Machine Learning + LLM reasoning + memory.

---

## 🎥 Demo

![demo](https://github.com/user-attachments/assets/b1c436dd-2d67-4428-89d9-7436549c754a)


---

## 🧠 Workflow Diagram

<img width="1536" height="1024" alt="workflow" src="https://github.com/user-attachments/assets/bfb5b14d-89f0-48dc-a31b-969df9766497" />

---

## 🔄 System Workflow

```text
System Metrics → Monitoring → Prediction → Planner → Decision
                                      ↓
                                 Knowledge ↔ FAISS Memory
                                      ↓
                             (if no similar incident)
                                      ↓
                                     LLM
                                      ↓
                                   Action
                                      ↓
                                  Learning → FAISS
                                      ↓
                                    Alert
```

##⚙️ Features

🔍 Real-time system monitoring (CPU, Memory)
🤖 ML-based anomaly detection (Isolation Forest)
🌳 Decision-making model (Decision Tree)
🧠 LLM reasoning using phi3 (Ollama)
📚 FAISS vector memory (learns from past incidents)
🚨 Telegram alert integration
📊 Streamlit dashboard visualization
🔁 Continuous learning system


##🧩 How It Works

1. Monitoring Agent

Collects real-time system metrics.

2. Prediction Agent

Detects anomalies using Isolation Forest.

3. Planner Agent

Generates system stabilization plan using LLM.

4. Decision Agent

Predicts action using trained ML model.

5. Knowledge Agent

Searches FAISS memory for similar incidents.

6. LLM Reasoning Agent

Provides fallback intelligent suggestions.

7. Action Agent

Executes automated system response.

8. Learning Agent

Stores new incidents into memory.

9. Alert Agent

Sends alerts via Telegram.


##🏗️ Project Structure
```text
ai-operations-commander/
│
├── agents/
├── core/
├── memory/
├── api/
├── dashboard/
├── models/
├── data/
│
├── run_platform.py
├── train_model.py
├── requirements.txt
└── README.md
```
##🛠️ Tech Stack

Python
FastAPI
Streamlit
Scikit-learn
FAISS
Sentence Transformers
Ollama (phi3)
