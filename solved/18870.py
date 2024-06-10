N = int(input())
coordinates = list(map(int, input().split()))

# 인덱스 지정
idxcor = []
for i, v in enumerate(coordinates):
    idxcor.append([i, v])

# 값 기준 정렬
idxcor.sort(key=lambda x: x[1])

# 좌표 압축
count = -1
temp = float("inf")
for i in range(N):
    if temp != idxcor[i][1]:
        count += 1
        temp = idxcor[i][1]

    idxcor[i][1] = count

# 재정렬
idxcor.sort()

for item in idxcor:
    print(item[1], end=" ")
