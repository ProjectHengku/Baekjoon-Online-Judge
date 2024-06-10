import random

fruit_unit = int(input())

rotation = []
distance = []

# 이동 방향과 거리를 기록하자
for _ in range(6):
    rot, dis = map(int, input().split())
    rotation.append(rot)
    distance.append(dis)

# 한 번 파인 직각육각형 (ㄱ자) 형태의 고찰
# 6번 중 1번만 불리는 방향이 2종, 2번 불리는 방향이 2종 존재함
# 이동 방향의 호출 순서를 원형으로 정렬하면, 횟수 기준으로 정렬했을 때 112222 꼴로 존재함
counts = [0] * 5
for i in range(6):
    counts[rotation[i]] += 1

# 1번 불리는 방향과 2번 불리는 방향 기억함
once = []
twice = []
for i in range(1, 5):
    if counts[i] == 1:
        once.append(i)
    elif counts[i] == 2:
        twice.append(i)

# 1번 불린거에서 아무거나 뽑는다
start = random.choice(once)
# 문제 조건은 반시계방향으로 회전하므로
# 임의의 1번 불린 방향에서 반시계 방향으로 흘러가면 반드시 2번 불리는 방향이 1바퀴를 도는 것보다 빨리 도출됨
twices = []
i = rotation.index(start)
while len(twices) < 4:
    i = (i + 1) % 6

    # ㄱ자 형태 특성상 2번째로 불리는 순서 4번 중 가운데 2 자리 수가 큰 직사각형에서 잘라내야 하는 작은 사각형의 가로 세로에 해당하는 변
    if rotation[i] in twice:
        twices.append(i)

small1 = distance[twices[1]]
small2 = distance[twices[2]]
big1 = distance[rotation.index(once[0])]
big2 = distance[rotation.index(once[1])]

area = big1 * big2 - small1 * small2

print(area * fruit_unit)
