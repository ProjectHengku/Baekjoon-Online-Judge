N = int(input())
num_in = list(input().split())

numbers = []
for num in num_in:
    numbers.append((int((num * 10)[:10]), len(num)))

numbers.sort(key=lambda x: x[0])

# make number
ans = ""

while numbers:
    num, end = numbers.pop()
    ans += (str(num))[:end]

if ans[0] == "0":
    print(0)
else:
    print(ans)
