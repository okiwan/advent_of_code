import os

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
