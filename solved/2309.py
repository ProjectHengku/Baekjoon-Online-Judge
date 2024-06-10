import itertools

dwarf = [int(input()) for i in range(9)]
combinations = list(itertools.combinations(dwarf, 7))

for case in combinations:
    if sum(case) == 100:
        case = list(case)
        case.sort()
        for man in case:
            print(man)
        break
