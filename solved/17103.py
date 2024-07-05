def primes(n):
    sieve = [True] * n

    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return {i: i for i in range(2, n) if sieve[i] == True}


T = int(input())
for testcase in range(T):
    n = int(input())

    prime_list = primes(n)
    half_list = [x for x in prime_list.keys() if x <= n / 2]

    count = 0
    for x in half_list:
        try:
            if prime_list[n - x]:
                count += 1
        except:
            pass

    print(count)
