numbers = [i for i in range(10001)]


def sum_degit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_degit(n // 10)


for n in range(10002):
    if (n + sum_degit(n) <= 10000) and (numbers[n + sum_degit(n)] == n + sum_degit(n)):
        numbers[n + sum_degit(n)] = 0

numbers = list(set(numbers))
numbers.sort()
del numbers[0]

for number in numbers:
    print(number)
