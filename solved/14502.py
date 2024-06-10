import itertools
import copy
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 0이 있는 곳만 뽑아내면
zeros = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zeros.append((i, j))

# 3개만 고르는 경우의 수
zeros3 = list(itertools.combinations(zeros, 3))

# 바이러스 최초 위치 지정
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))

# 2차원 이동
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 각각의 경우의 수에 대해서 시뮬레이션
results = []
for case in zeros3:
    # 연구실 복사
    simlab = copy.deepcopy(lab)

    for y, x in case:
        simlab[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    queue = deque()
    for y, x in virus:
        queue.append((y, x))
        visited[y][x] = True

    # BFS
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and simlab[ny][nx] == 0
                and not visited[ny][nx]
            ):
                simlab[ny][nx] = 2
                queue.append((ny, nx))
                visited[ny][nx] = True

    # 안전 영역 크기 계산
    safe = sum([row.count(0) for row in simlab])
    results.append(safe)

# 최대 안전 영역
print(max(results))
