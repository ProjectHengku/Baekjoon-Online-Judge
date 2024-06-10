i = 0
while i < 1:
    go = input().split()
    if go == ["0", "0", "0"]:
        i += 1
    else:
        gn = []
        gn.append(int(go[0]))
        gn.append(int(go[1]))
        gn.append(int(go[2]))

        gn.sort()

        if gn[0] * gn[0] + gn[1] * gn[1] == gn[2] * gn[2]:
            print("right")
        else:
            print("wrong")