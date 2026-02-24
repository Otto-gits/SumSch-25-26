import copy
import re
from typing import Dict, Tuple
import os
import random
ITEMS_HEADER_RE = re.compile(r"^\s*ITEMS SECTION\s*\(INDEX,\s*PROFIT,\s*WEIGHT,\s*ASSIGNED NODE NUMBER\)\s*:\s*$")


#To injest the knapsack problem instance into a knapsack class
class Knapsack:
    def __init__(self, filename):
        self.capacity = 0
        self.num_items = 0
        self.items: Dict[int, Tuple[float, float]] = {} # item_id: (profit, weight)
        self.bitstring: list[int] = []
        self.fitness = 0
        if self.injest_knapsack_instance(filename) is None:
            self.injest_knapsack_instance_complex(filename)    

    def injest_knapsack_instance(self, filename):
        # print(f"Attempting to injest knapsack instance from {filename} using simple parser...")
        here = os.path.dirname(__file__)
        data_path = os.path.join(here, filename)
        # print(f"Injesting knapsack instance from {data_path}")
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
                elif line.strip() == 'ITEMS SECTION (INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER):':
                    # print("Injesting items...")
                    for item_line in lines[i + 1: i + 1 + self.num_items]:
                        # Parse item id, profit, and weight from the items section
                        parts = item_line.split()
                        # print(parts[0], parts[1], parts[2])
                        item_id, profit, weight = int(parts[0]) - 1, float(parts[1]), float(parts[2])  # to 0-based index
                        self.items[item_id] = (profit, weight)
                    self.create_initial_solution()
                    self.calc_fitness()
                    return True
                    # print("Initial valid solution bitstring:", self.bitstring)
                    # print("Initial valid solution fitness:", self.fitness())
                      
                
    def injest_knapsack_instance_complex(self, filename):
        # print(f"Attempting to injest knapsack instance from {filename} using complex parser...")
        here = os.path.dirname(__file__)
        data_path = os.path.join(here, filename)

        with open(data_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        self.num_items = None
        self.capacity = None

        for i, line in enumerate(lines):
            if line.startswith("NUMBER OF ITEMS"):
                self.num_items = int(line.split(":", 1)[1].strip())
                self.bitstring = [0] * self.num_items

                # Ensure items container exists and is sized
                if not hasattr(self, "items") or self.items is None:
                    self.items = {}
            elif line.startswith("CAPACITY OF KNAPSACK"):
                self.capacity = int(line.split(":", 1)[1].strip())
            elif ITEMS_HEADER_RE.match(line):
                if self.num_items is None:
                    raise ValueError("Found ITEMS SECTION before NUMBER OF ITEMS")

                read = 0
                j = i + 1
                while j < len(lines) and read < self.num_items:
                    parts = lines[j].split()
                    j += 1
                    if len(parts) < 3:
                        continue  # skip blank/bad lines

                    item_id = int(parts[0]) - 1
                    profit = int(parts[1])
                    weight = int(parts[2])
                    # node = int(parts[3]) if len(parts) >= 4 else None  # keep if needed later

                    self.items[item_id] = (profit, weight)
                    read += 1

                if read != self.num_items:
                    raise ValueError(f"Expected {self.num_items} items, read {read}")

                self.create_initial_solution()
                self.calc_fitness()
                return

        raise ValueError("Could not find ITEMS SECTION header in file")
                    
        
    def random_initialization(self):
        for i in self.items.keys():
            profit, weight = self.items[i]
            if (random.random() < 0.05 ) & (weight > 5):
                self.items[i] = (profit, weight - 5)
            elif random.random() > 0.95:
                self.items[i] = (profit, weight + 5)
        return self
    
    def create_initial_solution(self):
        for i in self.items.keys():
            if random.random() < 0.5:
                self.bitstring[i] = 1
            else:
                self.bitstring[i] = 0
        self.calc_fitness()
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
        self.calc_fitness()
        return self
        
    
    def calc_fitness(self):
        sum_profit = 0
        sum_weight = 0
        for i in self.items.keys():
            if self.bitstring[i] == 1:
                sum_profit += self.items[i][0]
                sum_weight += self.items[i][1]
        if sum_weight > self.capacity:
            #Should always be a negative number so less fit than any valid solution but we are prioritizing solutions that are close to the capacity
            self.fitness = self.capacity - sum_weight
        else:
            self.fitness = sum_profit
    
    def crossover(self, p2):
        # print(f"before: {self.bitstring}")    
        for i in range(len(self.bitstring)):
            if random.random() >= 0.5:
                self.bitstring[i] = p2.bitstring[i]
        # print(f"after: {self.bitstring}")
        return self
    
    # def crossover(self, p2):
    #     cnt = 0
    #     for i in self.bitstring:
    #         cnt += 1
    #         if random.random() >= 0.5:
    #             self.bitstring[i] = p2.bitstring[i]
    #     print("crossover processed genes:", cnt)
    #     return self
    
    def mutate(self):
        # print("Mutating individual...")
        for i in range(len(self.bitstring)):
            if random.random() < 1/self.num_items:
                self.bitstring[i] ^= 1
        return self

