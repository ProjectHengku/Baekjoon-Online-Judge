N = int(input())

for _ in range(N):
    a, *A = list(map(int, input().split()))
    b, *B = list(map(int, input().split()))

    # 딱지의 가치는 별(4) >> 동그라비(3) >> 네모(2) >> 세모(1)
    if A.count(4) > B.count(4):
        print("A")
    elif A.count(4) < B.count(4):
        print("B")
    else:
        if A.count(3) > B.count(3):
            print("A")
        elif A.count(3) < B.count(3):
            print("B")
        else:
            if A.count(2) > B.count(2):
                print("A")
            elif A.count(2) < B.count(2):
                print("B")
            else:
                if A.count(1) > B.count(1):
                    print("A")
                elif A.count(1) < B.count(1):
                    print("B")
                else:
                    print("D")