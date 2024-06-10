T = int(input())
for i in range(T):
    x, y = map(int, input().split())

    distance = y - x

    # k is count
        
    k = 1
    l = 0
    truek = 0

    while distance - k > 0:
        distance = distance - k
        l += 1
        truek += 1
        if l == 2:
            k += 1
            l = 0

  
    if distance == 0:
        print(truek)
    else:
        print(truek + 1)