import sys

input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] * (N + 1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]

# 전처리 함
subsum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        subsum[i][j] = subsum[i][j - 1] + table[i][j]

for i in range(2, N + 1):
    for j in range(1, N + 1):
        subsum[i][j] += subsum[i - 1][j]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())

    sys.stdout.write(
        str(
            subsum[y2][x2]
            - (subsum[y2][x1 - 1] + subsum[y1 - 1][x2])
            + subsum[y1 - 1][x1 - 1]
        )
        + "\n"
    )
