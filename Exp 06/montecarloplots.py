# Author: Jigesh Sheoran
# Last Modified : 11 / 03 / 2026

import random
import matplotlib.pyplot as plt

N = 10000

inside_x = []
inside_y = []
outside_x = []
outside_y = []

count_inside = 0
pi_values = []

# MONTE CARLO SIMULATION
for i in range(1, N + 1):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        count_inside += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)

    # Running estimate of pi
    pi_estimate = 4 * count_inside / i
    pi_values.append(pi_estimate)

# FINAL OUTPUT
print("Estimated value of Pi:", pi_values[-1])

# PLOT 1: Scatter Plot
plt.figure()
plt.scatter(inside_x, inside_y, s=5)
plt.scatter(outside_x, outside_y, s=5)

plt.title("Monte Carlo Simulation (Inside vs Outside Circle)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Inside Circle", "Outside Circle"])
plt.gca().set_aspect('equal', adjustable='box')

# PLOT 2: Convergence Graph
plt.figure()
plt.plot(range(1, N + 1), pi_values)
plt.axhline(y=3.14159)

plt.title("Convergence of Pi using Monte Carlo Method")
plt.xlabel("Number of Iterations")
plt.ylabel("Estimated Pi")

plt.show()