# 백준 11967 불켜기
# https://www.acmicpc.net/problem/11967

from collections import deque, defaultdict

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n,m = map(int,input().split())

arr = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]
arr[0][0] = v[0][0] = 1

answer = 1
switch = defaultdict(list)

for _ in range(m):
    i,j,r,c = map(int,input().split())
    switch[i-1,j-1].append([r-1,c-1])

q = deque()
q.append((0,0))


while q:
    cr, cc = q.popleft()

    for sr, sc in switch[cr,cc]:
        if not arr[sr][sc]:
            answer += 1

        arr[sr][sc] = 1
        for d in range(4):
            nsr, nsc = sr+dr[d], sc+dc[d]
            if 0 <= nsr < n and 0 <= nsc < n and v[nsr][nsc] and not v[sr][sc]:
                q.append((sr,sc))
                v[sr][sc] = 1
                break

    for d in range(4):
        nr, nc = cr+dr[d], cc+dc[d]
        if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and arr[nr][nc]:
            v[nr][nc] = 1
            q.append((nr,nc))


print(answer)