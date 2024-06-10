N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

mul = [[(float("inf"), 0, 0)] * N for _ in range(N)]

for idx, value in enumerate(mat):
    row, col = value
    mul[0][idx] = (0, row, col)

for i in range(1, N):
    for j in range(N - i):
        for k in range(i):
            mul[i][j] = (
                min(
                    mul[i][j][0],
                    mul[k][j][0]
                    + mul[(i - 1) - k][(j + 1) + k][0]
                    + mul[k][j][1] * mul[k][j][2] * mul[(i - 1) - k][(j + 1) + k][2],
                ),
                mul[k][j][1],
                mul[(i - 1) - k][(j + 1) + k][2],
            )

print(mul[-1][0][0])
