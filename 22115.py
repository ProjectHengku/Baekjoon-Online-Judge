N, K = map(int, input().split())
coffee = list(map(int, input().split()))
coffee.sort()

point = -1
count = 0
caffeine = 0
vaild = True

while caffeine < K:
    try:
        if caffeine + coffee[point] <= K:
            caffeine += coffee[point]
            count += 1

    except IndexError:
        vaild = False
        break

    point -= 1

if caffeine != K:
    vaild = False

if vaild:
    print(count)
else:
    print(-1)
