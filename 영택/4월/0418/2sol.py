# 프로그래머스 정수삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

from collections import deque

def solution(t):
    n = len(t)
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = t[0][0]
    q = deque()
    q.append((0, 0))
    while q:
        cr, cc = q.popleft()
        nr = cr + 1
        nc1, nc2 = cc, cc + 1
        if nr == n:
            continue
        if dp[nr][nc1] < t[nr][nc1] + dp[cr][cc]:
            q.append((nr, nc1))
            dp[nr][nc1] = t[nr][nc1] + dp[cr][cc]
        if dp[nr][nc2] < t[nr][nc2] + dp[cr][cc]:
            q.append((nr, nc2))
            dp[nr][nc2] = t[nr][nc2] + dp[cr][cc]

    return max(dp[-1])