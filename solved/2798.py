# 입력받기
N, M = map(int, input().split()) # 카드의 개수 N과 숫자 M
cards = list(map(int, input().split())) # 카드에 쓰여 있는 수

# 초기화
answer = 0 # M과 가장 가까운 카드의 합

# 삼중 반복문으로 카드 세 장 뽑기
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      # 카드의 합 구하기
      sum = cards[i] + cards[j] + cards[k]
      # M을 넘지 않고, M과 가장 가까운 경우
      if sum <= M and sum > answer:
        # 갱신하기
        answer = sum

# 출력하기
print(answer)
