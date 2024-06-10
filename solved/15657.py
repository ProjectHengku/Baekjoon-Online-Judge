def series(depth, left, numbers):
    for i in range(len(numbers)):
        if depth == M:
            print((left + " " + str(numbers[i])).strip())
        else:
            series(depth + 1, left + " " + str(numbers[i]), numbers[i:])


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
# 백트래킹
series(1, "", numbers)
