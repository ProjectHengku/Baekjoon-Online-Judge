from collections import deque


def D(number):
    return (number * 2) % 10000


def S(number):
    if number == 0:
        number = 9999
    else:
        number -= 1

    return number


def L(number):
    if number < 1000:
        number = number * 10
    else:
        number = str(number)
        number = number[1:] + number[0]
        number = int(number)

    return number


def R(number):
    if number < 10:
        number = number * 1000
    elif number < 1000:
        d1 = number % 10
        number = 1000 * d1 + number // 10
    else:
        number = str(number)
        number = number[-1] + number[:-1]
        number = int(number)

    return number


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    # 너비 우선 탐색 사용함
    queue = deque()
    visited = [False] * 10000

    # 출발점 기록함
    queue.append([A, []])
    visited[A] = True

    while queue:
        now = queue.popleft()
        num, route = now[0], now[1]

        # 문제 조건상 A != B 이므로 예외처리 할 필요 없을듯
        # B 되면 탈출
        if num == B:
            break

        # D, L, S, R 4가지 경우의 수 변형이 가해지므로
        numD, numS, numL, numR = D(num), S(num), L(num), R(num)
        if visited[numD] == False:
            visited[numD] = True
            queue.append([numD, route + ["D"]])
        if visited[numS] == False:
            visited[numS] = True
            queue.append([numS, route + ["S"]])
        if visited[numL] == False:
            visited[numL] = True
            queue.append([numL, route + ["L"]])
        if visited[numR] == False:
            visited[numR] = True
            queue.append([numR, route + ["R"]])

    # 붙여써야됨
    answer = ""
    for letter in route:
        answer = answer + letter

    print(answer)
