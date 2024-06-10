from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
gym = [input() for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())

y1 -= 1
x1 -= 1
y2 -= 1
x2 -= 1

visited = [[float("inf")] * M for _ in range(N)]
visited[y1][x1] = 0

move = ((1, 0), (0, 1), (0, -1), (-1, 0))
finish = False

queue = deque([(y1, x1)])
while queue:
    y, x = queue.popleft()

    if (y, x) == (y2, x2):
        finish = True
        continue

    for dy, dx in move:
        for k in range(1, K + 1):
            ny, nx = y + k * dy, x + k * dx
            if not (0 <= ny < N and 0 <= nx < M):
                break
            if gym[ny][nx] == "#" or visited[ny][nx] <= visited[y][x]:
                break
            if visited[ny][nx] == float("inf"):
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

if finish:
    print(visited[y2][x2])
else:
    print(-1)
