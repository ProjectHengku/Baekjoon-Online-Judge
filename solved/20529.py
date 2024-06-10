import itertools

T = int(input())
for _ in range(T):
    N = int(input())
    # 어짜피 많아봤자 MTBI 16 종류임
    MBTI = {
        "ISTJ": 0,
        "ISFJ": 0,
        "INFJ": 0,
        "INTJ": 0,
        "ISTP": 0,
        "ISFP": 0,
        "INFP": 0,
        "INTP": 0,
        "ESTP": 0,
        "ESFP": 0,
        "ENFP": 0,
        "ENTP": 0,
        "ESTJ": 0,
        "ESFJ": 0,
        "ENFJ": 0,
        "ENTJ": 0,
    }

    for mbti in list(input().split()):
        MBTI[mbti] += 1

    # 0보다 크면 조합 가능함
    available = []
    for mbti in MBTI.keys():
        if MBTI[mbti] > 0:
            for _ in range(MBTI[mbti] if MBTI[mbti] < 3 else 3):
                available.append(mbti)

    if len(available) > 1:
        answer = 13
        comb = list(itertools.combinations(available, 3))

        for mbti1, mbti2, mbti3 in comb:
            count = 0
            for i in range(4):
                if mbti1[i] != mbti2[i]:
                    count += 1

            for i in range(4):
                if mbti2[i] != mbti3[i]:
                    count += 1

            for i in range(4):
                if mbti3[i] != mbti1[i]:
                    count += 1

            if count < answer:
                answer = count

        print(answer)

    # 한 종류 밖에 없으면
    else:
        print(0)
