from PEA import one_plus_one_EA

folder = '../instances/n100w1k10'
numEvalsPEA_list = []
print(f"{folder} PEA+1 Results:")
for i in range(30):
    budget = 100000000000000
    population_pea, numEvalsPEA = one_plus_one_EA(folder, budget)
    numEvalsPEA_list.append(numEvalsPEA)
    print(f"Run {i+1}: 1+1EA evaluations = {numEvalsPEA}")
    
