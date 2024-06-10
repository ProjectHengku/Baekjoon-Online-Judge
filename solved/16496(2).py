def num_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if is_left_bigger(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def is_left_bigger(a, b):
    if int(a + b) > int(b + a):
        return True
    elif int(a + b) < int(b + a):
        return False
    else:
        if len(a) < len(b):
            return True
        else:
            return False


N = int(input())
num_in = list(input().split())

num_sort(num_in)

# make number
ans = ""

while num_in:
    num = num_in.pop()
    ans += num

if ans[0] == "0":
    print(0)
else:
    print(ans)
