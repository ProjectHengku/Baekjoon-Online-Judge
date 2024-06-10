numbers = [0, 1, 2, 3, 5, 8]
n = int(input())

for _ in range(6, n + 1):
    numbers.append((numbers[-1] + numbers[-2]) % 10007)

print(numbers[n])