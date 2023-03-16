# 백준 피보나치
# https://www.acmicpc.net/problem/9009

from collections import deque
fibo = [1,2]

while fibo[-1] <1000000001 :
    fibo.append(fibo[-1]+fibo[-2])

t = int(input())

for _ in range(t) :
    num = int(input())
    answer = deque()
    for i in range(len(fibo)-1,-1,-1) :
        if fibo[i] <= num :
            num -= fibo[i]
            answer.appendleft(fibo[i])
            if num == 0 :
                break
    print(*answer)