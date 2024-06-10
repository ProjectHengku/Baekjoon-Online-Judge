from copy import deepcopy
import sys

input = sys.stdin.readline


N = int(input())

moved = [[] for _ in range(N + 1)]

# record travel in each
travel = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    start, end, length = map(int, input().split())
    travel[start][end] = length
    travel[end][start] = length
    # use 0th column for max value
    travel[start][0] = max(travel[start][0], length)
    travel[end][0] = max(travel[end][0], length)

    moved[start].append(end)
    moved[end].append(start)

    temp = deepcopy(moved[start])

    # extend when previous destination becones start
    for i in temp:
        if i != end:
            travel[i][end] = travel[i][start] + length
            travel[i][0] = max(travel[i][0], travel[i][end])
            moved[i].append(end)

            travel[end][i] = travel[i][end]
            travel[end][0] = max(travel[end][0], travel[end][i])
            moved[end].append(i)

for start in travel[1:]:
    print(start[0])
