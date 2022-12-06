import sys
sys.path.append('../')

from utils.helpers import read_input

def is_marker(marker):
    return len(list(marker)) == len(set(marker))

def get_bytes_processed_before_marker(data, marker_length):
    processed_characters = marker_length
    current_marker_position = 0 
    
    found_marker = is_marker(data[current_marker_position::marker_length])
    while not found_marker:
       current_marker_position += 1
       processed_characters += 1
       found_marker = is_marker(data[current_marker_position:current_marker_position+marker_length])

    return processed_characters

data = read_input("input.txt")
print(get_bytes_processed_before_marker(data[0], 4))
print(get_bytes_processed_before_marker(data[0], 14))
    
