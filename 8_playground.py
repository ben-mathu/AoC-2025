from input_parser import get_lines
from math import sqrt, pow
from math import prod
from collections import defaultdict
import operator

def parse_tuple(point: str):
    return tuple(map(lambda e: int(e), point.split(',')))

def find_distance(start: tuple, end: tuple):
    return pow(start[0] - end[0], 2) + pow(start[1] - end[1], 2) + pow(start[2] - end[2], 2)

def find_in(memo, pos):
    for key in memo:
        if pos in key:
            return True
    return False

def found_in(connections, pos):
    for connection in connections:
        if pos in connection:
            return connections.index(connection)
    return None

coords = [tuple(map(int, line.split(','))) for line in get_lines(8)]
distances = {}
for i in range(len(coords)):
    for j in range(len(coords)):
        if i < j:
            d = find_distance(coords[i], coords[j])
            distances[(i, j)] = d

parent = {i: i for i in range(len(coords))}
# print(parent)

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def merge_sets(a, b):
    parent[find_set(b)] = find_set(a)

connections = 10 if len(coords) == 20 else 1000
wire_count = 0
for i, k in enumerate(dict(sorted(distances.items(), key=operator.itemgetter(1)))):
    if i == connections:
        sizes = defaultdict(int)
        for x in range(len(coords)):
            sizes[find_set(x)] += 1

        print(prod(sorted(sizes.values(), reverse=True)[:3]))

    n_set = find_set(k[0])
    m_set = find_set(k[1])
    if n_set != m_set:
        wire_count+=1
        merge_sets(k[0], k[1])
        if wire_count == len(coords)-1:
            print(prod([coords[k[0]][0], coords[k[1]][0]]))
            break