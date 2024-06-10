from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort()

queue = deque()
visited = [0] * (N + 1)

queue.append(graph[R])
count = 1
visited[R] = count

while queue:
    nodes = queue.popleft()

    for node in nodes:
        if not visited[node]:
            queue.append(graph[node])
            visited[node] = True
            count += 1
            visited[node] = count

for i in range(1, N + 1):
    print(visited[i])
