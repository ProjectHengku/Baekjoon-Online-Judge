from collections import deque

N, M = map(int, input().split())

board = [i for i in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

queue = deque()
queue.append((1, 0))

visited = [False] * 101
visited[1] = True

while queue:
    now, count = queue.popleft()
    if now == 100:
        break

    for i in range(1, 7):
        if now + i <= 100 and not visited[now + i]:
            queue.append((board[now + i], count + 1))
            visited[now + i] = True

print(count)
