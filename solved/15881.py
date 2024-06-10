n = int(input())
obj = input()

if n < 4:
    count = 0
else:
    idx = 0
    count = 0
    while idx < n - 3:
        if obj[idx:idx + 4] == 'pPAp':
            count += 1
            idx += 4
        else:
            idx += 1

print(count)