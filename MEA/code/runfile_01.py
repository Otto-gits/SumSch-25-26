from PEA import one_plus_one_EA_K

folders = ['../instances/n50w1k10','../instances/n100w1k10','../instances/n200w1k10','../instances/n500w1k10','../instances/2n500w1k10']
k_values = [10]

for folder in folders:
    print(f"{folder} MEA Results:")
    for j in k_values:
        for i in range(1):
            budget = 10**15
            population_pea, numEvals = one_plus_one_EA_K(folder, budget, j)
            print(f"{numEvals}")
        print("\n")
