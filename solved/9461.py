T = int(input())

P = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    P.append(P[i - 1] + P[i - 5])

for _ in range(T):
    N = int(input())
    print(P[N])
