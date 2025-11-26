from Knapsack import Knapsack

class Population:
    def __init__ (self):
        self.individuals : list[Knapsack] = []
    
    def fill_population(self, size, first_individual: Knapsack):
        for _ in range(size):
            random_individual = first_individual.random_initialization()
            self.individuals.append(random_individual)

