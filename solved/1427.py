firstNumber = input()
digits = []

for digit in firstNumber:
    digits.append(digit)

digits.sort()
digits = digits[::-1]

newNumber = ""

for number in digits:
    newNumber += str(number)

print(int(newNumber))
