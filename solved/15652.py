def series(depth, left, right):
    for i in range(right, N + 1):
        if depth == M:
            print((left + " " + str(i)).strip())
        else:
            series(depth + 1, left + " " + str(i), i)


N, M = map(int, input().split())
series(1, "", 1)
