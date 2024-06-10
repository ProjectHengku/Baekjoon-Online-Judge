from heapq import heappop, heappush

N, K = map(int, input().split())

visited = [False] * 100001
visited[N] = True
heap = []
heappush(heap, (0, N))

while heap:
    time, now = heappop(heap)

    if now == K:
        break

    if 0 <= now * 2 <= 100000 and not visited[now * 2]:
        heappush(heap, (time, now * 2))
        visited[now * 2] = True

    if now + 1 <= 100000 and not visited[now + 1]:
        heappush(heap, (time + 1, now + 1))
        visited[now + 1] = True

    if 0 <= now - 1 and not visited[now - 1]:
        heappush(heap, (time + 1, now - 1))
        visited[now - 1] = True

print(time)
