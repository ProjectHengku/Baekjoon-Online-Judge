from collections import deque


def is_in(y, x):
    return 0 <= y < H and 0 <= x < W


K = int(input())
W, H = map(int, input().split())
travel = [list(map(int, input().split())) for _ in range(H)]

# horse-like move and normal move
horse_like = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
move = ((1, 0), (0, 1), (-1, 0), (0, -1))

visited = [[[False] * W for _ in range(H)] for _ in range(K + 1)]
visited[0][0][0] = True

queue = deque()
queue.append((0, 0, 0, 0))

while queue:
    y, x, jump, time = queue.popleft()

    if (y, x) == (H - 1, W - 1):
        print(time)
        exit()

    if jump < K:
        for dy, dx in horse_like:
            ny, nx = y + dy, x + dx
            if is_in(ny, nx) and travel[ny][nx] != 1:
                if not visited[jump + 1][ny][nx]:
                    visited[jump + 1][ny][nx] = True
                    queue.append((ny, nx, jump + 1, time + 1))

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if is_in(ny, nx) and travel[ny][nx] != 1:
            if not visited[jump][ny][nx]:
                visited[jump][ny][nx] = True
                queue.append((ny, nx, jump, time + 1))
else:
    print(-1)
