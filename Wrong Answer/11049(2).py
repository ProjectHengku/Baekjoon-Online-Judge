N = int(input())
mats = [list(map(int, input().split())) for _ in range(N)]

mul = [[[] for _ in range(N - 1)] for _ in range(N - 1)]

for i in range(N - 1):
    N2, M = mats[i]
    M, K = mats[i + 1]
    mul[0][i] = (N2 * M * K, N2, K)

for i in range(1, N):
    for j in range(N - (i + 1)):
        mul[i][j] = (
            min(
                mul[i - 1][j][0]
                + mul[i - 1][j][1] * mul[i - 1][j][2] * mats[j + (i + 1)][1],
                mul[i - 1][j + 1][0]
                + mul[i - 1][j + 1][1] * mul[i - 1][j + 1][2] * mats[j][1],
            ),
            mats[j][0],
            mats[j + (i + 1)][1],
        )

print(mul[-1][0][0])
