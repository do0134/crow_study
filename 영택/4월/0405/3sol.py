# 프로그래머스 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def dfs(hp, rest, cnt):
    global answer
    answer = max(cnt, answer)
    if not rest:
        return
    for i in range(len(rest)):
        if rest[i][0] <= hp:
            dfs(hp - rest[i][1], rest[:i] + rest[i + 1:], cnt + 1)


def solution(k, dungeons):
    global answer
    answer = 0

    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            dfs(k - dungeons[i][1], dungeons[:i] + dungeons[i + 1:], 1)

    return answer