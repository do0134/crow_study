# 프로그래머스 등산코스 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict
import heapq as hq

def solution(n, paths, gates, summits):
    tree = defaultdict(list)
    for s, e, w in paths:
        tree[s].append((e, w))
        tree[e].append((s, w))

    dp = [int(1e9)] * (n + 1)
    heap = list()
    summit = defaultdict(bool)

    for s in summits:
        summit[s] = True

    for gate in gates:
        hq.heappush(heap, (gate, 0))
        dp[gate] = 0

    answer = [int(1e9), int(1e9)]

    while heap:
        cc, inten = hq.heappop(heap)
        for nc, nw in tree[cc]:
            w = max(inten, nw)
            if dp[nc] > w:
                dp[nc] = w
                if summit[nc]:
                    if answer[1] > w:
                        answer = [nc, w]
                    elif answer[1] == w and answer[0] > nc:
                        answer = [nc, w]
                    continue
                hq.heappush(heap, (nc, w))

    return answer