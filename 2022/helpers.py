import os
import math

def read_input(filename):
    """Reads a file and returns a list of lines (strings)"""
    with open(filename) as source:
        return source.read().splitlines()

def get_input_filename(source):
    """Returns the standardized name of the input file"""
    return os.path.splitext(os.path.basename(source))[0] + ".in"

def get_digits(source):
    """Converts a string containing ints into a list with those ints"""
    return list(map(int, list(source.strip())))

def distance_2d(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
