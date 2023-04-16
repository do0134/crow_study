# 프로그래머스 프린터
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    paper = deque([i for i in range(len(priorities))])
    answer = 0
    while paper :
        now = paper.popleft()
        if priorities[now] == max(priorities) :
            answer += 1
            priorities[now] = 0
            if now == location :
                return answer
        else :
            paper.append(now)
    return answer