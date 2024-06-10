num = int(input())
maxlen = 0
maxseries = []

for number in range(1, num + 1):
    series = [num, number]

    new = 0
    while new >= 0:
        new = series[-2] - series[-1]
        series.append(new)

    if series[-1] < 0:
        series.pop()

    if len(series) > maxlen:
        maxlen = len(series)
        maxseries = series

print(maxlen)
print(*maxseries)
