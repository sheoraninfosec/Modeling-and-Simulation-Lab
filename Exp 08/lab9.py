# Experiment 9

import random
import matplotlib.pyplot as plt

cars = 50
road_length = 100
steps = 50

positions = []
for i in range(cars):
    positions.append(random.randint(0, road_length))

avg_speeds = []

# SIMULATION
for t in range(steps):
    speeds = []

    for i in range(cars):
        speed = random.randint(1, 5)
        positions[i] = (positions[i] + speed) % road_length
        speeds.append(speed)

    avg_speeds.append(sum(speeds)/len(speeds))

# Expected average speed
expected_speed = 3

expected_line = []
for i in range(steps):
    expected_line.append(expected_speed)

# PLOT: VALIDATION GRAPH
plt.figure()
plt.plot(avg_speeds, label="Observed Speed")
plt.plot(expected_line, linestyle='--', label="Expected Speed")

plt.title("Simulation Validation (Observed vs Expected)")
plt.xlabel("Time Step")
plt.ylabel("Average Speed")
plt.legend()
plt.grid()

plt.show()