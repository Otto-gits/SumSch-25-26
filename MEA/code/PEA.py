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