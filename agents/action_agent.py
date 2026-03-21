def act(decision):

    if decision == "reduce_cpu":
        action = "Scaling workload down"

    elif decision == "restart_service":
        action = "Restarting service"

    else:
        action = "System stable"

    print("Action:", action)

    return action