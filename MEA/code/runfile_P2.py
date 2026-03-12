from PEA import run_PEA_complex_graph
folders = ['../instances/n50comp', '../instances/n106', '../instances/n280']

k_values = [10]
 
for folder in folders:
    print(f"{folder} MEA Results:")
    for j in k_values:
        print(f"\n=== k: {j} ===")
        for i in range(5):
            budget = 10**6
            population_pea, numEvals = run_PEA_complex_graph(folder, (budget*j), j)
            print("\n")
