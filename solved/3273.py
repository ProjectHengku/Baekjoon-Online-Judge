n = int(input())

numbers = list(map(int, input().split()))
x = int(input())

# 일단 정렬함
numbers.sort()

# 투 포인터 알고리즘
start, end = 0, n - 1
count = 0

while start < end:
    sum_temp = numbers[start] + numbers[end]
    if sum_temp < x:
        start += 1
    elif sum_temp > x:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)
