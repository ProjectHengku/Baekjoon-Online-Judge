def findopp(dice, index):
    # 주사위의 전개도는 형태가 정해져 있으므로
    if index == 0:
        return dice[5]
    elif index == 1:
        return dice[3]
    elif index == 2:
        return dice[4]
    elif index == 3:
        return dice[1]
    elif index == 4:
        return dice[2]
    else:
        return dice[0]


N = int(input())
# 시작 주사위와 나머지 주사위들
start = list(map(int, input().split()))
dices = [list(map(int, input().split())) for _ in range(N - 1)]

result = []
# 시작 주사위가 위로 올라오는 수의 경우의 수 = 6
for i in range(6):
    top = start[i]
    bot = findopp(start, i)
    side = {1, 2, 3, 4, 5, 6} - {top, bot}

    maxsum = max(side)
    for dice in dices:
        bot = top
        top = findopp(dice, dice.index(bot))
        # 옆면 중에서 가장 큰 경우만 비교대상으로써 유효함
        side = {1, 2, 3, 4, 5, 6} - {top, bot}

        maxsum += max(side)

    result.append(maxsum)

print(max(result))
