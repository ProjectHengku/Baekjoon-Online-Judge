N = int(input())

house = [[int(i) for i in input()] for j in range(N)]

# 한 칸씩 이동해야 하므로 상, 하, 좌, 우 순서대로 이동한다 치면
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 현위치 기록장
stack = []

# 이동한 장소의 기록
visited = [[False] * N for i in range(N)]

# 단지내 집의 수
houseInApt = []

# 이동 시뮬레이션: 모든 좌표를 돌아보면서 집이 있는 곳을 만나면 그 인근을 돌아보기
for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and visited[i][j] == False:
            x, y, count = j, i, 1
            visited[i][j] = True
            stack.append([x, y, count])

            while stack:
                now = stack.pop()

                x, y = now[0], now[1]

                for k in range(4):
                    # 좌표 유효성 체크 후 이동 가능성 체크
                    if (
                        ((0 <= x + dx[k] < N) and (0 <= y + dy[k] < N))
                        and house[y + dy[k]][x + dx[k]] == 1
                        and visited[y + dy[k]][x + dx[k]] == False
                    ):
                        # 방문한 적이 있다고 체크하고 한칸씩 이동한다
                        visited[y + dy[k]][x + dx[k]] = True
                        count += 1
                        current = [x + dx[k], y + dy[k]]
                        stack.append(current)
            houseInApt.append(count)

houseInApt.sort()

print(len(houseInApt))
for number in houseInApt:
    print(number)
