import sys
input = sys.stdin.readline

stack = []
n = int(input())

for i in range(n):
    # make function 'push X' -> stack.append(X)
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    # make function 'pop' -> stack.pop()
    # and if stack is empty, print -1
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # make function 'size' -> len(stack)
    elif order[0] == 'size':
        print(len(stack))
    # make function 'empty' -> if len(stack) == 0: print(1)
    # else: print(0)
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # make function 'top' -> print(stack[-1])
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])