import sys

input = sys.stdin.readline

stack = []
answers = []
available = True

n = int(input())
now = 1

for _ in range(n):
    number = int(input())

    while now <= number:
        stack.append(now)
        answers.append("+")
        now += 1

    if stack[-1] == number:
        stack.pop()
        answers.append("-")
    else:
        available = False

if available:
    for i in answers:
        print(i)
else:
    print("NO")
