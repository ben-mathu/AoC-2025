with open('./input/ingredients.txt', 'r') as f:
    lines = f.readlines()
    space_found = False
    ranges = []
    ing_ids = []
    for s in lines:
        if s.strip() == '':
            space_found = True
            continue
        if space_found:
            ing_ids.append(s.strip())
        else:
            ranges.append(s.strip())
    
    count=0
    for id in ing_ids:
        for r in ranges:
            rang = r.split('-')
            if int(id) >= int(rang[0]) and int(id) <= int(rang[1]):
                count+=1
                break
    print(count)

    # Part 2

    valid_count = 0
    start_range = []
    end_range = []
    for s in lines:
        if s.strip() == '':
            break

        rang = s.strip().split('-')
        curr_count = int(rang[1]) - int(rang[0]) + 1
        for i in range(len(start_range)):
            if len(rang) == 0:
                break
            
            if int(rang[0]) >= start_range[i] and int(rang[1]) <= end_range[i]:
                c = int(rang[1]) - int(rang[0]) + 1
                curr_count -= c
                if c == 1:
                    rang = []
            elif start_range[i] <= int(rang[0]) and end_range[i] >= int(rang[0]):
                curr_count -= end_range[i] - int(rang[0]) + 1
                rang[0] = str(end_range[i] + 1)
            elif start_range[i] <= int(rang[1]) and end_range[i] >= int(rang[1]):
                curr_count -= int(rang[1]) - start_range[i] + 1
                rang[1] = str(start_range[i] - 1)
            elif int(rang[0]) <= start_range[i] and int(rang[1]) >= end_range[i]:
                curr_count -= end_range[i] - start_range[i] + 1

        if rang and curr_count > 0:
            start_range.append(int(rang[0]))
            end_range.append(int(rang[1]))
        valid_count += curr_count

    print(valid_count)
