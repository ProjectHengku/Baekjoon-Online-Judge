from heapq import heappush, heappop

N, L = map(int, input().split())
A = list(map(int, input().split()))

heap = []
heappush(heap, (A[0], 0))

D = [A[0]]
I = [0]

for i in range(1, N):
    if I[i - 1] > i - L:
        if D[i - 1] >= A[i]:
            D.append(A[i])
            I.append(i)
        else:
            D.append(D[i - 1])
            I.append(I[i - 1])
    else:
        flag = False
        while not flag and heap:
            value, v_index = heappop(heap)

            if v_index > i - L:
                if value < A[i]:
                    D.append(value)
                    I.append(v_index)

                    flag = True

        if not heap:
            D.append(A[i])
            I.append(i)

    heappush(heap, (A[i], i))

print(*D)
