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


input = sys.stdin.readline

N = int(input())
M = int(input())
table = [list(map(int, input().split())) for _ in range(M)]

table.sort(key=lambda x: x[2], reverse=True)

tree = [i for i in range(N + 1)]

total_cost = 0
connection = 0

while connection < N - 1:
    start, end, cost = table.pop()

    if find(start) != find(end):
        total_cost += cost
        connection += 1
        merge(start, end)

print(total_cost)
