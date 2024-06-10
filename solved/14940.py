import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

mapData = [list(map(int, input().split())) for i in range(N)]
# 방문한 곳 기록함
visited = [[0] * M for i in range(N)]

# 한 칸씩 이동해야 하므로 상, 하, 좌, 우 순서대로 이동한다 치면
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 현위치 기록장
queue = deque()

# 2까지의 최단경로이므로 2부터 출발해서 기록하면 될듯
# 시작 지점 데이터에 처음 2인 지점의 좌표와 경과일 카운터를 포함
for n in range(N):
    for m in range(M):
        if mapData[n][m] == 2:
            queue.append([m, n, 0])

# 이동 시뮬레이션
while queue:
    now = queue.popleft()
    x, y, count = now[0], now[1], now[2]
    for i in range(4):
        # 좌표 유효성 체크 후 이동 가능성 체크
        if ((0 <= x + dx[i] < M) and (0 <= y + dy[i] < N)) and (
            mapData[y + dy[i]][x + dx[i]] == 1
        ):
            # 갔다고 체크하고 한칸씩 이동한다
            # 갈 필요가 없는 곳과 갈 수 없는 곳을 굳이 구분하지 않아도 될듯
            mapData[y + dy[i]][x + dx[i]] = 0

            # 최단거리는 이동횟수로 기록하면 되겠음
            visited[y + dy[i]][x + dx[i]] = count + 1
            current = [x + dx[i], y + dy[i], count + 1]
            queue.append(current)

# 이러면, 갈 수 있는 곳인데 여전히 안 간 위치는 mapData상에서 1로 남아있을 것이므로
# visited에서 해당 좌표를 -1로 표기함
for n in range(N):
    for m in range(M):
        if mapData[n][m] == 1:
            visited[n][m] = -1

# 출력하면 됨
for n in range(N):
    print(*visited[n])