# 백준 물병
# https://www.acmicpc.net/problem/1052

n,k = map(int,input().split())
temp = 2
answer = list()
while temp < n :
    temp *= 2
    if temp > n :
        n -= temp // 2
        answer.append(temp//2)
        temp = 2


if len(answer)+n < k :
    print(0)
else :
    answer.append(n)
    bottle = 0
    while len(answer) > k :
        now = answer.pop()
        bottle += answer[-1] - now
        answer[-1] *= 2
    print(bottle)


