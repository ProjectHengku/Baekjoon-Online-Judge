field = [[False] * 101 for _ in range(101)]
area = 0

for _ in range(4):
    # 좌표 받음
    x1, y1, x2, y2 = map(int, input().split())

    # 점 격자를 면 격자로 변환
    # 면 찍음
    for y in range(y1, y2):
        for x in range(x1, x2):
            if not field[y][x]:
                field[y][x] = True
                area += 1

print(area)