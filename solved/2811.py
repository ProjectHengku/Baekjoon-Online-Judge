N = int(input())
emotions = list(map(int, input().split()))

days = []

continuous = 0
maximum = 0
for idx in range(N - 1, -1, -1):
    if continuous:
        if emotions[idx] < 0:
            continuous += 1
        else:
            maximum = max(maximum, continuous)
            days.append((idx + 1, continuous))
            continuous = 0
    else:
        if emotions[idx] < 0:
            continuous += 1

idx = 0
day = N - 1
lastday = N
flower = [0] * N
maximums = []
for glummy in days:
    day = glummy[0]

    present = 2 * glummy[1]

    for i in range(present):
        flower[day - (1 + i) if day - (1 + i) >= 0 else 0] = 1

    if glummy[1] == maximum:
        maximums.append(
            (
                day - glummy[1] * 3 if day - glummy[1] * 3 >= 0 else 0,
                day - glummy[1] * 2,
            )
        )

minmin = maximum
for start, end in maximums:
    minmin = min(sum(flower[start:end]) + (maximum - (end - start)), minmin)


print(sum(flower) + (maximum - minmin))
