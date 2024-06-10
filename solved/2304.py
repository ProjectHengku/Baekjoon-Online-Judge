N = int(input())

# 초기값 입력 후 세팅
pillar = []
for _ in range(N):
    L, H = map(int, input().split())
    pillar.append((L, H))

# 정렬
pillar.sort(key=lambda x: x[0])

# 시작점 끝점 정함
endL, endR = pillar[0][0], pillar[-1][0]
start = max(pillar, key=lambda x: x[1])[0]
maxH = max(pillar, key=lambda x: x[1])[1]

count = maxH
# 왼쪽으로
startL = start
while startL > endL:
    i = 0
    maxH = 0
    maxL = 0
    while pillar[i][0] < startL:
        if pillar[i][1] > maxH:
            maxH = pillar[i][1]
            maxL = pillar[i][0]
        i += 1
    count += maxH * (startL - maxL)
    startL = maxL

# 오른쪽으로
startR = start
while startR < endR:
    i = -1
    maxH = 0
    maxR = 0
    while pillar[i][0] > startR:
        if pillar[i][1] > maxH:
            maxH = pillar[i][1]
            maxR = pillar[i][0]
        i -= 1
    count += maxH * (maxR - startR)
    startR = maxR

print(count)
