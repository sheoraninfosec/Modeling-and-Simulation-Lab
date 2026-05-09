# Author: Jigesh Sheoran
# Experiment 5: Cellular Automata - Forest Fire Simulation
# Last Modified : 10 / 03 / 2026

import numpy as np
import matplotlib.pyplot as plt
import random

# PARAMETERS
size = 50
p_tree = 0.6
p_fire = 0.3

wind_direction = "right"   # up, down, left, right
wind_strength = 0.2

steps = 30

# STATES
EMPTY, TREE, FIRE = 0, 1, 2

# INITIALIZE GRID
grid = np.random.choice([EMPTY, TREE], size*size, p=[0.4, 0.6]).reshape(size, size)

# Ignite center cell
grid[size//2][size//2] = FIRE

# NEIGHBOR FUNCTION
def get_neighbors(x, y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                neighbors.append((nx, ny))
    return neighbors

# UPDATE FUNCTION
def update(grid):
    new_grid = grid.copy()

    for i in range(size):
        for j in range(size):

            if grid[i][j] == FIRE:
                new_grid[i][j] = EMPTY

            elif grid[i][j] == TREE:
                neighbors = get_neighbors(i, j)

                for nx, ny in neighbors:
                    if grid[nx][ny] == FIRE:
                        prob = p_fire

                        # Wind effect
                        if wind_direction == "right" and ny > j:
                            prob += wind_strength
                        elif wind_direction == "left" and ny < j:
                            prob += wind_strength
                        elif wind_direction == "up" and nx < i:
                            prob += wind_strength
                        elif wind_direction == "down" and nx > i:
                            prob += wind_strength

                        if random.random() < prob:
                            new_grid[i][j] = FIRE
                            break
    return new_grid

# VISUALIZATION
burnt_counts = []

plt.figure()

for t in range(steps):
    plt.clf()
    plt.imshow(grid, cmap='hot')
    plt.title(f"Forest Fire Simulation - Step {t}")
    plt.pause(0.2)

    # Count burnt cells (EMPTY)
    burnt = np.sum(grid == EMPTY)
    burnt_counts.append(burnt)

    grid = update(grid)

plt.show()

# GRAPH: BURNT AREA VS TIME
plt.figure()
plt.plot(range(steps), burnt_counts, marker='o')
plt.title("Burnt Area vs Time")
plt.xlabel("Time Step")
plt.ylabel("Number of Burnt Cells")
plt.grid()

plt.show()