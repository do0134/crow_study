# 프로그래머스 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626/solution_groups?language=python3

import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while scoville :
        a = hq.heappop(scoville)
        if a >= K :
            return answer
        if not scoville :
            return -1
        b = hq.heappop(scoville)
        hq.heappush(scoville, a+(b*2))
        answer += 1
    return -1