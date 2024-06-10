while True:
    try:
        N = int(input())
    except:
        break

    # DP
    if N > 0:
        for n in range(1, N + 1):
            if n == 1:
                result = 1
            else:
                result = result * 2 + (-1) ** (n)
    else:
        result = 1

    print(result)
