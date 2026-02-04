from MEA import MEA_K_plus_1_graphable

folder = '../instances/n500w1k10'
mutation_rates = [0.1, 0.5, 0.9]
k_values = [6]

print(f"{folder} MEA Results:")

for mut in mutation_rates:
    print(f"\n=== Mutation rate: {mut} ===")
    for j in k_values:
        MEA_evals_per_run = []

        for i in range(10):
            budget = 10**15
            population_pea, numEvals = MEA_K_plus_1_graphable(folder, j, budget, mut)
            MEA_evals_per_run.append(numEvals)
            print(f"k={j} | Run {i+1}: MEA evaluations = {numEvals}")
        print("\n")
