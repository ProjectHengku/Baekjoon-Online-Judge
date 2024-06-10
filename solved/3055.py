from collections import deque


def init(target):
    for i in range(R):
        for j in range(C):
            if forest[i][j] == target:
                return i, j

    return -1, -1


R, C = map(int, input().split())

forest = [input() for _ in range(R)]

# water-time simulation
flood_at = [[float("inf")] * C for _ in range(R)]

wy, wx = init("*")
if wy != -1:
    queue = deque()
    queue.append((wy, wx, 0))

    visited = [[False] * C for _ in range(R)]
    visited[wy][wx] = True

    flood_at[wy][wx] = 0

    while queue:
        y, x, time = queue.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < R and 0 <= nx < C)
                and (forest[ny][nx] != "D" and forest[ny][nx] != "X")
                and not visited[ny][nx]
            ):
                queue.append((ny, nx, time + 1))
                visited[ny][nx] = True
                flood_at[ny][nx] = time + 1

# find initial position
sy, sx = init("S")

queue = deque()
queue.append((sy, sx, 0))

visited = [[False] * C for _ in range(R)]
visited[sy][sx] = True

escape = False
while queue:
    y, x, time = queue.popleft()

    if forest[y][x] == "D":
        print(time)
        exit()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if (
            (0 <= ny < R and 0 <= nx < C)
            and (forest[ny][nx] != "X")
            and time + 1 < flood_at[ny][nx]
            and not visited[ny][nx]
        ):
            queue.append((ny, nx, time + 1))
            visited[ny][nx] = True
else:
    print("KAKTUS")
