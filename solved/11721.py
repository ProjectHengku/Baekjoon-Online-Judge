word = input()

for i in range(len(word) // 10 + 1):
    print(word[10 * i : 10 * (i + 1)])
