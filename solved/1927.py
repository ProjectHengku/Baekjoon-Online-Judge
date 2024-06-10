import sys
import heapq

input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if numbers:
            minimum = heapq.heappop(numbers)
            print(minimum)
        else:
            print(0)
    else:
        heapq.heappush(numbers, x)
