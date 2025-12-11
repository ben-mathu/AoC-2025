"""
Find tutorial from here: https://youtu.be/-w5mFTtRLE8?si=z3XdQz9-ZN0_2Ve5
Used 0xdf's solution to find my answer 
"""
from input_parser import get_lines
from math import pow
from operator import itemgetter
from functools import cache

coords = [tuple(map(int, line.strip().split(','))) for line in get_lines(9)]
# print(coords)

def get_area(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + 1) *(abs(coord1[1] - coord2[1]) + 1)

areas = []
for i in range(len(coords)):
    for j in range(len(coords)):
        if i < j:
            area = get_area(coords[i], coords[j])
            areas.append((area, coords[i], coords[j]))

print(f'Part 1: {sorted(areas, reverse=True)[:1]}')

def between_points(p, point, q):
    return (point[0] <= max(p[0], q[0]) and point[0] >= min(p[0], q[0]) and point[1] <= max(p[1], q[1]) and point[1] >= min(p[1], q[1]))

def point_in_poly(point):
    inside = False
    points = list(zip(coords, coords[1:] + coords[:1]))
    for (x1, y1), (x2, y2) in points:
        if (point[0] == x1 == x2 and min(y1, y2) <= point[1] <= max(y1, y2) or
            point[1] == y1 == y2 and min(x1, x2) <= point[0] <= max(x1, x2)):
            return True
        if ((y1 > point[1]) != (y2 > point[1])) and (point[0] < (x2 - x1) * (point[1] - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def orientation(p, point, q):
    val = (point[1] - p[1]) * (q[0] - point[0]) - (point[0] - p[0]) * (q[1] - point[1])

    if val == 0:
        return 0
    
    return 1 if val > 0 else 2

def do_intersect(p, point, q):
    o1 = orientation(p, point, q)
    if o1 == 0 and between_points(p, point, q):
        return True
    return False

@cache
def find_intersection(coords, point):
    for k in range(len(coords)):
        for l in range(len(coords)):
            if k < l:
                p, q = coords[k], coords[l]
                found_within = do_intersect(p, point, q)
                if found_within:
                    break
        if found_within:
            break

def edge_intersects_rect(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
    if ey1 == ey2:
        if y1 < ey1 < y2:
            if max(ex1, ex2) > x1 and min(ex1, ex2) < x2:
                return True
    else:
        if x1 < ex1 < x2:
            if max(ey1, ey2) > y1 and min(ey1, ey2) < y2:
                return True
    return False

def valid_poly(p, q):
    x1, x2 = sorted([p[0], q[0]])
    y1, y2 = sorted([p[1], q[1]])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        if not point_in_poly((x, y)):
            return False
    
    for (ex1, ey1), (ex2, ey2) in zip(coords, coords[1:] + coords[:1]):
        if edge_intersects_rect(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
            return False

    return True
part2 = 0
for i in range(len(coords)):
    for j in range(len(coords)):
        if i < j:
            p, q = coords[i], coords[j]

            # if coords[i][0] > coords[j][0]:
            #     point = (coords[j][0], coords[i][1])
            # elif coords[i][0] < coords[j][0]:
            #     point = (coords[i][0], coords[j][1])
            # else:
            #     area = get_area(coords[j], coords[i])
            #     new_areas.append((area, coords[i], coords[j]))
            #     continue

            # found_within = False
            # for k in range(len(coords)):
            #     for l in range(len(coords)):
            #         if k < l:
            #             p, q = coords[k], coords[l]
            #             found_within = do_intersect(p, point, q)
            #             if found_within:
            #                 break
            #     if found_within:
            #         break
            # if found_within:

            area = get_area(coords[i], coords[j])
            if area > part2 and valid_poly(p, q):
                part2 = area
    
print(f'Part 2: {part2}')