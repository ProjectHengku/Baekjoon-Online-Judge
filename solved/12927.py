lights = list(input())

switches = [False]

for light in lights:
    if light == "Y":
        switches.append(True)
    else:
        switches.append(False)

count = 0
for i in range(1, len(switches)):
    if switches[i]:
        for j in range(i, len(switches), i):
            switches[j] = not switches[j]
        count += 1

if any(switches):
    print(-1)
else:
    print(count)
