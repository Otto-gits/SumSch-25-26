import copy
from typing import Dict, Tuple
import os
import random

#To injest the knapsack problem instance into a knapsack class
class Knapsack:
    def __init__(self, filename):
        self.capacity = 0
        self.num_items = 0
        self.items: Dict[int, Tuple[float, float]] = {} # item_id: (profit, weight)
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
                elif line.strip() == 'ITEMS SECTION	(INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER):':
                    print("Injesting items...")
                    for item_line in lines[i + 1: i + 1 + self.num_items]:
                        # Parse item id, profit, and weight from the items section
                        parts = item_line.split()
                        print(parts[0], parts[1], parts[2])
                        item_id, profit, weight = int(parts[0]) - 1, float(parts[1]), float(parts[2])  # to 0-based index
                        self.items[item_id] = (profit, weight)
                    self.create_initial_solution()
                    print("Initial valid solution bitstring:", self.bitstring)
                    print("Initial valid solution fitness:", self.fitness())
                    break  
                
        
    def random_initialization(self):
        for i in self.items.keys():
            profit, weight = self.items[i]
            if (random.random() < 0.05 ) & (weight > 5):
                self.items[i] = (profit, weight - 5)
            elif random.random() > 0.95:
                self.items[i] = (profit, weight + 5)
        self.create_valid_p2w_solution()
        return self
    
    def create_initial_solution(self):
        for i in self.items.keys():
            if random.random() < 0.5:
                self.bitstring[i] = 1
            else:
                self.bitstring[i] = 0
        return self
    
    def create_valid_p2w_solution(self):
        sorted_items = sorted(self.items.items(), key=lambda x: x[1][0]/x[1][1], reverse=True) # Sort by profit-to-weight ratio
        total_weight = 0
        for item_id, (profit, weight) in sorted_items:
            if total_weight + weight <= self.capacity:
                self.bitstring[item_id] = 1
                total_weight += weight
            else:
                self.bitstring[item_id] = 0
        return self
        
    
    def fitness(self):
        sum_profit = 0
        sum_weight = 0
        for i in self.items.keys():
            if self.bitstring[i] == 1:
                sum_profit += self.items[i][0]
                sum_weight += self.items[i][1]
        if sum_weight > self.capacity:
            #Should always be a negative number so less fit than any valid solution but we are prioritizing solutions that are close to the capacity
            return self.capacity -  sum_weight
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
        # print("Mutating individual...")
        for i in range(self.num_items):
            if random.random() < 1/self.num_items:
                self.bitstring[i] ^= 1
        return self

