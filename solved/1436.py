count = 0
number = 0
dooms = []

while count < 10000:
    if "666" in str(number):
        dooms.append(number)
        count += 1
    number += 1

N = int(input())

print(dooms[N - 1])
