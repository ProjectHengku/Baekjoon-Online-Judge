N, M = map(int, input().split())

cards = [int(input()) for _ in range(N)]

for i in range(1, M + 1):
    position = 0
    while position < N - 1:
        if cards[position] % i > cards[position + 1] % i:
            cards[position], cards[position + 1] = cards[position + 1], cards[position]
        position += 1

for card in cards:
    print(card)
