# 백준 1124 언더프라임
# https://www.acmicpc.net/problem/1124

a, b = map(int,input().split())
pn1 = list()
pn2 = list()
check = [0]*(b+1)

for i in range(2,b+1) :
    if not check[i] :
        pn1.append(i)
        check[i] = 1
        if i < 18 :
            pn2.append(i)
        for j in range(i*2,b+1,i) :
            check[j] = 1

answer = 0

def x_pn(n) :
    global answer
    temp = 0
    while n >= 2 :
        for i in range(len(pn1)) :
            if not n % pn1[i] :
                n //= pn1[i]
                temp += 1
                break

    if temp in pn2 :
        answer += 1
        return

for i in range(a,b+1) :
    x_pn(i)

print(answer)