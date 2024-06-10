from collections import deque


N, M = map(int, input().split())

maze = [[int(i) for i in input()] for j in range(N)]

# 한 칸씩 이동해야 하므로 상, 하, 좌, 우 순서대로 이동한다 치면
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 현위치 기록장
queue = deque()

# 이동한 장소의 기록
visited = [[False] * M for i in range(N)]

# 시작 지점은 (1, 1)로 고정
x = 0
y = 0
visited[y][x] = True
count = 1

current = [x, y, count]

# 시작지점 기록
queue.append(current)

# 이동 시뮬레이션
while queue:
    now = queue.popleft()
    x, y, count = now[0], now[1], now[2]
    # 제일 먼저 도착하는 쪽이 최단경로이므로
    if x == (M - 1) and y == (N - 1):
        print(count)
        break
    for i in range(4):
        # 좌표 유효성 체크 후 이동 가능성 체크
        if (
            ((0 <= x + dx[i] < M) and (0 <= y + dy[i] < N))
            and maze[y + dy[i]][x + dx[i]] == 1
            and visited[y + dy[i]][x + dx[i]] == False
        ):
            # 방문한 적이 있다고 체크하고 한칸씩 이동한다
            visited[y + dy[i]][x + dx[i]] = True
            current = [x + dx[i], y + dy[i], count + 1]
            queue.append(current)
