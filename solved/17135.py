import itertools, copy


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 궁수 위치는 N 번째 줄 가로 어딘가
# 그 중에서 3개 골라서 배치
ay = N
archors = list(itertools.combinations(range(M), 3))

maxkill = 0
for archor in archors:
    # 게임 시뮬레이션
    # 적이 판에 존재하는 동안
    game = copy.deepcopy(board)
    kill = 0
    while any(map(any, game)):
        # 궁수 x좌표
        # 일단 적들 스캔함
        enemy = []
        for i in range(N):
            for j in range(M):
                if game[i][j] == 1:
                    enemy.append((i, j))

        delete = set()
        for ax in archor:
            # 범위 이내면 타겟 범주에 넣음
            target = []
            for y, x in enemy:
                dist = abs(ay - y) + abs(ax - x)
                if dist <= D:
                    target.append((dist, y, x))
            target.sort(key=lambda x: (x[0], x[2]))
            if target:
                delete.add((target[0][1], target[0][2]))
        # 제일 가까운 적 제거 (중복 가능)
        for y, x in delete:
            game[y][x] = 0
            kill += 1
        # 다 쏘면 앞으로 한 칸씩 당김
        del game[-1]
        game.insert(0, [0] * M)
    # 각 경우마다 최대값 갱신
    if kill > maxkill:
        maxkill = kill

print(maxkill)
