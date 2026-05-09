# Author: Jigesh Sheoran
# Experiment: Parallel and Distributed Simulation (Matrix Multiplication)
# Last Modified : 19 / 03 / 2026

import multiprocessing as mp
import time
import random
import matplotlib.pyplot as plt

# Generate Matrix
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Serial Multiplication
def serial_multiply(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Worker Function (Parallel)
def multiply_row(args):
    A, B, row = args
    n = len(B)
    result_row = []

    for j in range(n):
        val = 0
        for k in range(n):
            val += A[row][k] * B[k][j]
        result_row.append(val)

    return (row, result_row)

# Parallel Multiplication
def parallel_multiply(A, B, processes):
    n = len(A)
    pool = mp.Pool(processes)

    tasks = [(A, B, i) for i in range(n)]
    results = pool.map(multiply_row, tasks)

    pool.close()
    pool.join()

    result = [None]*n
    for row, value in results:
        result[row] = value
    return result

# MAIN
if __name__ == "__main__":

    n = 200  # matrix size (adjust if slow)

    A = generate_matrix(n)
    B = generate_matrix(n)

    print(f"\nMatrix Size: {n}x{n}")

    # SERIAL EXECUTION
    start = time.time()
    serial_result = serial_multiply(A, B)
    serial_time = time.time() - start

    print(f"Serial Time: {serial_time:.4f} sec")

    # PARALLEL EXECUTION (default cores)
    start = time.time()
    parallel_result = parallel_multiply(A, B, mp.cpu_count())
    parallel_time = time.time() - start

    print(f"Parallel Time: {parallel_time:.4f} sec")

    speedup = serial_time / parallel_time
    efficiency = speedup / mp.cpu_count()

    print(f"Speedup: {speedup:.2f}")
    print(f"Efficiency: {efficiency:.2f}")

    # PERFORMANCE GRAPH
    process_counts = [1, 2, 4]   # adjust based on your CPU
    speedups = []
    efficiencies = []

    for p in process_counts:
        start = time.time()
        parallel_multiply(A, B, p)
        parallel_time = time.time() - start

        sp = serial_time / parallel_time
        eff = sp / p

        speedups.append(sp)
        efficiencies.append(eff)

        print(f"Processes: {p}, Speedup: {sp:.2f}, Efficiency: {eff:.2f}")

    # PLOT 1: Speedup
    plt.figure()
    plt.plot(process_counts, speedups, marker='o')
    plt.title("Speedup vs Number of Processes")
    plt.xlabel("Number of Processes")
    plt.ylabel("Speedup")

    # PLOT 2: Efficiency
    plt.figure()
    plt.plot(process_counts, efficiencies, marker='o')
    plt.title("Efficiency vs Number of Processes")
    plt.xlabel("Number of Processes")
    plt.ylabel("Efficiency")

    plt.show()