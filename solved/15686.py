import itertools


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken_0 = []
house = []
# 민가와 치킨집 찾음
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken_0.append((i, j))

chicken = list(itertools.combinations(chicken_0, M))

min_dist = float("inf")
for chicken_case in chicken:
    dist = 0
    for r, c in house:
        shortest = float("inf")
        for y, x in chicken_case:
            dist_chicken = abs(y - r) + abs(x - c)
            if dist_chicken < shortest:
                shortest = dist_chicken
        dist += shortest
        if dist > min_dist:
            break
    if dist < min_dist:
        min_dist = dist


print(min_dist)
