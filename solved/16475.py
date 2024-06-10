from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, M, K, L, P = map(int, input().split())

trap = [False] * (N + 1)
trapzone = list(map(int, input().split()))
for zone in trapzone:
    trap[zone] = True

path = [[] for _ in range(N + 1)]
for _ in range(M - L):
    A, B, C = map(int, input().split())
    path[A].append((B, C))

trappath1 = [[] for _ in range(N + 1)]
trappath2 = [[] for _ in range(N + 1)]
for _ in range(L):
    A, B, C = map(int, input().split())
    trappath1[A].append((B, C))
    trappath2[B].append((A, C))

S, E = map(int, input().split())

visited = [[float("inf")] * (N + 1) for _ in range(2 * P + 1)]
visited[0][S] = 0

heap = [(0, S, 0, False)]
while heap:
    used, current, switch, reverse = heappop(heap)

    if current == E:
        print(used)
        exit()

    for next, cost in path[current]:
        exp = used + cost
        if visited[(switch + 1) % (2 * P) if trap[next] else switch][next] > exp:
            visited[(switch + 1) % (2 * P) if trap[next] else switch][next] = exp
            heappush(
                heap,
                (
                    exp,
                    next,
                    (switch + 1) % (2 * P) if trap[next] else switch,
                    not reverse if trap[next] and (switch + 1) % P == 0 else reverse,
                ),
            )

    if not reverse:
        for next, cost in trappath1[current]:
            exp = used + cost
            if visited[(switch + 1) % (2 * P) if trap[next] else switch][next] > exp:
                visited[(switch + 1) % (2 * P) if trap[next] else switch][next] = exp
                heappush(
                    heap,
                    (
                        exp,
                        next,
                        (switch + 1) % (2 * P) if trap[next] else switch,
                        (
                            not reverse
                            if trap[next] and (switch + 1) % P == 0
                            else reverse
                        ),
                    ),
                )
    else:
        for next, cost in trappath2[current]:
            exp = used + cost
            if visited[(switch + 1) % (2 * P) if trap[next] else switch][next] > exp:
                visited[(switch + 1) % (2 * P) if trap[next] else switch][next] = exp
                heappush(
                    heap,
                    (
                        exp,
                        next,
                        (switch + 1) % (2 * P) if trap[next] else switch,
                        (
                            not reverse
                            if trap[next] and (switch + 1) % P == 0
                            else reverse
                        ),
                    ),
                )
else:
    print(-1)
