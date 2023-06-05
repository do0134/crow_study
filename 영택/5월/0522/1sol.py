# 백준 14466 소가 길을 건너간 이유 6
# https://www.acmicpc.net/problem/14466

from collections import deque

n,k,r = map(int,input().split())
farm = [[0]*(n+1) for _ in range(n+1)]
road = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r) :
    r1,c1,r2,c2 = map(int,input().split())
    road[r1][c1].append((r2,c2))
    road[r2][c2].append((r1,c1))


cow = deque()
for _ in range(k) :
    a,b = map(int,input().split())
    cow.append((a,b))

answer = len(cow)*(len(cow)-1) // 2

dr = [1,-1,0,0]
dc = [0,0,1,-1]

while cow :
    n_cow = cow.popleft()
    q = deque()
    v = [[0]*(n+1) for _ in range(n+1)]
    q.append((n_cow[0],n_cow[1]))
    v[n_cow[0]][n_cow[1]] = 1

    while q :
        cr, cc = q.popleft()
        for d in range(4) :
            nr, nc = cr+dr[d], cc+dc[d]
            if (nr,nc) in road[cr][cc] :
                continue
            if 1 <= nr < n+1 and 1 <= nc < n+1 and not v[nr][nc] and not farm[nr][nc] :
                q.append((nr,nc))
                v[nr][nc] = 1
                if (nr,nc) in cow :
                    answer -= 1


print(answer)