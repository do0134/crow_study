# 백준 3197 백조의 호수
# https://www.acmicpc.net/problem/3197

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n, m = map(int,input().split())
swan = list()
lake = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lake[i][j] == "L":
            swan.append((i,j))
            lake[i][j] = "."
            if len(swan) == 2:
                break

melt = deque()
v = [[0]*m for _ in range(n)]
rank = [[0]*m for _ in range(n)]
root = [[(i,j) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        q = deque()
        if not v[i][j] and lake[i][j] == ".":
            v[i][j] = 1
            q.append((i,j))
            while q:
                cr, cc = q.popleft()
                root[cr][cc] = (i,j)
                for d in range(4):
                    nr, nc = cr + dr[d], cc+ dc[d]
                    if 0 <= nr < n and 0 <= nc < m and not v[nr][nc]:
                        if lake[nr][nc] == ".":
                            v[nr][nc] = 1
                            q.append((nr,nc))
                        elif lake[nr][nc] == "X":
                            v[nr][nc] = 1
                            melt.append((nr,nc))


def find(x):
    if root[x[0]][x[1]] == x :
        return x
    root[x[0]][x[1]] = find(root[x[0]][x[1]])
    return root[x[0]][x[1]]


def union(x1, x2):
    r1 = find(x1)
    r2 = find(x2)
    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1


day = 0
while find(swan[0]) != find(swan[1]):
    temp = deque()
    while melt:
        cr, cc = melt.popleft()
        lake[cr][cc] = "."
        to_union = list()

        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] and lake[nr][nc] == "X":
                temp.append((nr, nc))
                v[nr][nc] = 1
            elif 0 <= nr < n and 0 <= nc < m and lake[nr][nc] == "." and root[cr][cc] != root[nr][nc]:
                to_union.append((nr,nc))

        for nr,nc in to_union:
            if find((nr,nc)) != find((cr,cc)):
                union((nr,nc), (cr,cc))
    melt = temp
    day += 1

print(day)