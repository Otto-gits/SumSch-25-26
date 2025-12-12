from MEA import run_MEA2
import math

MEA_evals_per_run = []
print("MEA Results:")
k = [2,5,10] 
for j in k:
    MEA_evals_per_run = []     # reset per j
    for i in range(30):
        budget = 1000000000000000
        population_pea, numEvals = run_MEA2('../instances/n200w1k10', budget, j)
        MEA_evals_per_run.append(numEvals)
        print(f"Run {i+1}: MEA evaluations = {numEvals}")
    avg = sum(MEA_evals_per_run) / len(MEA_evals_per_run)
    std = math.sqrt(sum((x - avg) ** 2 for x in MEA_evals_per_run) / len(MEA_evals_per_run))
    print(f"MEA {j} average evals over 30: {avg}, for k={j} in n200w1k10")
    print(f"MEA {j} stddev evals over 30: {std},  for k={j} in n200w1k10")