# 프로그래머스 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    answer = -1
    n,a,b = len(queue1), sum(queue1), sum(queue2)
    c = a + b
    if c % 2:
        return answer

    q1, q2 = deque(queue1), deque(queue2)
    a_cnt = 0
    b_cnt = 0

    while a_cnt <= n * 2 and b_cnt <= n * 2:
        if a == b:
            return a_cnt + b_cnt
        elif a > b:
            temp = q1.popleft()
            a -= temp
            b += temp
            a_cnt += 1
            q2.append(temp)
        elif b > a :
            temp = q2.popleft()
            b -= temp
            a += temp
            b_cnt += 1
            q1.append(temp)
        if temp > c // 2:
            return answer

    if a == b:
        return a_cnt + b_cnt

    return answer