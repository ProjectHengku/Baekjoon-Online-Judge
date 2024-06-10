from collections import deque

N, K = map(int, input().split())

stack = deque()
starttime = 0
stack.append((N, starttime))

visited = [False] * 200001
visited[N] = True

while stack:
    x, time = stack.popleft()

    if x == K:
        break

    if 0 <= x + 1 <= 200000 and not visited[x + 1]:
        visited[x + 1] = True
        stack.append((x + 1, time + 1))
    if 0 <= x - 1 <= 200000 and not visited[x - 1]:
        visited[x - 1] = True
        stack.append((x - 1, time + 1))
    if 0 <= x * 2 <= 200000 and not visited[x * 2]:
        visited[x * 2] = True
        stack.append((x * 2, time + 1))

print(time)
