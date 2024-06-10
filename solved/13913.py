from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
visited[N] = True

queue = deque([(N, f"{N}", 0)])

while deque:
    now, route, time = queue.popleft()

    if now == K:
        print(time)
        print(route)
        exit()

    if now + 1 <= 100000 and not visited[now + 1]:
        visited[now + 1] = True
        queue.append((now + 1, route + f" {now+1}", time + 1))

    if now - 1 >= 0 and not visited[now - 1]:
        visited[now - 1] = True
        queue.append((now - 1, route + f" {now-1}", time + 1))

    if now * 2 <= 100000 and not visited[now * 2]:
        visited[now * 2] = True
        queue.append((now * 2, route + f" {now*2}", time + 1))
