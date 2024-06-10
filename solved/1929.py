M, N = map(int, input().split())

# 에라토스테네스의 체
prime = [True] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, N + 1, i):
            prime[j] = False

# 소수 출력
for i in range(M, N + 1):
    if i > 1 and prime[i]:
        print(i)
        