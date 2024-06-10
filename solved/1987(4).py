def dfs(y, x, count):
    global maximum

    maximum = max(maximum, count)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and not visited[board[ny][nx]]:
            visited[board[ny][nx]] = True
            dfs(ny, nx, count + 1)
            visited[board[ny][nx]] = False


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        board[i][j] = ord(board[i][j]) - ord("A")

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited = [False] * 26
maximum = 0

visited[board[0][0]] = True
dfs(0, 0, 1)

print(maximum)
