with open('input/print.txt', 'r') as f:
    lines = f.readlines()
    # i,j: i-1,j-1;i-1,j;i-1,j+1;i,j-1;i,j;i,j+1;i+1,j-1;i+1,j;i+1,j+1
    l = []
    for i in range(len(lines)):
        l.append([c for c in lines[i].strip()])

    print(l)
    remove_count = 0
    while True:
        count = 0
        remove = []
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] == '.' or l[i][j] == 'x':
                    continue

                neighbours = 0
                if j < len(l[i]) - 1 and l[i][j+1] == '@':
                    neighbours +=1
                
                if j > 0 and l[i][j-1] == '@':
                    neighbours +=1
                
                if i == 0 or i < len(l) - 1:
                    if j > 0 and l[i+1][j-1] == '@':
                        neighbours +=1

                    if l[i+1][j] == '@':
                        neighbours +=1

                    if j < len(l[i])-1 and l[i+1][j+1] == '@':
                        neighbours+=1

                if i > 0:
                    if j > 0 and l[i-1][j-1] == '@':
                        neighbours +=1

                    if l[i-1][j] == '@':
                        neighbours += 1

                    if j < len(l[i])-1 and l[i-1][j+1]== '@':
                        neighbours +=1
                
                if neighbours < 4:
                    remove.append([i,j])
                    count+=1
        
        if count == 0:
            break

        for item in remove:
            l[item[0]][item[1]] = 'x'
            remove_count +=1
    print(remove_count)