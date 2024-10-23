N, K = map(int, input().split())
S = input()

if N == K:
    print(S[::-1])
    exit()

head = S[: K - 1]
tail = S[K - 1 :]

print(tail + (head if (N - K) % 2 == 1 else head[::-1]))
