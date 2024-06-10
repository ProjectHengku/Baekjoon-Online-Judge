H, V = map(int, input().split())
N = int(input())

# 초기값 설정
cutH = [0]
cutV = [0]

result = []

for _ in range(N):
    direction, line = map(int, input().split())
    if direction == 0:
        cutV.append(line)
    else:
        cutH.append(line)

cutH.sort()
cutV.sort()
cutH.append(H)
cutV.append(V)

# 종이 자르기
for i in range(len(cutV) - 1):
    for j in range(len(cutH) - 1):
        temp = [[1] * (cutH[j + 1] - cutH[j]) for _ in range(cutV[i + 1] - cutV[i])]
        result.append(sum(map(sum, temp)))

# 제일 넓은거
print(max(result))