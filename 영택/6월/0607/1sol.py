# 백준 3109 빵집
# https://www.acmicpc.net/problem/3109

r,c = map(int,input().split())
arr = [list(input()) for _ in range(r)]
v = [[0]*c for _ in range(r)]

def dfs(r1,c1) :
    if c1 == c-1 :
        return True
    for d in (-1,0,1) :
        nr,nc = r1+d, c1+1
        if 0 <= nr < r and not v[nr][nc] and arr[nr][nc] == ".":
            v[nr][nc] = 1
            if dfs(nr,nc) :
                return True
    return False

answer = 0
for i in range(r) :
    if dfs(i,0) :
        answer += 1

print(answer)