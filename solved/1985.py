def digit_number(number):
    if number == 10:
        return 0
    elif number == -1:
        return 9
    else:
        return number

def is_friends(a, b):
    digitA = set()
    digitB = set()

    # 자릿수 파악
    for digit in a:
        digitA.add(digit)
    for digit in b:
        digitB.add(digit)

    if digitA == digitB:
        return True
    else:
        return False

def is_almostfriends(a, b):
    for index in range(len(a) - 1):
        listA = list(a)
        listA[index], listA[index + 1] = str(digit_number(int(listA[index]) + 1)), str(digit_number(int(listA[index + 1]) - 1))
        if listA[0] != "0":
            if is_friends(listA, b):
                return True

        listA = list(a)
        listA[index], listA[index + 1] = str(digit_number(int(listA[index]) - 1)), str(digit_number(int(listA[index + 1]) + 1))
        if listA[0] != "0":
            if is_friends(listA, b):
                return True

    for index in range(len(b) - 1):
        listB = list(b)
        listB[index], listB[index + 1] = str(digit_number(int(listB[index]) + 1)), str(digit_number(int(listB[index + 1]) - 1))
        if listB[0] != "0":
            if is_friends(a, listB):
                return True

        listB = list(b)
        listB[index], listB[index + 1] = str(digit_number(int(listB[index]) - 1)), str(digit_number(int(listB[index + 1]) + 1))
        if listB[0] != "0":
            if is_friends(a, listB):
                return True

    return False

for test_case in range(3):
    a, b = map(str, input().split())

    if is_friends(a, b):
        print("friends")
    elif is_almostfriends(a, b):
        print("almost friends")
    else:
        print("nothing")