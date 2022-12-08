"""
Part 1
"""

# Reading data from file
with open("01.in") as f:
    data = f.readlines()

elves_calories = []
current_calories = 0

for calories in data:
    try:
        int_calories = int(calories)
    except:
        int_calories = 0

    if int_calories:
        current_calories += int_calories
    else:
        elves_calories.append(current_calories)
        current_calories = 0

print(f"> Part 1: {max(elves_calories)}")

"""
Part 2
"""
sorted_elves_calories = sorted(elves_calories)
reverse_sec = sorted_elves_calories[::-1]

print(f"> Part 2: {reverse_sec[0]+reverse_sec[1]+reverse_sec[2]}")
