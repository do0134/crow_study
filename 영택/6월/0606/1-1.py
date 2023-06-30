from collections import deque

n = int(input())
arr = [list(input().split()) for _ in range(n)]

teacher = list()
student = list()
point = list()
d = ((1,0),(-1,0),(0,1),(0,-1))


for i in range(n) :
    for j in range(n) :
        if arr[i][j] == "T" :
            teacher.append((i,j))
        if arr[i][j] == "S" :
            student.append((i,j))

def bfs(r,c) :
    global point
    q = deque()

    for dr,dc in d :
        q.append((r,c,dr,dc))

    while q :
        cr, cc, pr,pc = q.popleft()
        nr, nc = cr +pr, cc + pc

        if 0 <= nr < n and 0 <= nc < n :
            if arr[nr][nc] == "T" :
                if arr[cr][cc] == "S" :
                    print("NO")
                    exit()
                else :
                    if (cr,cc) not in point :
                        point.append((cr,cc))

            elif arr[nr][nc] == "X" :
                q.append((nr,nc,pr,pc))

for r,c in student :
    bfs(r,c)

if len(point) > 3 :
    print(point)
    print("NO")
else :
    print("YES")