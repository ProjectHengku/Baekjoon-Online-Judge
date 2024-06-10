N = int(input())
count = 0

for n in range(N):
    word = input()
    groupWord = True
    check = set()

    for i in range(len(word)):
        letter = word[i]
        if letter in check:
            if word[i - 1] == letter:
                pass
            else:
                groupWord = False
                break
        else:
            check.add(letter)

    if groupWord:
        count += 1

print(count)
