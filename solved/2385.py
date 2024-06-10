def right_smaller(a, b):
    if int(a + b) > int(b + a):
        return True
    elif int(a + b) < int(b + a):
        return False
    else:
        if len(b) >= len(a):
            return True
        else:
            return False


def sort_share(arr):
    for j in range(N - 1):
        for i in range(N - 1):
            a, b = arr[i], arr[i + 1]
            if right_smaller(a, b):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return 0


def valid(arr):
    for idx, item in enumerate(arr):
        if item[0] != "0":
            return True, idx

    return False, -1


def find(idx):
    ans = float("inf")
    i = idx
    while i < N and share[i][0] == share[idx][0]:
        temp = share[i]
        for j, value in enumerate(share):
            if j != i:
                temp += value

        if int(temp) < ans:
            ans = int(temp)

        i += 1

    return ans


N = int(input())
share = list(input().split())

sort_share(share)

if share[0][0] == "0":
    valid, idx = valid(share)
    if valid:
        ans = find(idx)

        print(ans)

    else:
        print("INVALID")
else:
    ans = ""
    for value in share:
        ans += value
    print(ans)
