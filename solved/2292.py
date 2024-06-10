N = int(input())
i = 0
def f(x):
    return 6 * ((x + 1) * x / 2)

if N == 1:
    print(1)
    exit()

while True:
    if N >= f(i) + 2 and N < f(i + 1) + 2:
        break
    else:
        i += 1

print(i + 2)