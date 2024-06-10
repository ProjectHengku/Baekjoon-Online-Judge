from collections import deque


def findCycle(k):
    solution = range(1, 579)
    for n in solution:
        if 3 * (n - 1) * n < k - 1 <= 3 * n * (n + 1):
            return n


def findPosition(k, n):
    for idx, value in enumerate(range(3 * (n - 1) * n + 2, 3 * n * (n + 1) + 2)):
        if k == value:
            return idx + 1


def isVertex(pos, n):
    for i in range(1, 7):
        if pos == n * i:
            return True

    return False


def nxnodeVertex(pos, n):
    for a in range(1, 7):
        if pos == n * a:
            break
    # 바깥 사이클 부채꼴에서 3개
    if a != 6:
        next1 = (3 * n * (n + 1) + 1) + (n + 1) * a
        next2 = next1 + 1
        next3 = next1 - 1
    else:
        next1 = (3 * n * (n + 1) + 1) + (n + 1) * a
        next2 = (3 * n * (n + 1) + 1) + 1
        next3 = next1 - 1
    # 같은 사이클 인접 양옆 2개
    next4 = node + 1
    next5 = node - 1
    # 안쪽 사이클 쪼여서 1개
    next6 = (3 * (n - 2) * (n - 1) + 1) + (n - 1) * a

    return [next1, next2, next3, next4, next5, next6]


def nxnodeSide(pos, n):
    for a in range(0, 6):
        if n * a < pos < n * (a + 1):
            break
    # 바깥 사이클에서 2개
    next1 = (3 * n * (n + 1) + 1) + (pos + a)
    next2 = (3 * n * (n + 1) + 1) + (pos + a + 1)
    # 같은 사이클 인접 양옆 2개
    next3 = node + 1
    next4 = node - 1
    # 안쪽 사이클에서 2개
    next5 = (3 * (n - 2) * (n - 1) + 1) + (pos - a)
    next6 = (3 * (n - 2) * (n - 1) + 1) + (pos - a - 1)

    return [next1, next2, next3, next4, next5, next6]


start, end = map(int, input().split())

# 초기 환경 세팅
visited = [False] * 1000001

# 너비 우선 탐색
queue = deque()
queue.append((start, [start]))
visited[start] = True
flag = False
while queue:
    node, route = queue.popleft()

    # 도착했으면 중단
    if node == end:
        break

    if node > 1:
        # node가 몇 번째 cycle에 있는지 확인
        n = findCycle(node)

        # node가 cycle의 몇 번째 위치에 있는지 확인
        pos = findPosition(node, n)

        # 모서리일 때와 아닐 때 맞춰서 인접 노드 결정
        if isVertex(pos, n):
            nextnodes = nxnodeVertex(pos, n)
        else:
            nextnodes = nxnodeSide(pos, n)
    else:
        # 1은 한가운데라서 모양이 달라 예외처리
        nextnodes = [2, 3, 4, 5, 6, 7]

    # 인접 노드 방문했는가

    for nextnode in nextnodes:
        if nextnode > 1000000:
            continue
        elif nextnode == end:
            flag = True
            break
        if not visited[nextnode]:
            nextroute = route[:]
            nextroute.append(nextnode)
            queue.append((nextnode, nextroute))
            visited[nextnode] = True
    if flag:
        break

print(*route, end=" ")
if flag:
    print(end)
