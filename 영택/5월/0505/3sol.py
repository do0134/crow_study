# 백준 1195 킥다운
# https://www.acmicpc.net/problem/1195

from collections import deque

a = deque(list(input()))
b = deque(list(input()))

if len(a) < len(b) :
    a,b = b,a
a1 = len(a)
b1 = len(b)
answer = a1+b1
for i in range(len(b)) :
    a.appendleft(0)

idx = 0
while idx+len(b) <= len(a) :
    for i in range(len(b)) :
        if not a[0] :
            a_value = a[i]
        else :
            a_value = a[idx+i]
        if int(b[i]) + int(a_value) > 3 :
            if not a[0] :
                a.popleft()
            else :
                idx += 1
            break
    else :
        if not a[0] :
            answer = min(len(a), answer)
            a.popleft()
        else :
            answer = len(a)
            idx += 1
    if answer == len(a) :
        break

if answer > len(a) :
    a.append(0)
    while True :
        for i in range(len(b)) :
            if int(a[len(a)-len(b)+i]) + int(b[i]) > 3 :
                a.append(0)
                break
        else :
            answer = min(answer, len(a))
        if len(a) >= answer:
            break

print(answer)