# 백준 8972 미친 아두이노
# https://www.acmicpc.net/problem/8972

import sys
from collections import defaultdict

r,c = map(int,input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
num = list(sys.stdin.readline().rstrip())


for i in range(len(num)) :
    num[i] = int(num[i])

dr = [0,1,1,1,0,0,0,-1,-1,-1]
dc = [0,-1,0,1,-1,0,1,-1,0,1]

crazy = list()
jongsu = list()

for i in range(r) :
    for j in range(c) :
        if arr[i][j] == "R" :
            crazy.append((i,j))
        if arr[i][j] == "I" :
            jongsu = [i,j]

for i in range(len(num)) :
    bomb = defaultdict(int)
    arr[jongsu[0]][jongsu[1]] = "."
    nr,nc = jongsu[0] + dr[num[i]], jongsu[1] + dc[num[i]]

    if arr[nr][nc] == "R" :
        print(f"kraj {i+1}")
        break

    arr[nr][nc] = "I"
    jongsu = [nr,nc]

    for cr, cc in crazy :
        arr[cr][cc] = "."
        n_cr, n_cc = cr, cc
        if n_cr > nr :
            n_cr -= 1
        elif n_cr < nr :
            n_cr += 1

        if n_cc > nc :
            n_cc -= 1
        elif n_cc < nc :
            n_cc += 1

        if arr[n_cr][n_cc] == "I" :
            print(f"kraj {i+1}")
            exit()
        else :
            bomb[(n_cr, n_cc)] += 1

    temp = list()

    for cr, cc in bomb.keys() :
        if bomb[(cr,cc)] > 1 :
            arr[cr][cc] = "."
        else :
            arr[cr][cc] = "R"
            temp.append((cr,cc))

    crazy = temp
else :
    for i in arr :
        print(("").join(i))