import itertools, random

# 초기값 받음
N = int(input())
population = [0]
population.extend(list(map(int, input().split())))
graph = [0]
for _ in range(N):
    edges, *node = map(int, input().split())
    graph.append(node)

# 경우의 수 전개
cases = []
groupAll = set(range(1, N + 1))
for i in range(1, N):
    cases.extend(list(itertools.combinations(range(1, N + 1), i)))

# 각 경우의 수 별 선거구 계산
min_gap = float("inf")
available = False
for case in cases:
    groupA = set(case)
    groupB = groupAll - groupA

    # 일단 선거구로서 형태가 성립하는가?
    stack = []
    visited = [False] * (N + 1)
    first = random.choice(list(groupA))
    second = random.choice(list(groupB))
    stack.append(first)
    stack.append(second)
    visited[first] = True
    visited[second] = True

    # DFS
    while stack:
        current = stack.pop()
        for node in graph[current]:
            if not visited[node]:
                # A는 A끼리
                if current in groupA:
                    if node in groupA:
                        stack.append(node)
                        visited[node] = True
                # B는 B끼리
                else:
                    if node in groupB:
                        stack.append(node)
                        visited[node] = True

    # 서로의 영역이 이어져 있다면 A와 B구역 합쳐서 전부 돌아져야 함
    if sum(visited) == N:
        # 선거구의 인구수 차를 최소화
        gap = abs(
            sum([population[i] for i in groupA]) - sum([population[i] for i in groupB])
        )
        if gap < min_gap:
            min_gap = gap
        available = True
    else:
        continue

if available:
    print(min_gap)
else:
    print(-1)
