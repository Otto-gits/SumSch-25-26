from MEA import run_MEA_complex

MEA_evals_per_run = []
k = [3] 
for folder in ['../instances/n280']:
    print(f"{folder} MEA Results:")
    for j in k:
        print(f"\n=== k: {j} ===")
        for i in range(30):
            budget = 10**8
            population_pea, numEvals = run_MEA_complex(folder, budget, j)
