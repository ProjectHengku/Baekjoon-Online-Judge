import sys


def find(x):
    while x != tree[x]:
        x = tree[x]
    return x


def merge(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return -1

    if a < b:
        tree[b] = a
    else:
        tree[a] = b

    return 0


input = sys.stdin.readline


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

tree = [i for i in range(V + 1)]

edges.sort(key=lambda x: x[2], reverse=True)

total_cost = 0
elements = 0
while elements < V - 1:
    start, end, cost = edges.pop()

    if find(start) != find(end):
        total_cost += cost
        elements += 1
        merge(start, end)

print(total_cost)
