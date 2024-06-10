ipv6 = input()

continued = False
two = None
group = 0
for idx, letter in enumerate(ipv6):
    if letter == ":":
        continued = False
        if idx < len(ipv6) - 1:
            if ipv6[idx + 1] == ":":
                two = idx
        elif ipv6[idx - 1] == ":":
            pass
    else:
        if not continued:
            group += 1
        continued = True

if two != None:
    ipv6 = ipv6[:two] + ":0000" * (8 - group) + ipv6[two + 1 :]

if ipv6[0] == ":":
    ipv6 = ipv6[1:]

code = ["" for _ in range(8)]
pos = 0
for letter in ipv6:
    if letter == ":":
        pos += 1
    else:
        code[pos] += letter

for i in range(8):
    n = len(code[i])
    code[i] = "0" * (4 - n) + code[i]

print(":".join(code))
