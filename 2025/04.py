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

# Prepare data
clean_data = [list(line.strip()) for line in data]

"""
Part 1
"""

def is_position_busy(matrix, y, x):
    if y < 0 or x < 0 or y >= len(matrix) or x >= len(matrix[0]):
        return False

    if matrix[y][x] == "@":
        return True

    return False
 
def get_adjacent_rolls(matrix, y, x):
    adjacent_rolls = 0

    adjacent_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in adjacent_positions:
        is_busy = is_position_busy(matrix, y + i[0], x + i[1])
        adjacent_rolls += 1 if is_busy else 0

    return adjacent_rolls
  

def remove_rolls(matrix, limit): 
    total_accessible_rolls = 0
    total_executions = 0
    updated_map = copy.deepcopy(matrix)

    while True:
        pass_accessible_rolls = 0
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                if matrix[y][x] == ".":
                    continue

                adjacent_rolls = get_adjacent_rolls(matrix, y, x)
                if adjacent_rolls < 4:
                    updated_map[y][x] = "."
                    total_accessible_rolls += 1
                    pass_accessible_rolls += 1

        total_executions += 1
        matrix = copy.deepcopy(updated_map)
        if pass_accessible_rolls == 0 or total_executions == limit:
            break

    return total_accessible_rolls

matrix = copy.deepcopy(clean_data)
print(f"> Part 1: {remove_rolls(matrix, 1)}")

"""
Part 2
"""
matrix = copy.deepcopy(clean_data)
print(f"> Part 2: {remove_rolls(matrix, 1000)}")
