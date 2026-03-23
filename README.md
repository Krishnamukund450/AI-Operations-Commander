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
