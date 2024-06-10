from heapq import heappop, heappush
import sys

input = sys.stdin.readline

# game setup
game = [[0] * 501 for _ in range(501)]

# danger zone
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            game[y][x] = 1

# death zone
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            game[y][x] = float("inf")

# cost(as visited) memo
visited = [[251001] * 501 for _ in range(501)]
move = ((1, 0), (0, 1), (0, -1), (-1, 0))

heap = [(0, 0, 0)]

while heap:
    used, y, x = heappop(heap)

    if (y, x) == (500, 500):
        if used < 251001:
            print(used)
        else:
            print(-1)
        exit()

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 501 and 0 <= nx < 501:
            exp = used + game[ny][nx]
            if visited[ny][nx] > exp:
                visited[ny][nx] = exp
                heappush(heap, (exp, ny, nx))

print(-1)
