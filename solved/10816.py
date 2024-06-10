N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

answer = [0] * M

hash_table = {}
for card in cards:
    if card in hash_table:
        hash_table[card] += 1
    else:
        hash_table[card] = 1

for i, target in enumerate(targets):
    if target in hash_table:
        answer[i] = hash_table[target]

print(*answer)
