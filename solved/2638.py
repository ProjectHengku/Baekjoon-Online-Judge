from collections import deque

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

move = ((1, 0), (0, 1), (-1, 0), (0, -1))
time = 0

while any(map(any, cheese)):
    air = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    queue = deque([(0, 0)])

    # BFS
    while queue:
        y, x = queue.popleft()

        for dy, dx in move:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if cheese[ny][nx] == 0:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                else:
                    air[ny][nx] += 1

    # cheese gone
    for y in range(N):
        for x in range(M):
            if air[y][x] >= 2:
                cheese[y][x] = 0

    time += 1

print(time)
