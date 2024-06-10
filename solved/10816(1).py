import sys
import bisect

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ans = []

for num in nums:
    right = bisect.bisect_right(cards, num)
    left = bisect.bisect_left(cards, num)
    ans.append(right - left)

sys.stdout.write(" ".join(map(str, ans)))
