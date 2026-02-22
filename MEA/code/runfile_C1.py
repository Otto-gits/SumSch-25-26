from MEA import MEA_complex_K_plus_1

folder = '../instances/n280'
mutation_rates = [0.5]
k_values = [5]

print(f"{folder} MEA Results:")

for mut in mutation_rates:
    print(f"\n=== Mutation rate: {mut} ===")
    for j in k_values:
        MEA_evals_per_run = []

        for i in range(10):
            budget = 10**6
            population_pea, numEvals = MEA_complex_K_plus_1(folder, j, budget, mut)
            MEA_evals_per_run.append(numEvals)
            print(f"k={j} | Run {i+1}: MEA evaluations = {numEvals}")
        print("\n")
