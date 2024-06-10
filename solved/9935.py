string = input()
bomb = list(input())

stack = []
n = len(bomb)
for letter in string:
    stack.append(letter)
    while stack[-n:] == bomb:
        for _ in range(n):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
