times = [0, 1, 2, 4, 7]

for i in range(6):
    times.append(sum(times[-3:]))

T = int(input())
for _ in range(T):
    N = int(input())
    print(times[N])
