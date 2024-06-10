import heapq, sys

input = sys.stdin.readline

N = int(input())
tc = 0
while N:
    tc += 1
    rupee = [list(map(int, input().split())) for _ in range(N)]

    heap = []
    heapq.heappush(heap, (rupee[0][0], 0, 0))

    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    while heap:
        cost, y, x = heapq.heappop(heap)

        if (y, x) == (N - 1, N - 1):
            break

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                heapq.heappush(heap, (cost + rupee[ny][nx], ny, nx))
                visited[ny][nx] = True

    print(f"Problem {tc}: {cost}")

    N = int(input())
