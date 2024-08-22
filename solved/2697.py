def nextNumber(number):
    numberList = [int(digit) for digit in number]

    for backIdx in range(len(numberList)):
        numberFront = numberList[:(len(numberList) - 1 - backIdx)]
        numberBack = numberList[(len(numberList) - 1 - backIdx):]

        numberBackSorted = sorted(numberBack, reverse=True)
        if int("".join(list(map(str, numberFront + numberBackSorted)))) > int(number):

            checkCondition = max(numberBack)
            for digit in numberBack:
                if digit > numberBack[0] and digit < checkCondition:
                    checkCondition = digit

            numberBack.remove(checkCondition)
            numberBack.sort()

            return "".join(list(map(str, numberFront + [checkCondition] + numberBack)))

    return "BIGGEST"

T = int(input())

for testCase in range(T):
    number = input()
    print(nextNumber(number))
