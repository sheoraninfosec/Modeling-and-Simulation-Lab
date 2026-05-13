# Experiment 8

import random
import matplotlib.pyplot as plt

samples = 1000
means = [2, 5, 8]

# UNIFORM DISTRIBUTION
uniform_data = []
for i in range(samples):
    uniform_data.append(random.random())

# NORMAL (APPROX)
normal_data = []
for i in range(samples):
    val = (random.random() + random.random() + random.random() +
           random.random() + random.random() + random.random()) / 6
    normal_data.append(val)

# SENSITIVITY ANALYSIS
results = []

for mean in means:
    temp = []
    for i in range(samples):
        value = mean + random.uniform(-1, 1)
        temp.append(value)
    results.append(sum(temp)/len(temp))

# Expected = same as input means
expected = means

# PLOT 1: DISTRIBUTIONS OVERLAY
plt.figure()
plt.hist(uniform_data, bins=30, alpha=0.5)
plt.hist(normal_data, bins=30, alpha=0.5)
plt.title("Uniform vs Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

# PLOT 2: SENSITIVITY COMPARISON
plt.figure()
plt.plot(means, results, marker='o', label="Observed Output")
plt.plot(means, expected, linestyle='--', label="Expected Output")

plt.title("Sensitivity Analysis (Observed vs Expected)")
plt.xlabel("Input Mean")
plt.ylabel("Output Average")
plt.legend()
plt.grid()
plt.show()