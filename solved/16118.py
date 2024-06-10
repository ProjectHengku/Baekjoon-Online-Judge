from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    road[a].append((b, d))
    road[b].append((a, d))

fox = [float("inf")] * (N + 1)
wolf = [[float("inf")] * (N + 1) for _ in range(2)]

fox[1] = 0
wolf[0][1] = 0

# fox
heap = [(0, 1)]
while heap:
    time, current = heappop(heap)

    if time > fox[current]:
        continue

    for next, length in road[current]:
        exp = time + length
        if fox[next] > exp:
            fox[next] = exp
            heappush(heap, (exp, next))

# wolf
heap = [(0, 1, 0)]
while heap:
    time, current, mode = heappop(heap)

    if time > wolf[mode][current]:
        continue

    for next, length in road[current]:
        exp = time + (length / 2 if mode == 0 else length * 2)
        if wolf[(mode + 1) % 2][next] > exp:
            wolf[(mode + 1) % 2][next] = exp
            heappush(heap, (exp, next, (mode + 1) % 2))

count = 0
for i in range(1, N + 1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        count += 1

print(count)
