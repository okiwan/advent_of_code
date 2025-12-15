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


def prepare_input_part_1():
    operations = []
    first_line = True
    total_lines = len(data)
    for line_idx, line in enumerate(data):
        operands = line.split(" ")
        operands_list = []
        for operand in operands:
            clean_operand = operand.strip()
            if clean_operand:
                operands_list.append(clean_operand)
        
        for idx, operand in enumerate(operands_list):
            if first_line:
                operations.append([[int(operand)], ""])
                continue

            if line_idx == total_lines - 1:
                operations[idx][1] = operand
                continue
  
            operations[idx][0].append(int(operand))

        first_line = False

    return operations

def combine_and_strip_zeros(string_list):
    combined_string = "".join(string_list)
    stripped_string = combined_string.rstrip('0')
    if not stripped_string:
        return 0
    final_integer = int(stripped_string)
    return final_integer

def prepare_input_part_2():
    operations = []

    # Let's find out the max length of the numbers
    max_number = 0
    for row in data[:-1]:
        row_numbers = [int(i) for i in row.strip().split(" ") if i]
        max_number = max(max_number, max(row_numbers))
    max_number_length = len(str(max_number))

    # Let's re-read the input, then split by chunks of max length + 1
    data_operands_raw = []
    for row in data[:-1]:
        operands_raw = [
            row[i : i + max_number_length]
            for i in range(0, len(row), max_number_length + 1)
        ]
        data_operands_raw.append(operands_raw)

    # Let's convert spaces into 0s
    data_operands_processed = [
        [element.replace(" ", "0") for element in row]
        for row in data_operands_raw
    ]

    # Let's transpose the numbers
    transposed_result_tuples = list(zip(*data_operands_processed))
    grouped_operands = [list(group) for group in transposed_result_tuples]

    # Let's transpose again each row
    final_operands = []
    for row in grouped_operands:
        transposed_result_tuples = list(zip(*row))
        final_operands.append([int(combine_and_strip_zeros("".join(list(group)))) for group in transposed_result_tuples])
  
    final_operands.reverse()
 
    # Let's operate
    operations = [row for row in data[-1] if row != ' ' and row != '\n']
    operations.reverse()
    for idx, element in enumerate(final_operands):
        final_operands[idx] = [element, operations[idx]]
    
    return final_operands


def perform_operations(numbers, op_str):
    from functools import reduce
    import operator

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow
    }
    op_func = ops.get(op_str)
    
    return reduce(op_func, numbers)

def calculate_total(input_formatting):
    input = input_formatting()
    total = 0
    for i in input:
        total += perform_operations(i[0], i[1])
    return total

"""
Part 1
"""
total = calculate_total(prepare_input_part_1)
print(f"> Part 1: {total}")

"""
Part 2
"""
total = calculate_total(prepare_input_part_2)
print(f"> Part 2: {total}")
