from collections import deque

N, M = map(int, input().split())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))

# 투 포인터 알고리즘
answer = []

while len(answer) < N + M:
    if A and B:
        if A[0] <= B[0]:
            answer.append(A.popleft())
        else:
            answer.append(B.popleft())
    else:
        if not A:
            answer.append(B.popleft())
        else:
            answer.append(A.popleft())


print(*answer)