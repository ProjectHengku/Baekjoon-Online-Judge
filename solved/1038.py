def decrease(n):
    str_n = str(n)
    digit = 0

    while digit < len(str_n):
        if int(str_n[digit]) >= len(str_n) - 1 - digit:
            if digit > 0:
                if int(str_n[digit]) < int(str_n[digit - 1]):
                    digit += 1
                else:
                    return len(str_n) - 1 - digit
            else:
                digit += 1
        else:
            return len(str_n) - 1 - digit
    else:
        return -1


N = int(input())

n = 0
c = 0
E = -1
while c < N:
    if E == -1:
        n += 1

    if n > 9876543210:
        print(-1)
        exit()

    E = decrease(n)

    if E == -1:
        c += 1

    else:
        n = ((n // 10**E) + 1) * 10**E


print(n)
