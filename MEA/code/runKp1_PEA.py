from PEA import one_plus_one_EA
import math

folder = '../instances/n500w1k10'
numEvalsPEA_list = []
print(f"{folder} PEA+1 Results:")
for i in range(10):
    budget = 100000000000000
    population_pea, numEvalsPEA = one_plus_one_EA(folder, budget)
    numEvalsPEA_list.append(numEvalsPEA)
    print(f"Run {i+1}: 1+1EA evaluations = {numEvalsPEA}")
    
avg = sum(numEvalsPEA_list) / len(numEvalsPEA_list)
std = math.sqrt(sum((x - avg) ** 2 for x in numEvalsPEA_list) / len(numEvalsPEA_list))
print(f"PEA average evals over 10: {avg}, for k={j} in {folder}")
print(f"PEA stddev evals over 10: {std},  for k={j} in {folder}")