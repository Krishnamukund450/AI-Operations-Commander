def evaluate(metrics_before, metrics_after):

    cpu_before = metrics_before["cpu"]
    cpu_after = metrics_after["cpu"]

    if cpu_after < cpu_before:
        return "action_successful"

    return "action_failed"