import sys

input = sys.stdin.readline


def newrot(x, y, rot):
    # 방향 전환의 경우의 수는 수평면에서 총 8 가지, 꼭지점에서 4 가지
    if x == 0 and 0 < y < h:
        if rot == 2:
            rot = 0
        elif rot == 3:
            rot = 1
    elif x == w and 0 < y < h:
        if rot == 1:
            rot = 3
        elif rot == 0:
            rot = 2
    elif y == 0 and 0 < x < w:
        if rot == 3:
            rot = 2
        elif rot == 1:
            rot = 0
    elif y == h and 0 < x < w:
        if rot == 0:
            rot = 1
        elif rot == 2:
            rot = 3
    elif x == 0 and y == 0:
        rot = 0
    elif x == 0 and y == h:
        rot = 1
    elif x == w and y == 0:
        rot = 2
    elif x == w and y == h:
        rot = 3

    return rot


w, h = map(int, input().split())
p, q = map(int, input().split())
# 패턴 절삭
t = int(input()) % (w * h * 2)

# 이동 방향
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
rot = 0

# 이동 시킴
x, y = p, q
i = 0
while i < t:
    # 계속 시간 초과 띄우니까 부딪힐 때 까지 한꺼번에 점프한다
    if rot == 0:
        jump = min(w - x, h - y, t - i)
    elif rot == 1:
        jump = min(w - x, y, t - i)
    elif rot == 2:
        jump = min(x, h - y, t - i)
    else:
        jump = min(x, y, t - i)

    i += jump
    x = x + jump * dx[rot]
    y = y + jump * dy[rot]

    # 경계에 부딪히면
    if x == 0 or x == w or y == 0 or y == h:
        # 경로 정반사
        rot = newrot(x, y, rot)


print(x, y)
