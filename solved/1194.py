from collections import deque


def convert_keys(letter):
    return ord(letter) - ord("a")


def convert_door(letter):
    return ord(letter) - ord("A")


def start():
    for i in range(N):
        for j in range(M):
            if maze[i][j] == "0":
                return i, j


def is_open(door, key):
    if door & key:
        return True
    else:
        return False


N, M = map(int, input().split())
maze = [input() for _ in range(N)]

sy, sx = start()

visited = [[[False] * (2**6) for _ in range(M)] for _ in range(N)]
visited[sy][sx][0] = True

queue = deque()
queue.append((sy, sx, 0, 0))

while queue:
    y, x, own, time = queue.popleft()

    if maze[y][x] == "1":
        print(time)
        exit()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if (
            (0 <= ny < N and 0 <= nx < M)
            and maze[ny][nx] != "#"
            and not visited[ny][nx][own]
        ):
            # loot key
            if "a" <= maze[ny][nx] <= "f":
                new_own = own | (1 << convert_keys(maze[ny][nx]))
                visited[ny][nx][new_own] = True
                queue.append((ny, nx, new_own, time + 1))
            # door
            elif "A" <= maze[ny][nx] <= "F":
                if is_open(1 << convert_door(maze[ny][nx]), own):
                    visited[ny][nx][own] = True
                    queue.append((ny, nx, own, time + 1))
            else:
                visited[ny][nx][own] = True
                queue.append((ny, nx, own, time + 1))
else:
    print(-1)
