# graph = {1: [2, 3, 4, 5, 6, 7]}

# for n in range(1, 579):
#     for k in range(1, 6 * n + 1):
#         node = (3 * (n - 1) * n + 1) + k
#         if k in (1 * n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n):
#             a = k // n
#             # 바깥 사이클 부채꼴에서 3개
#             if a != 6:
#                 next1 = (3 * n * (n + 1) + 1) + (n + 1) * a
#                 next2 = next1 + 1
#                 next3 = next1 - 1
#             else:
#                 next1 = (3 * n * (n + 1) + 1) + (n + 1) * a
#                 next2 = (3 * n * (n + 1) + 1) + 1
#                 next3 = next1 - 1
#             # 같은 사이클 인접 양옆 2개
#             next4 = node + 1
#             next5 = node - 1
#             # 안쪽 사이클 쪼여서 1개
#             next6 = (3 * (n - 2) * (n - 1) + 1) + (n - 1) * a
#         else:
#             for a in range(0, 6):
#                 if n * a < k < n * (a + 1):
#                     break
#             # 바깥 사이클에서 2개
#             next1 = (3 * n * (n + 1) + 1) + (k + a)
#             next2 = (3 * n * (n + 1) + 1) + (k + a + 1)
#             # 같은 사이클 인접 양옆 2개
#             next3 = node + 1
#             next4 = node - 1
#             # 안쪽 사이클에서 2개
#             next5 = (3 * (n - 2) * (n - 1) + 1) + (k - a)
#             next6 = (3 * (n - 2) * (n - 1) + 1) + (k - a - 1)

#         graph.update({node: [next1, next2, next3, next4, next5, next6]})

# 씹쓰레기 최적화 문제
start, end = map(int, input().split())

graph = [[0] * 1500 for _ in range(1500)]

N = 1
cycle = 1
graph[750][750] = 1

dx = [-1, 0, 1, 1, 0, -1]
dy = [0, 1, 1, 0, -1, -1]

x, y = 750, 750

while N <= 1000000:
    for d in range(6):
        for k in range(cycle - 1 if d == 1 else cycle):
            X = x + dx[d]
            Y = y + dy[d]
            graph[X][Y] = N

            if N == start:
                sx, sy = X, Y

            N += 1
            x, y = X, Y
    cycle += 1

print(graph)

queue = [[0] * 2 for _ in range(1000001)]
front = rear = -1

rear += 1
queue[rear][0] = (sx, sy)

visited = [False] * 1000001
visited[start] = True

while front < rear:
    front += 1
    current = queue[front][0]
    x, y = current

    # 도착했으면 터뜨림
    if current == end:
        break

    nexts=[]
    for d in range(6):
        nexts.append(graph[])

    for next in graph[current]:
        if next > 1000000:
            continue
        if not visited[next]:
            visited[next] = True
            rear += 1
            queue[rear][0] = next
            queue[rear][1] = front

# 루트 역추적
path = []
while True:
    path.append(queue[front][0])
    if queue[front][0] == start:
        break
    front = queue[front][1]

reversepath = path[::-1]

print(*reversepath)
