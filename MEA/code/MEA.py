from Knapsack import Knapsack
from Population import Population
import random
import copy

    
def run_MEA(instance_filename, pop_size, generations):
    # Injest the knapsack instance
    knapsack_instance = Knapsack(instance_filename)

    # Initialize population
    population = Population()
    population.fill_population(pop_size, knapsack_instance)

    # Main MEA loop
    for gen in range(generations):
        # p1Ind = 0 # always select first individual as parent 1

        p1Ind = random.randint(0, pop_size - 1)
        p2Ind = random.randint(1, pop_size - 1)
        parent1 = population.individuals[p1Ind]
        parent2 = population.individuals[p2Ind]
        randInt = random.random()
        if (randInt < 0.7):
            child1, child2 = parent1.crossover(parent2)
        else:
            # mutate copies so parents stay unchanged
            child1 = copy.deepcopy(parent1).mutate()
            child2 = copy.deepcopy(parent2).mutate()
            
        
        
        if child1.fitness() > parent1.fitness():
            # print(f"parent1fit: {parent1.fitness()}, child1fit: {child1.fitness()}")
            # if (randInt < 0.7):
            #     print(f"Generation {gen}: Crossover {p1Ind, p2Ind} improved {p1Ind} fitness from {parent1.fitness()} to {child1.fitness()}")
            # elif (randInt >= 0.7):
            #     print(f"Generation {gen}: Mutation improved {p1Ind} fitness from {parent1.fitness()} to {child1.fitness()}")
            population.individuals[p1Ind] = child1
        # else:
            # print(f"Generation {gen}: No improvement for parent1 (child1: {child1.fitness()} vs parent1: {parent1.fitness()})")
        
        if child2.fitness() > parent2.fitness():
            # if (randInt < 0.7):
            #     print(f"Generation {gen}: Crossover {p2Ind, p1Ind} improved {p2Ind} fitness from {parent2.fitness()} to {child2.fitness()}")
            # elif (randInt >= 0.7):
                # print(f"Generation {gen}: Mutation improved {p2Ind} fitness from {parent2.fitness()} to {child2.fitness()}") 
            population.individuals[p2Ind] = child2
    
    return population