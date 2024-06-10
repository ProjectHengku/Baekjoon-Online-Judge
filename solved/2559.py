N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# 초기값 세팅
sums = []

# 합 구하기
# 계속 n번씩 더하는 건 비효율적일듯
# 처음에만 더하고 그 뒤에는 앞에거 빼고 뒤에거 더하는 식으로 해보자
# 투 포인터
# 1) 처음엔 일일이 더해준다
tempsum = sum(temperature[0:K])
sums.append(tempsum)

# 2) 제일 앞을 빼고, 전진해서 한 칸 앞을 더한다
for i in range(N - K):
    tempsum -= temperature[i]
    tempsum += temperature[i + K]
    sums.append(tempsum)

# 3) 최댓값 구함
print(max(sums))
