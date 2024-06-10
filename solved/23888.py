from math import gcd
import sys


input = sys.stdin.readline


a, d = map(int, input().split())
q = int(input())
for _ in range(q):
    com, l, r = map(int, input().split())
    if com == 1:
        al = a + d * (l - 1)
        result = al * (r - l + 1) + d * ((r - l) * (r - l + 1) // 2)
    else:
        al = a + d * (l - 1)
        if l == r:
            result = al
        else:
            result = gcd(a, d)

    print(result)
