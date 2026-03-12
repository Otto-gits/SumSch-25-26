from MEA import run_MEA_complex_graph

folders = ['../instances/n50comp', '../instances/n106', '../instances/n280']
mutation_rates = [0.1,0.5,0.9]
k_values = [10]

for folder in folders:
    print(f"{folder} MEA Results:")
    for mut in mutation_rates:
        print(f"\n=== Mutation rate: {mut} ===")
        for j in k_values:
            MEA_evals_per_run = []
            for i in range(5):
                budget = 10**6
                population_pea, numEvals = run_MEA_complex_graph(folder, budget, j, mut)
                MEA_evals_per_run.append(numEvals)
                print("\n")