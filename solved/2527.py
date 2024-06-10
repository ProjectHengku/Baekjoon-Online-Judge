for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 안 겹침
    if q1 < y2 or p1 < x2 or q2 < y1 or p2 < x1:
        print("d")
    elif x1 == p2 or x2 == p1:
        # 점 겹침
        if y2 == q1 or y1 == q2:
            print("c")
        # 선 겹침
        else:
            print("b")
    elif y2 == q1 or q2 == y1:
        print("b")
    # 면 겹침
    else:
        print("a")
