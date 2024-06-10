N, M = map(int, input().split())

everListened = set()
everSeen = set()

for n in range(N):
    everListened.add(input())

for m in range(M):
    everSeen.add(input())

neither = everListened.intersection(everSeen)
neither = sorted(list(neither))

print(len(neither))
for person in neither:
    print(person)
