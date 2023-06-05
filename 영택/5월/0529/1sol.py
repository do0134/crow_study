# 백준 1911 흙길 보수하기
# https://www.acmicpc.net/problem/1911

n, l = map(int,input().split())
arr = list()

for _ in range(n) :
    s, e = map(int,input().split())
    arr.append((s,e))

arr.sort()
answer = 0
temp = 0

for s, e in arr :
    temp = max(s, temp)
    cnt = (e- temp+l-1) // l
    answer += cnt
    temp += cnt * l


print(answer)