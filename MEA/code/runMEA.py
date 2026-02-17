from MEA import run_MEA2

MEA_evals_per_run = []
k = [2,5,10] 
for folder in ['../instances/n500w1k10', '../instances/2n500w1k10']:
    print(f"{folder} MEA Results:")
    for j in k:
        print(f"\n=== k: {j} ===")
        MEA_evals_per_run = [] 
        for i in range(30):
            if folder == '../instances/n500w1k10' and j == 2:
                break
            budget = 1000000000000000
            population_pea, numEvals = run_MEA2(folder, budget, j)
            MEA_evals_per_run.append(numEvals)
            print(f"{numEvals}")
