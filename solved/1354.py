import sys

sys.setrecursionlimit(10**6)


def find(i):
    while True:
        try:
            if i <= 0:
                return 1
            else:
                if A[i]:
                    return A[i]
        except:
            A[i] = find((i // P) - X) + find((i // Q) - Y)


N, P, Q, X, Y = map(int, input().split())

A = {}

print(find(N))
