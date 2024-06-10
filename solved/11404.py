import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))

answer = []
for i in range(1, n + 1):
    cheapest = [float("inf")] * (n + 1)

    cheapest[i] = 0
    stack = [(i, 0)]

    while stack:
        current, used = stack.pop()

        for node, cost in bus[current]:
            exp = used + cost
            if exp < cheapest[node]:
                cheapest[node] = exp
                stack.append((node, exp))

    for idx, best in enumerate(cheapest):
        if best == float("inf"):
            cheapest[idx] = 0

    answer.append(cheapest[1:])

for village in answer:
    print(*village)
