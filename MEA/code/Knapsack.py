import copy
from typing import Dict, Tuple
import os
import random

#To injest the knapsack problem instance into a knapsack class
class Knapsack:
    def __init__(self, filename):
        self.capacity = 0
        self.num_items = 0
        self.items: Dict[int, Tuple[float, float]] = {}
        self.bitstring: list[int] = []
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
                    self.bitstring = [0] * self.num_items
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
                
        
    def random_initialization(self):
        for i in self.items.keys():
            profit, weight = self.items[i]
            if random.random() < 0.05:
                self.items[i] = (profit, weight - 5)
            elif random.random() > 0.95:
                self.items[i] = (profit, weight + 5)
        return self
    
    def fitness(self):
        sum_profit = 0
        sum_weight = 0
        for i in self.items.keys():
            if self.bitstring[i] == 1:
                sum_profit += self.items[i][0]
                sum_weight += self.items[i][1]
        if sum_weight > self.capacity:
            return self.capacity - sum_weight
        else:
            return sum_profit
    
    def crossover(self, p2):
        n = len(self.bitstring)
        point = random.randint(1, n - 1)

        c1_bitstring = self.bitstring[:point] + p2.bitstring[point:]
        c2_bitstring = p2.bitstring[:point] + self.bitstring[point:]
        
        # Create new Knapsack objects with child bitstrings
        child1 = copy.deepcopy(self)
        child1.bitstring = c1_bitstring
        
        child2 = copy.deepcopy(self)
        child2.bitstring = c2_bitstring
        
        return child1, child2
        
    
    def mutate(self):
        for i in range(self.num_items):
            if random.random() < 0.2:
                self.bitstring[i] ^= 1
        return self

