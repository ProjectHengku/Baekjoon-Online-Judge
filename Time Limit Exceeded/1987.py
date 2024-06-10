def count(number):
    count = 0
    number = bin(number)

    for digit in number[2:]:
        if digit == "1":
            count += 1

    return count


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# convert into number
for i in range(R):
    for j in range(C):
        board[i][j] = ord(board[i][j]) - ord("A")

move = ((1, 0), (0, 1), (-1, 0), (0, -1))

stack = [(0, 0, 1 << board[0][0])]

maximum = 0
while stack:
    y, x, travel = stack.pop()

    traveled = count(travel)
    maximum = max(maximum, traveled)

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if (0 <= ny < R and 0 <= nx < C) and not (travel & (1 << board[ny][nx])):
            stack.append((ny, nx, travel | (1 << board[ny][nx])))

print(maximum)
