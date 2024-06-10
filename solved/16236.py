from collections import deque


def available(size):
    for i in range(N):
        for j in range(N):
            if space[i][j] != 0 and space[i][j] != 9 and space[i][j] < size:
                return True
    return False


def start():
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                return i, j


def fish(sy, sx):
    # bfs
    queue = deque([(sy, sx, 0)])

    visited = [[False] * N for _ in range(N)]
    visited[sy][sx] = True

    fishes = []

    while queue:
        y, x, time = queue.popleft()

        if space[y][x] != 0 and space[y][x] != 9 and space[y][x] < size:
            fishes.append((y, x, time))

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < N)
                and space[ny][nx] <= size
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True
                queue.append((ny, nx, time + 1))

    # 같은 거리면 위쪽이 먼저, 그 다음이 왼쪽
    fishes.sort(key=lambda x: (x[2], x[0], x[1]))

    if fishes:
        return fishes[0]
    else:
        print(total)
        exit()


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

size = 2
eat = 0
move = ((-1, 0), (0, -1), (0, 1), (1, 0))

total = 0
while available(size):
    sy, sx = start()

    fy, fx, time = fish(sy, sx)

    space[sy][sx] = 0
    space[fy][fx] = 9

    eat += 1
    if eat == size:
        size += 1
        eat = 0

    total += time

print(total)
