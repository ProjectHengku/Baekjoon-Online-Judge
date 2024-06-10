T = int(input())

for t in range(T):
    tc = t + 1

    sides = list(map(int, input().split()))
    sides.sort()

    a, b, c = sides

    print(f"Case #{tc}:", end=" ")
    if a == b == c:
        print("equilateral")
    elif a + b <= c:
        print("invalid!")
    elif a == b or b == c or a == c:
        print("isosceles")
    else:
        print("scalene")
