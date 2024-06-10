ina = input()
ans = []
alp = [0] * 26
chk = 0

for i in range(0, len(ina)):
    #convert character to ASCII
    conv = ord(ina[i])
    if conv > 96:
        conv = conv - 32
    alp[conv - 65] = alp[conv - 65] + 1

for j in range(0, 26):
    if alp[j] == max(alp):
        chk = chk + 1

if chk < 2:
    print(chr(alp.index(max(alp)) + 65))
else:
    print("?")