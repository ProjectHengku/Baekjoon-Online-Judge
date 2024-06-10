import sys

input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    K = int(input())

    if K == 0:
        data.pop(-1)
        continue
    data.append(K)

print(sum(data))
