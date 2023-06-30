# 백준 18430 무기공학
# https://www.acmicpc.net/problem/18430


n,m = map(int,input().split())
answer = 0
arr = [list(map(int,input().split())) for _ in range(n)]

dr = [1,-1,-1,1]
dc = [1,1,-1,-1]
visit = [[0]*m for _ in range(n)]


def make_weapon(r,c,value):
    global answer
    answer = max(answer, value)

    if c == m:
        c = 0
        r += 1

    if r == n:
        return

    if not visit[r][c]:
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visit[r][nc] and not visit[nr][c]:
                visit[r][c] = visit[r][nc] = visit[nr][c] = 1
                make_weapon(r,c+1,value+2*arr[r][c]+arr[r][nc]+arr[nr][c])
                visit[r][c] = visit[r][nc] = visit[nr][c] = 0

    make_weapon(r,c+1,value)


make_weapon(0,0,0)
print(answer)