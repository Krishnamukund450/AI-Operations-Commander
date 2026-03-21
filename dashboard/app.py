import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import datetime
import time

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(page_title="AI Operations Commander", layout="wide")

st.title("AI Operations Commander")

# auto refresh every 3 seconds
st_autorefresh(interval=3000, key="refresh")

# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "logs" not in st.session_state:
    st.session_state.logs = []

if "incidents" not in st.session_state:
    st.session_state.incidents = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# ------------------------------------------------
# API CALL
# ------------------------------------------------

try:
    res = requests.get("http://127.0.0.1:8000/run")
    data = res.json()
except:
    st.error("Backend API not running")
    st.info("Run backend using: uvicorn api.main:app --reload")
    st.stop()

cpu = data["metrics"]["cpu"]
memory = data["metrics"]["memory"]
decision = data["decision"]
action = data["action"]
plan = data.get("plan", "No plan generated")   # ✅ NEW

# ------------------------------------------------
# INCIDENT COUNTER
# ------------------------------------------------

if cpu > 85 or memory > 85:
    st.session_state.incidents += 1

# ------------------------------------------------
# STORE HISTORY
# ------------------------------------------------

st.session_state.history.append({
    "CPU": cpu,
    "Memory": memory
})

st.session_state.logs.append({
    "time": datetime.datetime.now().strftime("%H:%M:%S"),
    "cpu": cpu,
    "memory": memory,
    "decision": decision,
    "action": action
})

# ------------------------------------------------
# SYSTEM OVERVIEW
# ------------------------------------------------

uptime_seconds = int(time.time() - st.session_state.start_time)
uptime = str(datetime.timedelta(seconds=uptime_seconds))

health_score = max(0, 100 - max(cpu, memory))

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("CPU Usage", f"{cpu}%")
c2.metric("Memory Usage", f"{memory}%")
c3.metric("Incidents", st.session_state.incidents)
c4.metric("Uptime", uptime)
c5.metric("Health Score", f"{health_score}%")

# ------------------------------------------------
# HEALTH STATUS
# ------------------------------------------------

if cpu > 85 or memory > 85:
    st.error("CRITICAL INCIDENT DETECTED")

elif cpu > 70 or memory > 70:
    st.warning("HIGH SYSTEM LOAD")

else:
    st.success("SYSTEM HEALTHY")

st.divider()

# ------------------------------------------------
# LIVE MONITORING GRAPH
# ------------------------------------------------

st.subheader("System Monitoring")

df = pd.DataFrame(st.session_state.history[-30:])

st.line_chart(df, height=300)

st.divider()

# ------------------------------------------------
# CPU LOAD INDICATOR
# ------------------------------------------------

st.subheader("CPU Load")

st.progress(cpu / 100)

st.divider()

# ------------------------------------------------
# AI DECISION PANEL
# ------------------------------------------------

st.subheader("AI Decision Engine")

d1, d2 = st.columns(2)

d1.success(f"Decision: {decision}")
d2.info(f"Action: {action}")

# ✅ NEW AI PLAN SECTION
st.divider()

st.subheader("AI Plan")

st.info(plan)

st.divider()

# ------------------------------------------------
# AGENT PIPELINE
# ------------------------------------------------

st.subheader("Agent Pipeline")

p1, p2, p3, p4, p5 = st.columns(5)

p1.success("Monitoring")
p2.success("Prediction")
p3.success("Decision")

if decision != "ignore":
    p4.warning("LLM Reasoning")
else:
    p4.info("LLM Idle")

p5.success("Action")

st.divider()

# ------------------------------------------------
# AGENT STATUS TABLE
# ------------------------------------------------

st.subheader("Agent Status")

agent_status = {
    "Agent": [
        "Monitoring Agent",
        "Prediction Agent",
        "Decision Agent",
        "LLM Reasoning Agent",
        "Action Agent"
    ],
    "Status": [
        "Active",
        "Running",
        "Decision Ready",
        "Reasoning" if decision != "ignore" else "Idle",
        "Executing"
    ]
}

st.table(pd.DataFrame(agent_status))

st.divider()

# ------------------------------------------------
# INCIDENT TIMELINE
# ------------------------------------------------

st.subheader("Incident Timeline")

incident_logs = [
    log for log in st.session_state.logs
    if log["cpu"] > 85 or log["memory"] > 85
]

incident_df = pd.DataFrame(incident_logs[-10:])

if not incident_df.empty:
    st.table(incident_df)
else:
    st.info("No incidents recorded")

st.divider()

# ------------------------------------------------
# ACTIVITY LOG
# ------------------------------------------------

st.subheader("Recent Activity")

log_df = pd.DataFrame(st.session_state.logs[-15:])

# ✅ FIXED WARNING
st.dataframe(log_df, width="stretch")