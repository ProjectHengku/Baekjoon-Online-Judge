import sys

input = sys.stdin.readline


def find():
    start = 0
    minimum = float("inf")
    for idx in range(1, N):
        if not visited[idx] and dist[idx][0] < minimum:
            start = idx
            minimum = dist[idx][0]

    return start


# number of cities N, number of edges M, number of tex incresements K
N, M, K = map(int, input().split())
S, D = map(int, input().split())

road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    road[a].append((b, w))
    road[b].append((a, w))

# dijkstra
visited = [False] * N

dist = [(float("inf"), float("inf"))] * (N + 1)
dist[S] = (0, 0)

route = {}  # routes S from D

for _ in range(N - 1):
    current = find()

    for next, cost in road[current]:
        exp = dist[current][0] + cost

        if next == D:
            try:
                route[dist[current][1] + 1] = min(route[dist[current][1] + 1], exp)
            except:
                route[dist[current][1] + 1] = exp

        if dist[next][0] > exp:
            dist[next] = (exp, dist[current][1] + 1)
        elif dist[next][0] == exp and dist[next][1] > dist[current][1] + 1:
            dist[next] = (exp, dist[current][1] + 1)

    visited[current] = True

print(dist[D][0])

# calculate for tex increase
for _ in range(K):
    tax = int(input())

    for count in route.keys():
        route[count] += tax * count

    sys.stdout.write(str(min(route.values())) + "\n")
