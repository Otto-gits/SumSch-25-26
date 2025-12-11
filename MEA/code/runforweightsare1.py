from MEA import run_MEA2
import math
results = []
for _ in range(5):
    run = run_MEA2('../instances/n40w1k5', generations=10000)
    results.append([ind.fitness() for ind in run.individuals])
    
print("Results over 30 runs:")
for i, res in enumerate(results):
    print(f"Run {i+1}: {res}")

mean_results = [sum(col) / len(col) for col in zip(*results)]
print("Mean fitness per individual across runs:")
for i, mean_fit in enumerate(mean_results):
    print(f"Individual {i}: Mean Fitness = {mean_fit}")
    
stddev_results = [math.sqrt(sum((x - mean_results[i]) ** 2 for x in col) / len(col)) for i, col in enumerate(zip(*results))]
print("Standard Deviation of fitness per individual across runs:")
for i, stddev_fit in enumerate(stddev_results):
    print(f"Individual {i}: Std Dev = {stddev_fit}")