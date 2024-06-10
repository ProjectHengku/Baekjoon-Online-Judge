from collections import deque

N, M = map(int, input().split())
graph = [input() for _ in range(N)]

n = N - 1
m = M - 1

# crushed 맵을 추가하면 어떻게든 될 것 같음
visited = [[False] * M for _ in range(N)]
crushed = [[False] * M for _ in range(N)]
queue = deque()

visited[0][0] = True
queue.append((0, 0, False, 1))

terminal = False
while queue and not terminal:
    y, x, broken, length = queue.popleft()

    if (y, x) == (n, m):
        terminal = True
        continue

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny = y + dy
        nx = x + dx

        if not broken:
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == "0" and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, broken, length + 1))
                else:
                    if graph[ny][nx] == "1" and not crushed[ny][nx]:
                        crushed[ny][nx] = True
                        queue.append((ny, nx, True, length + 1))
        # 벽을 부숴버린 이후에는 다른 시간선임
        else:
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == "0" and not crushed[ny][nx]:
                    crushed[ny][nx] = True
                    queue.append((ny, nx, broken, length + 1))

if terminal:
    print(length)
else:
    print(-1)
