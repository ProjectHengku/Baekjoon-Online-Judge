N = int(input())
numbers = list(map(int, input().split()))

# 초기 값 세팅
status = "None"
count = 1
temp = False
result = []

# 경우의 수 좀 갈릴듯
for i in range(1, N):
    if numbers[i] > numbers[i - 1]:
        if status == "Increase":
            count += 1
            if temp:
                temp = False
        elif status == "Decrease":
            result.append(count)
            count = 2
            status = "Increase"
            if temp:
                count += temp - 1
                temp = False
        else:
            count += 1
            status = "Increase"
            if temp:
                temp = False
    elif numbers[i] < numbers[i - 1]:
        if status == "Increase":
            result.append(count)
            count = 2
            status = "Decrease"
            if temp:
                count += temp - 1
                temp = False
        elif status == "Decrease":
            count += 1
            if temp:
                temp = False
        else:
            count += 1
            status = "Decrease"
            if temp:
                temp = False
    else:
        count += 1
        if temp:
            temp += 1
        else:
            temp = 2

# 마지막 끝났을 때도 결과 기록함
result.append(count)

print(max(result))
