# 프로그래머스 숫자 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/12987

from collections import deque

def solution(A, B):
    a = deque(sorted(A))
    b = deque(sorted(B))
    answer = 0
    while b and a :
        if a[0] > b[-1] :
            break
        elif a[0] < b[0] :
            answer += 1
            a.popleft()
            b.popleft()
        else :
            b.popleft()
    return answer