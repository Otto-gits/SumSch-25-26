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
        p1Ind = random.randint(0, pop_size - 1)
        p2Ind = random.randint(0, pop_size - 1)
        parent1 =  population.individuals[p1Ind]
        parent2 =  population.individuals[p2Ind]
        
        if (random.random() < 0.7):
            child1, child2 = parent1.crossover(parent2)
        else:
            # mutate copies so parents stay unchanged
            child1 = copy.deepcopy(parent1).mutate()
            child2 = copy.deepcopy(parent2).mutate()
            
        
        
        if child1.fitness() > parent1.fitness():
            population.individuals[p1Ind] = child1
            
        if child2.fitness() > parent2.fitness():
            population.individuals[p2Ind] = child2
    
    return population