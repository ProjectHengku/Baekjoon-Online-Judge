def boy(x, switches):
    record = []

    # i가 x의 배수이면 스위치 조작
    for i in range(1, switch_count + 1):
        if i % x == 0:
            record.append(i)

    for switch in record:
        switches[switch - 1] = not switches[switch - 1]

    return switches


def girl(x, switches):
    i = 1

    switches[x - 1] = not switches[x - 1]

    # x 중심으로 날개 펼쳤을 때 대칭형이면 스위치 조작
    while 1 <= x + i <= switch_count and 1 <= x - i <= switch_count:
        if switches[(x - 1) + i] == switches[(x - 1) - i]:
            switches[(x - 1) + i] = not switches[(x - 1) + i]
            switches[(x - 1) - i] = not switches[(x - 1) - i]

            i += 1
        else:
            break

    return switches


def binToBool(lst):
    for i in range(switch_count):
        lst[i] = not (not lst[i])

    return lst


def boolToBin(lst):
    for i in range(switch_count):
        if lst[i]:
            lst[i] = 1
        else:
            lst[i] = 0

    return lst


# 초기 정보 받음
switch_count = int(input())
switches = binToBool(list(map(int, input().split())))
student_count = int(input())

for _ in range(student_count):
    command = list(map(int, input().split()))

    # 성별, 숫자 따라서 스위치 조작
    sex, number = command[0], command[1]
    if sex == 1:
        switches = boy(number, switches)
    else:
        switches = girl(number, switches)

switches = boolToBin(switches)
written = 0

while switches:
    switch = switches.pop(0)
    
    print(switch, end=" ")
    written += 1

    if written == 20:
        written = 0
        print()