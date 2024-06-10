import sys

input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

work.sort(key=lambda x: (-x[1], -x[0]))

play = float("inf")
for do, dead in work:
    play = min(play, dead)

    play -= do

print(play)
