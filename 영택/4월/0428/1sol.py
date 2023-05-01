# 백준 1019 책 페이지
# https://www.acmicpc.net/problem/1019

start = 1
n = int(input())
answer = [0]*10
point = 1

def calc(s,value) :
    global answer
    while s > 0 :
        answer[s%10] += value
        s //= 10

while start <= n :
    while start%10 != 0 and start <= n :
        calc(start,point)
        start += 1
    if start > n :
        break
    while n%10 != 9 and start <= n :
        calc(n,point)
        n -= 1

    plus = (n//10 - start//10 + 1)
    for i in range(10) :
        answer[i] += plus*point
    n //= 10
    start = 1
    point *= 10

print(*answer)




