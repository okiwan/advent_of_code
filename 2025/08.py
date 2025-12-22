import copy

import sys
import heapq
from functools import cache
from pathlib import Path
from math import sqrt

# Processing arguments
use_test = sys.argv[1] == "--test" if len(sys.argv) > 1 else False

# Reading data from file
suffix = "input" if not use_test else "test"
current_filename = Path(__file__).stem
with open(f"{current_filename}-{suffix}.in") as f:
    data = [line.rstrip() for line in f.readlines()]

# Preparing input as list of points
points = [(int(i[0]), int(i[1]), int(i[2])) for i in [line.split(',') for line in data]]

"""
Part 1
"""

def calculate_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def get_circuits(limit=None):
    distance_matrix = [[0 for _ in range(len(points))] for _ in range(len(points))]
    distance_list = []
    circuits_reference = dict()
    circuits = []

    # Create distance matrix (not necessary) and list
    y = 0
    while y < len(points):
        x = 0
        while x != y:
            distance = calculate_distance(points[x], points[y])
            distance_matrix[x][y] = distance_matrix[y][x] = distance
            distance_list.append((x, y, distance))
            x += 1
        y += 1

    # Get sorted distance list
    distance_list = sorted(distance_list, key=lambda x: x[2])
   
    # Connect circuits
    for idx, element in enumerate(distance_list):
        if limit and idx > limit:
            break

        # print(f"Processing element {idx}") 

        e0_ref = f"{points[element[0]][0]}/{points[element[0]][1]}/{points[element[0]][2]}"
        e1_ref = f"{points[element[1]][0]}/{points[element[1]][1]}/{points[element[1]][2]}"
        e0_circuit = circuits_reference.get(e0_ref, -1)
        e1_circuit = circuits_reference.get(e1_ref, -1)
        circuit_no = -1

        if e0_circuit == -1 and e1_circuit == -1:
            # Two independent junction boxes. We need to connect them.
            # print(f"----{points[element[0]]} / {points[element[1]]} - Creating new circuit")
            circuits.append({points[element[0]], points[element[1]]})
            circuit_no = len(circuits) - 1
            circuits_reference[e0_ref] = circuit_no
            circuits_reference[e1_ref] = circuit_no

        elif e0_circuit != -1 and e1_circuit == -1:
            # Once independent and another in a circuit. Merging. (case 1)
            # print(f"----{points[element[0]]} / {points[element[1]]} - Add left")
            circuits[e0_circuit].add(points[element[1]])
            circuits_reference[e1_ref] = e0_circuit
            circuit_no = e0_circuit

        elif e0_circuit == -1 and e1_circuit != -1:
            # Once independent and another in a circuit. Merging. (case 2)
            # print(f"----{points[element[0]]} / {points[element[1]]} - Add right")
            circuits[e1_circuit].add(points[element[0]])
            circuits_reference[e0_ref] = e1_circuit
            circuit_no = e1_circuit

        elif e0_circuit != -1 and e1_circuit != -1:
            if e0_circuit == e1_circuit:
                # Both junction boxes belong to the same circuit. Ignore.
                # print(f"----{points[element[0]]} / {points[element[1]]} - Ignoring")
                pass
            else:
                # print(f"----{points[element[0]]} / {points[element[1]]} - Merge two circuits?")
                for point in circuits[e1_circuit]:
                    ref = f"{point[0]}/{point[1]}/{point[2]}"
                    circuits_reference[ref] = e0_circuit
                circuits[e0_circuit] |= circuits[e1_circuit]
                circuits[e1_circuit] = set()
                circuit_no = e0_circuit

        if not limit and len(circuits[circuit_no]) == len(points):
            return points[element[0]][0] * points[element[1]][0]
       
    # Sort circuits by length
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

    return circuits


def calculate_result():
    circuits = get_circuits(limit=1000)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

result = calculate_result()
print(f"> Part 1: {result}")


"""
Part 2
"""

def calculate_result_2():
    circuits = get_circuits()
    return circuits

result = calculate_result_2()
print(f"> Part 2: {result}")
