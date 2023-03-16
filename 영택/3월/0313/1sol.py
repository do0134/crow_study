from collections import deque

n,m = map(int,input().split())
arr = list()
for _ in range(n) :
    arr.append(list(map(int,input().split())))
dr = [1,-1,0,0]
dc = [0,0,1,-1]

cant = deque()
dp = [[0]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        for d in range(4) :
            if 0 <= i+dr[d] < n and 0 <= j+dc[d] < m :
                if arr[i][j] < arr[i+dr[d]][j+dc[d]] :
                    dp[i][j] += 1
        if dp[i][j] == 0 :
            cant.append((i,j))

while cant :
    cr, cc = cant.popleft()
    if dp[cr][cc] == 0 :
        continue
    for d in range(4) :
        nr = cr + dr[d]
        nc = cc + dc[d]
        if 0 <= nr < n and 0 <= nc < m  :
            if dp[nr][nc] == 0 :
                dp[cr][cc] -= 1
            if dp[cr][cc] == 0 :
                cant.append((cr,cc))
                break


answer = 0
q = deque()
q.append((0,0,arr[0][0]))


while q :
    cr, cc, ch = q.popleft()

    if cr == n-1 and cc == m-1 :
        answer += 1
        continue
    for d in range(4) :
        nr = cr + dr[d]
        nc = cc + dc[d]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < ch and dp[nr][nc] > 0:
            q.append((nr,nc,arr[nr][nc]))


print(answer)
