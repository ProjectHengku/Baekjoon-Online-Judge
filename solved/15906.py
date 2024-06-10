from heapq import heappush, heappop


def search(y, x):
    output = []
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        while 0 <= ny < N and 0 <= nx < N:
            if game[ny][nx] == "#":
                output.append((ny, nx))
                break
            ny += dy
            nx += dx

    return output


N, t, r, c = map(int, input().split())
r -= 1
c -= 1
game = [input() for _ in range(N)]

visited = [[float("inf")] * N for _ in range(N)]
visited[0][0] = 0

teleport = [[float("inf")] * N for _ in range(N)]

move = ((1, 0), (0, 1), (0, -1), (-1, 0))
heap = [(0, 0, 0, False)]

while heap:
    time, y, x, transform = heappop(heap)

    if (y, x) == (r, c):
        print(time)
        exit()

    if transform:
        for ny, nx in search(y, x):
            if teleport[ny][nx] > time + 1:
                teleport[ny][nx] = time + 1
                # remain transform
                heappush(heap, (time + 1, ny, nx, True))
        # return normal
        if visited[y][x] > time:
            visited[y][x] = time
            heappush(heap, (time, y, x, False))
    else:
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N and 0 <= nx < N) and visited[ny][nx] > time + 1:
                visited[ny][nx] = time + 1
                heappush(heap, (time + 1, ny, nx, False))
        # transform
        if teleport[y][x] > time + t:
            teleport[y][x] = time + t
            heappush(heap, (time + t, y, x, True))
