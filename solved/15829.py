N = int(input())
S = input()
r = 31
M = 1234567891

def hash(S):
    h = 0
    for i in range(len(S)):
        h += (ord((S[i])) - 96) * (r ** i)
    return h % M

print(hash(S))