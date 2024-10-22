N, M = map(int, input().split())

nova = list(map(int, input().split()))
origin = list(map(int, input().split()))

nova.sort()
origin.sort()

v, vi = 0, 0

immune = 0
cooldown = 0
for time in nova:
    if immune - time <= 0 and cooldown - time <= 0:
        v += 1
        immune = time + 90
        cooldown = time + 100

immune = 0
cooldown = 0
for time in origin:
    if immune - time <= 0 and cooldown - time <= 0:
        vi += 1
        immune = time + 90
        cooldown = time + 360

print(v, vi)
