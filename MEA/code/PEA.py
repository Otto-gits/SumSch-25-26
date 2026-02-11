from Population import Population
import copy

def run_PEA(folder_path, budget, k):
    population = Population()
    population.injest_folder(folder_path, k)
    pop_size = len(population.individuals)
    t = pop_size
    done = [0]*pop_size
    evaluations = 0
    #EASY CALC OF OPTI SOL
    best_opt = copy.deepcopy(population.individuals[0])
    best_opt.create_valid_p2w_solution()
    
    while evaluations < budget :
        i = (t % pop_size)   
        individual = population.individuals[i]
        if individual.fitness == best_opt.fitness and done[i] == 0:
            done[i] = 1
            if sum(done) == pop_size:
                break
        child = copy.deepcopy(individual).mutate()
        evaluations += 1
        t += 1
        child.calc_fitness()
        if child.fitness > individual.fitness:
            population.individuals[i] = child
    
    
    return population, evaluations


def PEA_K_plus_1(folder_path, k):
    # print("started")
    population = Population()
    population.injest_folder(folder_path, k)
    pop_size = len(population.individuals)
    total_evals = 0
    evaluations = 0
    done_count = 0
    index = 0
    best_opt = copy.deepcopy(population.individuals[0])
    best_opt.create_valid_p2w_solution()
    # print("best optimal fitness should be:", best_opt.fitness)
    while done_count < pop_size and evaluations < 10000000:
        individual = population.individuals[index]
        child = copy.deepcopy(individual).mutate()
        evaluations += 1
        child.calc_fitness()
        if child.fitness > individual.fitness:
            population.individuals[index] = child

        
        if population.individuals[index].fitness == best_opt.fitness:
            # print(f"Individual {index} reached  fitness {population.individuals[index].fitness}. At {evaluations} evaluations.")
            total_evals += evaluations
            evaluations = 0
            done_count += 1
            index = (index + 1) % pop_size
             

    return population, total_evals

def one_plus_one_EA(folder_path, budget):
    population = Population()
    population.injest_folder(folder_path, k=1)
    best_opt = copy.deepcopy(population.individuals[0])
    best_opt.create_valid_p2w_solution()

    # print("best optimal fitness should be:", best_opt.fitness)
    evals = 0
    while evals < budget and population.individuals[0].fitness < best_opt.fitness:
        parent1 = population.individuals[0]
        child1 = copy.deepcopy(parent1).mutate()  
        child1.calc_fitness()
        evals += 1

        if child1.fitness > parent1.fitness:
            population.individuals[0] = child1
    return population, evals

def one_plus_one_EA_graphable(folder_path, budget):
    population = Population()
    population.injest_folder(folder_path, k=1)
    best_opt = copy.deepcopy(population.individuals[0])
    best_opt.create_valid_p2w_solution()

    # print("best optimal fitness should be:", best_opt.fitness)
    evals = 0
    print(f"{evals} {population.individuals[0].fitness}")
    while evals < budget and population.individuals[0].fitness < best_opt.fitness:
        parent1 = population.individuals[0]
        child1 = copy.deepcopy(parent1).mutate()  
        child1.calc_fitness()
        evals += 1

        if child1.fitness > parent1.fitness:
            population.individuals[0] = child1
            print(f"{evals} {population.individuals[0].fitness}")
    return population, evals