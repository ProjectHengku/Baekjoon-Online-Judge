from collections import deque

N, M = map(int, input().split())
zone = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
visited = [[False] * M for _ in range(N)]
dists = [[0] * M for _ in range(N)]

# find zone which shark exist
found = False
for i in range(N):
    for j in range(M):
        if zone[i][j] == 1:
            queue.append((i, j, 0))
            visited[i][j] = True

while queue:
    y, x, distance = queue.popleft()

    dists[y][x] = distance

    # 8 ways
    for dy, dx in (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and zone[ny][nx] == 0 and not visited[ny][nx]:
            queue.append((ny, nx, distance + 1))
            visited[ny][nx] = True

print(max(map(max, dists)))
