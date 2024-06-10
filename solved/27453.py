from copy import deepcopy as copy
from collections import deque


def find(target):
    for y in range(N):
        for x in range(M):
            if vill[y][x] == target:
                return y, x


N, M, K = map(int, input().split())
vill = [input() for _ in range(N)]

sy, sx = find("S")
hy, hx = find("H")

visited = [[[False, False, False, False] for _ in range(M)] for _ in range(N)]

move = ((1, 0), (0, 1), (0, -1), (-1, 0))

queue = deque([(0, sy, sx, -1, -1)])
while queue:
    travel, y, x, by, bx = queue.popleft()

    if (y, x) == (hy, hx):
        print(travel)
        exit()

    for rot in range(4):
        dy, dx = move[rot]
        ny, nx = y + dy, x + dx
        if (
            (0 <= ny < N and 0 <= nx < M)
            and (ny, nx) != (by, bx)
            and vill[ny][nx] != "X"
        ):
            if (
                (int(vill[ny][nx]) if vill[ny][nx].isdecimal() else 0)
                + (int(vill[y][x]) if vill[y][x].isdecimal() else 0)
                + (
                    int(vill[by][bx])
                    if ((by, bx) != (-1, -1) and vill[by][bx].isdecimal())
                    else 0
                )
            ) > K:
                continue
            if visited[ny][nx][rot]:
                continue

            visited[ny][nx][rot] = True
            queue.append((travel + 1, ny, nx, y, x))

print(-1)
