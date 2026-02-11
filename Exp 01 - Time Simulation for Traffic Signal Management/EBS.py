# Author: Jigesh Sheoran
# Last Modified: 02/02/2026

def event_based_simulation(total_time):
    print("Event-Based Simulation Started\n")

    current_time = 0
    signal = "GREEN"

    # durations
    durations = {
        "GREEN": 30,
        "YELLOW": 5,
        "RED": 30
    }

    # transition order
    next_signal = {
        "GREEN": "YELLOW",
        "YELLOW": "RED",
        "RED": "GREEN"
    }

    events = 0

    while current_time <= total_time:
        print(f"Time: {current_time}s | Signal: {signal}")

        # jump to next event
        current_time += durations[signal]
        signal = next_signal[signal]
        events += 1

    print(f"\nTotal Events Processed: {events}")
    print("Event-Based Simulation Ended\n")

event_based_simulation(total_time=120)
