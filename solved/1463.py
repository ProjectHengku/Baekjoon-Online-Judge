N = int(input())
counts = [0] * (N + 1)
counts[1] = 0

for i in range(2, N + 1):
    # 1을 빼는 경우
    counts[i] = counts[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        counts[i] = min(counts[i], counts[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        counts[i] = min(counts[i], counts[i // 3] + 1)

print(counts[N])
