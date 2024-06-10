i = 0
m = []
while i < 9:
    s = input()
    m.append(int(s))
    i = i + 1
ans = max(m)
inx = m.index(max(m)) + 1
print(ans)
print(inx)