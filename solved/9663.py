def queen(row, col, board):
    global count
    if row == N:
        count += 1
        return 0
    else:
        for i in board:
            available = True
            for j in range(len(col)):
                if abs(col[j] - i) == abs(row - j):
                    available = False
                    break
            if available:
                queen(row + 1, col + [i], board - {i})


N = int(input())

# 초기 환경 설정
count = 0
board = set(range(N))
col = []

queen(0, col, board)
print(count)
