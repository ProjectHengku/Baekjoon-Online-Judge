from collections import deque

N, M = map(int, input().split())

Hy, Hx = map(int, input().split())
Ey, Ex = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

# 시작, 목표값 재처리
Hx -= 1
Hy -= 1
Ex -= 1
Ey -= 1

queue = deque()
visited = [[False] * M for _ in range(N)]
magic = [[False] * M for _ in range(N)]

queue.append((Hy, Hx, False, 0))
visited[Hy][Hx] = True

escape = False
while queue and not escape:
    y, x, crushed, length = queue.popleft()

    if y == Ey and x == Ex:
        escape = True
        continue

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if not crushed:
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx, crushed, length + 1))
                    visited[ny][nx] = True
                elif maze[ny][nx] == 1 and not magic[ny][nx]:
                    queue.append((ny, nx, True, length + 1))
                    magic[ny][nx] = True
        else:
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 0 and not magic[ny][nx]:
                queue.append((ny, nx, crushed, length + 1))
                magic[ny][nx] = True

if escape:
    print(length)
else:
    print(-1)
