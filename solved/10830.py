def mul(A, B):
    X = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            x = 0
            for k in range(N):
                x += A[i][k] * B[k][j]
            X[i][j] = x % 1000
    return X


def square(mat, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] %= 1000
        return mat

    half = square(mat, B // 2)
    if B % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), mat)


N, B = map(int, input().split())


mat = [list(map(int, input().split())) for _ in range(N)]

ans = square(mat, B)
for row in ans:
    print(*row)
