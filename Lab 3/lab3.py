# Author: Jigesh Sheoran
# Last Modified : 05 / 04 / 2026

import matplotlib.pyplot as plt

# USER INPUT
steps = int(input("Enter number of steps: "))
simulations = int(input("Enter number of simulations: "))

# PSEUDO-RANDOM GENERATOR
seed = 12345

def pseudo_random():
    global seed
    seed = (1103515245 * seed + 12345) % (2**31)
    return seed % 2  # 0 or 1

# MONTE CARLO SIMULATION
all_walks = []

for s in range(simulations):
    position = 0
    walk = [position]

    for i in range(steps):
        r = pseudo_random()

        if r == 0:
            step = -1
        else:
            step = 1

        position += step
        walk.append(position)

    all_walks.append(walk)

# PLOT 1: RANDOM WALKS
plt.figure()

for walk in all_walks:
    plt.plot(walk)

plt.title("Random Walk Simulation")
plt.xlabel("Steps")
plt.ylabel("Position")

# PLOT 2: AVERAGE DISPLACEMENT
average_walk = []

for i in range(steps + 1):
    total = 0
    for walk in all_walks:
        total += walk[i]
    average_walk.append(total / simulations)

plt.figure()
plt.plot(average_walk)

plt.title("Average Displacement (Monte Carlo)")
plt.xlabel("Steps")
plt.ylabel("Average Position")

# SHOW OUTPUT
plt.show()