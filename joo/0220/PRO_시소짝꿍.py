# 프로그래머스 연습문제 - 시소 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict


def solution(weights):
    answer = 0
    cnts = defaultdict(int)
    # 가능한 비율 1:1, 1:2, 2:1, 2:3, 3:2, 3:4, 4:3
    for w in weights:
        answer += cnts[w] + cnts[w * 2] + cnts[w / 2] + cnts[(w * 2) / 3] \
                  + cnts[(w * 3) / 2] + cnts[(w * 4) / 3] + cnts[(w * 3) / 4]
        cnts[w] += 1
    return answer


w1 = [100, 180, 360, 100, 270]
print(solution(w1))
