# 백준 13627 Dangerous Dive
# https://www.acmicpc.net/problem/13627

n,r = map(int,input().split())
alive = list(map(int,input().split()))
if n == r :
    print("*")
else :
    answer = list()
    for i in range(1,n+1) :
        if i not in alive :
            answer.append(i)
    print(*answer)
