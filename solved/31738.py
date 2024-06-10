def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i % M
        num %= M
    return num


N, M = map(int, input().split())

if N >= M:
    print(0)
else:
    print(factorial(N))
