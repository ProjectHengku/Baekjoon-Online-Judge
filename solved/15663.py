import itertools

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

result = list(set(itertools.permutations(numbers, M)))
result.sort(key=lambda x: [x[i] for i in range(M)])

for case in result:
    print(*case)
