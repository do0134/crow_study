import math

n = int(input())

for _ in range(n) :
    s,e = map(int,input().split())
    d = e-s
    root = math.floor(math.sqrt(d))
    sq = root ** 2
    if d <= 3 :
        answer = d
    elif d == sq :
        answer = (root*2)-1
    elif sq < d <= root + sq :
        answer = root*2
    elif sq + root < d :
        answer = root*2+1

    print(answer)