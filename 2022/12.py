import copy
import helpers

def get_input_data():
    source_filename = helpers.get_input_filename(__file__)
    source_handler = open(source_filename, 'r')
    data = source_handler.read().split('\n')
    return data[0:len(data)-1]

"""
    First implementation. This is just a plain and simple backtracking, which
    obviously will have a terrible performance as the input starts to grow.

    The problem here is that we are looking by depth and this is the worst
    possible strategy witout any kind of prunning, which is not the case

    SO, it is time to change the strategy and start looking using a breadth
    search. The only problem with breadth is that you quickly have a huge
    list of potential candidates to choose from, so you need to take advantage
    of some kind of data structure to take the best one (in this case, the base
    with least cost). For that we could use a heap.

    def _get_pos(position, data):
        for y in range(len(data)):
            if position in data[y]:
                x = data[y].find(position)
                return y, x 

    def _get_value(c_y, c_x, d):
        if d[c_y][c_x] == 'E':
            return ord('z')
        if d[c_y][c_x] == 'S':
            return ord('a')
        return ord(d[c_y][c_x])

    def _next_move(c_x, c_y, d_x, d_y, d, v):
        best_result = 100000000
        found = False

        # Base case
        current_value = d[c_y][c_x]
        if current_value == 'E':
            return 1, True

        # Calculate possible moves
        possible_directions = []
        # Up
        new_y = c_y - 1
        new_x = c_x
        if new_y >= 0 and abs(_get_value(new_y, c_x, d) - _get_value(c_y, c_x, d)) <= 1 and (new_y, new_x) not in v:
            possible_directions.append((new_y, new_x))
        # Down
        new_y = c_y + 1
        new_x = c_x
        if new_y < len(d) and abs(_get_value(new_y, c_x, d) - _get_value(c_y, c_x, d)) <= 1 and (new_y, new_x) not in v:
            possible_directions.append((new_y, new_x))
        # Left
        new_y = c_y
        new_x = c_x - 1
        if new_x >= 0 and abs(_get_value(c_y, new_x, d) - _get_value(c_y, c_x, d)) <= 1 and (new_y, new_x) not in v:
            possible_directions.append((new_y, new_x))
        # Right
        new_y = c_y
        new_x = c_x + 1
        if new_x < len(d[0]) and abs(_get_value(c_y, new_x, d) - _get_value(c_y, c_x, d)) <= 1 and (new_y, new_x) not in v:
            possible_directions.append((new_y, new_x))

        #print(f"{c_y},{c_x} - {possible_directions}")

        for move in possible_directions:
            print(f"Trying from {c_y},{c_x} to {move[0]},{move[1]}")
            new_v = copy.deepcopy(v)
            new_v.append((move[0], move[1]))
            steps, end_reached = _next_move(move[1], move[0], d_x, d_y, d, new_v)
            if end_reached:
                best_result = min(best_result, steps+1)
                found = True

        return best_result, found

    def calculate_steps(data):
        steps = 0
        end_reached = False

        src_y, src_x = _get_pos('S', data)
        current_x = src_x
        current_y = src_y
        dst_y, dst_x = _get_pos('E', data)
        #print(f"Origin {src_x},{src_y} / Destination {dst_x},{dst_y}")

        steps = _next_move(current_x, current_y, dst_x, dst_y, data, [(current_y, current_x)])
        return steps
"""

def _get_position(value, data):
    for y in range(len(data)):
        if value in data[y]:
            x = data[y].find(value)
            return y, x

def _get_value(position, d):
    y, x = position
    if d[y][x] == 'E':
        return ord('z')
    if d[y][x] == 'S':
        return ord('a')

    return ord(d[c_y][c_x])

def get_shortest_distance(start_position, data):
    def shortest_path(start, end, data):
        from heapq import heappop, heappush
        import time
        
        visited = {start}
        next_nodes = [(0, start)]

        while True:
            if len(next_nodes) == 0:
                return 2e64

            steps, position = heappop(next_nodes)
            if position == end:
                return steps

            # Calculate next moves
            # Let's start by getting the neightbours
            neightbours = []
            final_neightbours = []
            n_y = position[0]
            n_x = position[1]
            if n_y-1 >= 0:
                neightbours.append((n_y-1, n_x))
            if n_y+1 < len(data):
                neightbours.append((n_y+1, n_x))
            if n_x-1 >= 0:
                neightbours.append((n_y, n_x-1))
            if n_x+1 < len(data[0]):
                neightbours.append((n_y, n_x+1))
            # We only want neightbours that are max +1 in height
            char = data[n_y][n_x]
            value = ord('a') if char == 'S' else ord(char)
            for ny, nx in neightbours:
                new_char = data[ny][nx]
                new_value = ord(new_char) if new_char.islower() else ord('z')
                if new_value - value <= 1:
                    final_neightbours.append((1, (ny, nx)))

            for cost, n in final_neightbours:
                if n in visited:
                    continue

                visited.add(n)
                heappush(next_nodes, (steps+cost, n))

    end_position = _get_position('E', data)
    return shortest_path(start_position, end_position, data)

def eval_shortest_path(data):
    min_steps = 2e64
    
    candidates = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'a':
                candidates.append((y, x))

    for candidate in candidates:
        steps = get_shortest_distance(candidate, data)
        min_steps = min(steps, min_steps)

    return min_steps

def main():
    data = get_input_data()
    sp_y, sp_x = _get_position('S', data)
    steps = get_shortest_distance((sp_y, sp_x), data)
    print(f"Question 1's answer is {steps}") 

    patch_y, patch_x = _get_position('S', data)
    data[patch_y] = data[patch_y].replace('S', 'a')


    steps = eval_shortest_path(data)
    print(f"Question 2's answer is {steps}") 


if __name__ == "__main__":
    main()
