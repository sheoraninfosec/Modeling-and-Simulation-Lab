# Author: Jigesh Sheoran
# Last Modified: 02/02/2026

def stepped_time_simulation(total_time, step_size=1):
    print("Stepped-Time Simulation Started\n")

    current_time = 0
    signal = "GREEN"
    time_in_signal = 0

    # durations
    green_time = 30
    yellow_time = 5
    red_time = 30

    checks = 0

    while current_time <= total_time:
        print(f"Time: {current_time}s | Signal: {signal}")

        current_time += step_size
        time_in_signal += step_size
        checks += 1

        # transition logic
        if signal == "GREEN" and time_in_signal >= green_time:
            signal = "YELLOW"
            time_in_signal = 0

        elif signal == "YELLOW" and time_in_signal >= yellow_time:
            signal = "RED"
            time_in_signal = 0

        elif signal == "RED" and time_in_signal >= red_time:
            signal = "GREEN"
            time_in_signal = 0

    print(f"\nTotal State Checks Performed: {checks}")
    print("Stepped-Time Simulation Ended\n")

stepped_time_simulation(total_time=120)
