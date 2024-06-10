import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
answers = [0] * M

cards.sort()

# binary search and take index of target
def binary_search (target, cards):
    left, right = 0, len(cards) - 1

    while left <= right:
        mid = (left + right) // 2

        if cards[mid] == target:
            return mid
        elif cards[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# judge both side of mid has same target
for i in range(M):
    index = binary_search(targets[i], cards)
    if index != -1:
        answers[i] += 1
        indexl, indexr = index - 1, index + 1
        while indexl >= 0 and cards[indexl] == targets[i]:
            answers[i] += 1
            indexl -= 1
        while indexr < N and cards[indexr] == targets[i]:
            answers[i] += 1
            indexr += 1

print(*answers)
