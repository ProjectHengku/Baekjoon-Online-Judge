from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001

queue = deque()
queue.append((N, 0))

count = 0
found = False
while queue:
    now, time = queue.popleft()

    visited[now] = True

    if now == K:
        if not found:
            found = True
            record = time
            count += 1
        else:
            if time == record:
                count += 1
            else:
                break

    # 최저 시간 갱신된 시점에서 굳이 더 탐색할 필요 없음
    if not found:
        if now + 1 <= 100000 and not visited[now + 1]:
            queue.append((now + 1, time + 1))

        if 0 <= now - 1 and not visited[now - 1]:
            queue.append((now - 1, time + 1))

        if 0 <= 2 * now <= 100000 and not visited[2 * now]:
            queue.append((2 * now, time + 1))

print(record)
print(count)
