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
clean_data = [entry.strip() for entry in data]

"""
Part 1
"""

def get_max_from_range(start, end, bank):
    # print(f"get_max_from_range: {start}, {end}")
    current_bank_index = start 
    current_joltage = bank[current_bank_index]
    for index_1 in range(start + 1, end):
        if bank[index_1] > current_joltage:
            current_joltage = bank[index_1]
            current_bank_index = index_1

    return current_bank_index, current_joltage

def get_max_joltage(num_digits):
    total_joltage = 0

    for bank in clean_data:
        bank_batteries = [int(digit) for digit in str(bank)]
        bank_indexes = [0, len(bank_batteries)]

        bank_joltage = [None] * num_digits
        bank_joltage_index = 0
        for i in range(num_digits, 0, -1):
            index, max_joltage = get_max_from_range(bank_indexes[0], bank_indexes[1] - (i - 1), bank_batteries)
            bank_joltage[bank_joltage_index] = max_joltage
            bank_joltage_index += 1
            bank_indexes[0] = index + 1

        total_joltage += int("".join(str(x) for x in bank_joltage))

    return total_joltage

print(f"> Part 1: {get_max_joltage(2)}")

"""
Part 2
"""
print(f"> Part 2: {get_max_joltage(12)}")
