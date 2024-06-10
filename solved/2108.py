import sys

input = sys.stdin.readline

# N is odd


# mathmatical round
def mRound(x):
    if x < 0:
        return int(x - 0.5) if (x * 10) % 10 > -5 else int(x)
    else:
        return int(x + 0.5) if (x * 10) % 10 >= 5 else int(x)


N = int(input())
numbers = []

# input data
for _ in range(N):
    numbers.append(int(input()))

# 1. mean
print(mRound(sum(numbers) / len(numbers)))

# 2. median
numbers.sort()

if len(numbers) % 2 != 0:
    print(numbers[len(numbers) // 2])
else:
    print(numbers[len(numbers) // 2 - 1])

# 3. mode
freq = {}

for v in numbers:
    freq.setdefault(v, 0)
    freq[v] += 1

max_freq = max(freq.values())

modes = [key for key, value in freq.items() if value == max_freq]
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

# 4. range
print(max(numbers) - min(numbers))
