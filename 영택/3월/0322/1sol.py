# 프로그래머스 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    j = -1
    for s,e in routes :
        if j == -1 :
            j = e
            answer += 1
        elif j < s :
            answer += 1
            j = e
    return answer