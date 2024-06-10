import heapq
import sys

input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if numbers:
            abs_minimum = heapq.heappop(numbers)
            print(abs_minimum[1])
        else:
            print(0)
    else:
        heapq.heappush(numbers, (abs(x), x))