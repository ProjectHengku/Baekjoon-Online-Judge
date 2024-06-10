white = input().split()

black = [1, 1, 2, 2, 2, 8]
cast = [0, 0, 0, 0, 0, 0]

for i in range(6):
    cast[i] = black[i] - int(white[i])

print(str(cast[0]) + " " + str(cast[1]) + " " + str(cast[2]) + " " + str(cast[3]) + " " + str(cast[4]) + " " + str(cast[5]))