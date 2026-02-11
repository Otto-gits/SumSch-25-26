from MEA import MEA_K_plus_1_graphable
from PEA import one_plus_one_EA_graphable

folder = '../instances/n100w1k10'
mutation_rates = [0.1, 0.5, 0.9]
k_values = [6]

print(f"{folder} MEA Results:")

for mut in mutation_rates:
    print(f"\n=== Mutation rate: {mut} ===")
    for j in k_values:

        for i in range(1):
            budget = 10**15
            population_pea, numEvals = MEA_K_plus_1_graphable(folder, j, budget, mut)
        print("\n")
one_plus_one_EA_graphable(folder, budget)
