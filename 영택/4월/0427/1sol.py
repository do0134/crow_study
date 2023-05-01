# 프로그래머스 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    if not s // n:
        return [-1]

    answer = [s // n] * n
    sum_v = sum(answer)
    for i in range(n - 1, -1, -1):
        if sum_v == s:
            return answer
        else:
            answer[i] += 1
            sum_v += 1

    return answer