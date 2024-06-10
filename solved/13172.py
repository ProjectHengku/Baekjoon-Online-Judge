import sys
from math import gcd

input = sys.stdin.readline


def exp(n, s):
    return (s * square(n, X - 2)) % X


def square(n, p):
    if p == 1:
        return n

    if p % 2 == 0:
        half = square(n, p // 2)
        return (half * half) % X
    else:
        return (n * square(n, p - 1)) % X


M = int(input())

X = 1000000007
ans = 0
for _ in range(M):
    n, s = map(int, input().split())

    a = gcd(n, s)
    n //= a
    s //= a

    ans = (ans + exp(n, s)) % X

print(ans)
