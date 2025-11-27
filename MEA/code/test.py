from Knapsack import Knapsack
from MEA import run_MEA

knap = Knapsack('a10.txt')
print(knap.capacity, knap.num_items)
print(knap.fitness())


print("Running MEA...")
population = run_MEA('a280.txt', pop_size=10, generations=100000)
best_individual = max(population.individuals, key=lambda ind: ind.fitness())
print("Best fitness in final population:", best_individual.fitness())