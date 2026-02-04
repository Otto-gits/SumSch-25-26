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

    
def run_MEA2(folder_path, budget, k):
    # Initialize population
    population = Population()
    population.injest_folder(folder_path, k)
    pop_size = len(population.individuals)
    done = [0]*pop_size

    # Main MEA loop
    evals = 0
    
    #EASY CALC OF OPTI SOL
    best_opt = copy.deepcopy(population.individuals[0])
    best_opt.create_valid_p2w_solution()
    
    while evals < budget and sum(done) < pop_size:
        p1Ind = random.randint(0, pop_size - 1)
        p2Ind = random.randint(0, pop_size - 1)
        parent1 = population.individuals[p1Ind]
        parent2 = population.individuals[p2Ind]
        if parent1.fitness == best_opt.fitness and done[p1Ind] == 0:
            done[p1Ind] = 1
        if parent2.fitness == best_opt.fitness and done[p2Ind] == 0:
            done[p2Ind] = 1
        
        randInt = random.random()
        if (randInt < 0.5):
            child1 = copy.deepcopy(parent1).crossover(parent2)
        else:
            child1 = copy.deepcopy(parent1).mutate()
        
        evals += 1
        child1.calc_fitness()
        
        if child1.fitness > parent1.fitness:
            population.individuals[p1Ind] = child1
        
    return population, evals

def MEA_K_plus_1(folder_path, k, budget=10000000, mutation_rate=0.5):
    population = Population()
    population.injest_folder(folder_path, k)
    evals = 0
    for i in range(k - 1):
        population.individuals[i].create_valid_p2w_solution()
        
    
    best_opt = copy.deepcopy(population.individuals[0])
    # print(f"{evals}, {population.individuals[-1].fitness}, X")
    # print("best optimal fitness should be:", best_opt.fitness)
    while population.individuals[-1].fitness < best_opt.fitness and evals < budget:
        parent1 = population.individuals[-1]
        
        p2Ind = random.randint(0, k - 2)
        parent2 = population.individuals[p2Ind]
        randInt = random.random()
        if (randInt > mutation_rate):
            child1 = copy.deepcopy(parent1).crossover(parent2)
        else:
            child1 = copy.deepcopy(parent1).mutate()
            
        evals += 1
        child1.calc_fitness()
        if child1.fitness > parent1.fitness:
            population.individuals[-1] = child1
            # if randInt > mutation_rate:
            #     # print(f"{evals}, {child1.fitness}, X")
            # else:
                # print(f"{evals}, {child1.fitness}, M")

            
        if population.individuals[-1].fitness == best_opt.fitness:
            break
            # print(f"Individual {k-1} reached  fitness {population.individuals[-1].fitness}. At {evals} evaluations.")
    return population, evals

def MEA_K_plus_1_graphable(folder_path, k, budget=10000000, mutation_rate=0.5):
    population = Population()
    population.injest_folder(folder_path, k)
    evals = 0
    for i in range(k - 1):
        population.individuals[i].create_valid_p2w_solution()
        
    
    best_opt = copy.deepcopy(population.individuals[0])
    print(f"{evals}, {population.individuals[-1].fitness}, X")
    # print("best optimal fitness should be:", best_opt.fitness)
    while population.individuals[-1].fitness < best_opt.fitness and evals < budget:
        parent1 = population.individuals[-1]
        
        p2Ind = random.randint(0, k - 2)
        parent2 = population.individuals[p2Ind]
        randInt = random.random()
        if (randInt > mutation_rate):
            child1 = copy.deepcopy(parent1).crossover(parent2)
        else:
            child1 = copy.deepcopy(parent1).mutate()
            
        evals += 1
        child1.calc_fitness()
        if child1.fitness > parent1.fitness:
            population.individuals[-1] = child1
            if randInt > mutation_rate:
                print(f"{evals}, {child1.fitness}, X")
            else:
                print(f"{evals}, {child1.fitness}, M")

            
        if population.individuals[-1].fitness == best_opt.fitness:
            break
            # print(f"Individual {k-1} reached  fitness {population.individuals[-1].fitness}. At {evals} evaluations.")

    return population, evals