with open('./input/ranges.txt', 'r') as f:
    line = f.read()
    ranges = line.split(',')
    invalid_ids = []
    for r in ranges:
        se = r.split('-')
        s = int(se[0])
        e = int(se[1])
        for i in range(s, e+1):
            build = ''
            for k in str(i):
                build += k
                invalid = []
                for j in range(0, len(str(i)), len(build)):
                    invalid.append(str(i)[j:j+len(build)])

                is_invalid = True if len(build) != len(str(i)) else False

                for l in range(1, len(invalid)):
                    if build != invalid[l]:
                        is_invalid = False
                if is_invalid:
                    invalid_ids.append(i)
                    break
    print(sum(invalid_ids))