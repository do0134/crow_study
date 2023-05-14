# 백준 15591 MooTube
# https://www.acmicpc.net/problem/15591

from collections import defaultdict, deque

video = defaultdict(list)

n,q = map(int,input().split())

for _ in range(n-1) :
    s,e,w = map(int,input().split())
    video[s].append((e,w))
    video[e].append((s,w))

for _ in range(q) :
    k, v = map(int,input().split())
    q = deque()
    cnt = 0
    visit = [0]*(n+1)
    q.append(v)
    visit[v] = 1
    while q :
        now = q.popleft()
        for next, w in video[now] :
            if not visit[next] and w >= k :
                cnt += 1
                q.append(next)
                visit[next] = 1

    print(cnt)