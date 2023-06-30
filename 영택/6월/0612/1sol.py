# 백준 2164 카드2
# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())
card = deque(list(x for x in range(1,n+1)))

while card :
    if len(card) == 1:
        break
    elif len(card) == 2 :
        card.popleft()
        break
    card.popleft()
    b = card.popleft()
    card.append(b)

print(card[0])
