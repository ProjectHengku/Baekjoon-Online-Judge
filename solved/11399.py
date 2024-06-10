N = int(input())
P = list(map(int, input().split()))

# 초반의 수가 계속 N회 가까이 누적된다.
# 따라서 연쇄적 증가의 합의 최소화를 위해서는, 오름차순 정렬 후 더하면 된다.
P.sort()
sumOfsum = 0

for n in range(N):
    sumOfsum += sum(P[: n + 1])

print(sumOfsum)
