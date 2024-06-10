N = int(input())

tri = []
for _ in range(N):
    tri.append(list(map(int, input().split())))

# 밑에서 위로 DP
for n in range(N - 2, -1, -1):
    for i in range(n + 1):
        tri[n][i] = max(tri[n + 1][i] + tri[n][i], tri[n + 1][i + 1] + tri[n][i])

print(tri[0][0])
