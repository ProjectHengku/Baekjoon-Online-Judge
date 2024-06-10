import sys
n = int(input())
a = []
input = sys.stdin.readline

# append int data into a n times

for i in range(n):
    a.append(int(input()))

a.sort()

if n == 0:
    print(0)
    exit()

b = float(len(a))

# function that make round calculation

def round2(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    
c = int(round2(b * 0.15))

d = sum(a[c:len(a) - c])/(len(a) - 2 * c)

print(int(round2(d)))
