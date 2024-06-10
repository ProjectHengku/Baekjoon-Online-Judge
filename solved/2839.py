sugars = int(input())
i = 0
j = 1

if sugars % 5 == 0:
    print(sugars // 5)
    exit()
else:
    # check if sugar is sum of 5 and 3
    while sugars - 5 * i >= 0:
            i += 1
    while sugars - 3 * j >= 0:
        if 3 * j > sugars - 5 * i:
            i -= 1
        if sugars - 5 * i - 3 * j == 0:
            print(i + j)
            exit()
        j += 1

print(-1)