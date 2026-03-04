from MEA import run_MEA_complex

folder = '../instances/n280'
mutation_rates = [0.1]
k_values = [10]

for folder in ['../instances/n280']:
    print(f"{folder} MEA Results:")
    for j in k_values:
        print(f"\n=== k: {j} ===")
        for i in range(30):
            budget = 10**6
            population_pea, numEvals = run_MEA_complex(folder, budget, j, mutation_rates[0])
            print("\n")
