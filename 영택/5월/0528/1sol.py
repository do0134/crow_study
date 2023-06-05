# 백준 2141 우체국
# https://www.acmicpc.net/problem/2141

import sys

n = int(input())

arr = list()
r = 0

for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    arr.append((a,b))
    r += b

arr.sort()
answer = 1
l = 0

for i in range(n) :
    l += arr[i][1]
    if r / 2 <= l :
        answer = arr[i][0]
        break

print(answer)


