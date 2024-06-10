import sys

input = sys.stdin.readline

V = int(input())

# build tree
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    start, *info, end = map(int, input().split())
    n = len(info)
    for i in range(0, n, 2):
        node, length = info[i], info[i + 1]
        tree[start].append((node, length))

# dfs 1
stack = [(1, 0)]
visited = [False] * (V + 1)
visited[1] = True

deepest = (-1, -1)
while stack:
    current, travel = stack.pop()

    # renew deepest
    if travel > deepest[1]:
        deepest = (current, travel)

    for node, length in tree[current]:
        if not visited[node]:
            stack.append((node, travel + length))
            visited[node] = True

# dfs 2
stack = [(deepest[0], 0)]
visited = [False] * (V + 1)
visited[deepest[0]] = True

diameter = -1
while stack:
    current, travel = stack.pop()

    # renew diameter
    if travel > diameter:
        diameter = travel

    for node, length in tree[current]:
        if not visited[node]:
            stack.append((node, travel + length))
            visited[node] = True

print(diameter)
