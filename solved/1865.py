import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def bellman_ford(start):
    time[start] = 0
    for i in range(N):
        for current, edges in enumerate(route):
            for node, cost in edges:
                if time[node] > time[current] + cost:
                    time[node] = time[current] + cost
                    if i == N - 1:
                        return "YES"

    return "NO"


TC = int(input())

for tc in range(TC):
    N, M, W = map(int, input().split())

    route = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        route[S].append((E, T))
        route[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        route[S].append((E, -T))

    results = []

    time = [10**9] * (N + 1)

    print(bellman_ford(1))
