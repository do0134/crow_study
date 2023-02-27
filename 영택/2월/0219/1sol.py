# 백준 이진 검색 트리
# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**9)
num = list()
while True :
    try :
        num.append(int(input()))
    except :
        break

def dfs(s,e) :
    if s > e :
        return

    mid = e + 1

    for i in range(s+1, e+1) :
        if num[s] < num[i] :
            mid = i
            break

    dfs(s+1,mid-1)
    dfs(mid,e)
    print(num[s])

dfs(0, len(num)-1)