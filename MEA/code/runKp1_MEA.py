from MEA import MEA_K_plus_1
import math

folder = '../instances/n500w1k10'
mutation_rates = [0.1, 0.5, 0.9]
k_values = [3, 6, 10]

print(f"{folder} MEA Results:")

for mut in mutation_rates:
    print(f"\n=== Mutation rate: {mut} ===")
    for j in k_values:
        MEA_evals_per_run = []  # reset per (mut, j)

        for i in range(10):
            budget = 10**15  # same number, nicer
            population_pea, numEvals = MEA_K_plus_1(folder, j, budget, mut)
            MEA_evals_per_run.append(numEvals)
            print(f"k={j} | Run {i+1}: MEA evaluations = {numEvals}")

        avg = sum(MEA_evals_per_run) / len(MEA_evals_per_run)
        std = math.sqrt(sum((x - avg) ** 2 for x in MEA_evals_per_run) / len(MEA_evals_per_run))

        print(f"k={j} | MEA mutation={mut} avg evals over 10: {avg}, in {folder}")
        print(f"k={j} | MEA mutation={mut} stddev evals over 10: {std}, in {folder}")
