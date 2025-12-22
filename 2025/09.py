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

def calculate_result():
    return 0

result = calculate_result()
print(f"> Part 1: {result}")


"""
Part 2
"""

def calculate_result_2():
    return 0

result = calculate_result_2()
print(f"> Part 2: {result}")
