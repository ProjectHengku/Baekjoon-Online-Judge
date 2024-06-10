# 초기값 받음
W, H = map(int, input().split())
N = int(input())
stores = []
for _ in range(N):
    r, c = map(int, input().split())
    stores.append((r, c))

# 동근 위치
campR, campC = map(int, input().split())

# 동근 위치에서 가장 가까운 상점까지의 거리
# 어짜피 왼쪽 아니면 오른쪽으로 가야하므로
result = []
for store in stores:
    storeR, storeC = store[0], store[1]

    # 왼쪽에 있으면 왼쪽이 더 가깝고, 오른쪽에 있으면 오른쪽이 더 가까움
    # 맞은편에 있으면 그냥 경우의 수 따지면 될듯
    # 같은편에 있으면 바로 최단경로 나옴

    # 동근 위치 기준으로 경우의 수 분기
    if campR == 1:
        left, right, opposite = 4, 3, 2
        if storeR == left:
            result.append((W - campC) + storeC)
        elif storeR == right:
            result.append(campC + storeC)
        elif storeR == opposite:
            turnleft = (W - campC) + H + (W - storeC)
            turnright = campC + H + storeC

            result.append(min(turnleft, turnright))
        else:
            result.append(abs(storeC - campC))
    elif campR == 2:
        left, right, opposite = 3, 4, 1
        if storeR == left:
            result.append(campC + (H - storeC))
        elif storeR == right:
            result.append((W - campC) + (H - storeC))
        elif storeR == opposite:
            turnleft = campC + H + storeC
            turnright = (W - campC) + H + (W - storeC)

            result.append(min(turnleft, turnright))
        else:
            result.append(abs(storeC - campC))
    elif campR == 3:
        left, right, opposite = 1, 2, 4
        if storeR == left:
            result.append(campC + storeC)
        elif storeR == right:
            result.append((H - campC) + storeC)
        elif storeR == opposite:
            turnleft = campC + W + storeC
            turnright = (H - campC) + W + (H - storeC)

            result.append(min(turnleft, turnright))
        else:
            result.append(abs(storeC - campC))
    else:
        left, right, opposite = 2, 1, 3
        if storeR == left:
            result.append((H - campC) + (W - storeC))
        elif storeR == right:
            result.append(campC + (W - storeC))
        elif storeR == opposite:
            turnleft = (H - campC) + W + (H - storeC)
            turnright = campC + W + storeC

            result.append(min(turnleft, turnright))
        else:
            result.append(abs(storeC - campC))

print(sum(result))
