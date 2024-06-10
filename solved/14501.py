def consult(schedule, income):
    global maxincome
    # 마감 기한
    deadline = len(schedule)

    if schedule:
        for i in range(deadline):
            # 더 할 수 있으면 이어서 함
            if schedule[i][0] <= deadline - i:
                consult(schedule[i + schedule[i][0] :], income + schedule[i][1])
            # 더 못하면 최종 수익 정산
            else:
                if income > maxincome:
                    maxincome = income
    # 일거리 더 없으면 최종 수익 정산
    else:
        if income > maxincome:
            maxincome = income
            return 0


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

maxincome = 0
consult(schedule, 0)

print(maxincome)
