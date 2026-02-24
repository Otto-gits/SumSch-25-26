from PEA import run_PEA_complex

k = [2, 5, 10] 
for folder in ['../instances/n280']:
    print(f"{folder} MEA Results:")
    for j in k:
        print(f"\n=== k: {j} ===")
        for i in range(30):
            budget = 10**6
            population_pea, numEvals = run_PEA_complex(folder, budget, j)
