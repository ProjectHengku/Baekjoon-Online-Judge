import itertools
import math

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

member = set(range(N))

noofcases = math.comb(N, N // 2)
cases = list(itertools.combinations(member, N // 2))

closest = float("inf")
for i in range(noofcases):
    teamA = set(cases[i])
    teamB = member - teamA

    statusA, statusB = list(itertools.combinations(teamA, 2)), list(
        itertools.combinations(teamB, 2)
    )
    sumA, sumB = 0, 0
    for case in statusA:
        i, j = case
        sumA += S[i][j] + S[j][i]

    for case in statusB:
        i, j = case
        sumB += S[i][j] + S[j][i]

    temp = abs(sumA - sumB)
    if temp < closest:
        closest = temp

print(closest)
