# 백준 기타줄
# https://www.acmicpc.net/problem/1049

n, m = map(int,input().split())
min1 = min2 = int(1e9)

for _ in range(m) :
    temp = list(map(int,input().split()))
    min1 = min(temp[0],min1)
    min2 = min(temp[1],min2)

answer = 0
cnt = 0

while cnt < n :
    need = min(6, n-cnt)

    if min1 <= min2*need :
        cnt += 6
        answer += min1
    else :
        cnt += need
        answer += min2*need

print(answer)


