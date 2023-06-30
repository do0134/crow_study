# 백준 1800 인터넷 설치
# https://www.acmicpc.net/problem/1800

import heapq as hq

n, p, k = map(int,input().split())
tree = {}

for i in range(1,n+1) :
    tree[i] = []

for _ in range(p) :
    s,e,w = map(int,input().split())
    tree[s].append((e,w))
    tree[e].append((s,w))

def dik(max_v) :
    heap = list()
    dp = [int(1e9)]*(n+1)
    hq.heappush(heap,(0,1))
    dp[1] = 0

    while heap :
        cw, cc = hq.heappop(heap)

        for nc,nw in tree[cc] :
            if nw > max_v :
                if dp[nc] > cw+1 :
                    dp[nc] = cw+1
                    hq.heappush(heap,(cw+1, nc))
            else :
                if dp[nc] > cw :
                    dp[nc] = cw
                    hq.heappush(heap, (cw, nc))

    if dp[n] > k :
        return False
    else :
        return True


l, r = 0, 1000001
answer = -1
while l <= r :
    mid = (l+r) // 2
    if dik(mid) :
        r = mid -1
        answer = mid
    else :
        l = mid+1

print(answer)