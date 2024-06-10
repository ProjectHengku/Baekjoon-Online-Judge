import sys


def find(x):
    if sets[x] != x:
        sets[x] = find(sets[x])
    return sets[x]


def merge(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        sets[b] = a
    else:
        sets[a] = b


def is_same_in(a, b):
    if find(a) == find(b):
        return "YES"
    else:
        return "NO"


sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

# make sets
sets = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        merge(a, b)

    else:
        print(is_same_in(a, b))
