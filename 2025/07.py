import copy

import sys
import heapq
from functools import cache
from pathlib import Path

# Processing arguments
use_test = sys.argv[1] == "--test" if len(sys.argv) > 1 else False

# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = [line.rstrip() for line in f.readlines()]


"""
Part 1
"""

def count_splits():
    def get_key(y, x):
        return str(y) + str(x)

    splits = 0
    split_dict = dict()

    # Let's add the first ray
    x = data[0].index('S')
    split_list = [(0, x)]
    y = 1

    while y < len(data):
        split_dict = dict()
        for split in split_list:
            if data[y][split[1]] == '.':
                split_dict[str(y) + str(split[1])] = (y, split[1])
                continue
            if data[y][split[1]] == '^':
                splits += 1
                if split[1] == 0:
                    split_dict[str(y) + str(split[1]+1)] = (y, split[1]+1)
                elif split[1] == len(data[0]) - 1:
                    split_dict[str(y) + str(split[1]-1)] = (y, split[1]-1)
                else:
                    split_dict[str(y) + str(split[1]+1)] = (y, split[1]+1)
                    split_dict[str(y) + str(split[1]-1)] = (y, split[1]-1)
                continue
        split_list = split_dict.values() 
        y += 1
 
    return splits

result = count_splits()
print(f"> Part 1: {result}")


"""
Part 2
"""

@cache
def count_timelines_rec(y, x):
    if y == len(data) - 1:
        return 1
    else:
        if data[y][x] == '.':
            next_timelines = count_timelines_rec(y + 1, x)
            return next_timelines
        if data[y][x] == '^':
            next_timelines_left = count_timelines_rec(y, x + 1)
            next_timelines_right = count_timelines_rec(y, x - 1)
            return next_timelines_left + next_timelines_right
            
def count_timelines():
    timelines = 0

    y = 0
    x = data[0].index('S')

    timelines = count_timelines_rec(y + 1, x)
      
    return timelines

result = count_timelines()
print(f"> Part 2: {result}")
