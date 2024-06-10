import copy


def scan(position, input_data):
    global min_pocket
    if position:
        y, x, cctv = position[0]
        for rot in range(4):
            office = copy.deepcopy(input_data)
            for dy, dx in camsight[cctv][rot]:
                k = 0
                while (
                    0 <= y + k * dy < N
                    and 0 <= x + k * dx < M
                    and office[y + k * dy][x + k * dx] != 6
                ):
                    if office[y + k * dy][x + k * dx] == 0:
                        office[y + k * dy][x + k * dx] = "#"
                    k += 1
            scan(position[1:], office)
    else:
        pocket = sum([row.count(0) for row in input_data])
        if pocket < min_pocket:
            min_pocket = pocket
            return 0


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

camsight = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [
        [(0, -1), (-1, 0), (0, 1)],
        [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)],
        [(1, 0), (0, -1), (-1, 0)],
    ],
}
memo = []

position = []
# 후보군
for i in range(N):
    for j in range(M):
        # 빈 칸이거나 벽이거나 전방향 CCTV가 아니라면
        if office[i][j] not in (0, 5, 6, "#"):
            position.append((i, j, office[i][j]))
        elif office[i][j] == 5:
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                k = 0
                while (
                    0 <= i + k * dy < N
                    and 0 <= j + k * dx < M
                    and office[i + k * dy][j + k * dx] != 6
                ):
                    if office[i + k * dy][j + k * dx] == 0:
                        office[i + k * dy][j + k * dx] = "#"
                    k += 1

min_pocket = N * M
scan(position, office)

print(min_pocket)
