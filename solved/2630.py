from collections import deque

# 2D 배열에서 체크하는거는 in으로 단번에 안되니까
def isIn(ele, arr):
    for row in arr:
        if ele in row:
            return True
        
    return False

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# 대기열에 추가함
queue = deque()
queue.append(field)

white = []
blue = []

# 분할 정복
while queue:
    check = queue.popleft()
    center = len(check) // 2
    
    isblue = isIn(1, check)
    iswhite = isIn(0, check)

    # 0과 1이 둘 다 들어있으면 쪼갠다
    if isblue and iswhite:
        new1 = []
        new2 = []
        new3 = []
        new4 = []
        for i in range(0, center):
            new1.append(check[i][:center])
        for i in range(0, center):
            new2.append(check[i][center:])
        for i in range(center, len(check)):
            new3.append(check[i][:center])
        for i in range(center, len(check)):
            new4.append(check[i][center:])


        queue.extend([new1, new2, new3, new4])
    else:
        # 아니면 색종이 개수에 합산
        if iswhite:
            white.append(check)
        else:
            blue.append(check)

# 결과물 출력
print(len(white))
print(len(blue))