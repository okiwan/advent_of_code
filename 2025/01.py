import sys
from pathlib import Path

# Processing arguments
use_test = sys.argv[1] == "--test" if len(sys.argv) > 1 else False

# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = f.readlines()
clean_data = [line.strip() for line in data]

"""
Part 1
"""
final_position = 50
exact_0s = 0
passing_0s = 0
for move in clean_data:
    # Backup
    original_position = final_position

    # Calculations
    sign = -1 if move[0] == "L" else 1
    full_rounds = int(int(move[1:]) / 100)
    moving_steps = int(move[1:]) - (full_rounds * 100)
    current_result = original_position + (sign * moving_steps)
    final_position = current_result % 100

    # Updating stats
    passing_0s += full_rounds    
    if (current_result < 0 and original_position != 0) or (int(current_result / 100) > 0 and final_position != 0): 
        passing_0s += 1
    if final_position == 0:
        exact_0s += 1

    print(f"Step: Original[{original_position}] Move[{move}] Current[{current_result}] Final[{final_position}] Exact 0s[{exact_0s}] Passing 0s[{passing_0s}]")

"""
Part 2
"""
print(f"> Part 2: {exact_0s + passing_0s}")
