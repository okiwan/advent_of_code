import copy
import helpers

def get_input_data():
    source_filename = helpers.get_input_filename(__file__)
    source_handler = open(source_filename, 'r')
    data = source_handler.read().split('\n')
    return data[0:len(data)-1]

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

def main():
    data = get_input_data()
    steps = calculate_steps(data)
    print(f"Question 1's answer is {steps}") 

if __name__ == "__main__":
    main()
