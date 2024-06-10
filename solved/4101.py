while True:
    test = input().split()
    if test == ["0", "0"]:
        break
    elif int(test[0]) > int(test[1]):
        print("Yes")
    else:
        print("No")