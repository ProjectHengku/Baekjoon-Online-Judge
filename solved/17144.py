R, C, T = map(int, input().split())

air = [list(map(int, input().split())) for _ in range(R)]

# 초기 값 설정
AP = -1
# 상 하 좌 우
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 바람의 궤적
# 공기청정기는 위 아래로만 붙어있으므로
whereAP = []
flag = False
for i in range(R):
    for j in range(C):
        if air[i][j] == AP:
            whereAP.append((i, j))
            whereAP.append((i + 1, j))
            flag = True
            break
    if flag:
        break

airflow = [[0] * C for _ in range(R)]
# 윗 순환: 우->상->좌->하
# 세로 방향으로 서있으면 출발 방향은 오른쪽이거나, 오른쪽이 안된다면 윗쪽일 것임
rot = 3
y, x = whereAP[0]
next_rot = {3: 0, 0: 2, 2: 1, 1: 3}
available = True
flow1 = []
while available:
    while True:

        dy, dx = direction[rot]
        ny = y + dy
        nx = x + dx

        if not (0 <= ny < R and 0 <= nx < C):
            rot = next_rot[rot]
            continue

        if air[ny][nx] == AP:
            available = False
        airflow[y][x] = rot
        flow1.append((y, x, rot))

        y, x = ny, nx
        break

flow1 = flow1[::-1]

# 아랫 순환: 우->하->좌->상
# 마찬가지로, 출발 방향은 오른쪽이거나, 오른쪽이 안된다면 아랫쪽일 것임
rot = 3
y, x = whereAP[1]
next_rot = {3: 1, 1: 2, 2: 0, 0: 3}
available = True
flow2 = []
while available:
    while True:

        dy, dx = direction[rot]
        ny = y + dy
        nx = x + dx

        if not (0 <= ny < R and 0 <= nx < C):
            rot = next_rot[rot]
            continue

        if air[ny][nx] == AP:
            available = False
        airflow[y][x] = rot
        flow2.append((y, x, rot))

        y, x = ny, nx
        break

flow2 = flow2[::-1]

for _ in range(T):
    # 먼지가 있는 곳 탐색
    # print(_)
    dust = []
    for i in range(R):
        for j in range(C):
            if air[i][j] > 0:
                dust.append((i, j))

    # 먼지가 자연스럽게 퍼진다 (순차적으로 말고 한 번에)

    spread = [[0] * C for _ in range(R)]

    # 일단 각 구역마다 시간을 멈추고 순차적으로 기록함
    for y, x in dust:
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < R and 0 <= nx < C) and air[ny][nx] != AP:
                spread[ny][nx] += air[y][x] // 5
                spread[y][x] -= air[y][x] // 5
    # 시간은 다시 흐른다
    for i in range(R):
        for j in range(C):
            air[i][j] += spread[i][j]

    # print(*air, sep="\n")
    # print()

    # 먼지가 바람에 날려 움직인다
    for y, x, rot in flow1:
        # 공기청정기에서 처음 출발하는 흐름인 경우
        if air[y][x] == AP:
            air[y + direction[rot][0]][x + direction[rot][1]] = 0
        # 공기청정기에 마지막으로 도달하는 흐름인 경우
        elif air[y + direction[rot][0]][x + direction[rot][1]] == AP:
            pass
        # 그 이외의 일반적인 경우
        else:
            air[y + direction[rot][0]][x + direction[rot][1]] = air[y][x]

    for y, x, rot in flow2:
        # 공기청정기에서 처음 출발하는 흐름인 경우
        if air[y][x] == AP:
            air[y + direction[rot][0]][x + direction[rot][1]] = 0
        # 공기청정기에 마지막으로 도달하는 흐름인 경우
        elif air[y + direction[rot][0]][x + direction[rot][1]] == AP:
            pass
        # 그 이외의 일반적인 경우
        else:
            air[y + direction[rot][0]][x + direction[rot][1]] = air[y][x]

    # print(*air, sep="\n")

# 최종 결과 분석
print(sum(map(sum, air)) + 2)
