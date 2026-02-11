# Author : Jigesh Sheoran
# Last Modified : 11/02/2026

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# ==============================
# CONFIGURATION
# ==============================
NUM_NODES = 100
TIME_STEPS = 50
P_INFECT = 0.3
P_RECOVER = 0.1
INITIAL_INFECTED = 1
VACCINATED_COUNT = 10
NETWORK_TYPE = "BA"   # "ER", "BA", "WS"
VACCINATION_STRATEGY = "targeted"  # "random", "targeted", None
NUM_RUNS = 50

# ==============================
# NETWORK CREATION
# ==============================
def create_network(net_type):
    if net_type == "ER":
        return nx.erdos_renyi_graph(NUM_NODES, 0.15)
    elif net_type == "BA":
        return nx.barabasi_albert_graph(NUM_NODES, 3)
    elif net_type == "WS":
        return nx.watts_strogatz_graph(NUM_NODES, 6, 0.2)

# ==============================
# VACCINATION
# ==============================
def vaccinate_nodes(G, states):
    if VACCINATION_STRATEGY is None:
        return states
    
    if VACCINATION_STRATEGY == "random":
        nodes = random.sample(range(NUM_NODES), VACCINATED_COUNT)
    
    elif VACCINATION_STRATEGY == "targeted":
        degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)
        nodes = [node for node, deg in degrees[:VACCINATED_COUNT]]
    
    for node in nodes:
        states[node] = 2
    
    return states

# ==============================
# SINGLE SIMULATION
# ==============================
def run_simulation(G):
    states = [0] * NUM_NODES
    
    for _ in range(INITIAL_INFECTED):
        states[random.randint(0, NUM_NODES - 1)] = 1
    
    states = vaccinate_nodes(G, states)

    S_hist, I_hist, R_hist = [], [], []
    
    for t in range(TIME_STEPS):
        new_states = states.copy()

        for node in range(NUM_NODES):
            if states[node] == 1:
                for nbr in G.neighbors(node):
                    if states[nbr] == 0 and random.random() < P_INFECT:
                        new_states[nbr] = 1
                
                if random.random() < P_RECOVER:
                    new_states[node] = 2
        
        states = new_states
        
        S_hist.append(states.count(0))
        I_hist.append(states.count(1))
        R_hist.append(states.count(2))
    
    return S_hist, I_hist, R_hist

# ==============================
# MONTE CARLO EXECUTION
# ==============================
all_S = []
all_I = []
all_R = []

peak_list = []
time_peak_list = []
final_R_list = []
extinction_list = []

G = create_network(NETWORK_TYPE)

for run in range(NUM_RUNS):
    S_hist, I_hist, R_hist = run_simulation(G)
    
    all_S.append(S_hist)
    all_I.append(I_hist)
    all_R.append(R_hist)
    
    peak = max(I_hist)
    peak_list.append(peak)
    time_peak_list.append(I_hist.index(peak))
    final_R_list.append(R_hist[-1])
    
    extinction = next((i for i, x in enumerate(I_hist) if x == 0), TIME_STEPS)
    extinction_list.append(extinction)

# ==============================
# AVERAGING
# ==============================
mean_S = np.mean(all_S, axis=0)
mean_I = np.mean(all_I, axis=0)
mean_R = np.mean(all_R, axis=0)

# ==============================
# PRINT AVERAGED METRICS
# ==============================
print("Network Type:", NETWORK_TYPE)
print("Average Peak Infection:", np.mean(peak_list))
print("Average Time to Peak:", np.mean(time_peak_list))
print("Average Final Recovered:", np.mean(final_R_list))
print("Average Extinction Time:", np.mean(extinction_list))
print("Average Degree:", sum(dict(G.degree()).values()) / NUM_NODES)
print("Clustering Coefficient:", nx.average_clustering(G))

# ==============================
# PLOT AVERAGED CURVES
# ==============================
plt.plot(mean_S, label="Susceptible (Mean)")
plt.plot(mean_I, label="Infected (Mean)")
plt.plot(mean_R, label="Recovered (Mean)")

plt.xlabel("Time")
plt.ylabel("Population")
plt.title(f"Monte Carlo SIR Simulation ({NETWORK_TYPE})")
plt.legend()
plt.show()
