T = int(input())
for tc in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    # DP
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for j in range(1, n):
        for i in range(2):
            # 대각선으로만 이어질듯
            dp[i][j] = max(
                dp[i - 1][j - 1] + sticker[i][j], max(dp[0][j - 1], dp[1][j - 1])
            )

    print(max(dp[0][-1], dp[1][-1]))
