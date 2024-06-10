T = int(input())

for i in range(T):
    test = input()
    stack = []
    for j in test:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                stack.append(j)
                break
            stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
        