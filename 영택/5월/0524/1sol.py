# 백준 17182 우주 탐사선
# https://www.acmicpc.net/problem/17182

import sys

sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
graph = [[int(1e9)]*n for _ in range(n)]

for i in range(n) :
    temp = list(map(int,input().split()))
    for j in range(n) :
        graph[i][j] = temp[j]

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = int(1e9)
def back_tracking(idx, v, value) :
    global answer
    if len(v) == n :
        answer = min(answer, value)
        return

    for i in range(n) :
        if i not in v :
            v.append(i)
            back_tracking(i, v, value + graph[idx][i])
            v.pop()


back_tracking(m,[m],0)
print(answer)