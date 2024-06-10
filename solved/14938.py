from heapq import heappush, heappop

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
road = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    road[a].append((b, l))
    road[b].append((a, l))

loot = [0] * (n + 1)

for land in range(1, n + 1):
    get = 0

    shortest = [float("inf")] * (n + 1)
    shortest[land] = 0

    heap = [(0, land)]
    while heap:
        used, current = heappop(heap)

        if used > m:
            break

        for next, cost in road[current]:
            exp = used + cost
            if shortest[next] > exp:
                shortest[next] = exp
                heappush(heap, (exp, next))

    for i in range(1, n + 1):
        if shortest[i] <= m:
            get += items[i]

    loot[land] = get

print(max(loot))
