# 백준 28245 배고파(HARD)
# https://www.acmicpc.net/problem/28245


l = list()
for i in range(60):
    temp = 2**i
    for j in range(i,60):
        l.append((temp+2**j, i,j))

l.sort()
f = len(l)

n = int(input())
for _ in range(n):
    m = int(input())
    answer = list()
    max_v = 10**18+1
    target = 10**18+1
    for i in range(f):
        a,b,c = l[i]
        if a == m:
            answer = [b,c]
            break
        else:
            if max_v > abs(m-a):
                max_v = abs(m-a)
                target = a
                answer = [b,c]
            elif max_v == abs(m-a):
                if target > a:
                    target = a
                    answer = [b,c]
            if a > m:
                break
    print(*answer)