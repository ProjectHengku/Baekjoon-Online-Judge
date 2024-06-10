import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, l = map(int, input().split())
    bus[a].append((b, l))
s, d = map(int, input().split())

heap = [(0, s, [s])]
visited = [float("inf")] * (n + 1)
visited[s] = 0

while heap:
    used, current, route = heappop(heap)

    if current == d:
        print(used)
        print(len(route))
        print(*route)

        exit()

    for next, cost in bus[current]:
        exp = used + cost
        if visited[next] > exp:
            visited[next] = exp

            heappush(heap, (exp, next, route + [next]))
