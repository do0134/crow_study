# 프로그래머스 인사고과
# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    s = sorted(scores[1:], key=lambda x: (-x[0], x[1]))
    wanho = scores[0]
    sum_wanho = sum(wanho)
    answer = 1
    min_s = 0
    for i in s:
        if i[0] > wanho[0] and i[1] > wanho[1]:
            return -1
        elif min_s <= i[1]:
            if sum_wanho < i[0] + i[1]:
                answer += 1
            min_s = i[1]
    return answer

