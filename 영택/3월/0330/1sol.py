# 프로그래머스 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    cnt = defaultdict(int)
    max_v = defaultdict(int)
    for order in orders:
        order = "".join(sorted(order))
        for i in course:
            for j in combinations(order, i):
                j = "".join(sorted(j))
                cnt[j] += 1
                if max_v[i] < cnt[j]:
                    max_v[i] = cnt[j]

    answer = []
    for j in cnt.keys():
        temp = len(j)
        if max_v[temp] == cnt[j] and max_v[temp] != 1:
            answer.append(j)

    answer.sort()
    return answer