import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

field = [list(map(int, input().split())) for i in range(N)]
times = []
results = []

min_height = min(map(min, field))
max_height = max(map(max, field))
heights = max_height - min_height

for h in range(heights + 1):
    time = 0
    tempB = B
    adjusted_height = min_height + h
    for row in field:
        for cell in row:
            if cell > adjusted_height:
                time += (cell - adjusted_height) * 2
                tempB += (cell - adjusted_height)
            elif cell < adjusted_height:
                time += adjusted_height - cell
                tempB -= (adjusted_height - cell)

    if tempB < 0:
        continue

    times.append(time)
    results.append(adjusted_height)

bestTime = min(times)
howManyTimes = []

for t in times:
    if t == bestTime:
        howManyTimes.append(t)

if len(howManyTimes) == 1:
    print(bestTime, results[times.index(bestTime)])
else:
    max_height = max(results[times.index(bestTime):])
    print(bestTime, max_height)
