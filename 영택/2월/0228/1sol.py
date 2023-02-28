# 프로그래머스 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3#
from collections import deque

def solution(n, computers):
    answer = 0

    v = [0] * n

    q = deque()

    for i in range(n):
        if not v[i]:
            v[i] = 1
            q.append(i)
            answer += 1
            while q:
                c_net = q.popleft()
                for j in range(i + 1, n):
                    if computers[c_net][j] == 1 and not v[j]:
                        v[j] = 1
                        q.append(j)

    return answer