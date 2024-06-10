import sys

input = sys.stdin.readline


# data input
T = int(input())

# repeat T times

for i in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))

    # simulation
    queue = [i for i in range(N)]
    result = []

    if N == 1:
        print(1)
        continue

    while len(result) < N:
        if priority[0] == max(priority):
            result.append(queue[0])
            queue.pop(0)
            priority.pop(0)
        else:
            queue.append(queue[0])
            priority.append(priority[0])
            queue.pop(0)
            priority.pop(0)

    print(result.index(M) + 1)
