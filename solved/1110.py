in1 = int(input())
inp = in1
cyc = 0

while True:
    if inp < 10:
        inptem = inp * 10

        intemp = inptem % 10 + inptem // 10
        inp = (inp % 10) * 10 + intemp % 10

    else:
        intemp = inp % 10 + inp // 10
        inp = (inp % 10) * 10 + intemp % 10
    
    cyc += 1

    if inp == in1:
        break

print(cyc)