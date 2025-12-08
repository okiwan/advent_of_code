import sys
from pathlib import Path

# Processing arguments
use_test = sys.argv[1] == "--test" if len(sys.argv) > 1 else False

# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = f.readlines()

# Prepare data
clean_data = [entry.split("-") for entry in data[0].split(",")]

"""
Part 1
"""
def is_half_equal(number):
    s = str(abs(number))
    n = len(s)
    if n % 2 != 0:
        return False
    half_length = n // 2
    first_half = s[:half_length] 
    second_half = s[n - half_length:] 
    return first_half == second_half

adding_half_equals = 0
for checking_range in clean_data:
    for id in range(int(checking_range[0]), int(checking_range[1])+1):
        if is_half_equal(id):
            adding_half_equals += int(id)
        
print(f"> Part 1: {adding_half_equals}")

"""
Part 2
"""
def decompose(number, chunk_size = 1):
    fragments = []
    number_str = str(number)
    for i in range(0, len(number_str), chunk_size):
        fragment = number_str[i:i + chunk_size]
        fragments.append(int(fragment))
    return fragments

adding_patterns = 0
for checking_range in clean_data:
    for id in range(int(checking_range[0]), int(checking_range[1])+1):
        for chunk_size in range(len(str(id))//2, 0, -1):
            fragments = decompose(id, chunk_size+1)
            if len(fragments) >= 2 and len(set(fragments)) == 1:
                adding_patterns += id
                break
 
print(f"> Part 2: {adding_patterns}")
