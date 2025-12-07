from input_parser import get_lines
def solution(d, t='e'):
    lines = list(map(lambda x: [c for c in x], get_lines(d, t)))
    count = 0
    lines[1][lines[0].index('S')] = '|'
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                if lines[i-1][j] == '|':
                    count+=1

                lines[i][j-1] = '|'
                lines[i][j+1] = '|'
            elif lines[i-1][j] == '|':
                lines[i][j] = '|'

    seen = {}
    def dfs(i, j):
        if i == len(lines)-1:
            seen[(i, j)] = 1
            return seen[(i, j)]
        
        l,c,r = (0, 0, 0)
        if j > 0 and lines[i+1][j-1] == '|' and (i+1, j-1) not in seen and lines[i+1][j] == '^':
            l = dfs(i+1, j-1)
        elif (i+1, j-1) in seen:
            l = seen[(i+1, j-1)]

        if lines[i+1][j] == '|' and (i+1, j) not in seen:
            c = dfs(i+1, j)
        elif (i+1, j) in seen:
            c = seen[(i+1, j)]

        if j < len(lines[i])-1 and lines[i+1][j+1] == '|' and (i+1, j+1) not in seen and lines[i+1][j] == '^':
            r = dfs(i+1, j+1)
        elif (i+1, j+1) in seen:
            r = seen[(i+1, j+1)]

        if c > 0:
            seen[(i,j)] = c
        else:
            seen[(i, j)] = l+r
        return seen[(i, j)]
    return (count, dfs(0, lines[0].index('S')))

print(solution(7))