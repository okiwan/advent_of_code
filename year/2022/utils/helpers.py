def read_input(filename):
    with open(filename) as source:
        return source.read().splitlines()
