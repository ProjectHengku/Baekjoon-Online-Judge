import sys

input = sys.stdin.readline

N = int(input())
T, P = [0 for _ in range(N + 2)], [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

# DP
DP = [0] * (N + 2)

for i in range(1, N + 1):
    DP[i] = max(DP[i], DP[i - 1])
    deadline = i + T[i]
    if deadline <= N + 1:
        DP[i + T[i]] = max(DP[i + T[i]], DP[i] + P[i])

print(max(DP))
