import random
import psutil

# Toggle mode here
MODE = "real"   # "real" or "simulation"


# -------------------------------
# REAL SYSTEM METRICS
# -------------------------------

def real_metrics():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return {
        "cpu": int(cpu),
        "memory": int(memory)
    }


# -------------------------------
# SIMULATION METRICS (OLD)
# -------------------------------

def simulated_metrics():

    cpu = random.randint(20, 60)
    memory = random.randint(30, 70)

    incident_chance = random.random()

    if incident_chance < 0.15:

        incident_type = random.choice([
            "cpu_spike",
            "memory_leak",
            "system_overload"
        ])

        if incident_type == "cpu_spike":
            cpu = random.randint(85, 100)

        if incident_type == "memory_leak":
            memory = random.randint(85, 100)

        if incident_type == "system_overload":
            cpu = random.randint(85, 100)
            memory = random.randint(85, 100)

    return {
        "cpu": cpu,
        "memory": memory
    }


# -------------------------------
# MAIN FUNCTION
# -------------------------------

def generate_metrics():

    if MODE == "real":
        return real_metrics()
    else:
        return simulated_metrics()