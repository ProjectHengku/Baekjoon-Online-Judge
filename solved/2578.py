def BINGO(board):
    count = 0

    # 가로
    for row in board:
        if all(row):
            count += 1

    # 세로
    board_rot = list(zip(*board[::-1]))
    for col in board_rot:
        if all(col):
            count += 1

    # 대각선
    cross1 = [board[i][i] for i in range(5)]
    cross2 = [board[i][4 - i] for i in range(5)]

    if all(cross1):
        count += 1

    if all(cross2):
        count += 1

    if count >= 3:
        return True
    else:
        return False


def find2D(arr, target):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == target:
                return i, j


select = [list(map(int, input().split())) for _ in range(5)]
game = [list(map(int, input().split())) for _ in range(5)]

# 초기값 세팅
board = [[False] * 5 for _ in range(5)]
count = 0

for i in range(5):
    for j in range(5):
        now = game[i][j]
        y, x = find2D(select, now)

        board[y][x] = True
        count += 1

        if BINGO(board):
            print(count)
            exit()
