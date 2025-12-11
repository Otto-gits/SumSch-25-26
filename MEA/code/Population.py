from Knapsack import Knapsack
import copy
import os
import re

class Population:
    def __init__ (self):
        self.individuals : list[Knapsack] = []
    
    def injest_folder(self, folder_path, k):
        # list .txt files and natural-sort them so that they are ordered numerically
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        def natural_key(name: str):
            parts = re.split(r'(\d+)', name)
            return [int(p) if p.isdigit() else p.lower() for p in parts]
        files.sort(key=natural_key)

        # reset individuals (avoid accumulation if called multiple times)
        self.individuals = []

        n_files = len(files)
        if n_files == 0:
            return

        # determine how many files to load (if k is None, load all)
        if k is None:
            to_load = n_files
        else:
            try:
                to_load = min(int(k), n_files)
            except (TypeError, ValueError):
                to_load = n_files

        for i, filename in enumerate(files[:to_load]):
            fullpath = os.path.join(folder_path, filename)
            knap_instance = Knapsack(fullpath)
            # ensure source_file recorded
            knap_instance.source_file = os.path.basename(fullpath)
            copy_inst = copy.deepcopy(knap_instance)
            self.individuals.append(copy_inst)
    
    def fill_population(self, size, first_individual: Knapsack):
        # keep for single-instance behaviour (creates `size` variants of one instance)
        for i in range(size):
            random_individual = copy.deepcopy(first_individual)
            random_individual.random_initialization()
            self.individuals.append(random_individual)
