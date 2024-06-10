import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 초기 환경 세팅
# 여자가 0, 남자가 1
room = [[[] for _ in range(6)], [[] for _ in range(6)]]

for _ in range(N):
    S, Y = map(int, input().split())

    Y = Y - 1
    if room[S][Y] and room[S][Y][-1] < K:
        room[S][Y][-1] += 1
    # 할당된 방이 없거나 이전 방이 꽉 차있으면 새로 방 배정해줌
    else:
        room[S][Y].append(1)

# 방 개수 세기
count = 0

for sex in room:
    for year in sex:
        count += len(year)

print(count)