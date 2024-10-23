from math import lcm


s = input()
t = input()

# s와 t의 길이의 최소공배수
l = lcm(len(s), len(t))

# s와 t의 길이를 최소공배수로 늘려줌
s *= l // len(s)
t *= l // len(t)

if s == t:
    print(1)
else:
    print(0)
