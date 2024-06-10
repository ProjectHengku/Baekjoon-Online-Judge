import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# search B in A
A.sort()
for b in B:
    # binary search
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == b:
            print(1)
            break
        elif A[mid] < b:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(0)