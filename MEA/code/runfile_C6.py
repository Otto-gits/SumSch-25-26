from MEA import run_MEA_complex

folder = '../instances/n106'
mutation_rates = [0.1,0.5,0.9]
k_values = [10]

for folder in ['../instances/n106']:
    print(f"{folder} MEA Results:")
    for j in k_values:
        print(f"\n=== k: {j} ===")
        for i in range(30):
            budget = 10**6
            for mut in mutation_rates:
                population_pea, numEvals = run_MEA_complex(folder, budget, j, mut)
                print("\n")
