from helpers import read_input

data = read_input("04.in")
fully_overlap = 0
partial_overlap = 0

for maps in data:
    map_a, map_b = maps.split(',')

    limits_a = map_a.split('-')
    limits_b = map_b.split('-')

    limits_a_inf = int(limits_a[0])
    limits_a_sup = int(limits_a[1])
    limits_b_inf = int(limits_b[0])
    limits_b_sup = int(limits_b[1])

    map_a_expanded = list(range(limits_a_inf, limits_a_sup + 1))
    map_b_expanded = list(range(limits_b_inf, limits_b_sup + 1))
    intersection = set(map_a_expanded).intersection(set(map_b_expanded))

    # Options B: check limits manually using if/and/or conditionals

    if intersection and (len(intersection) == len(map_a_expanded) or len(intersection) == len(map_b_expanded)):
        fully_overlap += 1
        partial_overlap += 1

    if intersection and len(intersection) != len(map_a_expanded) and len(intersection) != len(map_b_expanded): 
        print(f"{limits_a_inf}-{limits_a_sup} / {limits_b_inf}-{limits_b_sup}")
        partial_overlap += 1

print(f"Fully overlap on {fully_overlap} groups")
print(f"Partial overlap op {partial_overlap} groups")

