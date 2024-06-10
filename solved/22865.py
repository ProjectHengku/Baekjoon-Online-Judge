import sys
from heapq import heappush, heappop


def dijk(start):
    shortcut = [float("inf")] * (N + 1)
    shortcut[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        used, now = heappop(heap)

        for node, cost in road[now]:
            exp = used + cost
            if exp < shortcut[node]:
                shortcut[node] = exp
                heappush(heap, (exp, node))

    return shortcut


input = sys.stdin.readline

N = int(input())
A, B, C = map(int, input().split())
M = int(input())

road = [[] for _ in range(N + 1)]
for _ in range(M):
    D, E, L = map(int, input().split())
    road[D].append((E, L))
    road[E].append((D, L))

# farA = [float('inf')] * (N+1)
# farB = [float('inf')] * (N+1)
# farC = [float('inf')] * (N+1)

# 3-dijkstra
farA = dijk(A)
farB = dijk(B)
farC = dijk(C)

farX = [(i, min(farA[i], farB[i], farC[i])) for i in range(1, N + 1)]
farX.sort(key=lambda x: (-x[1], x[0]))

print(farX[0][0])
