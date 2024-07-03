n = int(input())
planet_travel = list(map(int, input().split()))

start = planet_travel[-1]

for i in range(-2, -(n + 1), -1):
    if planet_travel[i] > start:
        start = planet_travel[i]
    else:
        if start % planet_travel[i]:
            start = planet_travel[i] * (start // planet_travel[i] + 1)

print(start)
