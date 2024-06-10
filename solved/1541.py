equation = input()

letters = []

for letter in equation:
    if letter.isnumeric():
        letters.append(int(letter))
    else:
        letters.append(letter)

queue = []
calculation = []

for letter in letters:
    if letter not in ["+", "-"]:
        queue.append(letter)
    else:
        number = 0
        for i in range(len(queue)):
            number += queue[i] * (10 ** (len(queue) - i - 1))
        calculation.append(number)
        queue = []
        calculation.append(letter)
number = 0
for i in range(len(queue)):
    number += queue[i] * (10 ** (len(queue) - i - 1))
calculation.append(number)
queue = []

finalCalculation = []
if "-" in calculation:
    for i in range(len(calculation)):
        if calculation[i] == "+":
            calculation[i + 1] = calculation[i - 1] + calculation[i + 1]
            calculation[i - 1] = 0
            calculation[i] = 0
        elif calculation[i] == "-":
            calculation[i] = 0
    for number in calculation:
        if number != 0:
            finalCalculation.append(number)
    first = finalCalculation[0]
    rest = finalCalculation[1:]

    print(first - sum(rest))
else:
    for i in range(len(calculation)):
        if calculation[i] == "+":
            calculation[i] = 0
    print(sum(calculation))
