import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 부모 노드 기록하면 되지 않을까
tree = [0] * (N + 1)

# 그래프 생성
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1부터 뻗어나가면 될듯
for child in graph[1]:
    tree[child] = 1
    visited[child] = True
visited[1] = True
queue = deque()
queue.extend(graph[1])

while queue:
    parent = queue.popleft()

    children = graph[parent]
    for child in children:
        if not visited[child]:
            visited[child] = True
            tree[child] = parent
            queue.append(child)


for i in range(2, N + 1):
    sys.stdout.write(str(tree[i]) + "\n")
