import helpers

def solver(problem_input, tail_size):
    visited_cells = {(0, 0)}

    head_pos = (0, 0)
    tail_knots =[(0, 0) for _ in range(tail_size)]

    for movement in problem_input:
        dx = 0
        dy = 0
        if movement[0] == 'U':
            dy = 1
        elif movement[0] == 'D':
            dy = -1
        elif movement[0] == 'L':
            dx = -1
        elif movement[0] == 'R':
            dx = 1

        steps = movement[1]
        for _ in range(steps):
            # This one is the head
            previous_knot = (head_pos[0] + dx, head_pos[1] + dy)
            head_pos = previous_knot

            for tail_knot in range(tail_size):
                tail_pos = tail_knots[tail_knot]
                distance = helpers.distance_2d(previous_knot, tail_pos)

                if distance >= 1.9:
                    # Move tail
                    mov_delta_x = previous_knot[0] - tail_pos[0]
                    mov_delta_y = previous_knot[1] - tail_pos[1]

                    tail_dx = 1 if mov_delta_x > 0 else -1 if mov_delta_x < 0 else 0
                    tail_dy = 1 if mov_delta_y > 0 else -1 if mov_delta_y < 0 else 0
                    tail_knots[tail_knot] = (tail_pos[0] + tail_dx, tail_pos[1] + tail_dy)

                previous_knot = tail_knots[tail_knot]

            # Update positions list
            visited_cells.add(tail_knots[-1])

    #print(visited_cells)
    return len(visited_cells)

def solver_problem_1(problem_input):
    return solver(problem_input, 1)

def solver_problem_2(problem_input):
    return solver(problem_input, 9)

def main():
    problem_input = []

    source_filename = helpers.get_input_filename(__file__)
    with open(source_filename, 'r') as source:
        for line in source.readlines():
            elems = line.strip().split(' ')
            problem_input.append((elems[0], int(elems[1])))

    print(f"Question 1's answer is {solver_problem_1(problem_input)}")
    print(f"Question 2's answer is {solver_problem_2(problem_input)}")

if __name__ == "__main__":
    main()
