from PEA import run_PEA
import math

print("Running comparison of PEA on n200w1k10")
print("PEA Results:")
PEA_evals_per_run = []
k = [2,5,10]             # use list or sorted() for deterministic order
for j in k:
    PEA_evals_per_run = []     # reset per j
    for i in range(30):
        budget = 1000000000000000
        population_pea, numEvals = run_PEA('../instances/n200w1k10', budget, j)
        PEA_evals_per_run.append(numEvals)
        print(f"Run {i+1}: PEA evaluations = {numEvals}")
    avg = sum(PEA_evals_per_run) / len(PEA_evals_per_run)
    std = math.sqrt(sum((x - avg) ** 2 for x in PEA_evals_per_run) / len(PEA_evals_per_run))
    print(f"PEA {j} average evals over 30: {avg}, for k={j} in n200w1k10")
    print(f"PEA {j} stddev evals over 30: {std}, for k={j} in n200w1k10")

