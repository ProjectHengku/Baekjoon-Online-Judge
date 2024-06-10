N = int(input())
mats = [list(map(int, input().split())) for _ in range(N)]

mul = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N - 1):
    N2, M = mats[i]
    M, K = mats[i + 1]
    mul[0][i] = (N2 * M * K, N2, K)

for i in range(1, N - 1):
    for j in range(N - 2 - (i - 1)):
        mul[i][j] = (
            min(
                mul[i - 1][j][0]
                + mul[i - 1][j][1] * mul[i - 1][j][2] * mats[j + i + 1][1],
                mul[i - 1][j + 1][0]
                + mul[i - 1][j + 1][1] * mul[i - 1][j + 1][2] * mats[j][0],
            ),
            mats[j][0],
            mats[j + i + 1][1],
        )

print(mul[N - 2][0][0])
