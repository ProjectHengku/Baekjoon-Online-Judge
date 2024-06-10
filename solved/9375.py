T = int(input())

for t in range(T):
    N = int(input())

    # 데이터 입력
    clothes = {}
    for _ in range(N):
        cloth, piece = input().split()
        if piece not in clothes:
            clothes[piece] = [cloth]
        else:
            clothes[piece].append(cloth)

    # 경우의 수 추출
    pieces = list(clothes.keys())
    howmany = [len(clothes[pieces[i]]) for i in range(len(pieces))]

    answer = 1
    for count in howmany:
        answer *= count + 1

    answer -= 1

    print(answer)
