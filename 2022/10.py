import helpers

def render_problem_2(image):
    for x in range(6):
        base = x*40
        print(''.join(image[base:base+40]))

def solver_problem_2(problem_input):
    register_X = 1
    cycle = 0
    signal_strength = 0

    instruction_cycles = {
            "addx": 2,
            "noop": 1,
    }
    instruction_cycles_pending = 0
    instruction_pointer = -1
    image = [' ' for _ in range(240)]

    for execution_cycle in range(1, 240):
        if not instruction_cycles_pending:
            if instruction_pointer != -1 and problem_input[instruction_pointer][0] == 'addx':
                register_X += problem_input[instruction_pointer][1]

            instruction_pointer += 1
            if instruction_pointer < len(problem_input):
                instruction_cycles_pending = instruction_cycles[problem_input[instruction_pointer][0]]

        instruction_cycles_pending -= 1

        image[execution_cycle-1] = '#' if (execution_cycle-1)%40 >= register_X-1 and (execution_cycle-1)%40 <= register_X+1 else '.'

        if instruction_pointer >= len(problem_input):
            break

    return image

def solver_problem_1(problem_input):
    register_X = 1
    cycle = 0
    sampling_cycles = [20, 60, 100, 140, 180, 220]
    signal_strength = 0

    instruction_cycles = {
            "addx": 2,
            "noop": 1,
    }
    instruction_cycles_pending = 0
    instruction_pointer = -1

    for execution_cycle in range(1, 5000):
        if not instruction_cycles_pending:
            # Current instruction finished execution. Updating values
            if instruction_pointer != -1 and problem_input[instruction_pointer][0] == 'addx':
                register_X += problem_input[instruction_pointer][1]

            instruction_pointer += 1
            if instruction_pointer < len(problem_input):
                instruction_cycles_pending = instruction_cycles[problem_input[instruction_pointer][0]]

        instruction_cycles_pending -= 1

        if execution_cycle in sampling_cycles:
            signal_strength += execution_cycle * register_X

        if instruction_pointer >= len(problem_input):
            break

    return signal_strength

def main():
    problem_input = []

    source_filename = helpers.get_input_filename(__file__)
    with open(source_filename, 'r') as source:
        for line in source.readlines():
            elems = line.strip().split(' ')
            problem_input.append((elems[0], int(elems[1] if len(elems) > 1 else 0)))

    print(f"Question 1's answer is {solver_problem_1(problem_input)}")
    print("Question 2's answer is")
    output = solver_problem_2(problem_input)
    render_problem_2(output)

if __name__ == "__main__":
    main()
