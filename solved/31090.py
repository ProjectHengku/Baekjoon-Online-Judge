T = int(input())

for i in range(T):
    N = int(input())

    # last 2 degits of N
    L = N % 100

    if (N + 1) % L == 0:
        print("Good")
    else:
        print("Bye")