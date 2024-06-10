C, R = map(int, input().split())
wait = int(input())

# 초기값 설정
start = 1
cycle = 1
end = 2 * (C + R - 4 * (cycle - 1)) - 4

# 좌석 배정 불가능한 경우
if wait > C * R:
    print(0)
    exit()

# 대기열에 해당된 cycle 도출
# 이 아래로는 반드시 좌석 도출되므로
while True:
    if start <= wait <= end:
        break
    else:
        cycle += 1
        start = end + 1
        end = end + 2 * (C + R - 4 * (cycle - 1)) - 4

# 좌표 찾기
Q1 = (start + (R - 2 * (cycle - 1))) - 1
Q2 = (Q1 + (C - 2 * (cycle - 1))) - 1
Q3 = (Q2 + (R - 2 * (cycle - 1))) - 1
end = end + 2 * (C + R - 4 * (cycle - 1)) - 4

# 사각형 각 변별로 찾으면 될듯
if start <= wait <= Q1:
    x = cycle
    y = cycle + (wait - start)
elif Q1 < wait < Q2:
    x = cycle + (wait - Q1)
    y = R - (cycle - 1)
elif Q2 <= wait <= Q3:
    x = C - (cycle - 1)
    y = R - (cycle - 1) - (wait - Q2)
else:  # Q3 < wait <= end:
    x = C - (cycle - 1) - (wait - Q3)
    y = cycle

print(x, y)
