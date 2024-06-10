N, K = map(int, input().split())
unit = []
count = 0

for _ in range(N):
    unit.append(int(input()))

while K > 0:
    # 비싼것부터 한땀한땀 빼가면서 카운팅 함
    if K - unit[-1] >= 0:
        K = K - unit[-1]
        count += 1
    # 뺄 수 없으면 제외
    else:
        unit.pop()

print(count)
