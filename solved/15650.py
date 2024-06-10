def series(depth, left, right):
    for i in range(right, N - M + 1 + depth):
        if depth < M:
            series(depth + 1, (left + " " + str(i)), i + 1)
        else:
            print((left + " " + str(i)).strip())
    return 0


N, M = map(int, input().split())

series(1, "", 1)
