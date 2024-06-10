def isPrime(n, m):
    is_prime = [True] * (m + 1)
    is_prime[0] = is_prime[1] = False
  
    for i in range(2, int(m**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, m + 1, i):
                is_prime[j] = False

    primes = [i for i in range(n, m + 1) if is_prime[i]]
    return primes


M = int(input())
N = int(input())

primes = isPrime(M, N)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
