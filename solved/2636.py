from collections import deque

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

time = 0
while sum(map(sum, cheeze)) > 0:
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    change = [[False] * M for _ in range(N)]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                if cheeze[ny][nx] == 0:
                    queue.append((ny, nx))
                else:
                    change[ny][nx] = True

    # 바깥쪽 삭음
    for i in range(N):
        for j in range(M):
            if change[i][j]:
                cheeze[i][j] = 0

    time += 1

print(time)
print(sum(map(sum, change)))
