t = input()
i = 0
while i < int(t):
    data = input().split()

    h = int(data[0])
    w = int(data[1])
    n = int(data[2])

    if n % h == 0:
        orderw = n // h
        orderh = h
    else:
        orderw = n // h + 1
        orderh = n % h

    room = orderh * 100 + orderw
    print(room)
    i = i + 1