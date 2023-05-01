# 프로그래머스 부대복귀
# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import defaultdict, deque

def bfs(n, location, start):
    q = deque()
    v = [-1] * (n + 1)
    q.append((start, 0))
    v[start] = 0

    while q:
        cc, cnt = q.popleft()
        for i in location[cc]:
            if v[i] == -1:
                q.append((i, cnt + 1))
                v[i] = cnt + 1
    return v


def solution(n, roads, sources, destination):
    location = defaultdict(list)
    for s, e in roads:
        location[s].append(e)
        location[e].append(s)

    answer = bfs(n, location, destination)

    return [answer[source] for source in sources]