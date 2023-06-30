# 백준 2579 계단 오르기
# https://www.acmicpc.net/problem/2579

n = int(input())
dp = [[0, 0] for _ in range(n)]
stair = list()

for _ in range(n):
    stair.append(int(input()))


def dfs(idx, score, cons):
    global dp
    if idx == n-1:
        return

    if cons < 2 :
        score1 = score + stair[idx+1]
        if score1 > dp[idx+1][1]:
            dp[idx+1][1] = score1
            dfs(idx+1, score1, cons+1)

    if idx < n-2 :
        score2 = score + stair[idx+2]
        if score2 > dp[idx+2][0]:
            dp[idx+2][0] = score2
            dfs(idx+2, score2, 1)


dp[0][0] = stair[0]
if n > 1 :
    dp[1][0] = stair[1]
    dfs(1, stair[1], 1)
dfs(0, stair[0], 1)

print(max(dp[-1]))