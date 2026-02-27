from MEA import run_MEA_complex

k = [10] 
for folder in ['../instances/n50comp']:
    print(f"{folder} MEA Results:")
    for j in k:
        print(f"\n=== k: {j} ===")
        for i in range(30):
            budget = 10**6
            population_pea, numEvals = run_MEA_complex(folder, budget, j)
            print("\n")
