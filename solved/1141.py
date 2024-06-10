N = int(input())

words = [input() for _ in range(N)]

# greedy
for i in range(N):
    for j in [k for k in range(N) if (k != i and words[k])]:
        # is prefix
        if words[j][: len(words[i])] == words[i]:
            # then delete
            words[i] = False
            break

count = 0
for item in words:
    if item:
        count += 1

print(count)
