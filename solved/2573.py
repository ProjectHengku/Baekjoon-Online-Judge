from collections import deque


def howMany(graph):
    flag = False
    queue = deque()
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                queue.append((i, j))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    count = 1
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and graph[ny][nx] > 0
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True
                queue.append((ny, nx))

    flag = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                count += 1
                # queue.append((i, j))
                # visited[i][j] = True
                flag = True
                break
        if flag:
            break

    return count


N, M = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

time = 0
while howMany(glacier) == 1:
    queue = deque()
    for i in range(N):
        for j in range(M):
            if glacier[i][j] <= 0:
                queue.append((i, j))

    change = [[0] * M for _ in range(N)]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and glacier[ny][nx] > 0:
                change[ny][nx] -= 1

    # 빙하 녹음
    for i in range(N):
        for j in range(M):
            glacier[i][j] += change[i][j]
            if glacier[i][j] < 0:
                glacier[i][j] = 0

    time += 1
    # 다 녹아버림 ㅜㅜ
    if sum(map(sum, glacier)) <= 0:
        time = 0
        break

print(time)
