from copy import deepcopy
import sys

input = sys.stdin.readline

N = int(input())

# DP
maxDP = [[0, 0, 0], [0, 0, 0]]
minDP = [[0, 0, 0], [0, 0, 0]]

for _ in range(1, N + 1):
    left, center, right = map(int, input().split())

    maxDP[1][0] = max(maxDP[0][0], maxDP[0][1]) + left
    maxDP[1][1] = max(maxDP[0][0], maxDP[0][1], maxDP[0][2]) + center
    maxDP[1][2] = max(maxDP[0][1], maxDP[0][2]) + right

    minDP[1][0] = min(minDP[0][0], minDP[0][1]) + left
    minDP[1][1] = min(minDP[0][0], minDP[0][1], minDP[0][2]) + center
    minDP[1][2] = min(minDP[0][1], minDP[0][2]) + right

    maxDP[0] = deepcopy(maxDP[1])
    minDP[0] = deepcopy(minDP[1])


print(max(maxDP[1]), min(minDP[1]))
