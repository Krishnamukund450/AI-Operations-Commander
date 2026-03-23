# 🚀 AI Operations Commander

An intelligent multi-agent system that monitors system health, detects anomalies, makes decisions, and executes actions autonomously using Machine Learning + LLM reasoning + memory.

---

## 🎥 Demo

<p align="center">
  <img src="images/demo.gif" width="700"/>
</p>

---

## 🧠 Workflow Diagram

<p align="center">
  <img src="images/architecture.png" width="800"/>
</p>

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
