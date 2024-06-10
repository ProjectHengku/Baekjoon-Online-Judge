N = int(input())
series = list(map(int, input().split()))

# DP
DP = [1] * N

for i in range(1, N):
    more = []
    for j in range(i):
        if series[i] > series[j]:
            more.append(j)
    maxlen = 0
    for j in more:
        if DP[j] > maxlen:
            maxlen = DP[j]

    DP[i] = maxlen + 1

print(max(DP))
