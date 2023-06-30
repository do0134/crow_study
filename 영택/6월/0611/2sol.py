# 백준 11557 Yangjojang of The Year
# https://www.acmicpc.net/problem/11557

from collections import defaultdict

t = int(input())
for _ in range(t) :
    n = int(input())
    university = defaultdict(int)
    for _ in range(n) :
        univ, alchol = input().split()
        alchol = int(alchol)
        university[univ] += alchol

    max_v = 0
    answer = ""
    for u in university.keys() :
        if max_v < university[u] :
            max_v = university[u]
            answer = u
    print(answer)