def fmulti(base, exp):
    if exp == 1:
        return base % C

    if exp % 2 == 0:
        return (fmulti(base, exp // 2) ** 2) % C
    else:
        return ((fmulti(base, exp // 2) ** 2) * base) % C


A, B, C = map(int, input().split())

answer = fmulti(A, B)
print(answer)
