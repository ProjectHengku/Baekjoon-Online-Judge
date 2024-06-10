# 루트 50000은 223.6
import math


table = [0, 1]

for i in range(2, 50001):
    minimum = float("inf")
    for j in range(1, int(math.sqrt(i)) + 1):
        minimum = min(minimum, table[i - j**2])
    table.append(minimum + 1)

print(table[int(input())])
