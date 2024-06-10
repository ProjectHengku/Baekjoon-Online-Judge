T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    floors = []
    # after we know k and n, we can make a list of lists
    # floor 0
    floors.append([i for i in range(1, n+1)])

    # floor k
    for i in range(1, k+1):
        floors.append([sum(floors[i-1][:j+1]) for j in range(n)])

    print(floors[k][n-1])