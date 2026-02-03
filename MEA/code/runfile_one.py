from PEA import one_plus_one_EA

folder = '../instances/n500w1k10'
numEvalsPEA_list = []

print(f"\nOne + One EA Results:")
MEA_evals_per_run = []

for i in range(10):
    budget = 10**15
    population_pea, numEvals = one_plus_one_EA(folder, budget)
    MEA_evals_per_run.append(numEvals)
    print(f"Run {i+1}: 1+1EA evaluations = {numEvals}")