# 프로그래머스 요격 시스템
# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1], reverse = True)
    l = -1

    for i,j in targets :
        if l == -1 :
            answer += 1
            l = i
        elif j <= l :
            answer += 1
            l = i

    return answer