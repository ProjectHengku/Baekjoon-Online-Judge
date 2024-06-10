from collections import deque
import sys

input = sys.stdin.readline


N, M, K = map(int, input().split())
maze = [input() for _ in range(N)]

visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
visited[0][0][0] = True

queue = deque()
queue.append((0, 0, 0, 1))

escape = []

while queue:
    y, x, crushed, time = queue.popleft()
    daynight = time % 2

    if (y, x) == (N - 1, M - 1):
        print(time)
        exit()

    # noon = odd, night = even
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M:
            if maze[ny][nx] == "0" and not visited[crushed][ny][nx]:
                visited[crushed][ny][nx] = True
                queue.append((ny, nx, crushed, time + 1))
            elif (
                maze[ny][nx] == "1" and crushed < K and not visited[crushed + 1][ny][nx]
            ):
                # crushing only avaliable in noon
                if daynight:
                    visited[crushed + 1][ny][nx] = True
                    queue.append((ny, nx, crushed + 1, time + 1))
                # its avaliable to wait once, when infront of the wall, in night
                else:
                    queue.append((y, x, crushed, time + 1))
else:
    print(-1)
