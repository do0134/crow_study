# 백준 16967 배열 복원하기
# https://www.acmicpc.net/problem/16967

h,w,x,y = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(h+x)]
a = [[0]*w for _ in range(h)]

for i in range(h) :
    for j in range(w) :
        if i < x or j < y :
            a[i][j] = b[i][j]
        else :
            a[i][j] = b[i][j] - a[i-x][j-y]

for i in a :
    print(*i)