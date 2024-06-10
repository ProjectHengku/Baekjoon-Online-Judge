N = int(input())
road = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end, length = map(int, input().split())

    road[start].append((end, length))
    road[end].append((start, length))

# dfs
visited = [False] * (N + 1)
visited[1] = True

stack = [(1, 0)]
deep = (0, 0)

while stack:
    current, total = stack.pop()

    if total > deep[1]:
        deep = (current, total)

    for node, length in road[current]:
        if not visited[node]:
            visited[node] = True
            stack.append((node, total + length))

visited = [False] * (N + 1)
visited[deep[0]] = True

stack = [(deep[0], 0)]
oppo = (0, 0)

from_deep = [0] * (N + 1)

while stack:
    current, total = stack.pop()

    from_deep[current] = total

    if total > oppo[1]:
        oppo = (current, total)

    for node, length in road[current]:
        if not visited[node]:
            visited[node] = True
            stack.append((node, total + length))

visited = [False] * (N + 1)
visited[oppo[0]] = True

stack = [(oppo[0], 0)]

from_oppo = [0] * (N + 1)

while stack:
    current, total = stack.pop()

    from_oppo[current] = total

    for node, length in road[current]:
        if not visited[node]:
            visited[node] = True
            stack.append((node, total + length))

for i in range(1, N + 1):
    print(max(from_deep[i], from_oppo[i]))
