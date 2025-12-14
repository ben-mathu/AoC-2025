with open('./input/joltages.txt', 'r') as f:
    max_place_value = 12
    lines = f.readlines()
    total_jolts = 0
    for s in map(lambda x: x.strip(), lines):
        place_value = max_place_value
        build = [i for i in range(max_place_value)]
        i=0
        while i < max_place_value:
            search_range = len(s)-place_value+1
            last_index = 0
            if i>0:
                last_index = build[i-1]
                build[i] = last_index+1
            else:
                last_index = build[i]

            for k in range(last_index+1, search_range):
                if int(s[k]) > int(s[build[i]]) and build[len(build)-1] < len(s):
                    build[i] = k
            place_value-=1
            i+=1
            if build[len(build)-1] == len(s):
                break
        total_jolts += int(''.join(map(lambda c: str(s[c]), build)))

    print(total_jolts)