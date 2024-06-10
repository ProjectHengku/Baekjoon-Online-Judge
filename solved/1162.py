from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    road[a].append((b, t))
    road[b].append((a, t))

visited = [[float("inf")] * (N + 1) for _ in range(K + 1)]
visited[K][1] = 0
heap = [(0, 1, K)]

while heap:
    time, current, build = heappop(heap)

    if current == N:
        print(time)
        exit()

    if visited[build][current] < time:
        continue

    for next, time_spend in road[current]:
        if build > 0 and visited[build - 1][next] > time:
            visited[build - 1][next] = time
            heappush(heap, (time, next, build - 1))
        exp = time + time_spend
        if visited[build][next] > exp:
            visited[build][next] = exp
            heappush(heap, (exp, next, build))
