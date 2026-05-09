# Author: Jigesh Sheoran
# Last Modified : 11 / 03 / 2026

import random

def estimate_pi(N):
    count_inside = 0

    for i in range(N):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            count_inside += 1

    pi_estimate = 4 * count_inside / N
    return pi_estimate


# Run simulation for different iterations
iterations = [1000, 1500, 3000, 5000]

for N in iterations:
    pi_val = estimate_pi(N)
    print(f"Iterations: {N}, Estimated Pi: {pi_val}")

