from copy import deepcopy
import sys

input = sys.stdin.readline

# def start():
#     for i in range(N):
#         for j in range(M):
#             if not master[i][j]:
#                 return i, j


# def add_answer():
#     for i in range(N):
#         for j in range(M):
#             answer[i][j] = max(answer[i][j], visited[i][j])
#     return 0


move = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

N, M = map(int, input().split())
maze = [input() for _ in range(N)]
good = [[0] * M for _ in range(N)]
master = [[False] * M for _ in range(N)]

# while not all(map(all, master)):
#     sy, sx = start()

answer = 0
for i in range(N):
    for j in range(M):
        if not master[i][j]:
            temp = deepcopy(good)

            sy, sx = i, j
            # find start point
            visited = [[0] * M for _ in range(N)]
            visited[sy][sx] = 1
            temp[sy][sx] = 1
            count = 1
            master[sy][sx] = True
            stack = [(sy, sx)]

            # DFS
            while stack:
                y, x = stack.pop()

                dy, dx = move[maze[y][x]]
                ny, nx = y + dy, x + dx

                if not (0 <= ny < N and 0 <= nx < M):
                    good = temp
                    answer += count
                    break
                else:
                    if not visited[ny][nx]:
                        if master[ny][nx]:
                            if good[ny][nx]:
                                good = temp
                                answer += count
                            break
                        else:
                            stack.append((ny, nx))
                            visited[ny][nx] = 1
                            temp[ny][nx] = 1
                            count += 1
                            master[ny][nx] = True

# print(sum(map(sum, answer)))
print(answer)
