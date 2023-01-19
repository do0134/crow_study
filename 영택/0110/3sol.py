# 백준 분산처리
# https://www.acmicpc.net/problem/1009
from collections import defaultdict

my_dict = defaultdict(list)

for i in range(1,10) :
    idx = 1
    while True :
        if str(i**idx)[-1] in my_dict[i] :
            break
        else :
            my_dict[i].append(str(i**idx)[-1])
            idx += 1

n = int(input())
for _ in range(n) :
    m,k = map(int,input().split())
    if m % 10 == 0 :
        print(10)
        continue
    elif m > 10 :
        m = int(str(m)[-1])

    temp = k % len(my_dict[m])
    print(my_dict[m][temp-1])

