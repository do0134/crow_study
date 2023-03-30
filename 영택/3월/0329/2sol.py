# 백준 1103 게임
# https://www.acmicpc.net/problem/1103

n,m = map(int,input().split())
game = list()
for _ in range(n) :
    game.append(list(input()))
flag = False
dp = [[0]*m for _ in range(n)]
v = [[0]*m for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
answer = -1
def dfs(r, c, cnt) :
    global flag, answer
    answer = max(answer, cnt)
    if flag :
        return
    for d in range(4) :
        nr = dr[d]*int(game[r][c]) + r
        nc = dc[d]*int(game[r][c]) + c
        if 0 <= nr < n and 0 <= nc < m and game[nr][nc] != "H" and dp[nr][nc] < cnt + 1:
            if v[nr][nc] :
                flag = True
                return
            v[nr][nc] = 1
            dp[nr][nc] = cnt+1
            dfs(nr,nc,cnt+1)
            v[nr][nc] = 0

v[0][0] = 1
dfs(0,0,1)
if flag :
    print(-1)
else :
    print(answer)
