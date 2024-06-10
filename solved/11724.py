import random
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# 그래프 채움
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 초기 환경 설정
stack = []
stack.append(graph[1])
visited[1] = True
numbers = [1]
count = 0
visit = 1

while visit < N:
    # 깊이 우선 탐색
    while stack:
        current = stack.pop()

        for next in current:
            if not visited[next]:
                visited[next] = True
                stack.append(graph[next])
                numbers.append(next)

    count += 1

    # 안간 곳 하나 지정해줘야될듯
    where = list(range(1, N + 1))
    for node in numbers:
        if node in where:
            where.remove(node)

    if where:
        go = random.choice(where)
        stack.append(graph[go])
        numbers.append(go)
        visited[go] = True
        visit += 1

# 결과 나옴
print(count)
