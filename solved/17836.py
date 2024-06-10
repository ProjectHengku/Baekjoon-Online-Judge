from collections import deque

N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

fail = "Fail"

queue = deque()
visited = [[False] * M for _ in range(N)]
crushed = [[False] * M for _ in range(N)]

queue.append((0, 0, False, 0))
visited[0][0] = True

saved = False
while queue and not saved:
    y, x, item, time = queue.popleft()

    # item equipment
    if maze[y][x] == 2:
        item = True

    if y == N - 1 and x == M - 1:
        saved = True
        continue

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if item:
            if 0 <= ny < N and 0 <= nx < M and not crushed[ny][nx]:
                queue.append((ny, nx, item, time + 1))
                crushed[ny][nx] = True
        else:
            if (
                0 <= ny < N
                and 0 <= nx < M
                and maze[ny][nx] != 1
                and not visited[ny][nx]
            ):
                queue.append((ny, nx, item, time + 1))
                visited[ny][nx] = True

if saved and time <= T:
    print(time)
else:
    print(fail)
