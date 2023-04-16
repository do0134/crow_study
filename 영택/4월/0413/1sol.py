# 프로그래머스 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0])
    q = deque()
    v = [[int(1e9)]*m for _ in range(n)]
    q.append((0,0,1))
    v[0][0] = 1
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    while q :
        cr, cc, cnt = q.popleft()
        for d in range(4) :
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and v[nr][nc] > cnt+1:
                v[nr][nc] = cnt+1
                q.append((nr,nc,cnt+1))
    if v[n-1][m-1] == int(1e9) :
        return -1
    return v[n-1][m-1]