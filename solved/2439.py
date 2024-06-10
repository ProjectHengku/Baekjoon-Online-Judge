t = int(input())
i = 0
a = ""
m = " "
s = "*"
while i < t:
    j = 0
    k = 0
    while j < t - (i + 1):
        a = a + m
        j = j + 1
    while k < i + 1:
        a = a + s
        k = k + 1
    print(a)
    a = ""
    i = i + 1