from collections import deque


def checkrest():
    for i in range(N):
        for j in range(N):
            if heights[i][j] > h and not visited[i][j]:
                return True, i, j

    return False, -1, -1


N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]

# 2차원 이동
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 최대니까 가능한 높이로 다 테스트 해봐야겠네
maxheight = max(map(max, heights))
maxarea = 0
for h in range(maxheight):
    visited = [[False] * N for _ in range(N)]
    area = 0

    available, y, x = checkrest()
    # 더 진행할 수 있는가?
    while available:
        queue = deque()
        queue.append((y, x))
        visited[y][x] = True
        # 너비 우선 탐색
        while queue:
            y, x = queue.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if (
                    0 <= ny < N
                    and 0 <= nx < N
                    and heights[ny][nx] > h
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    queue.append((ny, nx))
        area += 1
        available, y, x = checkrest()
    if area > maxarea:
        maxarea = area

print(maxarea)
