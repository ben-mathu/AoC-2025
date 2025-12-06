import math
import re

with open('./input/6_cephalopods.txt', 'r') as f:
    lines = f.readlines()
    op = {}
    for s in lines:
        nums = re.split(r'\s+', s.strip())
        for i in range(len(nums)):
            n = nums[i]
            if i+1 in op:
                op[i+1] = op[i+1] + [int(n) if n != '*' and n != '+' else n]
            else:
                op[i+1] = [int(n) if n != '*' and n != '+' else n]

    total = 0
    for k in op:
        s = len(op[k])
        l = op[k][:-1]
        if op[k][s-1] == '*':
            total += math.prod(l)
        elif op[k][s-1] == '+':
            total += sum(l)
    print(total)

    start_index = 0
    total = 0
    for col in op:
        l = []
        s_len = len(str(max(op[col][:len(op[col])-1])))
        for row in lines:
            build = row[start_index:start_index+s_len]
            l.append(build)
        start_index = s_len+start_index+1

        start_j = l.index(max(l))
        operation = l[len(l)-1]
        t = 0
        for k in range(s_len-1, -1, -1):
            build = ''
            for j in range(0, len(l)-1):
                if l[j][k] != ' ' and l[j][k] != '+' and l[j][k] != '*':
                    build += l[j][k]
            if '+' in operation:
                t += int(build)
            if  '*' in operation:
                t = (1 if t == 0 else t) * int(build)
        total += t
    print(total)

