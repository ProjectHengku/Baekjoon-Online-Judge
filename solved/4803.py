def dfs(node, parent):
    global cycle

    for next in graph[node]:
        if next != parent and visited[next]:
            cycle = True

        if not visited[next]:
            visited[next] = True
            dfs(next, node)
            # visited[next] = False


n, m = map(int, input().split())
case = 0
while (n, m) != (0, 0):
    case += 1

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    T = 0
    while not all(visited[1:]):
        for i in range(1, n + 1):
            if not visited[i]:
                start = i
                visited[i] = True
                break

        cycle = False
        dfs(start, None)

        if not cycle:
            T += 1

    print(f"Case {case}:", end=" ")
    if T > 0:
        if T == 1:
            print("There is one tree.")
        else:
            print(f"A forest of {T} trees.")
    else:
        print("No trees.")

    n, m = map(int, input().split())
