import subprocess
import time

print("Starting AI Operations Commander...\n")

# Step 1: Train the model
print("Training ML model...")
subprocess.run(["python", "train_model.py"])

time.sleep(2)

# Step 2: Start FastAPI server
print("Starting API server...")
api_process = subprocess.Popen(
    ["uvicorn", "api.main:app"]
)

time.sleep(3)

# Step 3: Start Streamlit dashboard
print("Launching dashboard...")
dashboard_process = subprocess.Popen(
    ["streamlit", "run", "dashboard/app.py"]
)

print("\nSystem started successfully.")
print("API → http://127.0.0.1:8000")
print("Dashboard → http://localhost:8501")

# Keep processes alive
api_process.wait()
dashboard_process.wait()