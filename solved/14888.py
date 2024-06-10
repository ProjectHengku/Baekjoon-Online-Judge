N = int(input())
A = list(map(int, input().split()))
plus, minus, times, divisions = map(int, input().split())

# 깊이 우선 탐색
stack = []
if plus:
    stack.append((A[0], 1, "plus", plus - 1, minus, times, divisions))
if minus:
    stack.append((A[0], 1, "minus", plus, minus - 1, times, divisions))
if times:
    stack.append((A[0], 1, "times", plus, minus, times - 1, divisions))
if divisions:
    stack.append((A[0], 1, "divisions", plus, minus, times, divisions - 1))

minimum = float("inf")
maximum = float("-inf")

while stack:
    previous, now, operator, pp, mm, tt, dd = stack.pop()
    if operator == "plus":
        next = previous + A[now]
    elif operator == "minus":
        next = previous - A[now]
    elif operator == "times":
        next = previous * A[now]
    else:
        if previous > 0:
            next = previous // A[now]
        elif previous < 0:
            next = -(-previous // A[now])
        else:
            next = 0

    if now == N - 1:
        if next > maximum:
            maximum = next
        if next < minimum:
            minimum = next
    else:
        if pp:
            stack.append((next, now + 1, "plus", pp - 1, mm, tt, dd))
        if mm:
            stack.append((next, now + 1, "minus", pp, mm - 1, tt, dd))
        if tt:
            stack.append((next, now + 1, "times", pp, mm, tt - 1, dd))
        if dd:
            stack.append((next, now + 1, "divisions", pp, mm, tt, dd - 1))

print(maximum)
print(minimum)
