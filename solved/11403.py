N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]

# 그래프 작성
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and mat[i][j]:
            graph[i].append(j)

ans = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 그래프 탐색
        stack = []
        visited = [False] * N

        stack.append(i)

        available = False
        while stack:
            current = stack.pop()

            for node in graph[current]:
                if node == j:
                    available = True
                    break

                if not visited[node]:
                    stack.append(node)
                    visited[node] = True

            if available:
                break

        if available:
            ans[i][j] = 1

for row in ans:
    print(*row)
