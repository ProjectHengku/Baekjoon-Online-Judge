import math

N, M = map(int, input().split())

if N >= M:
    print(0)
else:
    print(math.factorial(N) % M)
