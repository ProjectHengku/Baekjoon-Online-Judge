def dfs(y, x, count):
    global maximum

    maximum = max(maximum, count)

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and not board[ny][nx] in alpha:
            alpha.add(board[ny][nx])
            dfs(ny, nx, count + 1)
            alpha.remove(board[ny][nx])


R, C = map(int, input().split())
board = [input() for _ in range(R)]

move = ((1, 0), (0, 1), (-1, 0), (0, -1))

alpha = {board[0][0]}
maximum = 0

dfs(0, 0, 1)

print(maximum)
