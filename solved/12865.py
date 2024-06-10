from copy import deepcopy


N, K = map(int, input().split())
products = [list(map(int, input().split())) for _ in range(N)]

worthy = [0] * (K + 1)
for weight, worth in products:
    previous = deepcopy(worthy)
    for current in range(K + 1):
        if current + weight <= K:
            worthy[current + weight] = max(
                worthy[current + weight], previous[current] + worth
            )

print(max(worthy))
