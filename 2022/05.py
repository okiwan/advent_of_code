import copy
from helpers import read_input

data = read_input("05.in")


def parse_crane_config(data):
    output = {}

    # Let's start by only retrieving the required information
    raw_crane_config = []
    for data_line in data:
        if not data_line:
            break
        else:
            raw_crane_config.append(data_line)
    raw_crane_config = raw_crane_config[::-1]

    # Let's get the reading position of each stack
    stacks_position = {}
    for i in range(0, len(raw_crane_config[0])):
        if raw_crane_config[0][i].strip():
            stacks_position[raw_crane_config[0][i]] = i
    raw_crane_config = raw_crane_config[1:]

    # Time to store the stack references into lists
    for config_line in raw_crane_config:
        for stack in stacks_position.keys():
            value = config_line[stacks_position[stack]].strip()
            if not value:
                continue

            if stack in output:
                output[stack].append(value)
            else:
                output[stack] = [value]

    return(output) 

def parse_arrangements(data):
    # Let's start by only retrieving the required information
    output = []
    process_line = False
    for data_line in data:
        if not data_line:
            process_line = True
        elif process_line:
            move_info = data_line.split(' ')
            output.append([(move_info[1], move_info[3], move_info[5])])

    return output

def print_top_stack(cc):
    output = []
    for stack in cc.values():
        if stack[-1]:
            output.append(stack[-1])

    return ''.join(output)

def apply_arrangements_9000(cc, ac):
    for move in ac:
        n, src, dst = move[0]
        for i in range(0, int(n)):
            try:
                tmp = cc[src].pop()
                cc[dst].append(tmp)
            except:
                continue

def apply_arrangements_9001(cc, ac):
    for move in ac:
        n, src, dst = move[0]
        tmp = []
        for i in range(0, int(n)):
            try:
                tmp.append(cc[src].pop())
            except:
                continue
        #print(tmp)
        cc[dst].extend(tmp[::-1])

original_crane_config = parse_crane_config(data)
arrange_config = parse_arrangements(data)

# Question 1
crane_config = copy.deepcopy(original_crane_config)
apply_arrangements_9000(crane_config, arrange_config)
print(f"Question 1's answer is {print_top_stack(crane_config)}")

# Question 2
crane_config = copy.deepcopy(original_crane_config)
apply_arrangements_9001(crane_config, arrange_config)
print(f"Question 2's answer is {print_top_stack(crane_config)}")
