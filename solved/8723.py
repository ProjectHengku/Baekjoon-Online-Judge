sides = list(map(int, input().split()))
sides.sort()

a, b, c = sides

equilateral = False
rightangled = False

if a == b == c:
    equilateral = True

if c**2 == a**2 + b**2:
    rightangled = True

if rightangled:
    print(1)
elif equilateral:
    print(2)
else:
    print(0)
