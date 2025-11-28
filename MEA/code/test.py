from Knapsack import Knapsack
from MEA import run_MEA

knap = Knapsack("a280.txt")
print(knap.capacity, knap.num_items)
print(knap.fitness())
knap.bitstring = [1]*knap.num_items
print(knap.fitness())
knap.mutate()
print(knap.fitness())

# population = run_MEA('a10.txt', pop_size=5, generations=100)
# best_individual = population.individuals[0]
# print("Best fitness in final population:", best_individual.fitness())

print("Running MEA...")
population = run_MEA('a280.txt', pop_size=3, generations=100)
best_individual = max(population.individuals, key=lambda ind: ind.fitness())
print("Best fitness in final population:", best_individual.fitness())

# testInst.capacity = 5
# testInst.num_items = 3
# knap.items = {0: (10, 2), 1: (15, 3), 2: (40, 4)}
# knap.bitstring = [0, 0, 1] 

# print("Test Instance Fitness:", knap.fitness()) 
