import sys

input = sys.stdin.readline

N = int(input())
data = []
rank = [1] * N
# input sequence
for i in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1

print(*rank)
