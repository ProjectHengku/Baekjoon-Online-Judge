N = int(input())

score1, score2 = 0, 0
time1, time2 = 0, 0
winchanges = True

for _ in range(N):
    team, time = input().split()

    if team == "1":
        score1 += 1
    else:
        score2 += 1

    # 처음 이기기 시작해서 동점이 될 때 까지를 기록
    if winchanges:
        record = int(time[:2]) * 60 + int(time[3:])
        winchanges = False
    else:
        if score1 == score2:
            winchanges = True
            now = int(time[:2]) * 60 + int(time[3:])
            # 어떤 팀이 동점슛을 넣었다면 그 때 까진 지고있었다는 것이므로
            if team == "1":
                time2 += now - record
            else:
                time1 += now - record

# 끝나고 이기고 있던 쪽의 시간을 추가 기록
if score1 > score2:
    time1 += 48 * 60 - record
elif score1 < score2:
    time2 += 48 * 60 - record

min1 = ("0" + str(time1 // 60))[-2:]
sec1 = ("0" + str(time1 % 60))[-2:]
min2 = ("0" + str(time2 // 60))[-2:]
sec2 = ("0" + str(time2 % 60))[-2:]

print(min1 + ":" + sec1)
print(min2 + ":" + sec2)
