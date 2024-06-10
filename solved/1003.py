import sys


input = sys.stdin.readline

howMany = [0, 0]
howManys = []


def fibonacci(n):
    if n == 0:
        howMany[0] += 1
        return 0
    elif n == 1:
        howMany[1] += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(5):
    howMany = [0, 0]
    fibonacci(i)
    howManys.append(howMany)

for i in range(36):
    a = howManys[i + 3][0] + howManys[i + 4][0]
    b = howManys[i + 3][1] + howManys[i + 4][1]
    howManys.append([a, b])

T = int(input())
for t in range(T):
    print(*howManys[int(input())])
