from collections import deque

N, K = map(int, input().split())

# precalculation of sister's position
sister = [K]
K2 = K

i = 0
while K2 + (i + 1) <= 500000:
    i += 1
    K2 += i
    sister.append(K2)

visited = [[False] * 500001 for _ in range(2)]
visited[0][N] = True

queue = deque([(N, 0)])

while queue:
    now, time = queue.popleft()

    if time >= len(sister):
        break

    if visited[time % 2][sister[time]]:
        print(time)
        exit()

    for next in (now - 1, now + 1, now * 2):
        if 0 <= next <= 500000 and not visited[(time + 1) % 2][next]:
            visited[(time + 1) % 2][next] = True
            queue.append((next, time + 1))

print(-1)
