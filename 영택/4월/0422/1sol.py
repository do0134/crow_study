# 프로그래머스 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    point = defaultdict(int)
    for i in range(len(name)):
        point[name[i]] = yearning[i]

    for p in photo:
        value = 0
        for i in p:
            value += point[i]
        answer.append(value)
    return answer