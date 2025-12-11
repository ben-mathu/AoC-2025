import input_parser
from math import prod
from operator import itemgetter

coords = [tuple(map(int, line.strip().split(','))) for line in input_parser.get_lines(9)]

areas = {}
for i in range(len(coords)):
  for j in range(len(coords)):
    if i < j:
      p, q = coords[i], coords[j]
      area = prod([abs(p[0] - q[0]) + 1, abs(p[1] - q[1]) + 1])
      areas[(p, q)] = area
      
print(sorted(areas.items(), key=itemgetter(1))[-1])
      