def ccw(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    a = x1 * y2 + x2 * y3 + x3 * y1
    b = y1 * x2 + y2 * x3 + y3 * x1

    return a - b


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

# 일반 교차
if ccw(p1, p2, p3)*ccw(p1, p2,p4)<0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)<0:
    print(1)
elif ccw(p1, p2, p3)*ccw(p1, p2,p4)==0 or ccw(p3,p4,p1)*ccw(p3,p4,p2)==0:
    # 4점 일직선상
    if ccw(p1, p2, p3)*ccw(p1, p2,p4)==0 and ccw(p3,p4,p1)*ccw(p3,p4,p2)==0:
        # p3 < p2 and p1 < p4: 교차하는 경우
        