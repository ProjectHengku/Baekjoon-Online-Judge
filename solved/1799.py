import sys

sys.setrecursionlimit(10**7)


def find(y, x, bishops):
    global maximum
    if y >= n:
        if len(bishops) > maximum:
            maximum = len(bishops)
            # print(*bishops)
        return 0

    if chess[y][x] == 1:
        for by, bx in bishops:
            if abs(y - by) == abs(x - bx):
                break
        else:
            find(
                y + 1 if x + 2 >= n else y,
                initx[(y + 1) % 2] if x + 2 >= n else x + 2,
                bishops + [(y, x)],
            )

    find(
        y + 1 if x + 2 >= n else y, initx[(y + 1) % 2] if x + 2 >= n else x + 2, bishops
    )


n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]

# black
maximum = 0
initx = [0, 1]
find(0, 0, [])

answer = [maximum]

# white
maximum = 0
initx = [1, 0]
find(0, 1, [])

answer.append(maximum)

print(sum(answer))
