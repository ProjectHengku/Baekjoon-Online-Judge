n, m = map(int, input().split())
r, c, d = map(int, input().split())
mapdata = [[None] * m for _ in range(n)]

for i in range(n):
    mapdata[i] = list(map(int, input().split()))

# 0: north, 1: east, 2: south, 3: west
# 0: empty, 1: wall, 2: cleaned

# case 1: no empty space around 4 directions
# case 2: empty space around 4 directions

count = 0

def clean(y, x):
    # clean current location
    if mapdata[y][x] == 0:
        mapdata[y][x] = 2
        global count
        count += 1

def move1(d):
    # 1. move to next location: case 1
    global r, c
    if d == 0:
        r = r + 1
    elif d == 1:
        c = c - 1
    elif d == 2:
        r = r - 1
    elif d == 3:
        c = c + 1

def turn2(d):
    # 1. turn left: case 2
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2
    return d

def move2(d):
    # 2. move to next location: case 2
    global r, c
    if d == 0:
        r = r - 1
    elif d == 1:
        c = c + 1
    elif d == 2:
        r = r + 1
    elif d == 3:
        c = c - 1

# assemble above situations functions into one algorithm
# start from initial location
while True:
    clean(r, c)
    if mapdata[r - 1][c] != 0 and mapdata[r][c + 1] != 0 and mapdata[r + 1][c] != 0 and mapdata[r][c - 1] != 0:
        move1(d)
        if mapdata[r][c] == 1:
            break
    else:
        d = turn2(d)
        # turn left until find empty space
        while True:
            if (d == 0 and mapdata[r - 1][c] == 0) or (d == 1 and mapdata[r][c + 1] == 0) or (d == 2 and mapdata[r + 1][c] == 0) or (d == 3 and mapdata[r][c - 1] == 0):
                break
            else:
                d = turn2(d)
        # move to next location
        move2(d)

print(count)