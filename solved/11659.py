import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

subsum = 0
sums = []

for i in range(N):
    subsum += numbers[i]
    sums.append(subsum)

for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(str(sums[end - 1]) + '\n')
    else:
        print(str(sums[end - 1] - sums[start - 2]) + '\n')