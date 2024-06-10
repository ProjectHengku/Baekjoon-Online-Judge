def check(number):
    number = list(map(int, list(str(number))))
    # 금지 숫자에 하나라도 있으면
    if any([digit in fucked for digit in number]):
        return False

    return True


N = int(input())
# 리모컨좀 새로 사라;
M = int(input())
fucked = []
if M:
    fucked.extend(list(map(int, input().split())))


available = False
gap = 0
able1, able2 = False, False
while not available and M < 10:
    case1, case2 = N + gap, N - gap

    able1 = check(case1) if case1 >= 0 else False
    able2 = check(case2) if case2 >= 0 else False
    if any((able1, able2)):
        available = True

    else:
        gap += 1

# 그리고 나서 +- 버튼 눌러야 되는 횟수 더함
times1 = float("inf")
times2 = float("inf")
if able1:
    times1 = len(str(case1)) + abs(N - case1)
if able2:
    times2 = len(str(case2)) + abs(N - case2)

# 그냥 기본값 100에서 움직이는게 더 빠른가?
default = 100

print(min(times1, times2, abs(default - N)))
