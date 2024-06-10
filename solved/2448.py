def re(tri):
    h = len(tri)
    tri2 = []
    # 윗쪽 반
    for line in tri:
        tri2.append(" " * h + line + " " * h)

    # 아랫쪽 반
    for line in tri:
        tri2.append(line + " " + line)

    return tri2


N = int(input())

tri = ["  *  ", " * * ", "*****"]

while len(tri) < N:
    tri = re(tri)

for line in tri:
    print(line)
