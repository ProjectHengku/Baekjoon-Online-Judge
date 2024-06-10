import math

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    available = False
    k = x
    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            available = True
            break

        k += M

    if available:
        print(k)
    else:
        print(-1)
