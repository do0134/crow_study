# 프로그래머스 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = list()
    prev = -1
    for i in arr :
        if prev == i :
            continue
        else :
            answer.append(i)
            prev = i
    return answer