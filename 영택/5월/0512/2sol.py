# 프로그래머스 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    roads = [[1] * m for _ in range(n)]

    for i, j in puddles:
        roads[j - 1][i - 1] = 0

    for i in range(n):
        if not roads[i][0]:
            for j in range(i + 1, n):
                roads[j][0] = 0
            break

    for i in range(m):
        if not roads[0][i]:
            for j in range(i + 1, m):
                roads[0][j] = 0
            break

    value = 1000000007

    for i in range(1, n):
        for j in range(1, m):
            if roads[i][j]:
                roads[i][j] = (roads[i - 1][j] % value) + (roads[i][j - 1] % value)

    return roads[n - 1][m - 1] % value