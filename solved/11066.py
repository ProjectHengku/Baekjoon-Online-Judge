import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    chapters = int(input())
    page = list(map(int, input().split()))

    cost = [[(float("inf"), 0)] * chapters for _ in range(chapters)]

    for idx, value in enumerate(page):
        cost[0][idx] = (0, value)

    for i in range(1, chapters):
        for j in range(chapters - i):
            for k in range(i):
                cost[i][j] = min(
                    cost[i][j],
                    (
                        cost[k][j][0]
                        + cost[(i - 1) - k][(j + 1) + k][0]
                        + (cost[k][j][1] + cost[(i - 1) - k][(j + 1) + k][1]),
                        cost[k][j][1] + cost[(i - 1) - k][(j + 1) + k][1],
                    ),
                    key=lambda x: x[0],
                )

    print(cost[-1][0][0])
