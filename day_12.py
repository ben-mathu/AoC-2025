from input_parser import get_lines
import math

def parse_input(lines):
    line_index = 0
    present_index = 0
    shapes = {}
    for l in lines:
        if 'x' in l:
            line_index = lines.index(l)
            break
        elif ':' in l:
            present_index = int(l.split(':')[0])
            continue
        elif '' == l:
            continue

        row = [p for p in l]
        if present_index in shapes:
            shapes[present_index].append(row)
        else:
            shapes[present_index] = [row]
    
    regions = lines[line_index:]
    temp_shapes = shapes.copy()

    rotation_map = {(0,0): (0,2), (0,1): (1,2), (0,2): (2,2), (1,2): (2,1), (2,2): (2,0), (2,1): (1,0), (2,0): (0,0), (1,0): (0,1)}
    for k in temp_shapes:
        shapes[k] = [temp_shapes[k]]
        for i in range(3):
            tmp_shape = shapes[k][-1]
            r_shape = [['.', '.', '.'] for j in range(3)]
            for j in range(len(tmp_shape)):
                for l in range(len(tmp_shape[j])):
                    if j == l == 1:
                        r_shape[j][l] = tmp_shape[j][l]
                    else:
                        r_shape[rotation_map[(j,l)][0]][rotation_map[(j,l)][1]] = tmp_shape[j][l]
            shapes[k].append(r_shape)
    return temp_shapes, shapes, regions

# Part 1 example
lines = get_lines(12, 'e')
shapes, rotated_shapes, regions = parse_input(lines)
count = 0
for region in regions:
    r_inputs = region.split(':')
    area = math.prod(list(map(int, r_inputs[0].split('x'))))
    print('Calculating region: ', region)
    print('region area:', area)
    total_shapes_area = 0
    for i, v in enumerate(r_inputs[1].strip().split(' ')):
        shape_area = 0
        for t_row in shapes[i]:
            for t in t_row:
                if t == '#':
                    shape_area += 1
        total_shapes_area += shape_area * int(v)
    print('Total shapes area:', total_shapes_area)
    print()
    if total_shapes_area <= area:
        count += 1

print(count)
