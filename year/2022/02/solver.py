# We read the whole input of the file
with open("input.txt") as f:
    data = f.readlines()

def calculate_solution(input, game_config):
    # Let's calculate the score for the whole play
    total_score = 0
    for game in data:
        opponent_move = game[0]
        your_move = game[2]

        total_score += game_config[f"{opponent_move}{your_move}"]

    return total_score

"""
Question 1
"""
preconfig_game_1 = {
        # Draw
        "AX": 1+3,
        "BY": 2+3,
        "CZ": 3+3,

        # You win
        "AY": 2+6,
        "BZ": 3+6,
        "CX": 1+6,

        # Opponent wins
        "AZ": 3+0,
        "BX": 1+0,
        "CY": 2+0,
        }


print(calculate_solution(data, preconfig_game_1))

"""
Question 2
"""
preconfig_game_2 = {
        # Draw
        "AY": 1+3,
        "BY": 2+3,
        "CY": 3+3,

        # You win
        "AZ": 2+6,
        "BZ": 3+6,
        "CZ": 1+6,

        # Opponent wins
        "AX": 3+0,
        "BX": 1+0,
        "CX": 2+0,
        }


print(calculate_solution(data, preconfig_game_2))

