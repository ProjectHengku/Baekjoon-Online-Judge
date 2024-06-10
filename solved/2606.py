import sys
from collections import deque 

input = sys.stdin.readline

PCnodes = int(input())
PCpairs = int(input())

# 네트워크 그래프
networks = []

for _ in range(PCpairs):
    pair = list(map(int, input().split()))
    networks.append(pair)
    networks.append(pair[::-1])

# 방문 시뮬레이션
queue = deque()

visited = [False] * (PCnodes + 1)

# 1에서 출발함
for item in networks:
    if item[0] == 1:
        queue.append(item)

visited[1] = True

while queue:
    now = queue.popleft()
    next = now[1]
    visited[now[0]] = True

    if visited[next] == False:
        for item in networks:
            if item[0] == next:
                queue.append(item)

# 1번 컴퓨터의 감염은 카운트로 세지 않는다.
count = visited.count(True) - 1
print(count)