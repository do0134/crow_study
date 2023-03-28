# programmers summer/winter coding(2019) - 멀쩡한 사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/62048

import math


def solution(w, h):
    answer = 0
    check = w if w < h else h
    comp = h if w < h else w
    past = comp
    i = 1
    while i < check + 1:
        now = comp - (comp * i / check)
        answer += int(math.floor(now))
        answer += int(comp - math.ceil(past))
        past = now
        if now == int(now):
            break
        i += 1
    repeat = check // i
    answer *= repeat
    return answer


print(solution(3, 11))
