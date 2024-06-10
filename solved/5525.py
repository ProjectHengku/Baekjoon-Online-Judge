N = int(input())
M = int(input())
S = input()

result = 0

# 모든 글자 순회
count = 0
now = 0

while now < M - 2:
    # 패턴이 일치하면
    if S[now : now + 3] == "IOI":
        # 그 다음꺼
        now += 2
        count += 1
        # 완성되면
        if count == N:
            result += 1
            # 그 다음꺼 다시 간재봄
            count -= 1
    else:
        # 그 옆에서 처음부터 재시작
        now += 1
        count = 0


print(result)
