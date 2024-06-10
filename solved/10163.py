field = [[0] * 1001 for _ in range(1001)]
N = int(input())

for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())

    # w x h 만큼 i로 칠하기
    for dy in range(h):
        for dx in range(w):
            field[y + dy][x + dx] = i

    
# 모든 절차 끝나고 i의 영역 넓이 세기
for i in range(1, N + 1):
    count = 0

    for row in field:
        count += row.count(i)

    print(count)