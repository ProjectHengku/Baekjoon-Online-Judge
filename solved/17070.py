N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# 가로: 0, 세로: 1, 대각선: 2
dy = [0, 1, 1]
dx = [1, 0, 1]

queue = []
queue.append((0, 1, 0))

count = 0

while queue:
    y, x, rot = queue.pop()

    if y == N - 1 and x == N - 1:
        count += 1

    # 이전 방향 따라서 진행 경로 달라짐
    if rot == 0:
        if x + 1 < N and field[y][x + 1] != 1:
            queue.append((y, x + 1, 0))
        if (
            y + 1 < N
            and x + 1 < N
            and field[y + 1][x + 1] != 1
            and field[y][x + 1] != 1
            and field[y + 1][x] != 1
        ):
            queue.append((y + 1, x + 1, 2))
    elif rot == 1:
        if y + 1 < N and field[y + 1][x] != 1:
            queue.append((y + 1, x, 1))
        if (
            y + 1 < N
            and x + 1 < N
            and field[y + 1][x + 1] != 1
            and field[y][x + 1] != 1
            and field[y + 1][x] != 1
        ):
            queue.append((y + 1, x + 1, 2))
    else:
        if x + 1 < N and field[y][x + 1] != 1:
            queue.append((y, x + 1, 0))
        if y + 1 < N and field[y + 1][x] != 1:
            queue.append((y + 1, x, 1))
        if (
            y + 1 < N
            and x + 1 < N
            and field[y + 1][x + 1] != 1
            and field[y][x + 1] != 1
            and field[y + 1][x] != 1
        ):
            queue.append((y + 1, x + 1, 2))


# 다 끝나고
print(count)
