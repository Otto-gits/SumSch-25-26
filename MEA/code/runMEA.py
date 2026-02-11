from MEA import run_MEA2
import math

MEA_evals_per_run = []
k = [2,5,10] 
for folder in ['../instances/n100w1k10', '../instances/n200w1k10', '../instances/n500w1k10']:
    print(f"{folder} MEA Results:")
    for j in k:
        MEA_evals_per_run = []     # reset per j
        for i in range(30):
            budget = 1000000000000000
            population_pea, numEvals = run_MEA2(folder, budget, j)
            MEA_evals_per_run.append(numEvals)
            print(f"{numEvals}")
        avg = sum(MEA_evals_per_run) / len(MEA_evals_per_run)
        std = math.sqrt(sum((x - avg) ** 2 for x in MEA_evals_per_run) / len(MEA_evals_per_run))
        print(f"MEA average evals over 30: {avg}, for k={j} in {folder}")
        print(f"MEA stddev evals over 30: {std},  for k={j} in {folder}")