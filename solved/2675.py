t = int(input())
i = 0
m = ""
while i < t:
    s = input().split()
    r = int(s[0])
    j = 0
    word = s[1]
    while j < len(word):
        k = 0
        while k < r:
            m = m + word[ j]
            k = k +1
        j = j + 1
    print(m)
    m = ""
    i = i + 1