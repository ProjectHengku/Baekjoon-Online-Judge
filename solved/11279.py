import sys
import heapq

input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if numbers:
            maximum = -heapq.heappop(numbers)
            print(maximum)
        else:
            print(0)
    else:
        heapq.heappush(numbers, -x)