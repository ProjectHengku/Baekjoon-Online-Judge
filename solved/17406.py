import copy


# backtracking
def exe(arr, depth):
    global A

    if depth == K:
        a = min(map(sum, arr))
        if a < A:
            A = a
        return 0

    for i in range(K):
        if not used[i]:
            used[i] = True
            r, c, s = cal[i]
            arr2 = copy.deepcopy(arr)
            arr2 = turn(arr2, r - 1, c - 1, s)
            exe(arr2, depth + 1)

            used[i] = False


def turn(arr, r, c, s):
    arr = copy.deepcopy(arr)

    # change value via clockwise route
    for i in range(s):
        starty, startx = r - (s - i), c - (s - i)
        y, x = starty, startx
        ny, nx = -1, -1
        rot = 0
        # save current value (backup)
        temp = arr[y][x]
        while (ny, nx) != (starty, startx):
            dy, dx = d[rot]
            ny, nx = y + dy, x + dx
            if r - (s - i) <= ny <= r + (s - i) and c - (s - i) <= nx <= c + (s - i):
                temp, arr[ny][nx] = arr[ny][nx], temp
                y, x = ny, nx
            else:
                rot = (rot + 1) % 4

    return arr


N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
cal = [list(map(int, input().split())) for _ in range(K)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
used = [False] * K

A = float("inf")
exe(arr, 0)

print(A)
