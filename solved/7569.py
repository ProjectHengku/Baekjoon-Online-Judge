from collections import deque


M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for xy in range(N)] for xyz in range(H)]

# 한 칸씩 이동해야 하므로 상, 하, 전, 후, 좌, 우 순서대로 이동한다 치면
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 현위치 기록장
queue = deque()

# 시작 지점 데이터에 처음 1인 지점의 좌표와 경과일 카운터를 포함
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append([m, n, h, 0])

# 이동 시뮬레이션
while queue:
    now = queue.popleft()
    x, y, z, count = now[0], now[1], now[2], now[3]
    for i in range(6):
        # 좌표 유효성 체크 후 이동 가능성 체크
        if (
            (0 <= x + dx[i] < M) and (0 <= y + dy[i] < N) and (0 <= z + dz[i] < H)
        ) and (box[z + dz[i]][y + dy[i]][x + dx[i]] == 0):
            # 익었다고 체크하고 한칸씩 이동한다
            box[z + dz[i]][y + dy[i]][x + dx[i]] = 1
            current = [x + dx[i], y + dy[i], z + dz[i], count + 1]
            queue.append(current)

# 익지 못하는 토미토가 남아있는지 확인
for floor in box:
    for row in floor:
        if 0 in row:
            print(-1)
            exit()
else:
    print(count)
