# 백준 1520 내리막길
# https://www.acmicpc.net/problem/1520

n,m = map(int,input().split())
road = list()
for _ in range(n) :
    road.append(list(map(int,input().split())))

dp = [[-1]*m for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def dfs(r,c) :
    global dp
    if dp[r][c] != -1 :
        return dp[r][c]

    if r == n-1 and c == m-1 :
        return 1
    dp[r][c] = 0
    for d in range(4) :
        nr = dr[d] + r
        nc = dc[d] + c
        if 0 <= nr < n and 0 <= nc < m and road[r][c] > road[nr][nc]:
            dp[r][c] += dfs(nr,nc)

    return dp[r][c]


print(dfs(0,0))
