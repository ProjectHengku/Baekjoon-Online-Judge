nn = int(input())
score = list(map(int, input().split()))
i = 0
mscore = []


i = 0
m = max(score)

while i < nn:
    mscore.append(score[i]/m*100)
    i += 1

n = sum(mscore)/nn
print(n)