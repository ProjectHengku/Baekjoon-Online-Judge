from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
gym = [input() for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())

visited = [[float("inf")] * M for _ in range(N)]
visited[y1 - 1][x1 - 1] = 0

queue = deque([(y1 - 1, x1 - 1)])

while queue:
    y, x = queue.popleft()

    # if (y, x) == (y2, x2):
    #     print(time)
    #     exit()

    for d in range(1, K + 1):
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + d * dy, x + d * dx

            if (
                (0 <= ny < N and 0 <= nx < M)
                and all([gym[y + k * dy][x + k * dx] != "#" for k in range(1, d + 1)])
                and visited[y][x] + 1 < visited[ny][nx]
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))


if visited[y2 - 1][x2 - 1] < float("inf"):
    print(visited[y2 - 1][x2 - 1])
else:
    print(-1)
