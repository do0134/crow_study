# 백준 10026 적록색약
# https://www.acmicpc.net/problem/10026

from collections import deque

def bfs(r,c,t) :
    q = deque()
    q.append((r,c))
    v[r][c] = 1

    while q :
        cr, cc = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)] :
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] :
                if t == "n" :
                    if rgb[cr][cc] == rgb[nr][nc] :
                        v[nr][nc] = 1
                        q.append((nr,nc))
                elif t == "rg" :
                    if rgb[cr][cc] == "B" and rgb[cr][cc] == rgb[nr][nc] :
                        v[nr][nc] = 1
                        q.append((nr,nc))
                    elif (rgb[cr][cc] == "R" or rgb[cr][cc] == "G") and (rgb[nr][nc] == "R" or rgb[nr][nc] == "G") :
                        v[nr][nc] = 1
                        q.append((nr,nc))




n = int(input())
rgb = [list(input()) for _ in range(n)]
answer = list()

for t in ("n", "rg") :
    cnt = 0
    v = [[0]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if not v[i][j] :
                cnt += 1
                bfs(i,j,t)
    answer.append(cnt)

print(*answer)

