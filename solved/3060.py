from copy import deepcopy

T = int(input())

for _ in range(T):
    N = int(input())
    pig = list(map(int, input().split()))

    day = 1
    while sum(pig) <= N:
        pig2 = deepcopy(pig)
        for i in range(6):
            pig2[i] += pig[i - 1]
            pig2[i] += pig[(i + 1) % 6]
            pig2[i] += pig[(i + 3) % 6]

        pig = pig2
        day += 1

    print(day)
