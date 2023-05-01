# 프로그래머스 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq as hq

def solution(n, works):
    works = [-1*work for work in works]
    hq.heapify(works)
    for i in range(n) :
        now = hq.heappop(works)
        if now != 0 :
            now += 1
        hq.heappush(works,now)
    answer = 0

    for work in works :
        answer += work**2
    return answer