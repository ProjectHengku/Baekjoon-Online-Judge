import sys
import itertools

input = sys.stdin.readline

N = int(input())

# input numbers until N
numbers = [0] * 10001
for i in range(N):
    numbers[int(input())] += 1

# print numbers
for i in range(10001):
    for j in range(numbers[i]):
        print(i)