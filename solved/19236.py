from copy import deepcopy


def move(sy, sx, current):
    fishes = [[0, 0, 0, 0] for _ in range(17)]
    for i in range(4):
        for j in range(4):
            if current[i][j][0]:
                fishes[current[i][j][0]] = (current[i][j][0], current[i][j][1], i, j)

    for fish, rot, y, x in fishes:
        if fish:
            for _ in range(8):
                dy, dx = direction[rot]
                ny, nx = y + dy, x + dx
                if (0 <= ny < 4 and 0 <= nx < 4) and (ny, nx) != (sy, sx):
                    fishes[current[y][x][0]] = (
                        current[y][x][0],
                        current[y][x][1],
                        ny,
                        nx,
                    )
                    fishes[current[ny][nx][0]] = (
                        current[ny][nx][0],
                        current[ny][nx][1],
                        y,
                        x,
                    )
                    current[y][x], current[ny][nx] = current[ny][nx], current[y][x]
                    break
                else:
                    rot = rot + 1 if rot + 1 <= 8 else 1
                    current[y][x][1] = rot

    return current


def eat(y, x, score, current):
    global maximum

    current = deepcopy(current)

    fish = current[y][x][0]
    rot = current[y][x][1]

    score += fish
    current[y][x][0] = 0

    if maximum < score:
        maximum = score

    current = move(y, x, current)

    dy, dx = direction[rot]
    for l in range(1, 4):
        ny, nx = y + l * dy, x + l * dx
        if (0 <= ny < 4 and 0 <= nx < 4) and current[ny][nx][0]:
            eat(ny, nx, score, current)


direction = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1),
}

space = []
for _ in range(4):
    fishes = list(map(int, input().split()))
    space.append([fishes[i : i + 2] for i in range(0, 8, 2)])

maximum = 0

eat(0, 0, 0, space)

print(maximum)
