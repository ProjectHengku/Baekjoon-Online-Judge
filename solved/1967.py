import sys

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

# dfs1
stack = []
point, expensive = 0, -1
visited = [False] * (n + 1)

stack.append((1, 0))
visited[1] = True

while stack:
    now, used = stack.pop()

    if used > expensive:
        point, expensive = now, used

    for node, cost in tree[now]:
        if not visited[node]:
            stack.append((node, used + cost))
            visited[node] = True

# dfs2
stack = []
radius = -1
visited = [False] * (n + 1)

stack.append((point, 0))
visited[point] = True

while stack:
    now, used = stack.pop()

    if used > radius:
        radius = used

    for node, cost in tree[now]:
        if not visited[node]:
            stack.append((node, used + cost))
            visited[node] = True

print(radius)
