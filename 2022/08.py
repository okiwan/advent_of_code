import helpers

def get_direction_heights(problem_input, y, x):
    return [
        [problem_input[up][x] for up in range(y-1, -1, -1)],
        [problem_input[down][x] for down in range(y+1, len(problem_input))],
        [problem_input[y][left] for left in range(x-1, -1, -1)],
        [problem_input[y][right] for right in range(x+1, len(problem_input[0]))],
    ]


def solver_problem_1(problem_input):
    visible_trees = 0

    # Assuming here it is a matrix
    height = len(problem_input)
    width = len(problem_input[0])

    for y in range(height):
        for x in range(width):
            """
            From a tree, we need to process its four directions.
            For each direction, we need to make sure all heights are lower than the current height of the tree.
            If any of the directions checks the previous statement, the tree is visible
            """
            current_tree_height = problem_input[y][x]

            if any(
                len(direction) == 0 or all(tree_height < current_tree_height for tree_height in direction)
                for direction in get_direction_heights(problem_input, y, x)
            ):
                visible_trees += 1

    return visible_trees

def solver_problem_2(problem_input):
    max_scenic_score = 0

    # Assuming here it is a matrix
    height = len(problem_input)
    width = len(problem_input[0])

    for y in range(height):
        for x in range(width):
            current_tree_scenic_score = 1
            current_tree_height = problem_input[y][x]
            for direction in get_direction_heights(problem_input, y, x):
                distance = 0
                # print(direction)
                for tree in direction:
                    distance += 1
                    if tree >= current_tree_height:
                        break

                current_tree_scenic_score *= distance
              
            # print(f"For node {current_tree_height}, scenic score is {current_tree_scenic_score}")
            max_scenic_score = max(max_scenic_score, current_tree_scenic_score)

    return max_scenic_score

def main():
    problem_input = []

    source_filename = helpers.get_input_filename(__file__)
    with open(source_filename, 'r') as source:
        for line in source.readlines():
            problem_input.append(helpers.get_digits(line))

    print(f"Question 1's answer is {solver_problem_1(problem_input)}")
    print(f"Question 2's answer is {solver_problem_2(problem_input)}")

if __name__ == "__main__":
    main()
