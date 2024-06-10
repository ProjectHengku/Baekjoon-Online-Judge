N = int(input())
A = list(map(int, input().split()))

asc = [1] * N
dec = [1] * N

ascending = 0
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            asc[i] = max(asc[i], asc[j] + 1)

maximum = 1
descending = 0
for i in range(N):
    for j in range(i):
        if A[-1 - i] > A[-1 - j]:
            dec[-1 - i] = max(dec[-1 - i], dec[-1 - j] + 1)


answer = max([asc[i] + dec[i] for i in range(N)]) - 1

print(answer)
