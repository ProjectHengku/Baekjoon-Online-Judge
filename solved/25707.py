N = int(input())
beads = list(map(int, input().split()))

beads.sort()
print(2 * (beads[-1] - beads[0]))