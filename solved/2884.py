t = input().split()
h1 = int(t[0])
m1 = int(t[1])

act = 60 * h1 + m1

if act < 45:
    alm = act - 45 + 1440
else:
    alm = act - 45

# get quotient and remainder via divmod
h2, m2 = divmod(alm, 60)
ans = str(h2) + " " + str(m2)
print(ans)