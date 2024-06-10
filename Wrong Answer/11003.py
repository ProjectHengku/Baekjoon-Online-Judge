N, L = map(int, input().split())
A = list(map(int, input().split()))
D = [A[0]]
I = [0]
# secondary minimum
S = [10**9]
J = [0]
for i in range(1, N):
    if i == 1:
        if D[i - 1] <= A[i]:
            D.append(D[i - 1])
            I.append(i - 1)
            S.append(A[i])
            J.append(i)
        else:
            D.append(A[i])
            I.append(i)
            S.append(D[i - 1])
            J.append(i - 1)
    else:
        if I[i - 1] > i - L:
            if D[i - 1] >= A[i]:
                D.append(A[i])
                I.append(i)
                S.append(D[i - 1])
                J.append(I[i - 1])
            else:
                D.append(D[i - 1])
                I.append(I[i - 1])
                if S[i - 1] >= A[i]:
                    S.append(A[i])
                    J.append(i)
                else:
                    if J[i - 1] > i - L:
                        S.append(S[i - 1])
                        J.append(J[i - 1])
                    else:
                        S.append(A[i])
                        J.append(i)
        else:
            if S[i - 1] < A[i]:
                D.append(S[i - 1])
                I.append(J[i - 1])
                S.append(A[i])
                J.append(i)
            else:
                D.append(A[i])
                I.append(i)
                S.append(S[i - 1])
                J.append(J[i - 1])

print(*D)
