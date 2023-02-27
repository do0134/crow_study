# 백준 서강그라운드
# https://www.acmicpc.net/problem/14938

from collections import deque

n,m,r = map(int,input().split())
items = [0]+list(map(int,input().split()))
INF = int(1e9)
tree = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r) :
    s,e,w = map(int,input().split())
    tree[s][e] = tree[e][s] = w

for i in range(n+1) :
    tree[i][i] = 0

for i in range(1,n+1) :
    for j in range(1,n+1) :
        for k in range(1,n+1) :
            tree[j][k] = min(tree[j][k], tree[j][i] + tree[i][k])

answer = 0
for i in range(1,n+1) :
    item = 0
    for j in range(1,n+1) :
        if tree[i][j] <= m :
            item += items[j]
    answer = max(answer, item)

print(answer)