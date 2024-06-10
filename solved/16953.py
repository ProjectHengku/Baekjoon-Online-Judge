from collections import deque

A, B = map(int, input().split())

# 해시테이블에 생길 때마다 넣어버리는게 제일 메모리랑 시간 덜 먹을 것 같다
queue = deque()
queue.append((A, 0))
visited = {A: True}

# 너비 우선 탐색
available = False
while queue:
    now, count = queue.popleft()
    # 목표 수 초과한 경우 아무것도 안함
    if now > B:
        pass
    elif now == B:
        available = True
        answer = count + 1
        break
    else:
        # 2를 곱하거나
        op1 = now * 2
        # 1을 오른쪽에 추가함
        op2 = int(str(now) + "1")

        try:
            if visited[op1]:
                pass
        except KeyError:
            queue.append((op1, count + 1))
            visited.update({op1: True})

        try:
            if visited[op2]:
                pass
        except KeyError:
            queue.append((op2, count + 1))
            visited.update({op2: True})

if available:
    print(answer)
else:
    print(-1)
