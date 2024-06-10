N, r, c = map(int,input().split())

# 몇 번째 사분면에 있는지 찾기
# x1, 2 각각 x축 왼쪽, 오른쪽 y1, 2 각각 y축 아래, 위
def find_q(n, x1, x2, y1, y2, row, col):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    if row >= y:
        if col >= x:
            ans = 3
            x1 = ((x1 + x2) // 2) + 1
            y1 = ((y1 + y2) // 2) + 1
        else:
            ans = 2
            x2 = (x1 + x2) // 2
            y1 = ((y1 + y2) // 2) + 1
    else:
        if col >= x:
            ans = 1
            x1 = ((x1 + x2) // 2) + 1
            y2 = (y1 + y2) // 2
        else:
            ans = 0
            x2 = (x1 + x2) // 2
            y2 = (y1 + y2) // 2

    if n == 0:
        return ans
    
    # 이짓거리를 재귀함수 반복하면 됨
    return (4 ** n) * ans + find_q(n - 1, x1, x2, y1, y2, row, col) 

x1, x2 = 0, (2 ** N) - 1
y1, y2 = 0, (2 ** N) - 1

answer = find_q(N - 1, x1, x2, y1, y2, r, c)
print(answer)