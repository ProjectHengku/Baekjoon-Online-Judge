import sys


def find(x):
    if x != rel[x]:
        x = find(rel[x])
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        rel[b] = a
    else:
        rel[a] = b


def is_friend(u, v):
    if find(u) == find(v):
        return 1
    else:
        return 0


sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    # number of users
    n = int(input())

    # relationship set table
    rel = [i for i in range(n)]

    if i > 1:
        print()

    # number of relationships
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    # number of searches
    m = int(input())
    print(f"Scenario {i}:")
    for _ in range(m):
        u, v = map(int, input().split())
        print(is_friend(u, v))
