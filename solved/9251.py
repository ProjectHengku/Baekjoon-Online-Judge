word1 = input()
word2 = input()

count1 = [0] * (len(word1))
count2 = [0] * (len(word2))

# dp
dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[len(word1)][len(word2)])
