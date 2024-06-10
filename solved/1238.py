import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M, X = map(int, input().split())
road = [[] for _ in range(N + 1)]
rrad = [[] for _ in range(N + 1)]

# N-dijkstra
for _ in range(M):
    s, e, t = map(int, input().split())

    road[s].append((e, t))
    rrad[e].append((s, t))

# go to X
goto = [0] + [float("inf")] * (N)
goto[X] = 0
heap = []
heappush(heap, (0, X))

while heap:
    used, now = heappop(heap)

    for node, cost in rrad[now]:
        exp = used + cost
        if exp < goto[node]:
            goto[node] = exp
            heappush(heap, (exp, node))

# back to home
back = [0] + [float("inf")] * (N)
back[X] = 0
heap = []
heappush(heap, (0, X))

while heap:
    used, now = heappop(heap)

    for node, cost in road[now]:
        exp = used + cost
        if exp < back[node]:
            back[node] = exp
            heappush(heap, (exp, node))

time_spent = [goto[i] + back[i] for i in range(N + 1)]

print(max(time_spent))
