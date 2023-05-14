# 백준 1325 효율적인 해킹
# https://www.acmicpc.net/problem/1325

from collections import defaultdict, deque

n,m = map(int,input().split())
tree = defaultdict(set)

for i in range(m) :
    s,e = map(int,input().split())
    tree[e].add(s)


answer = list()
max_v = 0

for i in range(1,n+1) :
    v = [0]*(n+1)
    v[i] = 1
    q = deque()
    q.append(i)
    cnt = 0
    while q :
        idx = q.popleft()
        for j in tree[idx] :
            if not v[j] :
                v[j] = 1
                cnt += 1
                q.append(j)

    if cnt > max_v :
        answer = [i]
        max_v = cnt
    elif cnt == max_v :
        answer.append(i)

print(*answer)