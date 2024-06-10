import sys

input = sys.stdin.readline

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 순서 1순위, 시작하는 순서 2순위로 정렬함
schedules.sort(key=lambda x: (x[1], x[0]))

# 탐색
count = 1
end = schedules[0][1]

for i in range(1, N):
    if schedules[i][0] >= end:
        count += 1
        end = schedules[i][1]

print(count)
