N = int(input())
plant = [list(map(int, input().split())) for _ in range(N)]

# initial eggplant position
start = (N // 2 - 1, N // 2 - 1)
end = (N // 2, N // 2)

# answer string
ans = ""

sy, sx = start
ey, ex = end

stop = False
while not stop:
    exp = [0, 0, 0, 0]

    # up down left right
    for _ in range(4):
        # up
        if 0 <= sy - 1 < N:
            U = sum(plant[sy - 1][i] for i in range(sx, ex + 1))
            if U > 0:
                exp[0] += U
        # down
        if 0 <= ey + 1 < N:
            D = sum(plant[ey + 1][i] for i in range(sx, ex + 1))
            if D > 0:
                exp[1] += D
        # left
        if 0 <= sx - 1 < N:
            L = sum(plant[i][sx - 1] for i in range(sy, ey + 1))
            if L > 0:
                exp[2] += L
        # right
        if 0 <= ex + 1 < N:
            R = sum(plant[i][ex + 1] for i in range(sy, ey + 1))
            if R > 0:
                exp[3] += R

    if any(exp):
        rot, value = max(enumerate(exp), key=lambda x: x[1])
        if rot == 0:
            ans += "U"
            sy -= 1

        elif rot == 1:
            ans += "D"
            ey += 1

        elif rot == 2:
            ans += "L"
            sx -= 1

        elif rot == 3:
            ans += "R"
            ex += 1

    else:
        stop = True

print(sum([sum(row[sx : ex + 1]) for row in plant[sy : ey + 1]]))
print(ans)
