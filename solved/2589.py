from collections import deque

N, M = map(int, input().split())
treasure = [input() for _ in range(N)]

# 기록장 초기화
# 보물은 가장 멀리 떨어져있음
maxdist = [[0] * M for _ in range(N)]

starts = []
# 시작 지점 전부 기록
for i in range(N):
    for j in range(M):
        if treasure[i][j] == "L":
            starts.append((i, j, 1))

# 가로 세로 이동
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 브루트포스
for start in starts:
    # 너비 우선 탐색
    queue = deque()
    queue.append(start)
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True

    while queue:
        y, x, dist = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and treasure[ny][nx] == "L"
                and not visited[ny][nx]
            ):
                # 최장거리 갱신함
                if dist > maxdist[ny][nx]:
                    maxdist[ny][nx] = dist
                visited[ny][nx] = True
                queue.append((ny, nx, dist + 1))

# 가장 큰 값이 보물 최단 경로
print(max(map(max, maxdist)))
