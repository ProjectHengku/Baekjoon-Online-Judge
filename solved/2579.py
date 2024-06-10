import sys

input = sys.stdin.readline

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

# DP
DP = [0] * (N + 1)
if N >= 1:
    DP[1] = stairs[1]
if N >= 2:
    DP[2] = stairs[1] + stairs[2]
if N >= 3:
    DP[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])

for i in range(4, N + 1):
    DP[i] = max(DP[i - 3] + stairs[i - 1] + stairs[i], DP[i - 2] + stairs[i])

print(DP[N])
