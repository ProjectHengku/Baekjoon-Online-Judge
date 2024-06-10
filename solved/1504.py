import sys
from heapq import heappop, heappush


def find_path(a, b):
    travel = [float("inf")] * (N + 1)
    heap = []

    heappush(heap, (0, a))
    travel[a] = 0

    while heap:
        total, now = heappop(heap)
        if travel[now] < total:
            continue

        for next, weight in dist[now]:
            exp = total + weight
            if exp < travel[next]:
                travel[next] = exp
                heappush(heap, (exp, next))

    return travel[b]


input = sys.stdin.readline

N, E = map(int, input().split())
dist = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    dist[a].append((b, c))
    dist[b].append((a, c))

v1, v2 = map(int, input().split())

# 한쪽 끝 부터 v1 까지 이동하기 + v1 에서 v2 로 이동하기 + v2 에서 반대 끝으로 이동하기
data = []
for a, b in ((1, v1), (N, v1), (v1, v2), (v2, 1), (v2, N)):
    data.append(find_path(a, b))

ans = min(data[0] + data[2] + data[4], data[1] + data[2] + data[3])

if ans == float("inf"):
    print(-1)
else:
    print(ans)
