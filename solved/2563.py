paper = [[0] * 101 for _ in range(101)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[y + i][x + j] = 1

print(sum(map(sum, paper)))
