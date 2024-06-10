from collections import deque

N, M = map(int, input().split())

# 그래프 작성
graph = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].add(b)
    graph[b].add(a)

scores = [0] * (N + 1)

for i in range(1, N + 1):
    queue = deque()

    dist = [0] * (N + 1)
    visited = [False] * (N + 1)
    for friend in graph[i]:
        queue.append((friend, 1))
        visited[friend] = True

    while queue:
        friend, num = queue.popleft()

        for j in [k for k in range(1, N + 1) if k != i]:
            if friend == j:
                if dist[j] != 0:
                    dist[j] = min(dist[j], num)
                else:
                    dist[j] = num

        for next_friend in graph[friend]:
            if not visited[next_friend]:
                queue.append((next_friend, num + 1))
                visited[next_friend] = True

    scores[i] = sum(dist)

print(scores.index(min(scores[1:])))
