n = int(input())
students = list(map(int, input().split()))
sequence = [1]


for i in range(1, n):
    if students[i] == 0:
        sequence.append(i + 1)
    else:
        sequence.insert(-students[i], i + 1)

print(*sequence)
