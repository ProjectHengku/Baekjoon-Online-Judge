import sys
input = sys.stdin.readline

# get N, M 
N, M = map(int, input().split())

# set perfect 8 * 8 chess board
# case 1: start with white
white_chess_board = []
for _ in range(4):
    white_chess_board.append("WBWBWBWB")
    white_chess_board.append("BWBWBWBW")
# case 2: start with black
black_chess_board = []
for _ in range(4):
    black_chess_board.append("BWBWBWBW")
    black_chess_board.append("WBWBWBWB")

# get N * M board
board = []
for _ in range(N):
    board.append(input())

# check if N * M board includes perfect 8 * 8 chess board
# case 1: start with white
min_cnt = 64
for i in range(N - 7):
    for j in range(M - 7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != white_chess_board[k][l]:
                    cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
# case 2: start with black
for i in range(N - 7):
    for j in range(M - 7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != black_chess_board[k][l]:
                    cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt

# print result
print(min_cnt)