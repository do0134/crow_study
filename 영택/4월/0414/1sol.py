# 프로그래머스 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    idx = {i: p for i, p in enumerate(players)}
    player = {p: i for i, p in enumerate(players)}
    for call in callings:
        now = player[call]
        fast = now - 1
        now_p = call
        fast_p = idx[fast]

        idx[now] = fast_p
        idx[fast] = now_p

        player[now_p] = fast
        player[fast_p] = now
    return list(idx.values())