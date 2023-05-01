def solution(t):
    n = len(t)
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = t[0][0]
    for i in range(n - 1):
        for j in range(i + 2):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + t[i + 1][j]
            elif j == i + 1:
                dp[i + 1][j] = dp[i][j - 1] + t[i + 1][j]
            else:
                dp[i + 1][j] = max(dp[i][j] + t[i + 1][j], dp[i][j - 1] + t[i + 1][j])

    return max(dp[-1])