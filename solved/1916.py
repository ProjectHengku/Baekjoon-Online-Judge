import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())

table = [[] for _ in range(N + 1)]
for depart, arrive, cost in bus:
    table[depart].append((arrive, cost))

cheapest = [float("inf")] * (N + 1)
cheapest[start] = 0
heap = []
heappush(heap, (0, start))

while heap:
    used, depart = heappop(heap)

    if used > cheapest[depart]:
        continue

    for arrive, cost in table[depart]:
        exp = used + cost
        if exp < cheapest[arrive]:
            cheapest[arrive] = exp
            heappush(heap, (exp, arrive))


print(cheapest[end])
