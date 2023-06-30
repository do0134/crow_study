# 백준 18427 함께 블록 쌓기
# https://www.acmicpc.net/problem/18427

n, m, h = map(int,input().split())
dp = [[0]*(h+1) for _ in range(n+1)]
arr = [list(map(int,input().split())) for _ in range(n)]
x = 10007
dp[0][0] = 1
for i in range(n):
    dp[i+1][0] = 1
    dp[i+1] = dp[i].copy()
    for block in arr[i]:
        for j in range(block, h+1):
            dp[i+1][j] += dp[i][j-block]

print(dp[n][h]%x)
