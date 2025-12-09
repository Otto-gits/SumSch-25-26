from Knapsack import Knapsack
from MEA import run_MEA, run_MEA2
from Population import Population
import os
# knap = Knapsack("n20-1.txt")
# print(knap.capacity, knap.num_items)
# print(knap.fitness())
# # knap.bitstring = [1]*knap.num_items
# # print(knap.fitness())
# knap.mutate()
# print(knap.fitness())
# population = run_MEA('a10.txt', pop_size=25, generations=100000)
# best_individual = population.individuals[0]
# print("Best fitness in final population:", best_individual.fitness())


# population = run_MEA('a10.txt', pop_size=5, generations=100)
# best_individual = population.individuals[0]
# print("Best fitness in final population:", best_individual.fitness())

# print("Running MEA...")
# population = run_MEA('a10.txt', pop_size=5, generations=1000)
# best_individual = overall_best = population.individuals[0]
# print("Best fitness in final population:", best_individual.fitness())

# testInst.capacity = 5
# testInst.num_items = 3
# knap.items = {0: (10, 2), 1: (15, 3), 2: (40, 4)}
# knap.bitstring = [0, 0, 1] 

# print("Test Instance Fitness:", knap.fitness()) 


# population = Population()
# print("cwd:", os.getcwd())
# population.injest_folder('../instances/weightsare1')

population_best = run_MEA2('../instances/weightsare1', generations=50000)

# diagnostic: show source_file and id(items) for each individual
for i, individual in enumerate(population_best.individuals):
    print(i, individual.source_file, id(individual.items))
    print(f"Individual {i} fitness: {individual.fitness()}")
    print(" Bitstring:", individual.bitstring)

