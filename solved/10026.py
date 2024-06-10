N = int(input())

# 전체 구역 받음
grids = [input() for _ in range(N)]

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수
visited = [[False] * N for _ in range(N)]
area_not_rg = 0
while not all(map(all, visited)):
    area_not_rg += 1

    # 초기 위치 선정
    stack = []
    is_found = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                is_found = True
                stack.append((i, j))
                visited[i][j] = True

                color = grids[i][j]
                break

        if is_found:
            break

    # 깊이 우선 탐색
    while stack:
        y, x = stack.pop()

        # 상하좌우
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            # 좌표 유효성 && 같은 구역 조건 && 방문하지 않음
            if (
                (0 <= ny < N and 0 <= nx < N)
                and grids[ny][nx] == color
                and not visited[ny][nx]
            ):
                stack.append((ny, nx))
                visited[ny][nx] = True

# 적록색약인 사람이 봤을 때 영역의 개수
visited = [[False] * N for _ in range(N)]
area_rg = 0
while not all(map(all, visited)):
    area_rg += 1
    redgreen = ("R", "G")

    # 초기 위치 선정
    stack = []
    is_found = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                is_found = True
                stack.append((i, j))
                visited[i][j] = True

                color = grids[i][j]
                break

        if is_found:
            break

    # 깊이 우선 탐색
    while stack:
        y, x = stack.pop()

        # 상하좌우
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            # 좌표 유효성 && 같은 구역 조건 && 방문하지 않음
            # 빨강-초록
            if color in redgreen:
                if (
                    (0 <= ny < N and 0 <= nx < N)
                    and grids[ny][nx] in redgreen
                    and not visited[ny][nx]
                ):
                    stack.append((ny, nx))
                    visited[ny][nx] = True
            # 파랑
            else:
                if (
                    (0 <= ny < N and 0 <= nx < N)
                    and grids[ny][nx] == color
                    and not visited[ny][nx]
                ):
                    stack.append((ny, nx))
                    visited[ny][nx] = True

print(area_not_rg, area_rg)
