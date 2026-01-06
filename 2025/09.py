import copy

import sys
import heapq
from functools import cache
from pathlib import Path
from math import sqrt

# Processing arguments
use_test = any(["--test" == arg for arg in sys.argv])
debug = any(["--debug" == arg for arg in sys.argv])


# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = [line.rstrip() for line in f.readlines()]

# Aux methods
def log(text):
    if not debug:
        return
    print(text)

"""
Part 1
"""

def calculate_area(tile_1, tile_2):
    x_diff = abs(tile_1[0] - tile_2[0]) + 1
    y_diff = abs(tile_1[1] - tile_2[1]) + 1
    return x_diff * y_diff

def calculate_result():
    """
    The input is small, so let's try brute force
    """

    # Process the points
    points = [(int(a[0]), int(a[1])) for a in [line.split(",") for line in data]]

    max_area = 0
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            max_area = max(max_area, calculate_area(points[i], points[j]))

    return max_area

result = calculate_result()
print(f"> Part 1: {result}")


"""
Part 2
"""

def calculate_result_2():
    """
    Our approach is going to avoid performing the calculation for every
    single combination, but rather select only the ones on the exterior
    side (creating king of a bound box) and then perform the calculation
    """
    return 0

result = calculate_result_2()
print(f"> Part 2: {result}")



