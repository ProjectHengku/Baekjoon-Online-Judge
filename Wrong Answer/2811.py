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
count = 0
while day >= 0 and idx < len(days):
    # 너무 앞서가면 차이 보정해줌 -> gap
    gap = (days[idx][0]) - lastday if lastday < days[idx][0] else 0
    day = days[idx][0]

    flower = 3 * days[idx][1] if days[idx][1] == maximum else 2 * days[idx][1]

    day -= flower
    # 다음 출발점마저 지나가버리면 그냥 건너뜀
    if lastday <= day:
        idx += 1
        continue

    count += flower - gap if day >= 0 else days[idx][0]
    lastday = day

    idx += 1


print(count)
