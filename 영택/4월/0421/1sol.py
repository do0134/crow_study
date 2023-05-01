# 프로그래머스 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    max_d = 0
    answer = 0
    tree = [[] for _ in range(n + 1)]
    for s, e in edge:
        tree[s].append(e)
        tree[e].append(s)

    v = [int(1e9)] * (n + 1)
    v[1] = 0
    q = deque()
    q.append([1, 0])
    while q:
        idx, distance = q.popleft()
        if distance == max_d:
            answer += 1
        elif distance > max_d:
            max_d = distance
            answer = 1
        for i in tree[idx]:
            if v[i] > distance + 1:
                q.append([i, distance + 1])
                v[i] = distance + 1

    return answer