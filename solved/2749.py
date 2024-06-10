def mat_mul(A, B):
    X = [[0, 0], [0, 0]]
    for y in range(2):
        for x in range(2):
            for i in range(2):
                X[y][x] += A[y][i] * B[i][x]
                X[y][x] %= d
    return X


def find(mat, m):
    if m == 1:
        for i in range(2):
            for j in range(2):
                mat[i][j] %= d
        return mat
    temp = find(mat, m // 2)
    if m % 2 == 0:
        return mat_mul(temp, temp)
    else:
        return mat_mul(mat_mul(temp, temp), mat)


n = int(input())
d = 1000000

mat = [[1, 1], [1, 0]]

print(find(mat, n)[0][1])
