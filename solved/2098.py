def dfs(now, visited):
    if visited == (1 << N) - 1:
        if cost[now][0]:
            return cost[now][0]
        else:
            return float("inf")

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = float("inf")
    for next in range(1, N):
        if cost[now][next] == 0 or visited & (1 << next):
            continue
        usage = dfs(next, visited | (1 << next)) + cost[now][next]
        min_cost = min(usage, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = {}

result = dfs(0, 1)
print(result)
