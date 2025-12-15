import copy

import sys
import heapq
from pathlib import Path

# Processing arguments
use_test = sys.argv[1] == "--test" if len(sys.argv) > 1 else False

# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = f.readlines()

def prepare_inputs():
    fresh_lookup_table = []
    ingredients_available = []
    insertion = 1

    for line in data:
        clean_line = line.strip()

        if len(clean_line) == 0:
            insertion = 0
            continue

        if insertion:
            fresh_id_range = clean_line.split("-")
            fresh_lookup_table.append([int(fresh_id_range[0]), int(fresh_id_range[1])])

        if not insertion:
            ingredients_available.append(int(clean_line))
        
    return fresh_lookup_table, ingredients_available

"""
Part 1
"""

lookup_table, ingredients = prepare_inputs()

fresh_ingredients_counter = 0
for ingredient in ingredients:
    for reference in lookup_table:
        if reference[0] <= ingredient <= reference[1]:
            fresh_ingredients_counter += 1
            break
  
print(f"> Part 1: {fresh_ingredients_counter}")

"""
Part 2
"""

lookup_table_sorted = sorted(lookup_table, key=lambda item: item[0])

new_lookup_table = []
for element_to_sort in lookup_table_sorted:
    placed = False
    # print(f"Sorting element {element_to_sort}") 
    for idx, v in enumerate(new_lookup_table):
        if new_lookup_table[idx][1] < element_to_sort[0]:
            # Ranges to not overlap. Do nothing
            continue

        if new_lookup_table[idx][0] <= element_to_sort[0]:
           if new_lookup_table[idx][1] >= element_to_sort[1]:
               # The new range is already in the current one. Do nothing
               placed = True
               break
           else:
               # Here the new range has more elements than the old one.
               # Let's calculate the range outside and continue its processing
               element_to_sort[0] = new_lookup_table[idx][1] + 1
               continue

    # We reach the end of the table without positioning. Adding at the end
    if not placed:
        new_lookup_table.append(element_to_sort)

total_fresh_ingredient_references = 0
for id_range in new_lookup_table:
    total_fresh_ingredient_references += id_range[1] - id_range[0] + 1

print(f"> Part 2: {total_fresh_ingredient_references}")
