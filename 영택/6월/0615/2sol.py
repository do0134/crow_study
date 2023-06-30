# 백준 2293 동전1
# https://www.acmicpc.net/problem/2293

n, k = map(int,input().split())
coin = list()

for _ in range(n):
    coin.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])