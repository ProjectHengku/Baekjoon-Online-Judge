N, M = map(int, input().split())
campus = [input() for _ in range(N)]

# DFS
stack = []
visited = [[False] * M for _ in range(N)]

# 도연의 위치
flag = False
for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            stack.append((i, j))
            visited[i][j] = True

            flag = True
            break
    if flag:
        break

count = 0
while stack:
    y, x = stack.pop()

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx

        if (
            0 <= ny < N
            and 0 <= nx < M
            and campus[ny][nx] != "X"
            and not visited[ny][nx]
        ):
            if campus[ny][nx] == "P":
                count += 1
            stack.append((ny, nx))
            visited[ny][nx] = True

if count:
    print(count)
else:
    print("TT")
