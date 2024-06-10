import math

i = 0
while True:
    i += 1
    a, b, c = map(int, input().split())

    # terminate condition
    if (a, b, c) == (0, 0, 0):
        break
    else:
        if i > 1:
            print()

    if c == -1:
        answer = math.sqrt(a**2 + b**2)
        print(f"Triangle #{i}")
        print(f"c = {answer:.3f}")

    elif b == -1:
        answersquare = c**2 - a**2
        print(f"Triangle #{i}")
        if answersquare > 0:
            print(f"b = {math.sqrt(answersquare):.3f}")
        else:
            print("Impossible.")

    else:
        answersquare = c**2 - b**2
        print(f"Triangle #{i}")
        if answersquare > 0:
            print(f"a = {math.sqrt(answersquare):.3f}")
        else:
            print("Impossible.")
