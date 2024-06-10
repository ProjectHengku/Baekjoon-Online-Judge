R, C = map(int, input().split())
board = [input() for _ in range(R)]

move = ((1, 0), (0, 1), (-1, 0), (0, -1))

stack = [(0, 0, {board[0][0]})]

maximum = 0
while stack:
    y, x, travel = stack.pop()

    maximum = max(maximum, len(travel))

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and not board[ny][nx] in travel:
            stack.append((ny, nx, travel | {board[ny][nx]}))

print(maximum)
