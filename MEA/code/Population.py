from Knapsack import Knapsack
import copy
import os

class Population:
    def __init__ (self):
        self.individuals : list[Knapsack] = []
    
    def injest_folder(self, folder_path):
        n_files = 0
        print(f"os.listdir(folder_path): {os.listdir(folder_path)}")
        
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                knap_instance = Knapsack(os.path.join(folder_path, filename))
                self.individuals.append(knap_instance)
                n_files += 1
        print(f"Injested {n_files} knapsack instances from {folder_path}")
    
    def fill_population(self, size, first_individual: Knapsack):
        for i in range(size):
            random_individual = copy.deepcopy(first_individual)
            random_individual.random_initialization()
            self.individuals.append(random_individual)

