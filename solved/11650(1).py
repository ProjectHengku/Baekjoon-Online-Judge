n = int(input()) + 1
xy_list = []

for i in range(1, n):
    inp = input().split()
    xy_list.append([int(inp[0]), int(inp[1])])

xy_list.sort()

for i in range(1, n):
    j = i
    while j > 1 and xy_list[j-1][0] == xy_list[j-2][0] and xy_list[j-1][1] < xy_list[j-2][1]:
        xy_list[j-1], xy_list[j-2] = xy_list[j-2], xy_list[j-1]
        j -= 1

for i in range(n-1):
    print(str(xy_list[i][0]) + " " + str(xy_list[i][1]))
