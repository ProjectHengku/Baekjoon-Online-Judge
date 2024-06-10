As = []
Bs = []

for i in range(0, 10):
    As.append(int(input()))
    Bs.append(As[i] % 42)

# delete duplicate degits via convert into set
Bs = set(Bs)
Bs = list(Bs)

print(len(Bs))