a = input()
b = input()
c = input()
i = 0
ans = [0] * 10

d = int(a) * int(b) * int(c)

while i < 10:
    ans[i] = str(d).count(chr(48 + i))
    print(str(ans[i]))
    i = i + 1