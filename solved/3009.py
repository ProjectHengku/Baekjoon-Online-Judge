# 세 점을 입력 받는다.

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

# 제 4의 점 찾기
# 축 하나를 잡고 기록하면 2점이 채워져있는 선과 1점만 있는 선이 나옴
# 1점만 있는 선의 유일한 점에서 좌표 하나를 확정하고 나머지 좌표를 다른 선의 교차하지 않는 점에서 확정함

X1 = [p1]
X2 = []

# 이분법적으로 구현 가능할듯
if p2[0] == p1[0]:
    X1.append(p2)
else:
    X2.append(p2)

if p3[0] == p1[0]:
    X1.append(p3)
else:
    X2.append(p3)

if len(X1) == 1:
    x = X1[0][0]
    if X1[0][1] == X2[0][1]:
        y = X2[1][1]
    else:
        y = X2[0][1]
else:
    x = X2[0][0]
    if X2[0][1] == X1[0][1]:
        y = X1[1][1]
    else:
        y = X1[0][1]

result = [x, y]
print(*result)
