# 프로그래머스 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def che(combi):
    m = max(combi)

    v = [0] * (m + 1)
    for i in range(2, int(m ** 0.5) + 1):
        if not v[i]:
            for j in range(i * 2, m + 1, i):
                v[j] = 1
    value = 0
    for i in combi:
        if i < 2:
            continue
        if not v[i]:
            value += 1

    return value


def dfs(num, s):
    global combi
    combi.add(int(num))
    if not s:
        return
    for i in range(len(s)):
        dfs(num + s[i], s[:i] + s[i + 1:])


def solution(numbers):
    global combi

    combi = set()

    for i in range(len(numbers)):
        if numbers[i] != "0":
            dfs(numbers[i], numbers[:i] + numbers[i + 1:])

    return che(combi)