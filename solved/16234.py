def DFS():
    change = []
    while stack:
        y, x = stack.pop()
        change.append((y, x))
        for dy, dx in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            ny, nx = y + dy, x + dx
            # 좌표가 유효하고 인구 조건도 맞고 방문한 적도 없다면
            if (
                (0 <= ny < N and 0 <= nx < N)
                and L <= abs(population[y][x] - population[ny][nx]) <= R
                and not visited[ny][nx]
            ):
                stack.append((ny, nx))
                visited[ny][nx] = True
    return change


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

# 초기 환경 설정
time = 0

# 더 이상 인구 이동이 안 일어날 때 까지
isChanged = True
while isChanged:

    # 초기 환경 설정
    stack = []
    visited = [[False] * N for _ in range(N)]
    isChanged = False

    # 모든 나라의 하루치 인구이동을 마칠 때 까지
    while not all(map(all, visited)):
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    stack.append((y, x))
                    visited[y][x] = True
                    change = DFS()
                    # 만약 연합이 성립했을 때
                    if len(change) > 1:
                        # 인구 이동 개시
                        changed = sum([population[y][x] for y, x in change]) // len(
                            change
                        )
                        for y, x in change:
                            population[y][x] = changed
                        isChanged = True

    if isChanged:
        time += 1

print(time)
