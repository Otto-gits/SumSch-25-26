from PEA import run_PEA

PEA_evals_per_run = []
k = [5] 
for folder in ['../instances/2n500w1k10']:
    print(f"{folder} PEA Results:")
    for j in k:
        print(f"\n=== k: {j} ===")
        PEA_evals_per_run = [] 
        for i in range(12):
            budget = 1000000000000000
            population_pea, numEvals = run_PEA(folder, budget, j)
            PEA_evals_per_run.append(numEvals)
            print(f"{numEvals}")