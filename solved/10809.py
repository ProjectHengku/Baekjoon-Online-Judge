t = input()
i = 0
j = 0
out = ""
ans = [-1] * 26

while i < 26:
    try:
        a = t.index(chr(97 + i))
        ans[i] = a
        i = i + 1
    except:
        i = i + 1
while j < 25:
    out = out + str(ans[j]) + " "
    j = j + 1
out = out + str(ans[25])
print(out)