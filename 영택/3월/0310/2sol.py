# 백준 피보나치 수 3
# https://www.acmicpc.net/problem/2749

n = int(input())
mod = 1000000
p = mod // 10*15

fibo = [0,1]

for i in range(2,p) :
    new = (fibo[i-2]+fibo[i-1]) % mod
    fibo.append(new)

print(fibo[n%p])

