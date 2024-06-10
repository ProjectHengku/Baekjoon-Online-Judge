while True:
    n = input()
    m = len(n)

    if int(n) == 0:
        break
    else:
        if len(n) % 2 == 1:
            if n[:(m // 2 + 1)] == (n[(m // 2):])[::-1]:
                print("yes")
            else:
                print("no")
        elif len(n) % 2 == 0:
            if n[:(m // 2)] == (n[(m // 2):])[::-1]:
                print("yes")
            else:
                print("no")