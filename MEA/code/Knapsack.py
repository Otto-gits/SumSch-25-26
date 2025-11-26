from typing import Dict, Tuple
import os

#To injest the knapsack problem instance into a knapsack class
class Knapsack:
    def __init__(self, filename):
        self.capacity = 0
        self.num_items = 0
        self.items: Dict[int, Tuple[float, float]] = {}
        self.injest_knapsack_instance(filename)

    def injest_knapsack_instance(self, filename):
        here = os.path.dirname(__file__)
        data_path = os.path.join(here, '../instances', filename)

        with open(data_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                # Extract the number of items and capacity from the file
                if line.startswith('NUMBER OF ITEMS'):
                    parts = line.split(':')
                    self.num_items = int(parts[1].strip())
                elif line.startswith('CAPACITY OF KNAPSACK'):
                    parts = line.split(':')
                    self.capacity = int(parts[1].strip())
                # Extract item weights and values
                elif line.strip() == 'ITEMS SECTION':
                    for item_line in lines[i + 1: i + 1 + self.num_items]:
                        # Parse item id, profit, and weight from the items section
                        parts = item_line.split()
                        item_id, profit, weight = int(parts[0]) - 1, float(parts[1]), float(parts[2])  # to 0-based index
                        self.items[item_id] = (profit, weight)

                    break  
                
        
        def random_initialization():
            pass
        
        def fitness():
            pass
        
        def crossover(parent2):
            pass
        
        def mutate():
            pass
            