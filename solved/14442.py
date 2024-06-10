import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
maze = [input() for _ in range(N)]

visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
visited[0][0][0] = True

queue = deque()
queue.append((0, 0, 0, 1))

while queue:
    y, x, crushed, length = queue.popleft()

    if (y, x) == (N - 1, M - 1):
        print(length)
        exit()

    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx
        if (0 <= ny < N and 0 <= nx < M) and not visited[crushed][ny][nx]:
            if maze[ny][nx] == "1":
                if crushed < K and not visited[crushed + 1][ny][nx]:
                    visited[crushed + 1][ny][nx] = True
                    queue.append((ny, nx, crushed + 1, length + 1))
            else:
                visited[crushed][ny][nx] = True
                queue.append((ny, nx, crushed, length + 1))
else:
    print(-1)
