start, end = map(int, input().split())

# 그래프 생성
graph = [[[] for _ in range(1500)] for _ in range(1500)]

# 가운데 1
graph[750][750] = 1

# 육각형 방향
dy = [1, 0, -1, -1, 0, 1]
dx = [1, 1, 0, -1, -1, 0]

N = 1
cycle = 0
x, y = 750, 750
while N < 1000000:
    cycle += 1
    # 육각형 방향으로 껍질 계층 수 만큼 이동하면서 쌓음
    for k in range(6):
        for i in range(cycle):
            N += 1
            # 정말 처음에는 위로 한 번 올라가야 됨
            if k == i == 0:
                y += 1
            else:
                y = y + dy[k]
                x = x + dx[k]
            graph[y][x] = N

            # 시작 좌표 지정
            if N == start:
                sy, sx = y, x

# 1에서 시작할 때의 예외처리
if start == 1:
    sy, sx = 750, 750

# 너비 우선 탐색
queue = [[0, 0] for _ in range(1000001)]
front = rear = -1

rear += 1
queue[rear][0] = (sy, sx)

visited = [False] * 1000001
visited[start] = True

while front < rear:
    front += 1
    current = queue[front][0]

    # 좌표 추출
    y, x = current
    now = graph[y][x]

    # 도착했으면 터뜨림
    if now == end:
        break

    # 이동 후보지 선정
    for i in range(6):
        ny = y + dy[i]
        nx = x + dx[i]

        next = graph[ny][nx]
        if graph[ny][nx] and next <= 1000000 and not visited[next]:
            visited[next] = True
            rear += 1
            queue[rear][0] = (ny, nx)
            queue[rear][1] = front

# 루트 역추적
path = []
while True:
    y, x = queue[front][0]
    path.append(graph[y][x])
    if graph[y][x] == start:
        break
    front = queue[front][1]

result = path[::-1]

print(*result)
