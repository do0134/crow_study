# 백준 1309 동물원
# https://www.acmicpc.net/problem/1309

n = int(input())
zoo = [0]*(n+1)
answer = 0
zoo[0] = 1
zoo[1] = 3

for i in range(2,n+1) :
    zoo[i] = (zoo[i-2] + zoo[i-1]*2)%9901
print(zoo[n])