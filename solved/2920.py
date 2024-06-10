a = input().split()
i = 0
b = 0
for i in range(0, 6):
    if int(a[i]) + 1 == int(a[i + 1]):
        b = b + 1
    elif int(a[i]) - 1 == int(a[i + 1]):
        b = b - 1
    i = i + 1

if b == 6:
    print('ascending')
elif b == -6:
    print('descending')
else:
    print('mixed')