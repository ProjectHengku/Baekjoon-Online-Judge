import sys
from heapq import heappop, heappush

input = sys.stdin.readline
output = sys.stdout.write

N, M, K = map(int, input().split())
S, D = map(int, input().split())

road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    road[a].append((b, w))
    road[b].append((a, w))

# dijkstra
visited = [False] * N

dist = [[float("inf")] * (N) for _ in range(N + 1)]
dist[S][0] = 0

heap = [(0, 0, S)]
while heap:
    used, count, current = heappop(heap)

    flag = False
    for i in range(count):
        if dist[current][i] < used:
            flag = True
            break

    if dist[current][count] < used or count == N - 1 or flag:
        continue

    for next, cost in road[current]:
        exp = used + cost
        if dist[next][count + 1] > exp:
            dist[next][count + 1] = exp
            heappush(heap, (exp, count + 1, next))

paid = dist[D]

output(str(min(paid)) + "\n")

# tax increasement
tax = 0
for _ in range(K):
    cost = float("inf")
    tax += int(input())
    for idx, used in enumerate(paid):
        cost = min(cost, used + tax * idx)

    output(str(cost) + "\n")
