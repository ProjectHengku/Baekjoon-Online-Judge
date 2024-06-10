n = int(input())

for i in range(n):
    triangle = list(map(int, input().split()))
    triangle.sort()

    print(f"Scenario #{i + 1}:")

    # 피타고라스의 정리
    if triangle[2] ** 2 == triangle[1] ** 2 + triangle[0] ** 2:
        print("yes")
    else:
        print("no")

    print()
