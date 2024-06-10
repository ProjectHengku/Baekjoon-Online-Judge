N, M = map(int, input().split())
T, *know = map(int, input().split())

event = [[] for _ in range(M)]

for party in range(M):
    P, *participants = map(int, input().split())
    event[party] = participants


know = set(know)

for _ in range(len(event)):
    for participants in event:
        if set(participants) & know:
            know = set(participants) | know

count = 0
for participants in event:
    if set(participants) & know:
        continue
    count += 1

print(count)
