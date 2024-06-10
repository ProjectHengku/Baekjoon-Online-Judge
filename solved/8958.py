t = int(input())

for i in range(0, t):
    q = input()
    score = 0
    getscore = 1
    for i in range(0, len(q)): 
        if q[i] == "O":
            if i > 0 and q[i - 1] == "O":
                getscore = getscore + 1
            score = score + getscore
        if q[i] == "X":
            getscore = 1
    print(score)