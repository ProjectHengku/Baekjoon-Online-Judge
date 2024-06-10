from heapq import heappush, heappop
import sys

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
M = int(input())
cost = [list(map(int, input().split())) for _ in range(M)]

complete = tuple(sorted(A))

visited = {tuple(A): 0}

heap = [(0, tuple(A))]
while heap:
    used, now = heappop(heap)

    if now == complete:
        print(used)
        exit()

    for l, r, c in cost:
        l -= 1
        r -= 1
        current = list(now)
        exp = used + c
        current[l], current[r] = current[r], current[l]
        next = tuple(current)
        try:
            if visited[next] > exp:
                visited[next] = exp
                heappush(heap, (exp, next))
        except KeyError:
            visited[next] = exp
            heappush(heap, (exp, next))

print(-1)
