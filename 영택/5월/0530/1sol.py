# 백준 1756 피자 굽기
# https://www.acmicpc.net/problem/1756

import sys

n, m = map(int,sys.stdin.readline().split())
oven = list(map(int,sys.stdin.readline().split()))
pizza = list(map(int,sys.stdin.readline().split()))

for i in range(1, n) :
    oven[i] = min(oven[i], oven[i-1])

idx = 0
answer = m-1
for i in range(n-1,-1,-1) :
    if idx == m :
        break
    if oven[i] >= pizza[idx] :
        idx += 1
        answer = i

if idx == m :
    print(answer + 1)
else :
    print(0)