from Knapsack import Knapsack
import copy

class Population:
    def __init__ (self):
        self.individuals : list[Knapsack] = []
    
    def fill_population(self, size, first_individual: Knapsack):
        for i in range(size):
            random_individual = copy.deepcopy(first_individual)
            random_individual.random_initialization()
            self.individuals.append(random_individual)

