import sys


def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
        # x = find(graph[x])
    return graph[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        graph[b] = a
    else:
        graph[a] = b


sys.setrecursionlimit(3000000)
input = sys.stdin.readline


N = int(input())
graph = [i for i in range(N + 1)]
for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

bridge = []
for i in range(1, N + 1):
    if i == graph[i]:
        bridge.append(i)

print(*bridge)
