import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(i, j):
    if not (0 <= i < N and 0 <= j < M):
        return 1

    if good[i][j] != -1:
        return good[i][j]

    good[i][j] = 0

    good[i][j] = max(good[i][j], find(i + move[maze[i][j]][0], j + move[maze[i][j]][1]))
    return good[i][j]


move = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

good = [[-1] * M for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(M):
        if good[i][j] == -1:
            if find(i, j) != 0:
                answer += 1
        elif good[i][j] == 1:
            answer += 1

print(answer)
