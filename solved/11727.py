N = int(input())

# DP
for n in range(1, N + 1):
    if n == 1:
        result = 1
    else:
        result = result * 2 + (-1) ** (n)

print(result % 10007)
