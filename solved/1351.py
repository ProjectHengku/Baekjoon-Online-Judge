import sys

sys.setrecursionlimit(10**6)


def find(i):

    while True:
        try:
            if A[i]:
                return A[i]
        except:
            A[i] = find(i // P) + find(i // Q)


N, P, Q = map(int, input().split())

A = {0: 1, 1: 2}

print(find(N))
