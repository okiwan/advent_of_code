
def read_input(filename):
    with open(filename) as fileinput:
        return fileinput.read().splitlines()

def get_item_priority(item):
    ascii_item = ord(item)
    base = 65
    offset = 27
    if ascii_item > 90:
        base = 97
        offset = 1

    priority = (ascii_item - base) + offset
    return priority

def get_rucksack_common_elements(rucksack):
    length = len(rucksack)
    first_compartment = set(rucksack[0:length//2])
    second_compartment = set(rucksack[length//2:])
    common_elements = first_compartment.intersection(second_compartment)
    # print(f"{first_compartment} x {second_compartment} = {common_elements}")
    return common_elements

def day03_question1(data):
    result = 0
    for rucksack in data:
        common_elements = get_rucksack_common_elements(rucksack)
        if len(common_elements):
            for element in common_elements: 
                result += get_item_priority(element) 

    return result

def get_rucksack_group_common_element(group_rucksack):
    temp_intersection = set(group_rucksack[0]).intersection(set(group_rucksack[1]))
    common_elements = set(group_rucksack[2]).intersection(temp_intersection)

    return get_item_priority(common_elements.pop()) 

def day03_question2(data):
    result = 0
    group_item = 0
    group_rucksack = []
    for rucksack in data:
        if group_item < 3:
            group_rucksack.append(rucksack)
            group_item += 1
        else:
            result += get_rucksack_group_common_element(group_rucksack)

            # Restart grouping
            group_item = 1
            group_rucksack = [rucksack]

    # Process last three lines
    result += get_rucksack_group_common_element(group_rucksack)

    return result

data = read_input("03.in")
result = day03_question1(data)
print(f"Question 1's result: {result}")
result = day03_question2(data)
print(f"Question 2's result: {result}")
