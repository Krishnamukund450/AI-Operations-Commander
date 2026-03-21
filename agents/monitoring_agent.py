from simulator.system_simulator import generate_metrics

def monitor():

    metrics = generate_metrics()

    print("Monitoring:", metrics)

    return metrics