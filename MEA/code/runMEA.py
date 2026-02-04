from MEA import run_MEA2
import math

folder = '../instances/n50w1k10'
MEA_evals_per_run = []
print(f"{folder} MEA Results:")
k = [2,5,10] 
for j in k:
    MEA_evals_per_run = []     # reset per j
    for i in range(30):
        budget = 1000000000000000
        population_pea, numEvals = run_MEA2(folder, budget, j)
        MEA_evals_per_run.append(numEvals)
        print(f"Run {i+1}: MEA evaluations = {numEvals}")
    avg = sum(MEA_evals_per_run) / len(MEA_evals_per_run)
    std = math.sqrt(sum((x - avg) ** 2 for x in MEA_evals_per_run) / len(MEA_evals_per_run))
    print(f"MEA average evals over 30: {avg}, for k={j} in {folder}")
    print(f"MEA stddev evals over 30: {std},  for k={j} in {folder}")