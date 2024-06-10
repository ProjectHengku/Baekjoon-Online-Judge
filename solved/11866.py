import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = []
Now = [i for i in range(1, N + 1)]

# implement cycle counting when overflows
point = 0

while Now:
    point = (point + K - 1) % len(Now)
    answer.append(Now.pop(point))

print("<", end="")
for i in range(N - 1):
    print(answer[i], end=", ")
print(answer[-1], end="")
print(">")