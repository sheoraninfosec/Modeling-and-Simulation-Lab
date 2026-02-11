# Author : Jigesh Sheoran
# Last Modified : 12/02/2026

import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
P0 = 100
r = 0.1
K = 1000          # carrying capacity 
t_max = 20
dt = 0.1          # small timestep for numerical solution

# DISCRETE EXPONENTIAL MODEL
time_discrete = np.arange(0, t_max + 1, 1)
population_discrete = [P0]

for i in range(1, len(time_discrete)):
    P_next = population_discrete[i - 1] * (1 + r)
    population_discrete.append(P_next)

population_discrete = np.array(population_discrete)

# CONTINUOUS ANALYTICAL EXPONENTIAL
time_cont = np.linspace(0, t_max, 200)
population_cont = P0 * np.exp(r * time_cont)

# CONTINUOUS NUMERICAL (Euler Method)
time_euler = np.arange(0, t_max, dt)
population_euler = [P0]

for t in time_euler[:-1]:
    P_current = population_euler[-1]
    dP = r * P_current
    population_euler.append(P_current + dP * dt)

population_euler = np.array(population_euler)

# LOGISTIC MODEL (Continuous)
population_logistic = [P0]

for t in time_euler[:-1]:
    P_current = population_logistic[-1]
    dP = r * P_current * (1 - P_current / K)
    population_logistic.append(P_current + dP * dt)

population_logistic = np.array(population_logistic)

# ERROR ANALYSIS
interp_cont = np.interp(time_discrete, time_cont, population_cont)
error = np.abs(population_discrete - interp_cont)
percent_error = (error / interp_cont) * 100

# PLOTS
plt.figure(figsize=(10, 6))
plt.plot(time_discrete, population_discrete, 'o-', label='Discrete Model')
plt.plot(time_cont, population_cont, '--', label='Continuous Analytical')
plt.plot(time_euler, population_euler, ':', label='Continuous (Euler)')
plt.plot(time_euler, population_logistic, label='Logistic Model')

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Discrete vs Continuous Population Growth Models")
plt.legend()
plt.grid(True)
plt.show()

# ERROR GRAPH
plt.figure(figsize=(8, 5))
plt.plot(time_discrete, percent_error, 'r-o')
plt.xlabel("Time")
plt.ylabel("Percentage Error (%)")
plt.title("Percentage Error: Discrete vs Continuous")
plt.grid(True)
plt.show()

# PRINT METRICS
print("Final Population Values at t =", t_max)
print("Discrete:", population_discrete[-1])
print("Continuous Analytical:", population_cont[-1])
print("Euler Numerical:", population_euler[-1])
print("Logistic Model:", population_logistic[-1])
print("\nMaximum Percentage Difference:", max(percent_error), "%")
