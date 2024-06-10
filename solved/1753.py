import heapq, sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]

# write cost table
cost = [[] for _ in range(V + 1)]
for start, end, weight in edges:
    cost[start].append((end, weight))

answer = ["INF"] * (V + 1)

# Dijkstra
heap = []
dist = [float("inf")] * (V + 1)

dist[K] = 0
heapq.heappush(heap, (0, K))
while heap:
    sum_cost, current = heapq.heappop(heap)

    if dist[current] < sum_cost:
        continue

    for node, weight in cost[current]:
        expected = sum_cost + weight
        if expected < dist[node]:
            dist[node] = expected
            heapq.heappush(heap, (expected, node))

for i in range(1, V + 1):
    if dist[i] < float("inf"):
        answer[i] = dist[i]

for item in answer[1:]:
    print(item)
