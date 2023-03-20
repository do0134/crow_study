# 프로그래머스 스킬체크 레벨 2

from collections import deque

def solution(N, road, K):
    village = [[] for _ in range(N+1)]
    for a,b,c in road :
        village[a].append((b,c))
        village[b].append((a,c))

    q = deque()
    q.append((1,0))
    v = [int(1e9)]*(N+1)
    v[1] = 0
    while q :
        location, time = q.popleft()
        for next_location, spend in village[location] :
            if v[next_location] >= time + spend and time+spend <= K:
                v[next_location] = time+spend
                q.append((next_location, time+spend))

    answer = len(v) - v.count(int(1e9))
    return answer