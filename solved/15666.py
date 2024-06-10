def series(depth, pool, result):
    n = len(pool)
    if depth == M:
        results.add(tuple(result))
        return 0
    else:
        for i in range(n):
            series(depth + 1, pool[i:], result + [pool[i]])


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
results = set()
series(0, numbers, [])

results = list(results)
results.sort(key=lambda x: [x[i] for i in range(M)])

for case in results:
    print(*case)
