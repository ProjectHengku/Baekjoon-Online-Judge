while True:

    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    islands = 0

    while any(map(any, maps)):
        islands += 1
        found = False

        stack = []

        # 첫 발을 내딛을 육지
        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1:
                    found = True
                    stack.append((i, j))
                    maps[i][j] = 0
                    break
            if found:
                break

        while stack:
            y, x = stack.pop()

            # 대각선 포함
            for dy, dx in (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ):
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and maps[ny][nx]:
                    stack.append((ny, nx))
                    maps[ny][nx] = 0

    print(islands)
