import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lan = []
for _ in range(K):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lan:
        total += i // mid

    if total >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
