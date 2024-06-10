import sys
from heapq import heappush, heappop

input = sys.stdin.readline
print = sys.stdin.write

N, T = map(int, input().split())
heat = list(map(int, input().split()))

route = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    I, V, W = map(int, input().split())
    route[I].append((V, W))
    route[V].append((I, W))

Q = int(input())

# dfs
visited = [False] * (N + 1)
visited[1] = True

stack = [(1, 0)]
deepest = (0, 0)


for _ in range(Q):
    start, end = map(int, input().split())
