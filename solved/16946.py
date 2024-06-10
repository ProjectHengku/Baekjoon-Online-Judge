import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mapmat = [input() for _ in range(N)]

answer = [["0"] * M for _ in range(N)]

wall_point = []
area_size = {0: 0}

visited = [[0] * M for _ in range(N)]
area = 0

for i in range(N):
    for j in range(M):
        if mapmat[i][j] == "0" and not visited[i][j]:
            area += 1
            count = 1
            visited[i][j] = area

            stack = [(i, j)]

            while stack:
                y, x = stack.pop()

                for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if (
                        (0 <= ny < N and 0 <= nx < M)
                        and mapmat[ny][nx] == "0"
                        and not visited[ny][nx]
                    ):
                        visited[ny][nx] = area
                        stack.append((ny, nx))
                        count += 1

            area_size[area] = count

        elif mapmat[i][j] == "1":
            wall_point.append((i, j))

for y, x in wall_point:
    area = 1
    areas = set()
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            areas.add(visited[ny][nx])
    for i in areas:
        area += area_size[i]
    answer[y][x] = str(area % 10)

for row in answer:
    print("".join(row))
