import sys

input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    data[i][0], data[i][1] = data[i][1], data[i][0]

data.sort()

for i in range(N):
    data[i][0], data[i][1] = data[i][1], data[i][0]

for i in range(N):
    print(*data[i])
