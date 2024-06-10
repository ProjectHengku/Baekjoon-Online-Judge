def is_left_bigger(a, b):
    a = str(a)
    b = str(b)
    if int(a + b) > int(b + a):
        return True
    elif int(a + b) < int(b + a):
        return False
    else:
        if len(a) < len(b):
            return True
        else:
            return False


def num_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if is_left_bigger(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


K, N = map(int, input().split())
numbers = [int(input()) for _ in range(K)]

# all numbers are natural number
for _ in range(N - K):
    numbers.append(max(numbers))

num_sort(numbers)

ans = ""
while numbers:
    num = numbers.pop()
    ans += str(num)

print(ans)
