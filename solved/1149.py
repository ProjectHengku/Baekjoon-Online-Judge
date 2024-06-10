import sys

input = sys.stdin.readline

N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

# DP
DP = [[0] * 3 for _ in range(N)]

for i in range(3):
    DP[0][i] = prices[0][i]

for i in range(1, N):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + prices[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + prices[i][1]
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + prices[i][2]

answer = min([DP[-1][i] for i in range(3)])
print(answer)
